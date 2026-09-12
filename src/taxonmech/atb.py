"""Build the AllTheBacteria catalogue and reproducible, evidenced crosswalks.

The full SQLite catalogue is a local cache. The matched metadata and derived
crosswalks under data/atb are committed so seeding and QC need no downloads.
"""

from __future__ import annotations

import argparse
import csv
import datetime
import hashlib
import json
import os
import re
import shutil
import sqlite3
import subprocess
import tempfile
import urllib.request
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlsplit

import yaml

from taxonmech.atb_catalog import (
    ASSEMBLY_COLUMNS,
    assembly_id,
    build_catalog,
    crosslink_exclusion_reason,
    is_sample_accession,
    normalize_release,
    validate_assembly_row,
)
from taxonmech.atb_links import build_evidence, build_links
from taxonmech.extract import (
    ASSEMBLY_FIELDS,
    GENOME_RECORD_FIELDS,
    RELATED_RECORD_FIELDS,
    describe_output,
    write_tsv,
)

ROOT = Path(__file__).resolve().parents[2]
ATB_DIR = ROOT / "data/atb"
CONFIG = ROOT / "conf/allthebacteria.yaml"
INPUT_NAMES = (
    "bacdive_strains.tsv", "strain_related_records.tsv", "strain_assemblies.tsv", "strain_genome_records.tsv",
)
STRAIN_FIELDS = ("strain_id", "atb_id", "sample_id", "sample_evidence_json")
GENOME_FIELDS = ("strain_id", "atb_id", "sample_id", "genome_id", "relationship", "source_evidence_json")
EXCLUSION_FIELDS = ("sample_id", "reason")
OUTPUT_NAMES = ("assemblies.tsv", "strain_links.tsv", "genome_links.tsv", "exclusions.tsv")
CROSSLINK_STATS = ("matched_samples", "assembly_identifiers", "strain_pairs", "strains",
                   "genome_pairs", "excluded_samples")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_rows(path: Path, *, required: tuple | list = (), nonempty: bool = False) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        fields = reader.fieldnames or []
        if (not fields or any(not field for field in fields) or len(fields) != len(set(fields))
                or not set(required) <= set(fields)):
            raise ValueError(f"{path}: missing or duplicate TSV headers")
        rows = []
        for row in reader:
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"{path}:{reader.line_num}: malformed TSV row")
            rows.append(row)
        if nonempty and not rows:
            raise ValueError(f"{path}: source inventory is empty")
        return rows


def _configuration(config: object, *, paths: bool = True) -> dict:
    if not isinstance(config, dict):
        raise ValueError("AllTheBacteria configuration must be a mapping")
    required = ["release", "url", "sha256", "license", "citation"]
    if paths:
        required.extend(("metadata_path", "index_path"))
    for field in required:
        if not isinstance(config.get(field), str) or not config[field].strip():
            raise ValueError(f"AllTheBacteria configuration requires a nonempty string for {field}")
    result = dict(config)
    result["release"] = normalize_release(config["release"])
    if not re.fullmatch(r"[a-fA-F0-9]{64}", config["sha256"]):
        raise ValueError("AllTheBacteria source sha256 must be a 64-character digest")
    result["sha256"] = config["sha256"].lower()
    for field in ("url", "citation", "license_url"):
        if field not in config:
            continue
        value = config[field]
        if not isinstance(value, str):
            raise ValueError(f"AllTheBacteria {field} must be an HTTPS URL")
        parsed = urlsplit(value)
        if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
            raise ValueError(f"AllTheBacteria {field} must be an HTTPS URL without credentials")
    for field in ("source_metadata_date", "osf_file_modified"):
        if field in config:
            value = config[field]
            if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                raise ValueError(f"AllTheBacteria {field} must be an ISO date string")
            datetime.date.fromisoformat(value)
    if "osf_file_version" in config and (type(config["osf_file_version"]) is not int
                                          or config["osf_file_version"] < 1):
        raise ValueError("AllTheBacteria osf_file_version must be a positive integer")
    return result


def settings(path: Path = CONFIG) -> dict:
    return _configuration(yaml.safe_load(path.read_text(encoding="utf-8")))


