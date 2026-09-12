"""Query the complete local AllTheBacteria catalogue without downloading genomes."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sqlite3
import sys
from pathlib import Path

import yaml

from taxonmech.atb import ATB_DIR, ROOT, _manifest, input_provenance, settings, sha256
from taxonmech.atb_catalog import (
    ASSEMBLY_COLUMNS,
    assembly_id,
    crosslink_exclusion_reason,
    is_ena_analysis_accession,
    is_sample_accession,
)


def open_catalog(index: Path, *, manifest: Path | None = None,
                 root: Path | None = None) -> sqlite3.Connection:
    """Open a completed snapshot; CLI callers also verify its current dependencies.

    A matching old manifest alone cannot establish that the source inventories
    or configured source pin still support the cached strain/genome links.
    Explicit snapshot API callers may omit root to read historical snapshots.
    """
    if root is not None and manifest is None:
        manifest = root / "data/atb/MANIFEST.yaml"
    if not index.is_file():
        raise ValueError(f"ATB index is missing: {index}; run just atb-fetch and just atb-index --apply")
    connection = sqlite3.connect(index.resolve().as_uri() + "?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        metadata = dict(connection.execute("SELECT key,value FROM metadata"))
        stamp = metadata.get("crosslink_manifest_sha256")
        if not stamp:
            raise ValueError("ATB index has no completed crosswalk; rebuild with just atb-index --apply")
        if manifest is not None and (not manifest.is_file() or stamp != sha256(manifest)):
            raise ValueError("ATB index differs from the committed crosswalk; "
                             "rebuild with just atb-index --apply")
        if root is not None:
            snapshot = _manifest(manifest.parent)
            config = settings(root / "conf/allthebacteria.yaml")
            expected = {key: value for key, value in config.items()
                        if key not in {"metadata_path", "index_path"}}
            if snapshot["source"] != expected:
                raise ValueError("ATB source pin changed; rebuild with just atb-index --apply")
            if snapshot["inputs"] != input_provenance(root / "data/raw"):
                raise ValueError("ATB source inventories changed; rebuild with just atb-index --apply")
            if (metadata.get("release") != snapshot["source"]["release"]
                    or metadata.get("source_sha256") != snapshot["source"]["sha256"]):
                raise ValueError("ATB index metadata differs from the pinned snapshot; "
                                 "rebuild with just atb-index --apply")
            # Reject a publication that changed the manifest while dependencies
            # were being read, instead of accepting a mixed snapshot.
            if stamp != sha256(manifest):
                raise ValueError("ATB crosswalk changed during query startup; retry the query")
        return connection
    except Exception:
        connection.close()
        raise


def _selector(by: str, value: str, release: str) -> tuple[str, tuple[str, ...]]:
    if by == "sample":
        # Composite unprocessed source keys remain queryable verbatim with --all-statuses.
        return "a.sample_accession = ?", (value.removeprefix("biosample:"),)
    if by == "ena_analysis":
        analysis = value.removeprefix("ena.analysis:")
        if not is_ena_analysis_accession(analysis):
            raise ValueError("ENA analysis lookup requires an ERZ accession")
        return "a.assembly_accession = ?", (analysis,)
    if by == "atb_id":
        if not value.startswith("atb.assembly:") or "." not in value.split(":", 1)[1]:
            raise ValueError("ATB identifier must be atb.assembly:YYYYMM.SAM…")
        sample = value.split(":", 1)[1].split(".", 1)[1]
        if value != assembly_id(release, sample):
            raise ValueError(f"ATB identifier does not belong to indexed snapshot {release}")
        return "a.sample_accession = ? AND a.asm_fasta_on_osf = '1'", (sample,)
    if by == "strain":
        return (
            "a.sample_accession IN (SELECT substr(s.sample_id,11) FROM strain_link s "
            "JOIN strain_alias x USING(strain_id) WHERE x.alias = ?)", (value,),
        )
    if by == "genome":
        if value.startswith("atb.assembly:"):
            return _selector("atb_id", value, release)
        if re.fullmatch(r"GC[AF]_[0-9]{9}(?:\.[1-9][0-9]*)?", value):
            value = "ncbi.assembly:" + value
        return (
            "a.sample_accession IN (SELECT substr(sample_id,11) FROM genome_link WHERE genome_id = ?)",
            (value,),
        )
    if by == "species":
        return "(a.scientific_name = ? OR a.sylph_species = ?)", (value, value)
    raise ValueError(f"unknown query field: {by}")


def query_catalog(
    connection: sqlite3.Connection, *, by: str, value: str, limit: int = 20, offset: int = 0,
    all_statuses: bool = False, evidence: bool = False,
) -> dict:
    """Return exact matches and explicit shared-BioSample crosslinks with stable paging."""
    if not 1 <= limit <= 1000 or offset < 0:
        raise ValueError("limit must be 1–1000 and offset must be nonnegative")
    if not value:
        raise ValueError("an exact lookup value is required")
    metadata = dict(connection.execute("SELECT key,value FROM metadata"))
    where, parameters = _selector(by, value, metadata["release"])
    if not all_statuses:
        where += " AND a.asm_fasta_on_osf = '1'"
    total = connection.execute(f"SELECT count(*) FROM assembly a WHERE {where}", parameters).fetchone()[0]
    records = []
    for raw in connection.execute(
        f"SELECT a.* FROM assembly a WHERE {where} ORDER BY a.sample_accession LIMIT ? OFFSET ?",
        (*parameters, limit, offset),
    ):
        row = dict(raw)
        sample = row["sample_accession"]
        row["atb_id"] = (
            assembly_id(metadata["release"], sample)
            if row["asm_fasta_on_osf"] == "1" and is_sample_accession(sample) else None
        )
        row["crosslink_exclusion"] = crosslink_exclusion_reason(dict(raw)) or None
        sample_id = "biosample:" + sample
        strain_links = [dict(item) for item in connection.execute(
            "SELECT * FROM strain_link WHERE sample_id = ? ORDER BY strain_id", (sample_id,),
        )]
        genome_links = [dict(item) for item in connection.execute(
            "SELECT * FROM genome_link WHERE sample_id = ? "
            "ORDER BY genome_id NOT LIKE 'ncbi.assembly:%',genome_id,strain_id", (sample_id,),
        )]
        if evidence:
            for item in strain_links:
                item["sample_evidence"] = json.loads(item.pop("sample_evidence_json"))
            for item in genome_links:
                item["source_evidence"] = json.loads(item.pop("source_evidence_json"))
        else:
            for item in strain_links:
                item.pop("sample_evidence_json")
            for item in genome_links:
                item.pop("source_evidence_json")
        row["strain_links"], row["genome_links"] = strain_links, genome_links
        records.append(row)
    return {"release": metadata["release"], "source_sha256": metadata["source_sha256"],
            "total": total, "offset": offset, "limit": limit, "results": records}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, help="SQLite catalogue path (default: configured cache)")
    selectors = parser.add_mutually_exclusive_group(required=True)
    for flag in ("sample", "ena-analysis", "atb-id", "strain", "genome", "species"):
        selectors.add_argument("--" + flag,
                               help="Exact identifier or source value; accession versions are preserved")
    selectors.add_argument("--info", action="store_true", help="Show catalogue snapshot and counts")
    parser.add_argument("--all-statuses", action="store_true", help="Include unavailable source rows")
    parser.add_argument("--evidence", action="store_true", help="Include the original source assertions")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--format", choices=("json", "tsv"), default="json")
    args = parser.parse_args(argv)
    connection = None
    try:
        connection = open_catalog(args.index or ROOT / settings()["index_path"],
                                  manifest=ATB_DIR / "MANIFEST.yaml", root=ROOT)
        if args.info:
            print(json.dumps(dict(connection.execute("SELECT key,value FROM metadata")), indent=2))
            return 0
        by = next(key for key in ("sample", "ena_analysis", "atb_id", "strain", "genome", "species")
                  if getattr(args, key) is not None)
        result = query_catalog(connection, by=by, value=getattr(args, by), limit=args.limit,
                               offset=args.offset, all_statuses=args.all_statuses, evidence=args.evidence)
        if args.format == "json":
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            fields = ["atb_id", *ASSEMBLY_COLUMNS, "crosslink_exclusion", "strain_links", "genome_links"]
            writer = csv.DictWriter(sys.stdout, fieldnames=fields, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            for row in result["results"]:
                writer.writerow({key: json.dumps(value, ensure_ascii=False, separators=(",", ":"))
                                 if isinstance(value, list) else value for key, value in row.items()})
    except (OSError, ValueError, sqlite3.Error, yaml.YAMLError) as exc:
        parser.exit(1, f"AllTheBacteria: {exc}\n")
    finally:
        if connection is not None:
            connection.close()
    return 0
