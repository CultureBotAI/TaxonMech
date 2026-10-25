#!/usr/bin/env python3
"""Seed TaxonRecords from the raw, AllTheBacteria and StrainInfo inventories.

Reads the committed inventories (``scripts/extract_source_inventory.py``
output), builds one harmonized concept per taxon in scope, and writes
``data/taxa/<domain>/<slug>.yaml`` through the closed-schema write gate.

Scope
-----
The inventories cover every taxon any strain-bearing source attests (tens of
thousands). The *committed corpus* is the subset named in
``curation/seed_scope.tsv``: one identifier per line, with the date and reason
it was added. That file is the reviewable, explicit answer to "which taxa are
records", and ``scripts/verify_corpus.py`` proves the corpus is exactly what
the inventories plus that scope produce. ``scripts/propose_scope.py`` ranks
candidates for it. ``--all`` bypasses the scope for exploratory runs; production
expansion updates the scope first so the reproduction gate sees the same records.

Usage
-----
    python3 scripts/seed_from_sources.py                     # dry-run report
    python3 scripts/seed_from_sources.py --apply --only NCBITaxon:562   # canary
    python3 scripts/seed_from_sources.py --apply             # the scoped corpus
    python3 scripts/seed_from_sources.py --apply --force     # also overwrite
"""

from __future__ import annotations

import argparse
import copy
import csv
import datetime
import hashlib
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "src"))

from taxonmech import atb, straininfo  # noqa: E402
from taxonmech.curate.curation_event import record_curation_event  # noqa: E402
from taxonmech.validation.write_validated import (  # noqa: E402
    ValidationFailedError,
    write_validated_taxon,
)

RAW_DIR = REPO_ROOT / "data" / "raw"
ATB_DIR = REPO_ROOT / "data" / "atb"
STRAININFO_DIR = REPO_ROOT / "data" / "straininfo"
TAXA_DIR = REPO_ROOT / "data" / "taxa"
SCOPE_PATH = REPO_ROOT / "curation" / "seed_scope.tsv"
CAUSAL_GRAPHS_DIR = REPO_ROOT / "curation" / "causal_graphs"
UNIPROT_PROTEINS_PATH = REPO_ROOT / "curation" / "uniprot_proteins.tsv"
PATHS_LOCKFILE = TAXA_DIR / "PATHS.tsv"

UNIPROT_PROTEIN_FIELDS = (
    "uniprot_id",
    "entry_name",
    "entry_status",
    "protein_name",
    "organism_taxon_id",
    "organism_label",
    "proteome_id",
    "gene_symbol",
    "locus_tag",
    "ec_numbers",
    "sequence_length",
    "sequence_crc64",
    "sequence_version",
    "release_version",
)
CRC64_PATTERN = re.compile(r"^[0-9A-F]{16}$")
BACDIVE_STRAIN_ID_PATTERN = re.compile(r"^kgmicrobe\.strain:bacdive_[1-9][0-9]*$")

SEED_CURATOR = "seed_from_sources"

# Retain every inventoried strain in records; the browser handles presentation.
# Optional caps remain available to isolated tests and downstream callers.
STRAIN_LISTING_CAP = None

# REPOSITORY RULE: TaxonMech records are species-level and below. A record is
# a species, or an infraspecific taxon (subspecies, strain, serotype, ...), or
# an unranked NCBI taxon that sits under a species. Genera and higher ranks
# are never records: they appear only as lineage entries, carried verbatim
# from NCBI Taxonomy. TaxonMech does not reconcile the NCBI, GTDB and LPSN
# hierarchies with one another, does not resolve conflicts between them, and
# never infers a placement. The lineage is NCBI's, as NCBI states it.
INFRASPECIFIC_RANKS = {
    "SUBSPECIES", "STRAIN", "VARIETAS", "SUBVARIETY", "FORMA", "FORMA_SPECIALIS",
    "SEROTYPE", "SEROGROUP", "BIOTYPE", "GENOTYPE", "ISOLATE", "MORPH", "PATHOGROUP",
}
RECORD_RANKS = {"SPECIES"} | INFRASPECIFIC_RANKS
# These entries need ancestry to establish their level. The inventory has
# CLADE entries beneath species; an explicitly higher rank must never use
# this fallback, even if an upstream parent assignment is inconsistent.
ANCESTRY_DEPENDENT_RANKS = {"", "NO_RANK", "CLADE"}

DOMAIN_ROOTS = {
    "NCBITaxon:2": "BACTERIA",
    "NCBITaxon:2157": "ARCHAEA",
    "NCBITaxon:2759": "EUKARYOTA",
    "NCBITaxon:10239": "VIRUSES",
}

SOURCE_ENUM = {
    "ncbitaxon": "NCBITAXON", "gtdb": "GTDB",
    "bacdive": "BACDIVE", "lpsn": "LPSN", "mediadive": "MEDIADIVE", "gold": "GOLD",
    "madin_etal": "MADIN", "bactotraits": "BACTOTRAITS",
}

# A slug becomes a filename, so it must not be able to escape the corpus
# directory. The lockfile is hand-editable (that is the rename mechanism), so
# this is validated on load rather than assumed.
SLUG_PATTERN = re.compile(r"^[a-z0-9][a-z0-9_]*$")


def _raise_csv_limit() -> None:
    limit = sys.maxsize
    while True:
        try:
            csv.field_size_limit(limit)
            return
        except OverflowError:
            limit //= 2


_raise_csv_limit()


def read_tsv(name: str) -> list[dict[str, str]]:
    path = RAW_DIR / name
    if not path.exists():
        raise SystemExit(f"inventory missing: {path} — run `just extract-inventory`")
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def split(value: str) -> list[str]:
    return [v for v in (value or "").split("|") if v]


def id_key(identifier: str) -> tuple[str, int, str]:
    """Sort CURIEs by prefix, then numerically where the local part is a
    number, then lexically — so a minted ``taxonmech:`` id sorts instead of
    crashing an ``int()`` (#11)."""
    prefix, _, local = identifier.partition(":")
    return (prefix, int(local) if local.isdigit() else sys.maxsize, local)


def slugify(text: str, maxlen: int = 72) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return (slug or "taxon")[:maxlen].rstrip("_")


def _seed_timestamp() -> str:
    """When the data this corpus is built from was extracted.

    Taken from the newest source manifest rather than now(): the corpus must be
    byte-reproducible, so a wall-clock stamp would make every re-seed a
    corpus-wide diff. The manifest's extracted_at is the honest answer to
    "when is this data from", and it changes only when the data does.
    """
    timestamps = [datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)]
    for manifest in (
        RAW_DIR / "MANIFEST.yaml", ATB_DIR / "MANIFEST.yaml", STRAININFO_DIR / "MANIFEST.yaml",
    ):
        if not manifest.exists():
            continue
        data = yaml.safe_load(manifest.read_text(encoding="utf-8")) or {}
        if value := data.get("extracted_at"):
            timestamp = datetime.datetime.fromisoformat(str(value).replace("Z", "+00:00"))
            if timestamp.tzinfo is None:
                raise ValueError(f"source manifest timestamp lacks timezone: {manifest}")
            timestamps.append(timestamp)
    return max(timestamps).astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------------------
# Inventory model
# ---------------------------------------------------------------------------