def fetch(config: dict, destination: Path, *, force: bool = False) -> Path:
    """Fetch only the pinned metadata file, verifying it before replacement."""
    config = _configuration(config)
    if destination.exists():
        if sha256(destination) == config["sha256"]:
            return destination
        if not force:
            raise ValueError(f"Existing metadata has a different hash: {destination}; use --force to replace")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=destination.parent, prefix=".atb-fetch-") as tmp:
        candidate = Path(tmp) / "metadata.xz"
        with urllib.request.urlopen(config["url"], timeout=120) as response, candidate.open("wb") as handle:
            shutil.copyfileobj(response, handle)
        if sha256(candidate) != config["sha256"]:
            raise ValueError("Downloaded AllTheBacteria metadata does not match the configured SHA256")
        os.replace(candidate, destination)
    return destination


def load_inputs(raw: Path) -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    strains = read_rows(raw / "bacdive_strains.tsv", nonempty=True,
                        required=("strain_id", "bacdive_id", "culture_collection_ids"))
    samples = [row for row in read_rows(raw / "strain_related_records.tsv", required=RELATED_RECORD_FIELDS,
                                       nonempty=True) if row["record_type"] == "BIOSAMPLE"]
    if not samples:
        raise ValueError("BioSample source inventory is empty")
    return (strains, samples,
            read_rows(raw / "strain_assemblies.tsv", required=ASSEMBLY_FIELDS, nonempty=True),
            read_rows(raw / "strain_genome_records.tsv", required=GENOME_RECORD_FIELDS, nonempty=True))


def _destinations(metadata: Path, index: Path, out: Path, raw: Path, config_path: Path | None) -> None:
    protected = {metadata.resolve(), CONFIG.resolve()}
    if config_path is not None:
        protected.add(config_path.resolve())
    targets = [index, *(out / name for name in (*OUTPUT_NAMES, "MANIFEST.yaml"))]
    resolved = [path.resolve() for path in targets]
    raw = raw.resolve()
    if (len(resolved) != len(set(resolved)) or protected & set(resolved)
            or any(path == raw or raw in path.parents for path in resolved)):
        raise ValueError("ATB output destinations must be distinct and cannot overwrite source inputs")
    if any(path.is_dir() for path in targets):
        raise ValueError("ATB output destinations must be files, not existing directories")


def _publish(work: Path, candidate: Path, out: Path, index: Path) -> None:
    """Publish the manifest last, rolling back completed moves on any failure.

    Output staging is on its destination filesystem. The SQLite candidate and
    its backup already share the index filesystem. Readers verify manifest
    hashes, so the short replacement interval cannot validate a mixed set.
    """
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".atb-publish-", dir=out.parent) as tmp:
        stage = Path(tmp)
        for name in (*OUTPUT_NAMES, "MANIFEST.yaml"):
            shutil.copyfile(work / name, stage / name)
        out.mkdir(parents=True, exist_ok=True)
        moves = [(stage / name, out / name, stage / f"old-{name}") for name in OUTPUT_NAMES]
        moves.extend(((candidate, index, work / "previous-index.sqlite"),
                      (stage / "MANIFEST.yaml", out / "MANIFEST.yaml", stage / "old-MANIFEST.yaml")))
        backups, installed = [], []
        try:
            for source, destination, backup in moves:
                if destination.exists() or destination.is_symlink():
                    os.replace(destination, backup)
                    backups.append((backup, destination))
                os.replace(source, destination)
                installed.append(destination)
        except BaseException:
            for destination in reversed(installed):
                destination.unlink(missing_ok=True)
            for backup, destination in reversed(backups):
                os.replace(backup, destination)
            raise


def input_provenance(raw: Path) -> list[dict]:
    return [{"path": f"data/raw/{name}", "bytes": (raw / name).stat().st_size,
             "sha256": sha256(raw / name)} for name in INPUT_NAMES]


