"""Source-native discovery catalogs, without inferred biological equivalence.

An index hit means the source record contains an identifier. It is not a
strain identity, taxonomic mapping, or genome equivalence assertion. Those
relationships use the stricter evidence adapters and generated taxon schema.
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import json
import re
import sqlite3
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = "data/catalog/MANIFEST.json"
INDEX_VERSION = 1


def sha256(path: Path) -> str:
    with path.open("rb") as handle:
        digest = hashlib.sha256()
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
        return digest.hexdigest()


def json_rows(path: Path):
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        for line in handle:
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"catalog row must be an object: {path}")
            yield value


def write_chunks(directory: Path, source: str, rows, *, chunk_size: int = 50_000) -> list[dict]:
    """Deterministic bounded files, preserving every row in source order."""
    if not re.fullmatch(r"[a-z0-9_-]+", source) or chunk_size <= 0:
        raise ValueError("invalid source name or chunk size")
    directory.mkdir(parents=True, exist_ok=True)
    outputs, batch = [], []

    def flush():
        path = directory / f"{source}-{len(outputs):04}.jsonl.gz"
        with path.open("wb") as raw, gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0) as handle:
            for row in batch:
                handle.write(
                    (
                        json.dumps(row, sort_keys=True, ensure_ascii=False, separators=(",", ":")) + "\n"
                    ).encode()
                )
        outputs.append(
            {"path": path.name, "rows": len(batch), "bytes": path.stat().st_size, "sha256": sha256(path)}
        )
        batch.clear()

    for row in rows:
        batch.append(row)
        if len(batch) == chunk_size:
            flush()
    if batch:
        flush()
    return outputs


def safe_path(root: Path, relative: str) -> Path:
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or not path.parts or path.parts[0] != "data":
        raise ValueError("catalog path must stay within repository data")
    return root / path


def load_manifest(root: Path = ROOT) -> dict:
    value = json.loads((root / MANIFEST).read_text())
    if value.get("format_version") != 1 or not isinstance(value.get("sources"), list):
        raise ValueError("unsupported source catalog manifest")
    names = [item.get("id") for item in value["sources"]]
    if len(names) != len(set(names)) or any(not re.fullmatch(r"[a-z0-9_-]+", str(n)) for n in names):
        raise ValueError("duplicate or invalid catalog source")
    for source in value["sources"]:
        for item in source["files"]:
            safe_path(root, item["path"])
        if source["rows"] != sum(item["rows"] for item in source["files"]):
            raise ValueError("catalog source total differs from its file counts")
    return value


def records(source: dict, root: Path = ROOT):
    for item in source["files"]:
        path = safe_path(root, item["path"])
        if source["format"] == "jsonl.gz":
            yield from json_rows(path)
        elif source["format"] == "tsv":
            with path.open(encoding="utf-8", newline="") as handle:
                yield from csv.DictReader(handle, delimiter="\t")
        elif source["format"] == "atb.tsv.xz":
            from taxonmech.atb_catalog import iter_assemblies

            yield from iter_assemblies(path)
        else:
            raise ValueError(f"unsupported catalog format: {source['format']}")


def _values(value):
    if isinstance(value, dict):
        for key, item in value.items():
            yield key, item
            yield from _values(item)
    elif isinstance(value, list):
        for item in value:
            yield from _values(item)


def index_terms(source: str, row: dict, *, snapshot: str = "") -> set[str]:
    """Exact source identifiers; index terms deliberately do not join sources."""
    terms = set()
    for field, value in _values(row):
        if isinstance(value, bool):
            continue
        if isinstance(value, (str, int)) and str(value):
            text = str(value)
            # Native CURIE-valued inventory fields, including pipe lists.
            for token in text.split("|"):
                if re.fullmatch(r"(?:NCBITaxon|GTDB|lpsn|bacdive|kgmicrobe\.strain):[^|]+", token):
                    terms.add(token)
            # Only named accession fields are indexed as identifiers; names,
            # publications and descriptive prose do not become join keys.
            if field in {
                "accession",
                "accessionNumber",
                "genome_id",
                "sample_accession",
                "biosample_accession",
                "bioproject_accession",
                "assembly_accession",
                "assemblyAccession",
                "genbankId",
                "ncbi_genbank_assembly_accession",
                "assembly",
                "INSDC accession",
                "BV-BRC accession",
                "IMG accession",
                "biosample",
                "bioproject",
                "ncbi_biosample",
                "ncbi_bioproject",
                "sample",
                "analysis",
                "ena_analysis",
                "AP IMG TAXON ID",
                "GENBANK ASSEMBLY ACCESSION",
                "NCBI BIOSAMPLE ACCESSION",
                "NCBI BIOPROJECT ACCESSION",
                "ORGANISM GOLD ID",
                "PROJECT GOLD ID",
                "AP GOLD ID",
                "AP ORGANISM GOLD ID",
                "doi",
                "uri",
            }:
                terms.add(text)
                if re.fullmatch(r"GC[AF]_[0-9]{9}(?:\.[1-9][0-9]*)?", text):
                    terms.add("ncbi.assembly:" + text)
                elif re.fullmatch(r"(?:RS_GCF|GB_GCA)_[0-9]{9}\.[1-9][0-9]*", text):
                    terms.add("gtdb.genome:" + text)
                elif re.fullmatch(r"SAM[NED][A-Z]?[0-9]+", text):
                    terms.add("biosample:" + text)
                elif re.fullmatch(r"G[oap][0-9]+", text):
                    terms.add("gold:" + text)
                elif re.fullmatch(r"ERZ[0-9]+", text):
                    terms.add("ena.analysis:" + text)
                if (field == "genome_id" and source == "bvbrc") or field == "BV-BRC accession":
                    terms.add("patric:" + text)
                if field in {"IMG accession", "AP IMG TAXON ID"} and text.isdigit():
                    terms.add("img.taxon:" + text)
            if field in {
                "ncbi_taxid",
                "taxid",
                "species_taxid",
                "ORGANISM NCBI TAX ID",
                "ncbi",
                "NCBI tax id",
                "taxon_id",
            } and text.isdigit() and int(text) > 0:
                terms.add("NCBITaxon:" + text)
            if source == "bacdive" and field == "BacDive-ID":
                terms.add("bacdive:" + text)
            if source == "straininfo" and field in {"siID", "siDP"}:
                terms.add(("straininfo.strain:" if field == "siID" else "straininfo.deposit:") + text)
            if source == "straininfo" and field == "lpsn" and text.isdigit():
                terms.add("lpsn:" + text)
            if source.startswith("gold_") and field == "AP PROJECT GOLD IDS":
                for token in re.split(r"[;,|\s]+", text):
                    if re.fullmatch(r"Gp[0-9]+", token):
                        terms.update({token, "gold:" + token})
            if source.startswith("gold_") and field == "AP GENBANK":
                try:
                    references = json.loads(text)
                except ValueError:
                    references = None
                if isinstance(references, list):
                    for reference in references:
                        if isinstance(reference, dict):
                            terms.update(index_terms(source, reference))
            if source.startswith("seqcode") and field == "id" and value == row.get("id"):
                terms.add("seqcode:" + text)
            if field in {
                "culture collection no.",
                "ncbi_strain_identifiers",
                "ORGANISM CULTURE COLLECTION ID",
                "ORGANISM STRAIN",
                "culture_collection",
                "strain",
                "designation",
                "infraspecific_name",
            }:
                # Search is exact and preserves the source spelling. No bare
                # alias normalization participates in biological crosslinks.
                terms.add(text)
                terms.update(part.strip() for part in re.split(r"[;,|]", text) if part.strip())
    if source == "allthebacteria":
        from taxonmech.atb_catalog import assembly_id, is_sample_accession
        if snapshot and row.get("asm_fasta_on_osf") == "1" and is_sample_accession(row["sample_accession"]):
            terms.add(assembly_id(snapshot, row["sample_accession"]))
        terms.update(row.get("run_accession", "").split(","))
    return terms - {"", "na", "none", "None"}


def check(root: Path = ROOT, *, count_rows: bool = True) -> list[str]:
    failures = []
    manifest = load_manifest(root)
    for item in manifest["inputs"]:
        path = root / item["path"]
        if sha256(path) != item["sha256"]:
            failures.append(f"catalog dependency changed: {item['path']}")
    for source in manifest["sources"]:
        for item in source["files"]:
            path = safe_path(root, item["path"])
            if path.stat().st_size != item["bytes"] or sha256(path) != item["sha256"]:
                failures.append(f"source catalog differs from its pin: {item['path']}")
        if count_rows and sum(1 for _ in records(source, root)) != source["rows"]:
            failures.append(f"source catalog census differs: {source['id']}")
    return failures


def build_index(source: dict, root: Path = ROOT) -> Path:
    """Reuse a disposable index only for the same byte-verified source files."""
    for item in source["files"]:
        path = safe_path(root, item["path"])
        if sha256(path) != item["sha256"] or path.stat().st_size != item["bytes"]:
            raise ValueError("cannot index a source projection that differs from its pin")
    fingerprint = hashlib.sha256(
        json.dumps({"source": source, "index_version": INDEX_VERSION}, sort_keys=True).encode()
    ).hexdigest()
    directory = root / "data/indexes"
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / f"source-{source['id']}-{fingerprint}.sqlite"
    if target.is_file():
        return target
    with tempfile.TemporaryDirectory(prefix="source-index-", dir=directory) as temporary:
        path = Path(temporary) / "index.sqlite"
        with sqlite3.connect(str(path)) as db:
            db.execute("CREATE TABLE records (position INTEGER PRIMARY KEY, document TEXT)")
            db.execute(
                "CREATE TABLE terms (term TEXT, position INTEGER, PRIMARY KEY(term, position)) WITHOUT ROWID"
            )
            count = 0
            for number, row in enumerate(records(source, root)):
                db.execute("INSERT INTO records VALUES (?, ?)", (number, json.dumps(row, ensure_ascii=False)))
                db.executemany(
                    "INSERT INTO terms VALUES (?, ?)",
                    ((term, number) for term in sorted(index_terms(
                        source["id"], row, snapshot=source.get("snapshot", "")))),
                )
                count += 1
            if count != source["rows"]:
                raise ValueError("catalog row count differs while indexing")
        path.replace(target)
    return target


def query(source: dict, identifier: str, root: Path = ROOT, *, limit: int = 20):
    """Query exact source identifiers, with a total independent of the limit."""
    if limit <= 0:
        raise ValueError("query limit must be positive")
    path = build_index(source, root)
    with sqlite3.connect(f"file:{path}?mode=ro", uri=True) as db:
        count = db.execute("SELECT count(*) FROM terms WHERE term = ?", (identifier,)).fetchone()[0]
        rows = db.execute(
            "SELECT document FROM terms JOIN records USING(position) "
            "WHERE term = ? ORDER BY position LIMIT ?",
            (identifier, limit),
        )
        return {
            "source": source["id"],
            "identifier": identifier,
            "total": count,
            "interpretation": "Source-record occurrence; not an identity or equivalence assertion.",
            "records": [json.loads(row[0]) for row in rows],
        }