@dataclass
class Inventory:
    taxa: dict[str, dict[str, str]]
    gtdb: dict[str, list[dict[str, str]]]            # ncbitaxon_id -> mapping rows
    lpsn: dict[str, dict[str, str]]                  # lpsn_id -> row
    lpsn_by_taxon: dict[str, list[str]]              # ncbitaxon_id -> lpsn ids
    strains: dict[str, list[dict[str, str]]]         # ncbitaxon_id -> strain rows
    cc_strains: dict[str, list[str]]                 # ncbitaxon_id -> culture-collection strain ids
    media: dict[str, dict[str, str]]
    gold: dict[str, int]
    madin: dict[str, int]
    bacto: dict[str, int]
    strain_assemblies: dict[str, list[dict[str, Any]]] = field(default_factory=dict)
    strain_genome_records: dict[str, list[dict[str, Any]]] = field(default_factory=dict)
    strain_related_records: dict[str, list[dict[str, Any]]] = field(default_factory=dict)
    causal_graphs: dict[str, list[dict[str, Any]]] = field(default_factory=dict)
    causal_graph_events: dict[str, list[dict[str, Any]]] = field(default_factory=dict)

    def parent(self, tid: str) -> str:
        return (self.taxa.get(tid) or {}).get("parent_id", "")

    def children(self, tid: str) -> list[str]:
        if not hasattr(self, "_children"):
            index: dict[str, list[str]] = defaultdict(list)
            for child, row in self.taxa.items():
                if row.get("parent_id"):
                    index[row["parent_id"]].append(child)
            self._children = index
        return self._children.get(tid, [])

    def descendants(self, tid: str) -> list[str]:
        """Every inventoried taxon below ``tid``, in a stable order."""
        out: list[str] = []
        stack = list(self.children(tid))
        seen = {tid}
        while stack:
            cur = stack.pop()
            if cur in seen:
                continue
            seen.add(cur)
            out.append(cur)
            stack.extend(self.children(cur))
        return sorted(out, key=lambda t: int(t.split(":")[1]))

    def lineage(self, tid: str) -> list[str]:
        """Ancestors root-first, stopping at the first id the inventory lacks."""
        chain: list[str] = []
        cur = self.parent(tid)
        seen = {tid}
        while cur and cur in self.taxa and cur not in seen:
            chain.append(cur)
            seen.add(cur)
            cur = self.parent(cur)
        return list(reversed(chain))

    def is_species_or_below(self, tid: str) -> bool:
        """The repository rule: a record is a species, an infraspecific taxon,
        or an unranked/clade taxon with a species above it."""
        rank = (self.taxa.get(tid) or {}).get("rank", "")
        if rank in RECORD_RANKS:
            return True
        if rank not in ANCESTRY_DEPENDENT_RANKS:
            return False
        return any((self.taxa.get(a) or {}).get("rank") == "SPECIES" for a in self.lineage(tid))

    def has_attested_descendant(self, tid: str) -> bool:
        """True when at least one descendant taxon in the inventory is directly attested."""
        return any((self.taxa.get(d) or {}).get("attested_by") for d in self.descendants(tid))

    def domain(self, tid: str) -> str:
        for ancestor in [tid, *self.lineage(tid)]:
            if ancestor in DOMAIN_ROOTS:
                return DOMAIN_ROOTS[ancestor]
        return "OTHER"


def load_uniprot_proteins(path: Path = UNIPROT_PROTEINS_PATH) -> dict[str, dict[str, str]]:
    """Read the pinned UniProtKB protein reference catalog from ``curation/uniprot_proteins.tsv``."""
    if not path.exists():
        return {}
    proteins: dict[str, dict[str, str]] = {}
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        if tuple(reader.fieldnames or ()) != UNIPROT_PROTEIN_FIELDS:
            raise SystemExit(
                f"{path}: expected columns {list(UNIPROT_PROTEIN_FIELDS)}, got {reader.fieldnames}"
            )
        for line_no, row in enumerate(reader, start=2):
            uid = (row.get("uniprot_id") or "").strip()
            if not uid.startswith("UniProtKB:"):
                raise SystemExit(f"{path}:{line_no}: invalid uniprot_id {uid!r}")
            if uid in proteins:
                raise SystemExit(f"{path}:{line_no}: duplicate uniprot_id {uid!r}")
            if row.get("entry_status") not in ("SWISS_PROT", "TREMBL"):
                raise SystemExit(f"{path}:{line_no}: invalid entry_status for {uid!r}")
            if not (row.get("organism_taxon_id") or "").startswith("NCBITaxon:"):
                raise SystemExit(f"{path}:{line_no}: invalid organism_taxon_id for {uid!r}")
            if row.get("proteome_id") and not row["proteome_id"].startswith("UP:UP"):
                raise SystemExit(f"{path}:{line_no}: invalid proteome_id for {uid!r}")
            try:
                seq_len = int(row.get("sequence_length") or "0")
                seq_ver = int(row.get("sequence_version") or "0")
            except ValueError as exc:
                raise SystemExit(f"{path}:{line_no}: non-integer sequence metadata for {uid!r}") from exc
            if seq_len <= 0 or seq_ver <= 0:
                raise SystemExit(f"{path}:{line_no}: non-positive sequence length/version for {uid!r}")
            crc64 = (row.get("sequence_crc64") or "").strip()
            if not CRC64_PATTERN.match(crc64):
                raise SystemExit(f"{path}:{line_no}: invalid sequence_crc64 {crc64!r} for {uid!r}")
            proteins[uid] = dict(row)
    return proteins


def _taxon_lineage(taxa: dict[str, dict[str, str]], tid: str) -> list[str]:
    chain: list[str] = []
    cur = (taxa.get(tid) or {}).get("parent_id", "")
    seen = {tid}
    while cur and cur in taxa and cur not in seen:
        chain.append(cur)
        seen.add(cur)
        cur = (taxa.get(cur) or {}).get("parent_id", "")
    return list(reversed(chain))


def _taxon_is_species_or_below(taxa: dict[str, dict[str, str]], tid: str) -> bool:
    rank = (taxa.get(tid) or {}).get("rank", "")
    if rank in RECORD_RANKS:
        return True
    if rank not in ANCESTRY_DEPENDENT_RANKS:
        return False
    return any((taxa.get(a) or {}).get("rank") == "SPECIES" for a in _taxon_lineage(taxa, tid))


def _taxa_lineage_compatible(taxa: dict[str, dict[str, str]], tid_a: str, tid_b: str) -> bool:
    """Return True when ``tid_a`` and ``tid_b`` are identical or on the same ancestor/descendant chain."""
    return (
        tid_a == tid_b
        or tid_a in _taxon_lineage(taxa, tid_b)
        or tid_b in _taxon_lineage(taxa, tid_a)
    )