def _add_index_links(connection: sqlite3.Connection, strains: list[dict], strain_links: list[dict],
                     genome_links: list[dict]) -> None:
    for table, fields, rows in (("strain_link", STRAIN_FIELDS, strain_links),
                               ("genome_link", GENOME_FIELDS, genome_links)):
        columns = ", ".join(f"{field} TEXT NOT NULL" for field in fields)
        connection.execute(f"CREATE TABLE {table} ({columns})")
        placeholders = ",".join("?" for _ in fields)
        connection.executemany(f"INSERT INTO {table} VALUES ({placeholders})",
                               (tuple(row[field] for field in fields) for row in rows))
        for field in ("strain_id", "sample_id", "atb_id"):
            connection.execute(f"CREATE INDEX {table}_{field} ON {table}({field})")
    connection.execute("CREATE INDEX genome_link_genome_id ON genome_link(genome_id)")
    connection.execute("CREATE TABLE strain_alias (alias TEXT, strain_id TEXT, PRIMARY KEY(alias,strain_id))")
    aliases = set()
    for row in strains:
        sid = row["strain_id"]
        for alias in (sid, f"bacdive:{row['bacdive_id']}", *row["culture_collection_ids"].split("|")):
            if alias:
                aliases.add((alias, sid))
    connection.executemany("INSERT INTO strain_alias VALUES (?,?)", sorted(aliases))


def generate(metadata: Path, index: Path, out: Path, raw: Path, config: dict, *, apply: bool = False,
             config_path: Path | None = None) -> dict:
    """Build and validate a complete snapshot before rollback-protected publication."""
    config = _configuration(config)
    _destinations(metadata, index, out, raw, config_path)
    inputs = input_provenance(raw)
    strains, samples, ncbi, genomes = load_inputs(raw)
    known_strains = {row["strain_id"] for row in strains}
    if len(known_strains) != len(strains) or any(
        not re.fullmatch(r"kgmicrobe\.strain:bacdive_[0-9]+", sid) for sid in known_strains
    ):
        raise ValueError("strain inventory has invalid or duplicate BacDive identifiers")
    if any(row["strain_id"] not in known_strains for row in samples):
        raise ValueError("BioSample evidence refers to a strain outside the strain inventory")
    if apply:
        index.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".atb-index-", dir=index.parent if apply else None) as tmp:
        work = Path(tmp)
        candidate = work / "catalog.sqlite"
        catalog = build_catalog(metadata, candidate, release=config["release"],
                                expected_sha256=config["sha256"])
        connection = sqlite3.connect(candidate)
        connection.row_factory = sqlite3.Row
        try:
            connection.execute("CREATE TEMP TABLE wanted_sample (sample_accession TEXT PRIMARY KEY)")
            connection.executemany("INSERT INTO wanted_sample VALUES (?)",
                                   [(sample,) for sample in sorted({r["record_id"].split(":", 1)[1]
                                                                   for r in samples})])
            matched = [dict(row) for row in connection.execute(
                "SELECT a.* FROM assembly a JOIN wanted_sample w USING(sample_accession) "
                "ORDER BY sample_accession"
            )]
            strain_links, genome_links, exclusions = build_links(matched, samples, ncbi, genomes,
                                                                 release=config["release"])
            outputs = (("assemblies.tsv", ASSEMBLY_COLUMNS, matched),
                       ("strain_links.tsv", STRAIN_FIELDS, strain_links),
                       ("genome_links.tsv", GENOME_FIELDS, genome_links),
                       ("exclusions.tsv", EXCLUSION_FIELDS, exclusions))
            for name, fields, rows in outputs:
                write_tsv(work / name, list(fields), rows)
            manifest = {
                "source": {key: value for key, value in config.items()
                           if key not in ("metadata_path", "index_path")},
                "catalog": catalog, "inputs": inputs,
                "outputs": [describe_output(work / name) for name in OUTPUT_NAMES],
                "crosslinks": {"matched_samples": len(matched), "assembly_identifiers":
                               len({r["atb_id"] for r in strain_links}), "strain_pairs": len(strain_links),
                               "strains": len({r["strain_id"] for r in strain_links}),
                               "genome_pairs": len({(r["atb_id"], r["genome_id"]) for r in genome_links}),
                               "excluded_samples": len(exclusions)},
            }
            old_manifest = out / "MANIFEST.yaml"
            old = yaml.safe_load(old_manifest.read_text()) if old_manifest.exists() else {}
            if not isinstance(old, dict):
                old = {}
            old_stamp = old.pop("extracted_at", None)
            now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            manifest = {"extracted_at": old_stamp if old == manifest and old_stamp else now, **manifest}
            (work / "MANIFEST.yaml").write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
            # Exercise the same inner evidence checks used by the seeder before
            # publishing any generated file.
            genome_records(work)
            # Refuse a mixed snapshot if another process refreshed the input inventories during the build.
            if inputs != input_provenance(raw):
                raise ValueError("TaxonMech source inventories changed while the ATB index was building")
            if apply:
                _add_index_links(connection, strains, strain_links, genome_links)
                connection.execute("INSERT INTO metadata(key,value) VALUES (?,?)",
                                   ("crosslink_manifest_sha256", sha256(work / "MANIFEST.yaml")))
                connection.commit()
        finally:
            connection.close()
        if apply:
            _publish(work, candidate, out, index)
        return manifest


