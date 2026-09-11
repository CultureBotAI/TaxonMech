#!/usr/bin/env python3
"""Extract taxon and strain inventories from a kg-microbe checkout.

TaxonMech does not vendor kg-microbe's multi-gigabyte KGX dumps. It vendors
the *inventories* derived from them — small, reviewable TSVs under
``data/raw/`` that name every taxon the strain-bearing sources speak about,
what each source says, and how much data sits behind it. Those TSVs are the
seed input for ``scripts/seed_from_sources.py``; seeding, validation and tests
run from them without kg-microbe present.

Sources read (all under the kg-microbe checkout):

* ``data/transformed/ontologies/ncbitaxon_{nodes,edges}.tsv`` — NCBI Taxonomy
  labels, parents (``biolink:subclass_of``) and the GC_ID genetic-code xref.
* ``data/raw/ncbitaxon.db`` — the semantic-sql build of ncbitaxon.owl, read
  only for ``has_rank`` and typed synonyms, which the KGX transform drops.
* ``data/transformed/gtdb/{nodes,edges}.tsv`` — GTDB species, the assemblies
  under them, and their ``close_match`` / ``broad_match`` edges to NCBI taxa.
* ``data/transformed/lpsn/{nodes,edges}.tsv`` — LPSN names with authority and
  rank, ``close_match`` to NCBI taxa, GTDB species and type-strain deposits,
  ``same_as`` to synonymous names.
* ``data/transformed/lpsn_api/{nodes,edges}.tsv`` — nomenclatural status,
  cited publications and INSDC sequence accessions per name.
* ``data/transformed/bacdive/{nodes,edges}.tsv`` — BacDive strains, their
  NCBI and LPSN parents, and their culture-collection deposits.
* ``data/raw/bacdive_strains.json`` — strain-to-assembly assertions that
  the BacDive KGX transform does not carry.
* ``data/transformed/mediadive/edges.tsv`` — growth media per taxon / strain.
* ``data/transformed/gold/edges.tsv`` — GOLD organisms per taxon.
* ``data/transformed/madin_etal/edges.tsv``, ``bactotraits/edges.tsv`` —
  trait assertions per taxon.

The **universe** of taxa inventoried is every NCBI taxon that at least one of
BacDive, LPSN, MediaDive, GOLD, Madin or BactoTraits attests, plus every
ancestor of those. GTDB mappings are kept only where they land inside that
universe: GTDB alone maps 322k species to strain-level NCBI taxa nothing else
mentions, and inventorying those would triple the corpus for no attestation.

Usage
-----
    python3 scripts/extract_source_inventory.py --kg-microbe /path/to/kg-microbe
    python3 scripts/extract_source_inventory.py --dry-run     # counts only, no writes
"""

from __future__ import annotations

import argparse
import csv
import datetime
import hashlib
import os
import re
import sqlite3
import subprocess
import sys
from collections import Counter, defaultdict
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import ijson
import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = REPO_ROOT / "data" / "raw"
CONF_PATH = REPO_ROOT / "conf" / "sources.yaml"

MANIFEST_NAME = "MANIFEST.yaml"

# The kg-microbe predicate MediaDive uses for "grows in".
GROWS_IN = "METPO:2000517"

# NCBI domains, for the lineage-derived filesystem bucket.
DOMAIN_ROOTS = {
    "NCBITaxon:2": "BACTERIA",
    "NCBITaxon:2157": "ARCHAEA",
    "NCBITaxon:2759": "EUKARYOTA",
    "NCBITaxon:10239": "VIRUSES",
}

ATTESTING_SOURCES = ("bacdive", "lpsn", "mediadive", "gold", "madin_etal", "bactotraits")

_STRAIN_NAME = re.compile(r"^bacdive_(?P<id>\d+) (?:as (?P<designation>.+?) of|strain of) NCBITaxon:\d+$")
_LPSN_URL_RANK = re.compile(r"^https://lpsn\.dsmz\.de/(?P<rank>[a-z]+)/")
_ASSEMBLY_ACCESSION = re.compile(r"GC[AF]_[0-9]{9}(?:\.[1-9][0-9]*)?")
ASSEMBLY_FIELDS = [
    "strain_id", "assembly_id", "source", "source_id", "source_reference_id",
    "assembly_level", "assembly_name", "taxon_id",
]


# csv's default field-size limit (128 KiB) is smaller than some kg-microbe
# synonym cells. Raise it to the platform maximum rather than letting the
# reader raise mid-stream on one long row.
def _raise_csv_limit() -> None:
    limit = sys.maxsize
    while True:
        try:
            csv.field_size_limit(limit)
            return
        except OverflowError:
            limit //= 2