def validate_causal_graph_structure(
    graphs_by_taxon: dict[str, list[dict[str, Any]]],
) -> None:
    """Validate internal referential integrity and required slots of causal-graph overlays."""
    for tid, graphs in sorted(graphs_by_taxon.items()):
        for graph in graphs:
            gid = graph.get("graph_id", "<unnamed>")
            g_ctx = f"{tid} graph {gid!r}"
            nodes = graph.get("nodes")
            seen_node_ids: set[str] = set()
            if nodes is not None:
                if not isinstance(nodes, list) or not nodes:
                    raise SystemExit(f"{g_ctx}: 'nodes' must be a non-empty list")
                for node in nodes:
                    if not isinstance(node, dict):
                        raise SystemExit(f"{g_ctx}: each node must be a mapping")
                    nid = (node.get("node_id") or "").strip() if isinstance(node.get("node_id"), str) else ""
                    if not nid:
                        raise SystemExit(f"{g_ctx}: node missing 'node_id'")
                    if nid in seen_node_ids:
                        raise SystemExit(f"{g_ctx}: duplicate node_id {nid!r}")
                    seen_node_ids.add(nid)
                    lbl = (node.get("label") or "").strip() if isinstance(node.get("label"), str) else ""
                    raw_ntype = node.get("node_type")
                    ntype = (raw_ntype or "").strip() if isinstance(raw_ntype, str) else ""
                    if not lbl or not ntype:
                        raise SystemExit(f"{g_ctx} node {nid!r}: requires non-empty 'label' and 'node_type'")

            edges = graph.get("edges")
            if edges is not None:
                if not isinstance(edges, list) or not edges:
                    raise SystemExit(f"{g_ctx}: 'edges' must be a non-empty list")
                seen_edge_ids: set[str] = set()
                for edge in edges:
                    if not isinstance(edge, dict):
                        raise SystemExit(f"{g_ctx}: each edge must be a mapping")
                    eid = (edge.get("edge_id") or "").strip() if isinstance(edge.get("edge_id"), str) else ""
                    if not eid:
                        raise SystemExit(f"{g_ctx}: edge missing 'edge_id'")
                    if eid in seen_edge_ids:
                        raise SystemExit(f"{g_ctx}: duplicate edge_id {eid!r}")
                    seen_edge_ids.add(eid)
                    e_ctx = f"{g_ctx} edge {eid!r}"
                    subj = (edge.get("subject") or "").strip() if isinstance(edge.get("subject"), str) else ""
                    raw_pred = edge.get("predicate")
                    pred = (raw_pred or "").strip() if isinstance(raw_pred, str) else ""
                    obj = (edge.get("object") or "").strip() if isinstance(edge.get("object"), str) else ""
                    if not subj or not pred or not obj:
                        raise SystemExit(f"{e_ctx}: requires non-empty 'subject', 'predicate', and 'object'")
                    if subj == obj:
                        raise SystemExit(f"{e_ctx}: self-loop subject == object {subj!r} is not allowed")
                    if nodes is not None:
                        if subj not in seen_node_ids:
                            raise SystemExit(
                                f"{e_ctx}: subject {subj!r} does not reference a defined node_id"
                            )
                        if obj not in seen_node_ids:
                            raise SystemExit(
                                f"{e_ctx}: object {obj!r} does not reference a defined node_id"
                            )
                    ev_list = edge.get("evidence")
                    if not isinstance(ev_list, list) or not ev_list:
                        raise SystemExit(f"{e_ctx}: requires non-empty 'evidence' list")
                    for ev in ev_list:
                        ref = (
                            (ev.get("reference") or "").strip()
                            if isinstance(ev, dict) and isinstance(ev.get("reference"), str)
                            else ""
                        )
                        if not ref:
                            raise SystemExit(f"{e_ctx}: each evidence item requires non-empty 'reference'")