def _manifest(directory: Path, *, check_outputs: bool = True) -> dict:
    manifest = yaml.safe_load((directory / "MANIFEST.yaml").read_text(encoding="utf-8"))
    if not isinstance(manifest, dict):
        raise ValueError("ATB manifest must be a mapping")
    source = _configuration(manifest.get("source"), paths=False)
    if source != manifest["source"]:
        raise ValueError("ATB manifest source pin must use canonical release and digest forms")
    stamp = manifest.get("extracted_at")
    if not isinstance(stamp, str):
        raise ValueError("ATB manifest requires an extraction timestamp")
    try:
        datetime.datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError as exc:
        raise ValueError("ATB manifest has a malformed extraction timestamp") from exc
    catalog = manifest.get("catalog")
    if (not isinstance(catalog, dict) or catalog.get("release") != source["release"]
            or catalog.get("source_sha256") != source["sha256"]
            or type(catalog.get("rows")) is not int or catalog["rows"] <= 0):
        raise ValueError("ATB catalog provenance is missing or differs from the pinned source")
    count_fields = ("rows", "available_assemblies", "unavailable_rows", "non_single_sample_rows")
    if (any(type(catalog.get(field)) is not int or catalog[field] < 0 for field in count_fields)
            or catalog["rows"] != catalog["available_assemblies"] + catalog["unavailable_rows"]
            or catalog["non_single_sample_rows"] > catalog["unavailable_rows"]):
        raise ValueError("ATB catalog counts are inconsistent")
    for field in ("datasets", "filters"):
        counts = catalog.get(field)
        if (not isinstance(counts, dict) or not counts
                or any(not isinstance(key, str) or type(value) is not int or value < 0
                       for key, value in counts.items())
                or sum(counts.values()) != catalog["rows"]):
            raise ValueError(f"ATB catalog {field} counts are inconsistent")
    crosslinks = manifest.get("crosslinks")
    if (not isinstance(crosslinks, dict) or set(crosslinks) != set(CROSSLINK_STATS)
            or any(type(value) is not int or value < 0 for value in crosslinks.values())):
        raise ValueError("ATB manifest requires a complete crosslink summary")
    for section, names in (("inputs", {f"data/raw/{name}" for name in INPUT_NAMES}),
                           ("outputs", set(OUTPUT_NAMES))):
        entries = manifest.get(section)
        if (not isinstance(entries, list) or len(entries) != len(names)
                or any(not isinstance(entry, dict) or not isinstance(entry.get("path"), str)
                       for entry in entries)
                or {entry.get("path") for entry in entries} != names):
            raise ValueError(f"ATB manifest must cover each required {section} file exactly once")
        for entry in entries:
            if (type(entry.get("bytes")) is not int or entry["bytes"] <= 0
                    or not isinstance(entry.get("sha256"), str)
                    or not re.fullmatch(r"[a-f0-9]{64}", entry["sha256"])):
                raise ValueError(f"ATB manifest {section} requires valid sizes and SHA256 digests")
            if section == "outputs":
                if type(entry.get("rows")) is not int or entry["rows"] < 0:
                    raise ValueError("ATB output provenance requires nonnegative row counts")
                if check_outputs and entry != describe_output(directory / entry["path"]):
                    raise ValueError(f"ATB {entry['path']} differs from its manifest")
    return manifest