_raise_csv_limit()


def read_tsv(path: Path) -> Iterator[dict[str, str]]:
    """Stream a KGX-style TSV as dicts. Raises if the file is missing."""
    if not path.exists():
        raise FileNotFoundError(f"required source file not found: {path}")
    with path.open(newline="", encoding="utf-8") as fh:
        yield from csv.DictReader(fh, delimiter="\t")


def write_tsv(path: Path, fieldnames: list[str], rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, delimiter="\t",
                                extrasaction="raise", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: ("" if row.get(k) is None else row.get(k)) for k in fieldnames})


def sha256_of(path: Path, chunk: int = 1 << 20) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        while block := fh.read(chunk):
            digest.update(block)
    return digest.hexdigest()


def joined(values) -> str:
    return "|".join(sorted(set(v for v in values if v)))


# ---------------------------------------------------------------------------
# NCBI Taxonomy
# ---------------------------------------------------------------------------

def load_ncbitaxon(kgm: Path) -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    """Return (nodes, parents): every NCBI taxon's label and GC_ID, and its parent."""
    nodes: dict[str, dict[str, Any]] = {}
    for row in read_tsv(kgm / "data/transformed/ontologies/ncbitaxon_nodes.tsv"):
        tid = row["id"]
        if not tid.startswith("NCBITaxon:"):
            continue
        gc = ""
        for xref in (row.get("xref") or "").split("|"):
            if xref.startswith("GC_ID:"):
                gc = xref.split(":", 1)[1]
        nodes[tid] = {"label": row.get("name") or "", "genetic_code": gc}
    parents: dict[str, str] = {}
    for row in read_tsv(kgm / "data/transformed/ontologies/ncbitaxon_edges.tsv"):
        if row["predicate"] == "biolink:subclass_of" and row["subject"].startswith("NCBITaxon:"):
            parents[row["subject"]] = row["object"]
    return nodes, parents


def load_ranks_and_synonyms(db_path: Path) -> tuple[dict[str, str], dict[str, dict[str, list[str]]]]:
    """Read has_rank and typed synonyms from the semantic-sql NCBITaxon build.

    The KGX transform carries neither rank nor synonym scope, and both are what
    make a taxon record readable, so these fields come directly from the raw
    (non-transformed) kg-microbe input.
    """
    if not db_path.exists():
        raise FileNotFoundError(
            f"NCBITaxon semantic-sql build not found: {db_path} (needed for ranks)"
        )
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        ranks: dict[str, str] = {}
        for subject, obj in conn.execute(
            "SELECT subject, object FROM statements WHERE predicate='obo:ncbitaxon#has_rank'"
        ):
            ranks[subject] = _rank_enum(obj)
        synonyms: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
        for pred, scope in (("oio:hasExactSynonym", "EXACT_SYNONYM"),
                            ("oio:hasRelatedSynonym", "RELATED_SYNONYM"),
                            ("oio:hasBroadSynonym", "BROAD_SYNONYM")):
            for subject, value in conn.execute(
                "SELECT subject, value FROM statements WHERE predicate=?", (pred,)
            ):
                if value:
                    synonyms[subject][scope].append(value)
    finally:
        conn.close()
    return ranks, synonyms


def _rank_enum(value: str) -> str:
    """``NCBITaxon:species`` -> ``SPECIES``; ``obo:NCBITaxon#_species_group`` -> ``SPECIES_GROUP``."""
    local = value.rsplit(":", 1)[-1]
    local = local.split("#_", 1)[-1] if "#_" in local else local
    return local.upper()


def ancestors_of(taxa: set[str], parents: dict[str, str]) -> set[str]:
    out: set[str] = set()
    for tid in taxa:
        cur = parents.get(tid)
        while cur and cur not in out:
            out.add(cur)
            cur = parents.get(cur)
    return out


# ---------------------------------------------------------------------------
# Attesting sources
# ---------------------------------------------------------------------------