def validate_causal_graph_proteins(
    graphs_by_taxon: dict[str, list[dict[str, Any]]],
    *,
    uniprot_proteins: dict[str, dict[str, str]] | None = None,
    taxa: dict[str, dict[str, str]] | None = None,
    strains: dict[str, list[dict[str, str]]] | None = None,
) -> None:
    """Validate GENE_OR_PROTEIN nodes against pinned UniProtKB metadata, NCBI Taxonomy lineage,
    and BacDive strain inventory."""
    strain_taxa: dict[str, set[str]] | None = None
    if strains is not None:
        strain_taxa = defaultdict(set)
        for s_tid, s_rows in strains.items():
            for s_row in s_rows:
                sid = (s_row.get("strain_id") or "").strip()
                if sid:
                    strain_taxa[sid].add(s_tid)
    for tid, graphs in sorted(graphs_by_taxon.items()):
        for graph in graphs:
            gid = graph.get("graph_id", "<unnamed>")
            for node in graph.get("nodes") or []:
                if not isinstance(node, dict) or node.get("node_type") != "GENE_OR_PROTEIN":
                    continue
                nid = node.get("node_id", "<unnamed>")
                ctx = f"{tid} graph {gid!r} node {nid!r}"
                raw_grounding = node.get("grounding")
                grounding = (raw_grounding or "").strip() if isinstance(raw_grounding, str) else ""
                if not grounding.startswith("UniProtKB:"):
                    raise SystemExit(f"{ctx}: GENE_OR_PROTEIN grounding must start with 'UniProtKB:'")
                org_tid = (
                    (node.get("organism_taxon_id") or "").strip()
                    if isinstance(node.get("organism_taxon_id"), str)
                    else ""
                )
                if not org_tid.startswith("NCBITaxon:"):
                    raise SystemExit(f"{ctx}: GENE_OR_PROTEIN missing valid 'organism_taxon_id'")
                raw_strain_id = node.get("strain_id")
                strain_id = ""
                if raw_strain_id is not None:
                    strain_id = raw_strain_id.strip() if isinstance(raw_strain_id, str) else ""
                    if not BACDIVE_STRAIN_ID_PATTERN.match(strain_id):
                        raise SystemExit(f"{ctx}: GENE_OR_PROTEIN invalid 'strain_id' {raw_strain_id!r}")
                status = node.get("entry_status")
                if status not in ("SWISS_PROT", "TREMBL"):
                    raise SystemExit(f"{ctx}: GENE_OR_PROTEIN invalid 'entry_status' {status!r}")
                gene_symbol = (node.get("gene_symbol") or "").strip() if node.get("gene_symbol") else ""
                locus_tag = (node.get("locus_tag") or "").strip() if node.get("locus_tag") else ""
                if not (gene_symbol or locus_tag):
                    raise SystemExit(f"{ctx}: GENE_OR_PROTEIN requires 'gene_symbol' or 'locus_tag'")
                proteome_id = (node.get("proteome_id") or "").strip() if node.get("proteome_id") else ""
                if proteome_id and not proteome_id.startswith("UP:UP"):
                    raise SystemExit(f"{ctx}: GENE_OR_PROTEIN invalid 'proteome_id' {proteome_id!r}")
                seq_len = node.get("sequence_length")
                if not isinstance(seq_len, int) or isinstance(seq_len, bool) or seq_len <= 0:
                    raise SystemExit(f"{ctx}: GENE_OR_PROTEIN requires positive integer 'sequence_length'")
                crc64 = node.get("sequence_crc64")
                if not isinstance(crc64, str) or not CRC64_PATTERN.match(crc64):
                    raise SystemExit(f"{ctx}: GENE_OR_PROTEIN requires 16-hex 'sequence_crc64'")
                seq_ver = node.get("sequence_version")
                if not isinstance(seq_ver, int) or isinstance(seq_ver, bool) or seq_ver <= 0:
                    raise SystemExit(f"{ctx}: GENE_OR_PROTEIN requires positive integer 'sequence_version'")

                if uniprot_proteins is not None:
                    ref = uniprot_proteins.get(grounding)
                    if ref is None:
                        raise SystemExit(
                            f"{ctx}: {grounding} is not registered in curation/uniprot_proteins.tsv"
                        )
                    if status != ref["entry_status"]:
                        raise SystemExit(
                            f"{ctx}: entry_status {status!r} != {ref['entry_status']!r} for {grounding}"
                        )
                    if org_tid != ref["organism_taxon_id"]:
                        expected_org = ref["organism_taxon_id"]
                        raise SystemExit(
                            f"{ctx}: organism_taxon_id {org_tid!r} != {expected_org!r} for {grounding}"
                        )
                    if proteome_id != ref["proteome_id"]:
                        raise SystemExit(
                            f"{ctx}: proteome_id {proteome_id!r} != {ref['proteome_id']!r} for {grounding}"
                        )
                    if locus_tag != ref["locus_tag"]:
                        raise SystemExit(
                            f"{ctx}: locus_tag {locus_tag!r} != {ref['locus_tag']!r} for {grounding}"
                        )
                    ref_gene = ref["gene_symbol"]
                    allowed_genes = {ref_gene} if ref_gene else {"", ref["locus_tag"]}
                    if gene_symbol not in allowed_genes:
                        raise SystemExit(
                            f"{ctx}: gene_symbol {gene_symbol!r} != {ref_gene!r} for {grounding}"
                        )
                    if seq_len != int(ref["sequence_length"]):
                        raise SystemExit(
                            f"{ctx}: sequence_length {seq_len} != {ref['sequence_length']} for {grounding}"
                        )
                    if crc64 != ref["sequence_crc64"]:
                        raise SystemExit(
                            f"{ctx}: sequence_crc64 {crc64!r} != {ref['sequence_crc64']!r} for {grounding}"
                        )
                    if seq_ver != int(ref["sequence_version"]):
                        raise SystemExit(
                            f"{ctx}: sequence_version {seq_ver} != {ref['sequence_version']} for {grounding}"
                        )
                    node_ecs = [
                        x for x in (node.get("xrefs") or []) if isinstance(x, str) and x.startswith("EC:")
                    ]
                    ref_ecs = split(ref["ec_numbers"])
                    if any(ec not in ref_ecs for ec in node_ecs):
                        raise SystemExit(
                            f"{ctx}: EC xrefs {node_ecs} do not match reference {ref_ecs} for {grounding}"
                        )

                if taxa is not None:
                    if tid not in taxa:
                        raise SystemExit(f"{ctx}: record taxon {tid} is absent from ncbitaxon_taxa.tsv")
                    if org_tid not in taxa:
                        raise SystemExit(
                            f"{ctx}: organism_taxon_id {org_tid} is absent from ncbitaxon_taxa.tsv"
                        )
                    org_lineage = _taxon_lineage(taxa, org_tid)
                    tid_lineage = _taxon_lineage(taxa, tid)
                    lineage_ok = (
                        org_tid == tid
                        or tid in org_lineage
                        or (org_tid in tid_lineage and _taxon_is_species_or_below(taxa, org_tid))
                    )
                    if not lineage_ok:
                        raise SystemExit(
                            f"{ctx}: organism_taxon_id {org_tid} is not lineage-consistent with {tid}"
                        )

                if strain_id and strain_taxa is not None:
                    linked_tids = strain_taxa.get(strain_id)
                    if not linked_tids:
                        raise SystemExit(
                            f"{ctx}: strain_id {strain_id!r} is absent from bacdive_strains.tsv"
                        )
                    if taxa is not None:
                        strain_lineage_ok = any(
                            s_tid in taxa
                            and _taxa_lineage_compatible(taxa, s_tid, tid)
                            and _taxa_lineage_compatible(taxa, s_tid, org_tid)
                            for s_tid in linked_tids
                        )
                        if not strain_lineage_ok:
                            raise SystemExit(
                                f"{ctx}: strain_id {strain_id!r} (taxa {sorted(linked_tids)}) "
                                f"is not lineage-consistent with {tid} and {org_tid}"
                            )