def _sample_links(encoded: str, sid: str, sample: str) -> list[dict]:
    try:
        rows = json.loads(encoded)
    except (TypeError, ValueError) as exc:
        raise ValueError("ATB sample evidence must be JSON") from exc
    allowed = set(RELATED_RECORD_FIELDS) - {"strain_id"}
    if not isinstance(rows, list) or not rows:
        raise ValueError("ATB sample evidence must be a nonempty list of source assertions")
    for row in rows:
        if (not isinstance(row, dict) or set(row) - allowed
                or any(not isinstance(value, str) or not value for value in row.values())
                or row.get("record_id") != sample or row.get("record_type") != "BIOSAMPLE"
                or row.get("source") not in {"GTDB", "GOLD"}):
            raise ValueError("ATB sample evidence must contain typed assertions for the same BioSample")
        for field, pattern in (("taxon_id", r"NCBITaxon:[0-9]+"),
                               ("source_organism_id", r"gold:Go[0-9]+"),
                               ("source_project_id", r"gold:Gp[0-9]+")):
            if field in row and not re.fullmatch(pattern, row[field]):
                raise ValueError(f"ATB sample evidence has malformed {field}")
    indexed, _ = build_evidence([{"strain_id": sid, **row} for row in rows], [], [])
    expected = indexed.get((sid, sample), [])
    if expected != rows:
        raise ValueError("ATB sample evidence must preserve canonical, distinct source assertions")
    return rows


def genome_records(directory: Path = ATB_DIR) -> dict[str, list[dict]]:
    """Convert the committed ATB crosswalk into ordinary typed genome links."""
    manifest = _manifest(directory)
    release = manifest["source"]["release"]
    assemblies = {}
    for row in read_rows(directory / "assemblies.tsv", required=ASSEMBLY_COLUMNS):
        validate_assembly_row(row)
        if row["sample_accession"] in assemblies:
            raise ValueError("ATB assembly inventory has duplicate sample keys")
        assemblies[row["sample_accession"]] = row
    result = defaultdict(list)
    seen = set()
    for link in read_rows(directory / "strain_links.tsv", required=STRAIN_FIELDS):
        sample_id = link["sample_id"]
        if not sample_id.startswith("biosample:") or not is_sample_accession(sample_id.split(":", 1)[1]):
            raise ValueError("ATB strain link requires a BioSample CURIE")
        sample = sample_id.split(":", 1)[1]
        row = assemblies.get(sample)
        if row is None:
            raise ValueError("ATB strain link refers to a sample absent from the assembly inventory")
        if reason := crosslink_exclusion_reason(row):
            raise ValueError(f"ATB strain link refers to an ineligible assembly: {reason}")
        if link["atb_id"] != assembly_id(release, sample):
            raise ValueError("ATB crosswalk identifier does not match its snapshot/sample")
        pair = (link["strain_id"], sample)
        if pair in seen:
            raise ValueError("ATB strain inventory has duplicate strain/sample links")
        seen.add(pair)
        sample_links = _sample_links(link["sample_evidence_json"], link["strain_id"], sample_id)
        evidence = {"release": release, "sample_id": link["sample_id"], "dataset": row["dataset"],
                    "run_accessions": row["run_accession"], "assembly_seqkit_sum": row["assembly_seqkit_sum"],
                    "assembly_filter": row["asm_pipe_filter"], "hq_filter": row["hq_filter"],
                    "download_url": row["aws_url"], "archive_url": row["osf_tarball_url"],
                    "archive_filename": row["osf_tarball_filename"],
                    "sample_links": sample_links}
        if row["assembly_accession"] not in ("", "NA"):
            evidence["ena_analysis_id"] = f"ena.analysis:{row['assembly_accession']}"
        if row["sylph_species"] not in ("", "NA"):
            evidence["sylph_species"] = row["sylph_species"]
        result[link["strain_id"]].append({"genome_id": link["atb_id"], "source_database": "allthebacteria",
                                         "source": "ALLTHEBACTERIA", "source_id": link["atb_id"],
                                         "genome_name": row["scientific_name"], "atb_evidence": evidence})
    return dict(result)


