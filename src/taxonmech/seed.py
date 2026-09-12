#!/usr/bin/env python3
"""Seed TaxonRecords from the inventories in data/raw/.

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
candidates for it. ``--all`` seeds the whole attested universe instead, for a
future full corpus.

Usage
-----
    python3 scripts/seed_from_sources.py                     # dry-run report
    python3 scripts/seed_from_sources.py --apply --only NCBITaxon:562   # canary
    python3 scripts/seed_from_sources.py --apply             # the scoped corpus
    python3 scripts/seed_from_sources.py --apply --force     # also overwrite
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "src"))

from taxonmech.curate.curation_event import record_curation_event  # noqa: E402
from taxonmech.validation.write_validated import (  # noqa: E402
    ValidationFailedError,
    write_validated_taxon,
)

RAW_DIR = REPO_ROOT / "data" / "raw"
TAXA_DIR = REPO_ROOT / "data" / "taxa"
SCOPE_PATH = REPO_ROOT / "curation" / "seed_scope.tsv"
PATHS_LOCKFILE = TAXA_DIR / "PATHS.tsv"

SEED_CURATOR = "seed_from_sources"

# Strains listed per record. The count is always the full number; the listing
# is capped so a species with thousands of BacDive entries stays a readable
# record. Type strains come first.
STRAIN_LISTING_CAP = 200

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

    Taken from data/raw/MANIFEST.yaml rather than now(): the corpus must be
    byte-reproducible, so a wall-clock stamp would make every re-seed a
    corpus-wide diff. The manifest's extracted_at is the honest answer to
    "when is this data from", and it changes only when the data does.
    """
    manifest = RAW_DIR / "MANIFEST.yaml"
    if manifest.exists():
        for line in manifest.read_text(encoding="utf-8").splitlines():
            if line.startswith("extracted_at:"):
                return line.split(":", 1)[1].strip().strip("'\"")
    return "1970-01-01T00:00:00Z"


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
    strain_assemblies: dict[str, list[dict[str, str]]] = field(default_factory=dict)
    strain_genome_records: dict[str, list[dict[str, str]]] = field(default_factory=dict)
    strain_related_records: dict[str, list[dict[str, str]]] = field(default_factory=dict)

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

    def domain(self, tid: str) -> str:
        for ancestor in [tid, *self.lineage(tid)]:
            if ancestor in DOMAIN_ROOTS:
                return DOMAIN_ROOTS[ancestor]
        return "OTHER"


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
    strain_assemblies: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in read_tsv("strain_assemblies.tsv"):
        strain_assemblies[r["strain_id"]].append(r)
    strain_genome_records: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in read_tsv("strain_genome_records.tsv"):
        strain_genome_records[r["strain_id"]].append(r)
    strain_related_records: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in read_tsv("strain_related_records.tsv"):
        strain_related_records[r["strain_id"]].append(r)
    return Inventory(taxa, gtdb, lpsn, lpsn_by_taxon, strains, cc_strains, media, gold, madin, bacto,
                     strain_assemblies, strain_genome_records, strain_related_records)


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
    doc["mapping_status"] = "SEEDED"

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
            f"Seeded from data/raw/ inventories; attested by {', '.join(sources)}. "
            + (f"In scope: {concept.scope_reason}" if concept.scope_reason else "In scope: --all.")
        ),
        timestamp=SEED_TIMESTAMP,
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
        identifiers = sorted((t for t, r in inv.taxa.items()
                              if r.get("attested_by") and inv.is_species_or_below(t)), key=id_key)
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
    for n, count in sorted(Counter(len(c.sources) + 1 for c in concepts).items()):
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