def load_causal_graphs(
    path: Path = CAUSAL_GRAPHS_DIR,
    *,
    uniprot_path: Path | None = None,
    taxa: dict[str, dict[str, str]] | None = None,
    strains: dict[str, list[dict[str, str]]] | None = None,
) -> tuple[dict[str, list[dict[str, Any]]], dict[str, list[dict[str, Any]]]]:
    """Read maintained causal-graph overlays from ``curation/causal_graphs/*.yaml``.

    Returns ``(graphs_by_taxon, events_by_taxon)`` keyed by ``TaxonRecord.identifier``.
    Overlays survive ``just seed-apply --force`` and ``just verify-corpus`` because
    ``build_document()`` merges them deterministically into ``doc["causal_graphs"]``
    and appends any declared ``curation_history`` events.
    """
    if not path.exists():
        return {}, {}
    graphs_by_taxon: dict[str, list[dict[str, Any]]] = {}
    events_by_taxon: dict[str, list[dict[str, Any]]] = {}
    allowed_top_keys = {"identifier", "causal_graphs", "curation_history"}
    for overlay_file in sorted(path.glob("*.yaml")):
        data = yaml.safe_load(overlay_file.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise SystemExit(f"{overlay_file}: causal-graph overlay must be a YAML mapping")
        unknown = set(data) - allowed_top_keys
        if unknown:
            raise SystemExit(
                f"{overlay_file}: unexpected top-level keys in causal-graph overlay: {sorted(unknown)}"
            )
        identifier = (data.get("identifier") or "").strip() if isinstance(data.get("identifier"), str) else ""
        if not identifier:
            raise SystemExit(f"{overlay_file}: missing or invalid 'identifier'")
        if identifier in graphs_by_taxon:
            raise SystemExit(f"{overlay_file}: duplicate causal-graph overlay for {identifier}")
        graphs = data.get("causal_graphs")
        if not isinstance(graphs, list) or not graphs:
            raise SystemExit(f"{overlay_file}: 'causal_graphs' must be a non-empty list")
        seen_graph_ids: set[str] = set()
        for graph in graphs:
            if not isinstance(graph, dict):
                raise SystemExit(f"{overlay_file}: each causal_graphs entry must be a mapping")
            gid = (graph.get("graph_id") or "").strip() if isinstance(graph.get("graph_id"), str) else ""
            if not gid:
                raise SystemExit(f"{overlay_file}: causal_graphs entry missing 'graph_id'")
            if gid in seen_graph_ids:
                raise SystemExit(f"{overlay_file}: duplicate graph_id {gid!r} for {identifier}")
            seen_graph_ids.add(gid)
        graphs_by_taxon[identifier] = graphs
        events = data.get("curation_history")
        if events is not None:
            if not isinstance(events, list) or any(not isinstance(e, dict) for e in events):
                raise SystemExit(f"{overlay_file}: 'curation_history' must be a list of event mappings")
            events_by_taxon[identifier] = events
    validate_causal_graph_structure(graphs_by_taxon)
    resolved_uniprot_path = uniprot_path
    if resolved_uniprot_path is None and UNIPROT_PROTEINS_PATH.exists():
        resolved_uniprot_path = UNIPROT_PROTEINS_PATH
    uniprot_proteins = load_uniprot_proteins(resolved_uniprot_path) if resolved_uniprot_path else None
    validate_causal_graph_proteins(
        graphs_by_taxon,
        uniprot_proteins=uniprot_proteins,
        taxa=taxa,
        strains=strains,
    )
    return graphs_by_taxon, events_by_taxon


def load_inventory() -> Inventory:
    taxa = {r["taxon_id"]: r for r in read_tsv("ncbitaxon_taxa.tsv")}
    gtdb: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in read_tsv("gtdb_mappings.tsv"):
        gtdb[r["ncbitaxon_id"]].append(r)
    lpsn = {r["lpsn_id"]: r for r in read_tsv("lpsn_names.tsv")}
    lpsn_by_taxon: dict[str, list[str]] = defaultdict(list)
    for lid, r in lpsn.items():
        for tid in split(r["ncbitaxon_ids"]):
            lpsn_by_taxon[tid].append(lid)
    strains: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in read_tsv("bacdive_strains.tsv"):
        for tid in split(r["taxon_ids"]):
            strains[tid].append(r)
    cc_strains: dict[str, list[str]] = defaultdict(list)
    for r in read_tsv("culture_collection_strains.tsv"):
        for tid in split(r["taxon_ids"]):
            cc_strains[tid].append(r["strain_id"])
    media = {r["taxon_id"]: r for r in read_tsv("mediadive_taxa.tsv")}
    gold = {r["taxon_id"]: int(r["organism_count"]) for r in read_tsv("gold_organisms.tsv")}
    madin = {r["taxon_id"]: int(r["assertion_count"]) for r in read_tsv("madin_taxa.tsv")}
    bacto = {r["taxon_id"]: int(r["assertion_count"]) for r in read_tsv("bactotraits_taxa.tsv")}
    strain_assemblies: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in read_tsv("strain_assemblies.tsv"):
        strain_assemblies[r["strain_id"]].append(r)
    strain_genome_records: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in read_tsv("strain_genome_records.tsv"):
        strain_genome_records[r["strain_id"]].append(r)
    for strain_id, records in atb.genome_records(ATB_DIR).items():
        strain_genome_records[strain_id].extend(records)
    strain_related_records: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in read_tsv("strain_related_records.tsv"):
        strain_related_records[r["strain_id"]].append(r)
    # The converter validates the committed overlay and requires its manifest;
    # missing source evidence must not silently seed a partial production corpus.
    si_assemblies, si_related = straininfo.record_links(STRAININFO_DIR)
    for strain_id, records in si_assemblies.items():
        strain_assemblies[strain_id].extend(records)
    for strain_id, records in si_related.items():
        strain_related_records[strain_id].extend(records)
    causal_graphs, causal_graph_events = load_causal_graphs(CAUSAL_GRAPHS_DIR)
    validate_causal_graph_proteins(
        {tid: graphs for tid, graphs in causal_graphs.items() if tid in taxa},
        taxa=taxa,
        strains=strains,
    )
    return Inventory(taxa, gtdb, lpsn, lpsn_by_taxon, strains, cc_strains, media, gold, madin, bacto,
                     strain_assemblies, strain_genome_records, strain_related_records,
                     causal_graphs, causal_graph_events)


# ---------------------------------------------------------------------------
# Scope
# ---------------------------------------------------------------------------

def load_scope(path: Path = SCOPE_PATH) -> dict[str, dict[str, str]]:
    """The committed corpus scope: identifier -> {added, reason}."""
    if not path.exists():
        return {}
    scope: dict[str, dict[str, str]] = {}
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for line_no, row in enumerate(reader, start=2):
            identifier = (row.get("identifier") or "").strip()
            if not identifier:
                raise SystemExit(f"{path}:{line_no}: blank identifier")
            if identifier in scope:
                raise SystemExit(f"{path}:{line_no}: duplicate identifier {identifier}")
            scope[identifier] = {"added": row.get("added") or "", "reason": row.get("reason") or ""}
    return scope


# ---------------------------------------------------------------------------
# Concepts
# ---------------------------------------------------------------------------

@dataclass
class Concept:
    identifier: str
    label: str
    rank: str
    domain: str
    row: dict[str, str]
    sources: set[str] = field(default_factory=set)
    scope_reason: str = ""


def build_concepts(inv: Inventory, identifiers: list[str]) -> list[Concept]:
    concepts = []
    for tid in identifiers:
        row = inv.taxa.get(tid)
        if row is None:
            raise SystemExit(f"{tid} is not in data/raw/ncbitaxon_taxa.tsv; re-extract or fix the scope")
        if not inv.is_species_or_below(tid):
            raise SystemExit(
                f"{tid} ({row['label']}, rank {row['rank'] or 'NO_RANK'}) is above species level. "
                "TaxonMech records are species and strains only; higher taxa appear as lineage entries. "
                "Remove it from curation/seed_scope.tsv."
            )
        c = Concept(tid, row["label"], row["rank"] or "NO_RANK", inv.domain(tid), row)
        c.sources = set(split(row["attested_by"]))
        if inv.gtdb.get(tid):
            c.sources.add("gtdb")
        concepts.append(c)
    return concepts


def _bool(value: str) -> bool | None:
    return {"1": True, "0": False}.get(value)


def build_document(concept: Concept, inv: Inventory) -> dict[str, Any]:
    tid = concept.identifier
    row = concept.row
    doc: dict[str, Any] = {
        "identifier": tid,
        "label": concept.label,
        "rank": concept.rank,
        "taxon_domain": concept.domain,
    }
    if row.get("parent_id"):
        doc["parent_taxon"] = row["parent_id"]
    lineage = inv.lineage(tid)
    if lineage:
        doc["lineage"] = [
            {"taxon_id": a, "taxon_label": inv.taxa[a]["label"], "rank": inv.taxa[a]["rank"] or "NO_RANK"}
            for a in lineage
        ]
    doc["grounding_status"] = "EXACT"
    doc["mapping_status"] = "DEPRECATED" if row.get("retired_into") else "SEEDED"
    if not hasattr(inv, "_replaces"):
        inv._replaces = defaultdict(list)
        for old, old_row in inv.taxa.items():
            successor = old_row.get("retired_into", "")
            if successor.startswith("NCBITaxon:"):
                inv._replaces[successor].append(old)
    if inv._replaces.get(tid):
        doc["replaces"] = sorted(inv._replaces[tid], key=id_key)

    # --- synonyms -----------------------------------------------------------
    synonyms: dict[tuple[str, str, str], dict[str, str]] = {}

    def add_syn(text: str, kind: str, source: str, source_id: str = "") -> None:
        if not text or text == concept.label:
            return
        key = (text, kind, source)
        if key not in synonyms:
            entry = {"synonym_text": text, "synonym_type": kind, "source": source}
            if source_id:
                entry["source_id"] = source_id
            synonyms[key] = entry

    for kind, column in (("EXACT_SYNONYM", "exact_synonyms"), ("RELATED_SYNONYM", "related_synonyms"),
                         ("BROAD_SYNONYM", "broad_synonyms")):
        for text in split(row.get(column, "")):
            add_syn(text, kind, "NCBITaxon")

    # --- nomenclature (LPSN) ---------------------------------------------------
    nomenclature = []
    xrefs: set[str] = set()
    type_strain_ids: set[str] = set()
    for lid in sorted(inv.lpsn_by_taxon.get(tid, []), key=lambda x: int(x.split(":")[1])):
        name = inv.lpsn[lid]
        entry: dict[str, Any] = {"source": "LPSN", "name_id": lid, "name": name["name"]}
        if name.get("rank"):
            entry["rank"] = name["rank"]
        if name.get("authority"):
            entry["authority"] = name["authority"]
        if name.get("status"):
            entry["nomenclatural_status"] = name["status"]
        for key in ("validly_published", "legitimate", "is_correct_name"):
            flag = _bool(name.get(key, ""))
            if flag is not None:
                entry[key] = flag
        if name.get("url"):
            entry["url"] = name["url"]
        designations = split(name.get("type_strain_ids", ""))
        if designations:
            entry["type_strain_designations"] = designations
            type_strain_ids.update(designations)
        # LPSN cites DOIs as `doi:`; the Mech family writes references as `DOI:`.
        pubs = sorted({("DOI:" + p[4:]) if p.startswith("doi:") else p
                       for p in split(name.get("publications", ""))})
        if pubs:
            entry["publications"] = pubs
        seqs = split(name.get("sequence_accessions", ""))
        if seqs:
            entry["sequence_accessions"] = seqs
        if name.get("deprecated") == "1":
            entry["notes"] = "LPSN marks this name deprecated (a synonym of a later correct name)."
        nomenclature.append(entry)
        if name.get("is_correct_name") == "1" and name.get("deprecated") != "1":
            xrefs.add(lid)
        current = name.get("is_correct_name") == "1" and name.get("deprecated") != "1"
        if name["name"] != concept.label:
            # A name LPSN lists as a synonym is usually heterotypic (a
            # different type strain), which is not an exact synonym (#7).
            add_syn(name["name"], "EXACT_SYNONYM" if current else "RELATED_SYNONYM", "LPSN", lid)
        # Names LPSN links with same_as, in either direction: kg-microbe
        # points the edge from the synonym to the correct name (#3).
        for other in split(name.get("synonyms", "")) + split(name.get("synonym_of", "")):
            other_row = inv.lpsn.get(other)
            if other_row and other_row["name"]:
                add_syn(other_row["name"], "RELATED_SYNONYM", "LPSN", other)
        # LPSN's own GTDB mapping is an equivalence claim about this name.
        for gid in split(name.get("gtdb_ids", "")):
            xrefs.add(gid)
    if nomenclature:
        doc["nomenclature"] = nomenclature

    # --- taxonomy mappings (GTDB) ----------------------------------------------
    # kg-microbe emits skos:closeMatch for a 1:1 GTDB<->NCBI species mapping and
    # skos:broadMatch whenever several GTDB species pool onto one NCBI taxon
    # (a genome NCBI labels as this taxon that GTDB places in another species).
    # A broadMatch is therefore a pooling signal, not an identity claim: the
    # GTDB species that IS this taxon is the one LPSN links to its name, or a
    # 1:1 closeMatch. Those come first and are the only ones that become
    # xrefs or synonyms.
    lpsn_gtdb = {g for lid in inv.lpsn_by_taxon.get(tid, [])
                 for g in split(inv.lpsn[lid].get("gtdb_ids", ""))}
    mappings = []
    for m in inv.gtdb.get(tid, []):
        identity = m["gtdb_id"] in lpsn_gtdb or m["predicate"] == "skos:closeMatch"
        entry: dict[str, Any] = {
            "source": "GTDB",
            "source_id": m["gtdb_id"],
            "source_label": m["gtdb_label"],
            "mapping_predicate": m["predicate"],
            "genome_count": int(m["genome_count"]),
        }
        if m["gtdb_id"] in lpsn_gtdb:
            entry["notes"] = "LPSN links this GTDB species to the taxon's name."
        elif m["predicate"] == "skos:broadMatch":
            entry["notes"] = ("Pooled: GTDB places genomes NCBI labels as this taxon in this species, "
                              "which also maps to other NCBI taxa (kg-microbe broadMatch).")
        mappings.append((not identity, m["gtdb_id"] not in lpsn_gtdb, -int(m["genome_count"]),
                         m["gtdb_id"], entry))
        if identity:
            xrefs.add(m["gtdb_id"])
            add_syn(m["gtdb_label"].split("__", 1)[-1].replace("_", " "), "EXACT_SYNONYM", "GTDB",
                    m["gtdb_id"])
    mappings.sort(key=lambda t: t[:4])
    mappings = [t[4] for t in mappings]
    if mappings:
        doc["taxonomy_mappings"] = mappings

    if synonyms:
        doc["synonyms"] = sorted(synonyms.values(), key=lambda s: (s["synonym_text"], s["source"]))
    if xrefs:
        doc["xrefs"] = sorted(xrefs)
    if row.get("genetic_code"):
        doc["genetic_code"] = int(row["genetic_code"])

    # --- strains (BacDive) ------------------------------------------------------
    # BacDive files a type strain under a strain-level taxon ("Acinetobacter
    # baumannii ATCC 19606 = CIP 70.34") at least as often as under the
    # species, so a record gathers the strains of its whole NCBI subtree.
    # Every record is species-level or below, so the subtree is small.
    strain_sources: list[tuple[str, dict[str, str]]] = [(tid, s) for s in inv.strains.get(tid, [])]
    descendant_taxa: list[str] = []
    for desc in inv.descendants(tid):
        rows = inv.strains.get(desc, [])
        if rows:
            descendant_taxa.append(desc)
            strain_sources.extend((desc, s) for s in rows)
    seen_strains: set[str] = set()
    strain_rows = []
    entries = []
    for filed_under, s in strain_sources:
        if s["strain_id"] in seen_strains:
            continue
        seen_strains.add(s["strain_id"])
        strain_rows.append(s)
        ccs = split(s.get("culture_collection_ids", ""))
        entry: dict[str, Any] = {
            "strain_id": s["strain_id"],
            "source": "BACDIVE",
            "source_id": f"bacdive:{s['bacdive_id']}",
        }
        if s.get("designation"):
            entry["designation"] = s["designation"]
        if filed_under != tid:
            entry["classified_as"] = filed_under
        if ccs:
            entry["culture_collection_ids"] = ccs
        if type_strain_ids & set(ccs):
            entry["is_type_strain"] = True
        if s.get("medium_count") and int(s["medium_count"]):
            entry["medium_count"] = int(s["medium_count"])
        assemblies = inv.strain_assemblies.get(s["strain_id"], [])
        if assemblies:
            entry["genome_assemblies"] = [
                {key: value for key, value in assembly.items() if key != "strain_id" and value}
                for assembly in assemblies
            ]
        genome_records = inv.strain_genome_records.get(s["strain_id"], [])
        if genome_records:
            entry["genome_records"] = [
                {key: value for key, value in genome.items() if key != "strain_id" and value}
                for genome in genome_records
            ]
        related_records = inv.strain_related_records.get(s["strain_id"], [])
        if related_records:
            entry["related_records"] = [
                {key: value for key, value in related.items() if key != "strain_id" and value}
                for related in related_records
            ]
        entries.append(entry)
    # Type strains first, then the best-deposited, then by BacDive id.
    entries.sort(key=lambda e: (
        not e.get("is_type_strain", False),
        -len(e.get("culture_collection_ids") or []),
        int(e["source_id"].split(":")[1]),
    ))
    doc["strain_count"] = len(entries)
    if entries:
        doc["strains"] = entries[:STRAIN_LISTING_CAP]

    # --- source attestations ----------------------------------------------------
    attestations: list[dict[str, Any]] = [{
        "source": "NCBITAXON",
        "source_id": tid,
        "source_label": concept.label,
        "assertion_count": 1,
        "assertion_unit": "NAME",
    }]
    if row.get("taxonomy_snapshot"):
        attestations[0]["notes"] = f"NCBI taxonomy snapshot: {row['taxonomy_snapshot']}."
    if row.get("retired_into"):
        successor = row["retired_into"]
        attestations[0]["notes"] = (
            "Retired NCBI identifier; "
            f"{'merged into ' + successor if successor != 'deleted' else 'deleted by NCBI'}. "
            f"Prior taxonomy values retained from {row.get('taxonomy_snapshot', 'the preceding inventory')}."
        )
    if nomenclature:
        correct = [n for n in nomenclature if n.get("is_correct_name")]
        chosen = correct[0] if correct else nomenclature[0]
        attestations.append({
            "source": "LPSN",
            "source_id": chosen["name_id"],
            "source_label": chosen["name"],
            "mapping_predicate": "skos:closeMatch",
            "assertion_count": len(nomenclature),
            "assertion_unit": "NAME",
        })
    if mappings:
        primary = mappings[0]
        pooled = len(mappings) - 1
        attestations.append({
            "source": "GTDB",
            "source_id": primary["source_id"],
            "source_label": primary["source_label"],
            "mapping_predicate": primary["mapping_predicate"],
            # Genomes of the primary species only: the pooled species' genomes
            # belong to other taxa and summing them would inflate the number.
            "assertion_count": primary["genome_count"],
            "assertion_unit": "GENOME",
            **({"notes": f"{pooled} further GTDB species pool onto this taxon by broadMatch; "
                          "see taxonomy_mappings."} if pooled else {}),
        })
    if strain_rows or inv.cc_strains.get(tid):
        deposits = {c for s in strain_rows for c in split(s.get("culture_collection_ids", ""))}
        cc_only = [c for c in inv.cc_strains.get(tid, []) if c not in deposits]
        notes = []
        if descendant_taxa:
            from_desc = sum(1 for e in entries if e.get("classified_as"))
            notes.append(f"{from_desc} strains are filed under {len(descendant_taxa)} descendant "
                         "NCBI taxa (see classified_as).")
        if cc_only:
            notes.append(f"{len(cc_only)} further culture-collection deposits are classified here "
                         "without a BacDive entry of their own.")
        attestations.append({
            "source": "BACDIVE",
            "source_id": tid,
            "source_label": concept.label,
            "assertion_count": len(strain_rows),
            "assertion_unit": "STRAIN",
            **({"notes": " ".join(notes)} if notes else {}),
        })
    # These counts are direct-only: unlike strains, records filed under
    # descendant taxa are not gathered (#8; see docs/HARMONIZATION.md).
    direct = ({"notes": "Records filed directly under this taxon; descendant taxa are not gathered."}
              if inv.descendants(tid) else {})
    for source, table, unit, value in (
        ("MEDIADIVE", inv.media, "MEDIUM", lambda r: int(r["medium_count"])),
        ("GOLD", inv.gold, "ORGANISM", lambda n: n),
        ("MADIN", inv.madin, "TRAIT_ASSERTION", lambda n: n),
        ("BACTOTRAITS", inv.bacto, "TRAIT_ASSERTION", lambda n: n),
    ):
        if tid in table:
            attestations.append({
                "source": source,
                "source_id": tid,
                "source_label": concept.label,
                "assertion_count": value(table[tid]),
                "assertion_unit": unit,
                **direct,
            })
    doc["source_attestations"] = attestations

    sources = sorted({a["source"] for a in attestations})
    record_curation_event(
        doc,
        curator=SEED_CURATOR,
        action="SEEDED_FROM_SOURCES",
        changes=(
            "Seeded from data/raw/, data/atb/ and data/straininfo/ inventories; "
            f"attested by {', '.join(sources)}. "
            + (f"In scope: {concept.scope_reason}" if concept.scope_reason else "In scope: --all.")
        ),
        timestamp=SEED_TIMESTAMP,
    )
    overlay_graphs = inv.causal_graphs.get(tid)
    if overlay_graphs:
        doc["causal_graphs"] = [copy.deepcopy(g) for g in overlay_graphs]
        for event in inv.causal_graph_events.get(tid, []):
            record_curation_event(
                doc,
                curator=event.get("curator") or "curate-causal-graphs",
                action=event.get("action") or "ADDED_CAUSAL_GRAPHS",
                changes=event.get("changes"),
                llm_assisted=bool(event.get("llm_assisted", False)),
                timestamp=event.get("timestamp") or SEED_TIMESTAMP,
            )
    return doc


SEED_TIMESTAMP = _seed_timestamp()


# ---------------------------------------------------------------------------
# Filenames
# ---------------------------------------------------------------------------

def load_lockfile(path: Path = PATHS_LOCKFILE) -> dict[str, str]:
    """Read the committed identifier -> slug assignments.

    Missing file is not an error: the first seed of a fresh corpus mints every
    slug. Malformed or unsafe slugs ARE an error — the file is hand-editable,
    and a slug containing a path separator would write outside the corpus.
    """
    if not path.exists():
        return {}
    lock: dict[str, str] = {}
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for line_no, row in enumerate(reader, start=2):
            identifier = (row.get("identifier") or "").strip()
            slug = (row.get("slug") or "").strip()
            if not identifier or not slug:
                raise SystemExit(f"{path}:{line_no}: blank identifier or slug")
            if not SLUG_PATTERN.match(slug):
                raise SystemExit(
                    f"{path}:{line_no}: unsafe slug {slug!r} — slugs must match "
                    f"{SLUG_PATTERN.pattern} so they cannot escape {TAXA_DIR.name}/"
                )
            if identifier in lock:
                raise SystemExit(f"{path}:{line_no}: duplicate identifier {identifier}")
            lock[identifier] = slug
    taken: dict[str, str] = {}
    for identifier, slug in lock.items():
        if slug in taken:
            raise SystemExit(f"{path}: slug {slug!r} claimed by both {taken[slug]} and {identifier}")
        taken[slug] = identifier
    return lock


def write_lockfile(assignments: dict[str, str], path: Path = PATHS_LOCKFILE) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["identifier", "slug"], delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for identifier in sorted(assignments):
            writer.writerow({"identifier": identifier, "slug": assignments[identifier]})


def assign_paths(concepts: list[Concept], lockfile: dict[str, str] | None = None
                 ) -> tuple[dict[str, Path], dict[str, str]]:
    """Map each concept to its output file. Returns (paths, slug assignments).

    Filenames are pinned by ``data/taxa/PATHS.tsv``: a concept already in the
    lockfile keeps its slug, always; a new concept takes ``slugify(label)``, or
    ``<base>__<id hash>`` when that is taken (NCBI has homonyms across
    kingdoms, and the corpus will grow around every record). Slugs are unique
    corpus-wide, so a record moving between domain directories cannot collide.
    Renaming a record is a deliberate edit to PATHS.tsv followed by a re-seed.
    """
    lockfile = lockfile or {}
    assignments: dict[str, str] = {}
    taken: set[str] = set()
    ordered = sorted(concepts, key=lambda c: c.identifier)
    for concept in ordered:
        slug = lockfile.get(concept.identifier)
        if slug is not None:
            assignments[concept.identifier] = slug
            taken.add(slug)
    for concept in ordered:
        if concept.identifier in assignments:
            continue
        base = slugify(concept.label)
        if base not in taken:
            slug = base
        else:
            suffix = hashlib.sha1(concept.identifier.encode()).hexdigest()[:8]
            slug = f"{base}__{suffix}"
            if slug in taken:
                raise SystemExit(f"slug collision for {concept.identifier}: both {base!r} and {slug!r} "
                                 f"are taken. Resolve by hand in {PATHS_LOCKFILE}.")
        assignments[concept.identifier] = slug
        taken.add(slug)
    paths = {c.identifier: TAXA_DIR / c.domain.lower() / f"{assignments[c.identifier]}.yaml" for c in ordered}
    return paths, assignments


def find_stale_files(expected: set[Path]) -> list[Path]:
    return sorted(p for p in TAXA_DIR.rglob("*.yaml") if p not in expected)


# ---------------------------------------------------------------------------
# Corpus
# ---------------------------------------------------------------------------

@dataclass
class Corpus:
    concepts: list[Concept]
    inventory: Inventory
    scope: dict[str, dict[str, str]]


def build_corpus(*, everything: bool = False) -> Corpus:
    inv = load_inventory()
    scope = load_scope()
    if everything:
        identifiers = sorted(
            (
                t
                for t, r in inv.taxa.items()
                if inv.is_species_or_below(t)
                and (r.get("attested_by") or inv.has_attested_descendant(t))
            ),
            key=id_key,
        )
    else:
        identifiers = sorted(scope, key=id_key)
    concepts = build_concepts(inv, identifiers)
    for c in concepts:
        c.scope_reason = scope.get(c.identifier, {}).get("reason", "")
    return Corpus(concepts, inv, scope)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--apply", action="store_true", help="Write files (default is a dry-run report).")
    parser.add_argument("--force", action="store_true", help="Overwrite records that already exist.")
    parser.add_argument("--prune", action="store_true",
                        help="Delete record files the current assignment does not account for. "
                             "Ignored on --only/--limit runs, whose path set is not authoritative.")
    parser.add_argument("--only", nargs="*", metavar="IDENTIFIER",
                        help="Seed only these identifiers (they must be in scope, or pass --all). "
                             "Use for the one-record canary before a bulk run.")
    parser.add_argument("--limit", type=int, help="Seed at most N records (after sorting by identifier).")
    parser.add_argument("--all", action="store_true",
                        help="Seed every attested species-or-below taxon in the inventory, "
                             "not just curation/seed_scope.tsv.")
    args = parser.parse_args(argv)

    corpus = build_corpus(everything=args.all)
    concepts = corpus.concepts
    inv = corpus.inventory

    print("=== scope ===")
    print(f"  taxa in inventory:     {len(inv.taxa)} "
          f"({sum(1 for r in inv.taxa.values() if r.get('attested_by'))} attested)")
    print(f"  taxa in scope:         {len(concepts)}" + (" (--all)" if args.all else
          f" (from {SCOPE_PATH.relative_to(REPO_ROOT)})"))
    print("\n=== domain ===")
    for domain, count in Counter(c.domain for c in concepts).most_common():
        print(f"  {domain:12s} {count:6d}")
    print("\n=== rank ===")
    for rank, count in Counter(c.rank for c in concepts).most_common():
        print(f"  {rank:16s} {count:6d}")
    print("\n=== sources per record ===")
    for n, count in sorted(Counter(len(c.sources | {"ncbitaxon"}) for c in concepts).items()):
        print(f"  {n} source(s)        {count:6d}")

    selected = concepts
    if args.only:
        wanted = set(args.only)
        selected = [c for c in concepts if c.identifier in wanted]
        missing = wanted - {c.identifier for c in selected}
        if missing:
            print(f"\nERROR: --only identifiers not in scope: {', '.join(sorted(missing))}", file=sys.stderr)
            return 2
    if args.limit:
        selected = sorted(selected, key=lambda c: c.identifier)[: args.limit]

    lockfile = load_lockfile()
    paths, assignments = assign_paths(concepts, lockfile)
    full_run = not args.only and not args.limit
    inherited = sum(1 for i in assignments if i in lockfile)
    stale = find_stale_files(set(paths.values())) if TAXA_DIR.exists() else []

    print("\n=== filename assignment ===")
    print(f"  pinned by {PATHS_LOCKFILE.relative_to(REPO_ROOT)}: {inherited}")
    print(f"  newly minted:                 {len(assignments) - inherited}")
    if stale:
        print(f"  stale files (record left scope, or moved domain): {len(stale)}")
        for path in stale[:5]:
            print(f"    {path.relative_to(REPO_ROOT)}")
        if not full_run:
            print("    (partial run — not pruning; re-run a full seed to reconcile)")
        elif not args.prune:
            print("    (pass --prune to delete them)")

    if not args.apply:
        print(f"\n--dry-run: would write {len(selected)} record(s) under {TAXA_DIR.relative_to(REPO_ROOT)}")
        for concept in sorted(selected, key=lambda c: c.identifier)[:5]:
            print(f"  {concept.identifier:24s} -> {paths[concept.identifier].relative_to(REPO_ROOT)}")
        if len(selected) > 5:
            print(f"  ... and {len(selected) - 5} more")
        print("\nRun with --apply to write. Seed one record first: --apply --only <IDENTIFIER>")
        return 0

    written = skipped = failed = 0
    for concept in sorted(selected, key=lambda c: c.identifier):
        path = paths[concept.identifier]
        if path.exists() and not args.force:
            skipped += 1
            continue
        doc = build_document(concept, inv)
        try:
            write_validated_taxon(doc, path)
        except ValidationFailedError as exc:
            failed += 1
            print(f"\nFAILED {concept.identifier} -> {path}", file=sys.stderr)
            print(exc.summary(), file=sys.stderr)
            if failed >= 5:
                print("\naborting after 5 validation failures", file=sys.stderr)
                return 1
            continue
        written += 1

    if full_run:
        write_lockfile(assignments)
        print(f"wrote {PATHS_LOCKFILE.relative_to(REPO_ROOT)} ({len(assignments)} assignments)")
    else:
        print(f"partial run — {PATHS_LOCKFILE.relative_to(REPO_ROOT)} left unchanged")

    pruned = 0
    if stale and full_run and args.prune:
        for path in stale:
            path.unlink()
            pruned += 1
        for directory in sorted(TAXA_DIR.rglob("*"), reverse=True):
            if directory.is_dir() and not any(directory.iterdir()):
                directory.rmdir()
        print(f"pruned {pruned} stale record file(s)")

    print(f"\nwrote {written}, skipped {skipped} (already present; --force to overwrite), failed {failed}")
    if stale and not pruned:
        print(f"WARNING: {len(stale)} stale file(s) remain on disk.", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