def provenance_problems(root: Path = ROOT, *, reproduce: bool = True) -> list[str]:
    """Check the compact crosswalk, its raw-input dependencies, and exact reproduction."""
    try:
        return _provenance_problems(root, reproduce=reproduce)
    except (OSError, ValueError, TypeError, KeyError, yaml.YAMLError) as exc:
        return [f"ATB provenance is missing or malformed: {exc}"]


def _provenance_problems(root: Path, *, reproduce: bool) -> list[str]:
    directory = root / "data/atb"
    manifest_path = directory / "MANIFEST.yaml"
    if not manifest_path.exists():
        return ["ATB manifest missing; run just atb-fetch and just atb-index --apply"]
    manifest = _manifest(directory, check_outputs=False)
    config = settings(root / "conf/allthebacteria.yaml")
    failures = []
    expected_source = {key: value for key, value in config.items()
                       if key not in ("metadata_path", "index_path")}
    if manifest.get("source") != expected_source or not manifest.get("extracted_at"):
        failures.append("ATB source pin or extraction timestamp differs from configuration")
    if manifest.get("inputs") != input_provenance(root / "data/raw"):
        failures.append("ATB input inventories changed; rebuild with just atb-index --apply")
    if {item.get("path") for item in manifest.get("outputs", [])} != set(OUTPUT_NAMES):
        failures.append("ATB manifest must cover exactly the four crosswalk inventories")
    for name in OUTPUT_NAMES:
        path = directory / name
        entry = next((item for item in manifest.get("outputs", []) if item.get("path") == name), None)
        if not path.exists() or entry != describe_output(path):
            failures.append(f"ATB {name}: missing or changed since extraction")
    tracked = subprocess.check_output(["git", "ls-files", "--", "data/atb/*.tsv"], cwd=root, text=True)
    if {Path(line).name for line in tracked.splitlines()} != set(OUTPUT_NAMES):
        failures.append("ATB manifest inventories must all be tracked, with no uncovered TSV files")
    if failures or not reproduce:
        return failures
    _, samples, ncbi, genomes = load_inputs(root / "data/raw")
    strain_links, genome_links, exclusions = build_links(read_rows(directory / "assemblies.tsv"), samples,
                                                         ncbi, genomes, release=config["release"])
    for name, expected in (("strain_links.tsv", strain_links), ("genome_links.tsv", genome_links),
                           ("exclusions.tsv", exclusions)):
        if read_rows(directory / name) != expected:
            failures.append(f"ATB {name} does not reproduce from the committed source evidence")
    summary = {
        "matched_samples": len(read_rows(directory / "assemblies.tsv")),
        "assembly_identifiers": len({row["atb_id"] for row in strain_links}),
        "strain_pairs": len(strain_links), "strains": len({row["strain_id"] for row in strain_links}),
        "genome_pairs": len({(row["atb_id"], row["genome_id"]) for row in genome_links}),
        "excluded_samples": len(exclusions),
    }
    if manifest["crosslinks"] != summary:
        failures.append("ATB crosslink summary does not reproduce from the committed source evidence")
    return failures


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("fetch", "index"))
    parser.add_argument("--config", type=Path, default=CONFIG)
    parser.add_argument("--metadata", type=Path)
    parser.add_argument("--index", type=Path)
    parser.add_argument("--apply", action="store_true", help="Publish the index and committed crosswalks")
    parser.add_argument("--force", action="store_true", help="Replace an existing metadata cache on fetch")
    args = parser.parse_args(argv)
    try:
        config = settings(args.config)
        metadata = args.metadata or ROOT / config["metadata_path"]
        if args.command == "fetch":
            print(fetch(config, metadata, force=args.force))
        else:
            manifest = generate(metadata, args.index or ROOT / config["index_path"], ATB_DIR,
                                ROOT / "data/raw", config, apply=args.apply, config_path=args.config)
            print(json.dumps({"catalog": manifest["catalog"], "crosslinks": manifest["crosslinks"]},
                             indent=2))
            print("Index and crosswalks written." if args.apply else
                  "Dry run: no index or crosswalks published.")
    except (OSError, ValueError, sqlite3.Error) as exc:
        parser.exit(1, f"AllTheBacteria: {exc}\n")
    return 0