def extract_bacdive_assemblies(
    path: Path, strain_ids: set[str],
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Keep explicit BacDive strain-to-NCBI-assembly assertions, without inference.

    Read only ``Genome sequences``; 16S accessions, chromosome sequences,
    WGS projects, PATRIC and IMG identifiers are not NCBI assembly IDs.
    Keep missing versions missing, and never manufacture a GCF from a GCA.
    A row is an assertion by BacDive, not proof of identical isolates or an
    equivalence between the assembly and the strain's culture deposits.
    """
    rows: dict[tuple[str, ...], dict[str, str]] = {}
    dropped = []
    with path.open("rb") as fh:
        events = ijson.parse(fh)
        if next(events, None) != ("", "start_array", None):
            raise ValueError("BacDive source must be a JSON array of strain records")
        for record in ijson.items(events, "item"):
            if not isinstance(record, dict):
                raise ValueError("BacDive strain record must be an object")
            sequences = record.get("Sequence information")
            if sequences is None:
                continue
            if not isinstance(sequences, dict):
                raise ValueError("BacDive Sequence information must be an object")
            genomes = sequences.get("Genome sequences")
            if genomes is None:
                continue
            if isinstance(genomes, dict):
                genomes = [genomes]
            if not isinstance(genomes, list) or any(not isinstance(g, dict) for g in genomes):
                raise ValueError("BacDive Genome sequences must contain genome objects")
            for genome in genomes:
                accession = str(genome.get("accession") or "").strip()
                if not accession.startswith(("GCA_", "GCF_")):
                    continue
                bid = str((record.get("General") or {}).get("BacDive-ID") or "")
                if not bid.isdigit():
                    raise ValueError(f"assembly {accession}: missing or invalid BacDive-ID {bid!r}")
                sid = f"kgmicrobe.strain:bacdive_{bid}"
                reason = ""
                if not _ASSEMBLY_ACCESSION.fullmatch(accession):
                    reason = "malformed NCBI assembly accession in BacDive Genome sequences"
                elif sid not in strain_ids:
                    reason = "BacDive strain absent from bacdive_strains.tsv"
                if reason:
                    dropped.append({"kind": "bacdive_assembly", "id": f"{sid}/{accession}",
                                    "reason": reason})
                    continue
                taxon = str(genome.get("NCBI tax ID") or "")
                ref = str(genome.get("@ref") or "")
                if taxon and not taxon.isdigit():
                    raise ValueError(f"{sid}/{accession}: invalid NCBI tax ID {taxon!r}")
                if ref and not ref.isdigit():
                    raise ValueError(f"{sid}/{accession}: invalid BacDive reference ID {ref!r}")
                row = {
                    "strain_id": sid,
                    "assembly_id": f"ncbi.assembly:{accession}",
                    "source": "BACDIVE",
                    "source_id": f"bacdive:{bid}",
                    "source_reference_id": ref,
                    "assembly_level": str(genome.get("assembly level") or ""),
                    "assembly_name": str(genome.get("description") or ""),
                    "taxon_id": f"NCBITaxon:{taxon}" if taxon else "",
                }
                # Deduplicate only identical assertions. Distinct references,
                # versions and conflicting source metadata remain visible.
                rows[tuple(row[field] for field in ASSEMBLY_FIELDS)] = row
    return [rows[key] for key in sorted(rows)], sorted(dropped, key=lambda r: (r["id"], r["reason"]))


def extract_bacdive(kgm: Path) -> tuple[dict[str, dict[str, Any]], dict[str, set[str]]]:
    """Return (strains, cc_parents).

    ``strains`` is keyed on the ``kgmicrobe.strain:bacdive_N`` id and carries
    the parsed designation, NCBI and LPSN parents, and culture-collection
    deposits (the ``kgmicrobe.strain:DSM-...`` ids it ``close_match``es).
    ``cc_parents`` maps a culture-collection strain id to its NCBI parents, so
    a type strain LPSN names can be placed even when no BacDive entry links
    it.
    """
    strains: dict[str, dict[str, Any]] = {}
    for row in read_tsv(kgm / "data/transformed/bacdive/nodes.tsv"):
        sid = row["id"]
        if not sid.startswith("kgmicrobe.strain:bacdive_"):
            continue
        name = row.get("name") or ""
        m = _STRAIN_NAME.match(name)
        strains[sid] = {
            "strain_id": sid,
            "bacdive_id": m.group("id") if m else sid.rsplit("_", 1)[-1],
            "designation": (m.group("designation") or "") if m else name,
            "taxon_ids": set(),
            "lpsn_ids": set(),
            "culture_collection_ids": set(),
            "medium_count": 0,
        }
    cc_parents: dict[str, set[str]] = defaultdict(set)
    for row in read_tsv(kgm / "data/transformed/bacdive/edges.tsv"):
        subject, predicate, obj = row["subject"], row["predicate"], row["object"]
        if not subject.startswith("kgmicrobe.strain:"):
            continue
        if subject in strains:
            if predicate == "biolink:subclass_of" and obj.startswith("NCBITaxon:"):
                strains[subject]["taxon_ids"].add(obj)
            elif predicate == "biolink:subclass_of" and obj.startswith("lpsn:"):
                strains[subject]["lpsn_ids"].add(obj)
            elif predicate == "biolink:close_match" and obj.startswith("kgmicrobe.strain:"):
                strains[subject]["culture_collection_ids"].add(obj)
        elif predicate == "biolink:subclass_of" and obj.startswith("NCBITaxon:"):
            cc_parents[subject].add(obj)
    return strains, cc_parents


def extract_mediadive(kgm: Path) -> tuple[dict[str, set[str]], Counter]:
    """Return (media per taxon, media count per strain)."""
    taxon_media: dict[str, set[str]] = defaultdict(set)
    strain_media: Counter = Counter()
    for row in read_tsv(kgm / "data/transformed/mediadive/edges.tsv"):
        if row["predicate"] != GROWS_IN:
            continue
        subject, obj = row["subject"], row["object"]
        if subject.startswith("NCBITaxon:"):
            taxon_media[subject].add(obj)
        elif subject.startswith("kgmicrobe.strain:"):
            strain_media[subject] += 1
    return taxon_media, strain_media


def count_subjects_by_object(path: Path, subject_prefix: str, predicate: str) -> Counter:
    counts: Counter = Counter()
    for row in read_tsv(path):
        if row["predicate"] == predicate and row["subject"].startswith(subject_prefix) \
                and row["object"].startswith("NCBITaxon:"):
            counts[row["object"]] += 1
    return counts


def count_taxon_subjects(path: Path) -> Counter:
    counts: Counter = Counter()
    for row in read_tsv(path):
        if row["subject"].startswith("NCBITaxon:"):
            counts[row["subject"]] += 1
    return counts


def extract_lpsn(kgm: Path) -> dict[str, dict[str, Any]]:
    names: dict[str, dict[str, Any]] = {}
    for row in read_tsv(kgm / "data/transformed/lpsn/nodes.tsv"):
        lid = row["id"]
        if not lid.startswith("lpsn:"):
            continue
        url = row.get("xref") or ""
        m = _LPSN_URL_RANK.match(url)
        names[lid] = {
            "lpsn_id": lid,
            "name": row.get("name") or "",
            "rank": m.group("rank").upper() if m else "",
            "authority": row.get("description") or "",
            "url": url,
            "deprecated": "1" if (row.get("deprecated") or "").strip().lower() == "true" else "0",
            "status": "",
            "validly_published": "",
            "legitimate": "",
            "is_correct_name": "",
            "parent_lpsn_id": "",
            "ncbitaxon_ids": set(),
            "gtdb_ids": set(),
            "type_strain_ids": set(),
            "synonym_of": set(),
            "synonyms": set(),
            "publications": set(),
            "sequence_accessions": set(),
        }
    for row in read_tsv(kgm / "data/transformed/lpsn/edges.tsv"):
        subject, predicate, obj = row["subject"], row["predicate"], row["object"]
        entry = names.get(subject)
        if entry is None:
            continue
        if predicate == "biolink:subclass_of" and obj.startswith("lpsn:"):
            entry["parent_lpsn_id"] = obj
        elif predicate == "biolink:close_match":
            if obj.startswith("NCBITaxon:"):
                entry["ncbitaxon_ids"].add(obj)
            elif obj.startswith("GTDB:"):
                entry["gtdb_ids"].add(obj)
            elif obj.startswith("kgmicrobe.strain:"):
                entry["type_strain_ids"].add(obj)
        elif predicate == "biolink:same_as" and obj.startswith("lpsn:"):
            # kg-microbe emits same_as from the deprecated name to the correct
            # one, so the correct name only learns its synonyms from the
            # reverse index (#3).
            entry["synonym_of"].add(obj)
            if obj in names:
                names[obj]["synonyms"].add(subject)
    # The API transform adds status, publications and sequence accessions.
    api_nodes = kgm / "data/transformed/lpsn_api/nodes.tsv"
    api_edges = kgm / "data/transformed/lpsn_api/edges.tsv"
    if api_nodes.exists():
        for row in read_tsv(api_nodes):
            entry = names.get(row["id"])
            if entry is None or row.get("category") != "biolink:OrganismTaxon":
                continue
            status = row.get("description") or ""
            entry["status"] = status
            entry["validly_published"] = "1" if "validly published" in status else "0"
            entry["legitimate"] = "1" if status.startswith("legitimate=True") else "0"
            entry["is_correct_name"] = "1" if "correct name" in status else "0"
        for row in read_tsv(api_edges):
            entry = names.get(row["subject"])
            if entry is None:
                continue
            obj = row["object"]
            if row["predicate"] == "biolink:close_match":
                if obj.startswith(("doi:", "PMID:")):
                    entry["publications"].add(obj)
                elif obj.startswith("INSDC:"):
                    entry["sequence_accessions"].add(obj)
            elif row["predicate"] == "biolink:same_as" and obj in names:
                # The API transform carries same_as pairs the main transform
                # lacks; a target the main transform does not name cannot
                # supply a synonym label and is skipped (#3).
                entry["synonym_of"].add(obj)
                names[obj]["synonyms"].add(row["subject"])
    return names


def extract_gtdb(kgm: Path) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    """Return (species nodes with parent + genome count, mapping rows to NCBI)."""
    species: dict[str, dict[str, Any]] = {}
    for row in read_tsv(kgm / "data/transformed/gtdb/nodes.tsv"):
        gid = row["id"]
        if gid.startswith("GTDB:s__"):
            species[gid] = {"label": row.get("name") or gid.split(":", 1)[1], "parent": "", "genomes": 0}
    mappings: list[dict[str, Any]] = []
    for row in read_tsv(kgm / "data/transformed/gtdb/edges.tsv"):
        subject, predicate, obj = row["subject"], row["predicate"], row["object"]
        if predicate == "biolink:subclass_of":
            if subject.startswith("ncbi.assembly:") and obj in species:
                species[obj]["genomes"] += 1
            elif subject in species and obj.startswith("GTDB:"):
                species[subject]["parent"] = obj
        elif predicate in ("biolink:close_match", "biolink:broad_match") and subject in species \
                and obj.startswith("NCBITaxon:"):
            mappings.append({"gtdb_id": subject, "ncbitaxon_id": obj,
                             "predicate": row.get("relation") or predicate})
    return species, mappings


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------

def git_head(path: Path) -> str:
    try:
        out = subprocess.run(["git", "rev-parse", "HEAD"], cwd=path, check=True,
                             capture_output=True, text=True, timeout=10).stdout.strip()
        return f"kg-microbe@{out}"
    except (OSError, subprocess.SubprocessError):
        return "kg-microbe@unknown"


def describe_input(kgm: Path, relative: str) -> dict[str, Any]:
    path = kgm / relative
    stat = path.stat()
    return {
        "path": relative,
        "bytes": stat.st_size,
        "mtime": datetime.datetime.fromtimestamp(stat.st_mtime, datetime.timezone.utc)
        .strftime("%Y-%m-%dT%H:%M:%SZ"),
        "sha256": sha256_of(path),
    }


def _unhashed_input(kgm: Path, relative: str) -> dict[str, Any]:
    path = kgm / relative
    stat = path.stat()
    return {
        "path": relative, "bytes": stat.st_size,
        "mtime": datetime.datetime.fromtimestamp(stat.st_mtime, datetime.timezone.utc)
        .strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def _extracted_at(previous_manifest: Path, inputs: list[dict[str, Any]]) -> str:
    """The data's timestamp, not the run's.

    Every record's seed event is stamped with this value, so a wall-clock
    stamp turns a re-extraction of unchanged data into a corpus-wide diff
    (#4). When the previous manifest hashed the same inputs to the same
    digests, the data has not changed and neither does its timestamp.
    """
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if not previous_manifest.exists() or any("sha256" not in i for i in inputs):
        return now
    previous = yaml.safe_load(previous_manifest.read_text(encoding="utf-8")) or {}
    old = {(i.get("path"), i.get("sha256")) for i in previous.get("inputs", []) if i.get("sha256")}
    new = {(i["path"], i["sha256"]) for i in inputs}
    if old == new and previous.get("extracted_at"):
        return str(previous["extracted_at"])
    return now


def describe_output(path: Path) -> dict[str, Any]:
    with path.open(newline="", encoding="utf-8") as fh:
        rows = sum(1 for _ in csv.reader(fh, delimiter="\t")) - 1
    return {"path": path.name, "rows": rows, "bytes": path.stat().st_size, "sha256": sha256_of(path)}


def resolve_kg_microbe(flag: str | None) -> Path:
    if flag:
        return Path(flag).expanduser().resolve()
    env = os.environ.get("KG_MICROBE_ROOT")
    if env:
        return Path(env).expanduser().resolve()
    conf = yaml.safe_load(CONF_PATH.read_text(encoding="utf-8")) or {}
    root = conf.get("kg_microbe_root")
    if not root:
        raise SystemExit("no kg-microbe checkout configured: pass --kg-microbe, set KG_MICROBE_ROOT, "
                         "or set kg_microbe_root in conf/sources.yaml")
    return Path(root).expanduser().resolve()


INPUTS = [
    "data/transformed/ontologies/ncbitaxon_nodes.tsv",
    "data/transformed/ontologies/ncbitaxon_edges.tsv",
    "data/raw/ncbitaxon.db",
    "data/transformed/gtdb/nodes.tsv",
    "data/transformed/gtdb/edges.tsv",
    "data/transformed/lpsn/nodes.tsv",
    "data/transformed/lpsn/edges.tsv",
    "data/transformed/lpsn_api/nodes.tsv",
    "data/transformed/lpsn_api/edges.tsv",
    "data/transformed/bacdive/nodes.tsv",
    "data/transformed/bacdive/edges.tsv",
    "data/raw/bacdive_strains.json",
    "data/transformed/mediadive/edges.tsv",
    "data/transformed/gold/edges.tsv",
    "data/transformed/madin_etal/edges.tsv",
    "data/transformed/bactotraits/edges.tsv",
]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--kg-microbe", help="Path to a kg-microbe checkout.")
    parser.add_argument("--out", type=Path, default=RAW_DIR, help="Where to write the inventories.")
    parser.add_argument("--dry-run", action="store_true", help="Report counts without writing files.")
    parser.add_argument("--skip-input-hashes", action="store_true",
                        help="Do not sha256 the inputs (the 14 GB ncbitaxon.db takes a while). "
                             "The manifest then records bytes and mtime only; use for a dry-run.")
    args = parser.parse_args(argv)

    kgm = resolve_kg_microbe(args.kg_microbe)
    print(f"kg-microbe checkout: {kgm} ({git_head(kgm)})")
    for relative in INPUTS:
        if not (kgm / relative).exists():
            raise SystemExit(f"missing input: {kgm / relative}")

    print("reading NCBI Taxonomy ...", flush=True)
    nodes, parents = load_ncbitaxon(kgm)
    print(f"  {len(nodes)} taxa, {len(parents)} subclass edges")
    ranks, synonyms = load_ranks_and_synonyms(kgm / "data/raw/ncbitaxon.db")
    print(f"  {len(ranks)} ranks, {len(synonyms)} taxa with typed synonyms")

    print("reading BacDive ...", flush=True)
    strains, cc_parents = extract_bacdive(kgm)
    print(f"  {len(strains)} BacDive strains, {len(cc_parents)} culture-collection ids with parents")
    print("reading MediaDive, GOLD, Madin, BactoTraits ...", flush=True)
    taxon_media, strain_media = extract_mediadive(kgm)
    for sid, n in strain_media.items():
        if sid in strains:
            strains[sid]["medium_count"] = n
    gold = count_subjects_by_object(kgm / "data/transformed/gold/edges.tsv", "gold:Go", "biolink:subclass_of")
    madin = count_taxon_subjects(kgm / "data/transformed/madin_etal/edges.tsv")
    bacto = count_taxon_subjects(kgm / "data/transformed/bactotraits/edges.tsv")
    print("reading LPSN ...", flush=True)
    lpsn = extract_lpsn(kgm)
    print(f"  {len(lpsn)} LPSN names")
    print("reading GTDB ...", flush=True)
    gtdb_species, gtdb_mappings = extract_gtdb(kgm)
    print(f"  {len(gtdb_species)} GTDB species, {len(gtdb_mappings)} mappings to NCBI")

    # --- the universe -----------------------------------------------------
    attested: dict[str, set[str]] = defaultdict(set)
    for strain in strains.values():
        for tid in strain["taxon_ids"]:
            attested[tid].add("bacdive")
    for tids in cc_parents.values():
        for tid in tids:
            attested[tid].add("bacdive")
    for entry in lpsn.values():
        for tid in entry["ncbitaxon_ids"]:
            attested[tid].add("lpsn")
    for tid in taxon_media:
        attested[tid].add("mediadive")
    for tid in gold:
        attested[tid].add("gold")
    for tid in madin:
        attested[tid].add("madin_etal")
    for tid in bacto:
        attested[tid].add("bactotraits")
    dropped_rows: list[dict[str, Any]] = []
    unknown = sorted(t for t in attested if t not in nodes)
    for t in unknown:
        dropped_rows.append({"kind": "attested_taxon", "id": t,
                             "reason": "not in the NCBITaxon transform (removed or merged id)"})
    if unknown:
        print(f"  WARNING: {len(unknown)} attested taxa are not in the NCBI transform "
              f"(e.g. {unknown[:3]}); they are dropped", file=sys.stderr)
        for t in unknown:
            attested.pop(t)
    dropped_attested = len(unknown)
    core = set(attested)
    lineage = ancestors_of(core, parents)
    universe = core | lineage
    print(f"\nuniverse: {len(core)} attested taxa + {len(lineage - core)} ancestors = {len(universe)}")
    for source in ATTESTING_SOURCES:
        print(f"  attested by {source:12s} {sum(1 for s in attested.values() if source in s):7d}")

    # --- rows -------------------------------------------------------------
    taxa_rows = []
    for tid in sorted(universe, key=lambda t: int(t.split(":")[1])):
        syn = synonyms.get(tid, {})
        taxa_rows.append({
            "taxon_id": tid,
            "label": nodes[tid]["label"],
            "rank": ranks.get(tid, "NO_RANK"),
            "parent_id": parents.get(tid, ""),
            "genetic_code": nodes[tid]["genetic_code"],
            "exact_synonyms": joined(syn.get("EXACT_SYNONYM", [])),
            "related_synonyms": joined(syn.get("RELATED_SYNONYM", [])),
            "broad_synonyms": joined(syn.get("BROAD_SYNONYM", [])),
            "attested_by": "|".join(s for s in ATTESTING_SOURCES if s in attested.get(tid, ())),
        })

    mapping_rows = []
    for m in gtdb_mappings:
        if m["ncbitaxon_id"] not in universe:
            continue
        sp = gtdb_species[m["gtdb_id"]]
        mapping_rows.append({
            "gtdb_id": m["gtdb_id"], "gtdb_label": sp["label"], "gtdb_parent": sp["parent"],
            "ncbitaxon_id": m["ncbitaxon_id"], "predicate": m["predicate"], "genome_count": sp["genomes"],
        })
    mapping_rows.sort(key=lambda r: (r["ncbitaxon_id"], r["gtdb_id"]))

    # LPSN names that map into the universe, plus the names they are
    # synonyms of / that are synonyms of them, so synonym labels resolve.
    lpsn_keep = {lid for lid, e in lpsn.items() if e["ncbitaxon_ids"] & universe}
    for lid in list(lpsn_keep):
        lpsn_keep.update(lpsn[lid]["synonym_of"])
    for lid, e in lpsn.items():
        if e["synonym_of"] & lpsn_keep:
            lpsn_keep.add(lid)
    lpsn_rows = []
    for lid in sorted(lpsn_keep, key=lambda x: int(x.split(":")[1])):
        e = lpsn[lid]
        lpsn_rows.append({
            "lpsn_id": lid, "name": e["name"], "rank": e["rank"], "authority": e["authority"],
            "url": e["url"], "deprecated": e["deprecated"], "status": e["status"],
            "validly_published": e["validly_published"], "legitimate": e["legitimate"],
            "is_correct_name": e["is_correct_name"], "parent_lpsn_id": e["parent_lpsn_id"],
            "ncbitaxon_ids": joined(e["ncbitaxon_ids"]), "gtdb_ids": joined(e["gtdb_ids"]),
            "type_strain_ids": joined(e["type_strain_ids"]), "synonym_of": joined(e["synonym_of"]),
            "synonyms": joined(e["synonyms"]),
            "publications": joined(e["publications"]),
            "sequence_accessions": joined(e["sequence_accessions"]),
        })

    strain_rows = []
    for sid in sorted(strains, key=lambda s: int(strains[s]["bacdive_id"])):
        s = strains[sid]
        if not s["taxon_ids"] & universe:
            dropped_rows.append({"kind": "bacdive_strain", "id": sid,
                                 "reason": ("no NCBI parent" if not s["taxon_ids"] else
                                            "NCBI parent not in the transform: " + joined(s["taxon_ids"]))})
            continue
        strain_rows.append({
            "strain_id": sid, "bacdive_id": s["bacdive_id"], "designation": s["designation"],
            "taxon_ids": joined(s["taxon_ids"]), "lpsn_ids": joined(s["lpsn_ids"]),
            "culture_collection_ids": joined(s["culture_collection_ids"]),
            "medium_count": s["medium_count"],
        })
    cc_rows = [{"strain_id": cc, "taxon_ids": joined(tids)}
               for cc, tids in sorted(cc_parents.items()) if tids & universe]

    print("reading BacDive strain-to-assembly links ...", flush=True)
    assembly_rows, assembly_drops = extract_bacdive_assemblies(
        kgm / "data/raw/bacdive_strains.json", {r["strain_id"] for r in strain_rows},
    )
    dropped_rows.extend(assembly_drops)

    media_rows = [{"taxon_id": t, "medium_count": len(m), "media_ids": joined(m)}
                  for t, m in sorted(taxon_media.items()) if t in universe]
    gold_rows = [{"taxon_id": t, "organism_count": n} for t, n in sorted(gold.items()) if t in universe]
    madin_rows = [{"taxon_id": t, "assertion_count": n} for t, n in sorted(madin.items()) if t in universe]
    bacto_rows = [{"taxon_id": t, "assertion_count": n} for t, n in sorted(bacto.items()) if t in universe]

    outputs = [
        ("ncbitaxon_taxa.tsv", ["taxon_id", "label", "rank", "parent_id", "genetic_code", "exact_synonyms",
                                "related_synonyms", "broad_synonyms", "attested_by"], taxa_rows),
        ("gtdb_mappings.tsv", ["gtdb_id", "gtdb_label", "gtdb_parent", "ncbitaxon_id", "predicate",
                               "genome_count"], mapping_rows),
        ("lpsn_names.tsv", ["lpsn_id", "name", "rank", "authority", "url", "deprecated", "status",
                            "validly_published", "legitimate", "is_correct_name", "parent_lpsn_id",
                            "ncbitaxon_ids", "gtdb_ids", "type_strain_ids", "synonym_of", "synonyms",
                            "publications", "sequence_accessions"], lpsn_rows),
        ("bacdive_strains.tsv", ["strain_id", "bacdive_id", "designation", "taxon_ids", "lpsn_ids",
                                 "culture_collection_ids", "medium_count"], strain_rows),
        ("strain_assemblies.tsv", ASSEMBLY_FIELDS, assembly_rows),
        ("culture_collection_strains.tsv", ["strain_id", "taxon_ids"], cc_rows),
        ("mediadive_taxa.tsv", ["taxon_id", "medium_count", "media_ids"], media_rows),
        ("gold_organisms.tsv", ["taxon_id", "organism_count"], gold_rows),
        ("madin_taxa.tsv", ["taxon_id", "assertion_count"], madin_rows),
        ("bactotraits_taxa.tsv", ["taxon_id", "assertion_count"], bacto_rows),
        # What extraction refused, item by item, so a kg-microbe regression
        # that unlinks thousands of strains cannot pass silently (#6).
        ("dropped.tsv", ["kind", "id", "reason"], dropped_rows),
    ]
    print("\n=== inventories ===")
    for name, _fields, rows in outputs:
        print(f"  {name:34s} {len(rows):8d} rows")

    if args.dry_run:
        print("\n--dry-run: no files written")
        return 0

    args.out.mkdir(parents=True, exist_ok=True)
    for name, fields, rows in outputs:
        write_tsv(args.out / name, fields, rows)
        print(f"wrote {args.out / name}")

    inputs = [describe_input(kgm, r) if not args.skip_input_hashes else _unhashed_input(kgm, r)
              for r in INPUTS]
    manifest: dict[str, Any] = {
        "extracted_at": _extracted_at(args.out / MANIFEST_NAME, inputs),
        "kg_microbe_source": git_head(kgm),
        "universe": {
            "attested_taxa": len(core),
            "ancestor_taxa": len(lineage - core),
            "total_taxa": len(universe),
            # Attested by a source but absent from kg-microbe's NCBITaxon
            # transform (a removed or merged id); they get no record.
            "dropped_attested_taxa": dropped_attested,
            "dropped_bacdive_strains": sum(1 for r in dropped_rows if r["kind"] == "bacdive_strain"),
        },
        "inputs": inputs,
        "outputs": [describe_output(args.out / name) for name, _f, _r in outputs],
    }
    header = (
        "# Provenance for the inventories in data/raw/.\n"
        "# Regenerate with: just extract-inventory\n"
        "# Emitted by scripts/extract_source_inventory.py — do not hand-edit.\n"
    )
    (args.out / MANIFEST_NAME).write_text(
        header + yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8"
    )
    print(f"wrote {args.out / MANIFEST_NAME}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
