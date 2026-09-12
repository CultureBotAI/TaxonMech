"""Publish and verify a pinned StrainInfo snapshot and deposit-specific links."""

from __future__ import annotations

import argparse
import csv
import datetime
import gzip
import io
import json
import os
import re
import shutil
import subprocess
import tempfile
from collections import Counter, defaultdict
from collections.abc import Iterator
from itertools import zip_longest
from pathlib import Path

import yaml

from taxonmech.atb import sha256
from taxonmech.extract import describe_output, write_tsv
from taxonmech.genome_sources import normalize_culture_identifier
from taxonmech.straininfo_links import (
    ASSEMBLY,
    ASSEMBLY_COLUMNS,
    DEPOSIT_STATUSES,
    DOI,
    EXCLUSION_FIELDS,
    NUCLEOTIDE,
    RELATED_COLUMNS,
    STRAIN_FIELDS,
    STRAIN_STATUSES,
    build_links,
    positive_id,
    read_records,
)

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "data/straininfo"
CONFIG = ROOT / "conf/straininfo.yaml"
TABLES = {
    "strain_links.tsv": STRAIN_FIELDS,
    "assemblies.tsv": ASSEMBLY_COLUMNS,
    "related_records.tsv.gz": RELATED_COLUMNS,
    "exclusions.tsv": EXCLUSION_FIELDS,
}
OUTPUT_NAMES = ("SOURCE.json", "records.jsonl.gz", *TABLES)
INPUT_PATHS = ("data/raw/bacdive_strains.tsv", "src/taxonmech/data/cafi_acronyms.json")
SHA = re.compile(r"[0-9a-f]{64}")


def iter_rows(path: Path, *, required: tuple | list = (), nonempty: bool = False) -> Iterator[dict]:
    """Read either table format without keeping a second copy during replay."""
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        fields = reader.fieldnames or []
        if (
            not fields
            or len(fields) != len(set(fields))
            or any(not f for f in fields)
            or not set(required) <= set(fields)
        ):
            raise ValueError(f"{path}: missing or duplicate TSV headers")
        count = 0
        for row in reader:
            if None in row or any(v is None for v in row.values()):
                raise ValueError(f"{path}:{reader.line_num}: malformed TSV row")
            count += 1
            yield row
        if nonempty and not count:
            raise ValueError(f"{path}: empty source inventory")


def read_rows(path: Path, *, required: tuple | list = (), nonempty: bool = False) -> list[dict]:
    return list(iter_rows(path, required=required, nonempty=nonempty))


def write_table(path: Path, fields: tuple | list, rows: list[dict]) -> None:
    if path.suffix != ".gz":
        write_tsv(path, list(fields), rows)
        return
    with (
        path.open("wb") as raw,
        gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as zipped,
        io.TextIOWrapper(zipped, encoding="utf-8", newline="") as handle,
    ):
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def settings(path: Path = CONFIG) -> dict:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    required = {
        "snapshot",
        "snapshot_path",
        "snapshot_sha256",
        "api_version",
        "api_base",
        "license",
        "license_url",
        "citation",
    }
    if (
        not isinstance(value, dict)
        or set(value) != required
        or any(not isinstance(v, str) or not v for v in value.values())
    ):
        raise ValueError("StrainInfo configuration must supply the complete source pin")
    if not SHA.fullmatch(value["snapshot_sha256"]):
        raise ValueError("StrainInfo snapshot SHA256 is malformed")
    datetime.date.fromisoformat(value["snapshot"])
    if (
        value["api_base"] != "https://api.straininfo.dsmz.de"
        or value["api_version"] != "2.1.0"
        or value["license"] != "CC-BY-4.0"
        or value["license_url"] != "https://creativecommons.org/licenses/by/4.0/"
        or value["citation"] != "https://doi.org/10.1093/database/baaf059"
    ):
        raise ValueError("StrainInfo source/API/license contract differs from the supported primary resource")
    return value


def input_provenance(root: Path = ROOT) -> list[dict]:
    return [
        {"path": name, "bytes": (root / name).stat().st_size, "sha256": sha256(root / name)}
        for name in INPUT_PATHS
    ]


def file_info(path: Path) -> dict:
    return {"path": path.name, "bytes": path.stat().st_size, "sha256": sha256(path)}


def output_info(path: Path) -> dict:
    if path.name.endswith(".tsv.gz"):
        with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
            rows = sum(1 for _ in csv.reader(handle, delimiter="\t")) - 1
        return {"path": path.name, "rows": rows, "bytes": path.stat().st_size, "sha256": sha256(path)}
    return describe_output(path) if path.suffix == ".tsv" else file_info(path)


def source_metadata(path: Path) -> dict:
    source = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(source, dict) or source.get("format_version") != 1:
        raise ValueError("StrainInfo snapshot metadata has an unsupported format")
    stamp = source.get("captured_at")
    if not isinstance(stamp, str):
        raise ValueError("StrainInfo snapshot requires a UTC capture timestamp")
    datetime.datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%SZ")
    if (
        source.get("api_version") != "2.1.0"
        or source.get("license") != "CC-BY-4.0"
        or source.get("api_base") != "https://api.straininfo.dsmz.de"
    ):
        raise ValueError("StrainInfo snapshot identifies a different API or license")
    for key in ("catalog_count", "candidate_count"):
        if type(source.get(key)) is not int or source[key] <= 0:
            raise ValueError(f"StrainInfo snapshot requires positive {key}")
    if source["candidate_count"] > source["catalog_count"]:
        raise ValueError("StrainInfo candidate count exceeds the complete search catalog")
    record = source.get("records")
    if (
        not isinstance(record, dict)
        or record.get("path") != "records.jsonl.gz"
        or type(record.get("rows")) is not int
        or record["rows"] != source["candidate_count"]
        or type(record.get("bytes")) is not int
        or record["bytes"] <= 0
        or not isinstance(record.get("sha256"), str)
        or not SHA.fullmatch(record["sha256"])
    ):
        raise ValueError("StrainInfo source projection metadata is incomplete")
    responses = source.get("responses")
    if not isinstance(responses, list) or not responses:
        raise ValueError("StrainInfo snapshot must retain primary request provenance")
    seen = set()
    for response in responses:
        if (
            not isinstance(response, dict)
            or response.get("kind") not in {"ids", "search", "records"}
            or not isinstance(response.get("url"), str)
            or not response["url"].startswith(source["api_base"] + "/")
            or type(response.get("bytes")) is not int
            or response["bytes"] <= 0
            or not isinstance(response.get("sha256"), str)
            or not SHA.fullmatch(response["sha256"])
            or response["url"] in seen
        ):
            raise ValueError("StrainInfo response metadata is incomplete or duplicated")
        seen.add(response["url"])
    if {r["kind"] for r in responses} != {"ids", "search", "records"}:
        raise ValueError("StrainInfo snapshot must include the census, search pages and rich records")
    return source


def _checked_records(path: Path, source: dict) -> Iterator[dict]:
    """Verify the actual unique SI-ID census, not only its declared row count."""
    seen = set()
    for record in read_records(path):
        number = positive_id(record["strain"].get("siID"), "strain.siID")
        if number in seen:
            raise ValueError(f"Duplicate StrainInfo projected record: straininfo.strain:{number}")
        seen.add(number)
        yield record
    if len(seen) != source["candidate_count"] or len(seen) != source["records"]["rows"]:
        raise ValueError("StrainInfo actual source record count differs from its captured candidate count")


def summary(tables: tuple[list, list, list, list], source: dict) -> dict:
    links, assemblies, related, exclusions = tables
    return {
        "catalog_strains": source["catalog_count"],
        "source_records": source["candidate_count"],
        "straininfo_strains": len({r["straininfo_strain_id"] for r in links}),
        "straininfo_deposits": len({r["straininfo_deposit_id"] for r in links}),
        "taxonmech_strains": len({r["strain_id"] for r in links}),
        "deposit_matches": len(links),
        "ncbi_assemblies": len({r["assembly_id"] for r in assemblies}),
        "ncbi_strain_pairs": len({(r["strain_id"], r["assembly_id"]) for r in assemblies}),
        "assembly_assertions": len(assemblies),
        "nucleotide_sequences": len(
            {r["record_id"] for r in related if r["record_type"] == "NUCLEOTIDE_SEQUENCE"}
        ),
        "related_assertions": len(related),
        "exclusions": len(exclusions),
        "exclusion_reasons": dict(sorted(Counter(r["reason"] for r in exclusions).items())),
    }


def _publish(work: Path, directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    installed, backups = [], []
    try:
        for name in (*OUTPUT_NAMES, "MANIFEST.yaml"):
            target, backup = directory / name, work / ("previous-" + name)
            if target.exists() or target.is_symlink():
                os.replace(target, backup)
                backups.append((backup, target))
            os.replace(work / name, target)
            installed.append(target)
    except BaseException:
        for target in reversed(installed):
            target.unlink(missing_ok=True)
        for backup, target in reversed(backups):
            os.replace(backup, target)
        raise


def generate(
    snapshot: Path,
    directory: Path,
    root: Path,
    config: dict,
    *,
    apply: bool = False,
    config_path: Path | None = None,
) -> dict:
    source_path, records_path = snapshot / "SNAPSHOT.json", snapshot / "records.jsonl.gz"
    protected = {
        source_path.resolve(),
        records_path.resolve(),
        CONFIG.resolve(),
        *((root / name).resolve() for name in INPUT_PATHS),
    }
    if config_path is not None:
        protected.add(config_path.resolve())
    targets = [(directory / name).resolve() for name in (*OUTPUT_NAMES, "MANIFEST.yaml")]
    if (
        len(set(targets)) != len(targets)
        or protected.intersection(targets)
        or any(
            path == (root / "data/raw").resolve() or (root / "data/raw").resolve() in path.parents
            for path in targets
        )
        or any(path.is_dir() for path in targets)
    ):
        raise ValueError("StrainInfo destinations cannot overwrite inputs or another output")
    before = input_provenance(root)
    if sha256(source_path) != config["snapshot_sha256"]:
        raise ValueError("StrainInfo snapshot differs from the configured SHA256")
    source = source_metadata(source_path)
    if source.get("inputs") != before:
        raise ValueError("StrainInfo snapshot was selected against different strain/authority inventories")
    if {k: v for k, v in source["records"].items() if k != "rows"} != file_info(records_path):
        raise ValueError("StrainInfo projected source records differ from their pinned snapshot")
    strains = read_rows(
        root / INPUT_PATHS[0], required=("strain_id", "bacdive_id", "culture_collection_ids"), nonempty=True
    )
    tables = build_links(_checked_records(records_path, source), strains)
    if apply:
        directory.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=".straininfo-build-", dir=directory.parent if apply else None
    ) as tmp:
        work = Path(tmp)
        shutil.copyfile(source_path, work / "SOURCE.json")
        shutil.copyfile(records_path, work / "records.jsonl.gz")
        for (name, fields), rows in zip(TABLES.items(), tables, strict=True):
            write_table(work / name, fields, rows)
        manifest = {
            "extracted_at": source["captured_at"],
            "source": {k: v for k, v in config.items() if k != "snapshot_path"},
            "inputs": before,
            "outputs": [output_info(work / name) for name in OUTPUT_NAMES],
            "summary": summary(tables, source),
        }
        (work / "MANIFEST.yaml").write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
        del tables  # Replay/convert without retaining a second complete set of derived rows.
        record_links(work, root=root, config=config)
        if before != input_provenance(root) or sha256(source_path) != config["snapshot_sha256"]:
            raise ValueError("StrainInfo source inputs changed during generation")
        if sha256(records_path) != source["records"]["sha256"]:
            raise ValueError("StrainInfo projected records changed during generation")
        if apply:
            _publish(work, directory)
    return manifest


def _manifest(directory: Path) -> dict:
    manifest = yaml.safe_load((directory / "MANIFEST.yaml").read_text(encoding="utf-8"))
    if not isinstance(manifest, dict) or not isinstance(manifest.get("source"), dict):
        raise ValueError("StrainInfo manifest must contain the source pin")
    source = source_metadata(directory / "SOURCE.json")
    if (
        manifest.get("extracted_at") != source["captured_at"]
        or manifest["source"].get("snapshot_sha256") != sha256(directory / "SOURCE.json")
        or manifest.get("inputs") != source.get("inputs")
    ):
        raise ValueError("StrainInfo manifest disagrees with its captured primary source")
    outputs = manifest.get("outputs")
    if (
        not isinstance(outputs, list)
        or len(outputs) != len(OUTPUT_NAMES)
        or any(not isinstance(e, dict) for e in outputs)
        or {entry.get("path") for entry in outputs} != set(OUTPUT_NAMES)
    ):
        raise ValueError("StrainInfo manifest must cover exactly all component outputs")
    for entry in outputs:
        if entry != output_info(directory / entry["path"]):
            raise ValueError(f"StrainInfo output differs from its manifest: {entry['path']}")
    if {k: v for k, v in source["records"].items() if k != "rows"} != file_info(
        directory / "records.jsonl.gz"
    ):
        raise ValueError("StrainInfo committed source projection differs from the pinned primary snapshot")
    return manifest


def _replay(directory: Path, manifest: dict, root: Path) -> tuple[list, list, list, list]:
    """Verify every binding against source records and current inventoried deposits."""
    before = input_provenance(root)
    if manifest["inputs"] != before:
        raise ValueError("StrainInfo input inventories changed; capture and rebuild the overlay")
    source = source_metadata(directory / "SOURCE.json")
    strains = read_rows(
        root / INPUT_PATHS[0], required=("strain_id", "bacdive_id", "culture_collection_ids"), nonempty=True
    )
    tables = build_links(_checked_records(directory / "records.jsonl.gz", source), strains)
    for (name, columns), expected in zip(TABLES.items(), tables, strict=True):
        actual = iter_rows(directory / name, required=columns)
        for expected_row, actual_row in zip_longest(expected, actual):
            if expected_row != actual_row:
                raise ValueError(f"StrainInfo {name} does not reproduce from primary deposit evidence")
    if summary(tables, source) != manifest.get("summary"):
        raise ValueError("StrainInfo counts do not reproduce from the committed evidence")
    if before != input_provenance(root):
        raise ValueError("StrainInfo input inventories changed during source replay")
    for entry in manifest["outputs"]:
        path = directory / entry["path"]
        if path.stat().st_size != entry["bytes"] or sha256(path) != entry["sha256"]:
            raise ValueError(f"StrainInfo output changed during source replay: {entry['path']}")
    if yaml.safe_load((directory / "MANIFEST.yaml").read_text(encoding="utf-8")) != manifest:
        raise ValueError("StrainInfo manifest changed during source replay")
    return tables


def _link(row: dict, *, assembly: bool) -> tuple[str, dict]:
    evidence = json.loads(row["straininfo_evidence_json"])
    required = {
        "strain_id",
        "deposit_id",
        "deposit_designation",
        "strain_status",
        "deposit_status",
        "match_method",
    }
    optional = {
        "strain_doi",
        "source_bacdive_id",
        "sequence_type",
        "sequence_deposit_id",
        "bacdive_reference_conflict",
    }
    if (
        not isinstance(evidence, dict)
        or not required <= evidence.keys()
        or evidence.keys() - required - optional
        or any(
            not isinstance(v, str) or not v for k, v in evidence.items() if k != "bacdive_reference_conflict"
        )
    ):
        raise ValueError("StrainInfo links require a complete, closed evidence object")
    if (
        not re.fullmatch(r"straininfo\.strain:[1-9][0-9]*", evidence["strain_id"])
        or not re.fullmatch(r"straininfo\.deposit:[1-9][0-9]*", evidence["deposit_id"])
        or row["source"] != "STRAININFO"
        or row["source_id"] != evidence["strain_id"]
        or evidence["strain_status"] not in STRAIN_STATUSES
        or evidence["deposit_status"] not in DEPOSIT_STATUSES - {"erroneous data"}
        or evidence["match_method"] != "culture_identifier"
        or row["source_strain_field"] != "deposits.designation"
        or row["source_strain_identifiers"] != evidence["deposit_designation"]
        or not row["matched_strain_id"].startswith("kgmicrobe.strain:")
        or not (key := normalize_culture_identifier(evidence["deposit_designation"]))
        or normalize_culture_identifier(row["matched_strain_id"].split(":", 1)[1]) != key
    ):
        raise ValueError("StrainInfo link has inconsistent strain/deposit evidence")
    if "bacdive_reference_conflict" in evidence and type(evidence["bacdive_reference_conflict"]) is not bool:
        raise ValueError("StrainInfo conflict flag must be boolean")
    if "strain_doi" in evidence:
        match = DOI.fullmatch(evidence["strain_doi"].removeprefix("DOI:"))
        if (
            not evidence["strain_doi"].startswith("DOI:")
            or not match
            or match[1] != evidence["strain_id"].split(":")[1]
        ):
            raise ValueError("StrainInfo DOI identifies a different strain")
    seq_type = evidence.get("sequence_type")
    if assembly:
        valid = (
            row["assembly_id"].startswith("ncbi.assembly:")
            and ASSEMBLY.fullmatch(row["assembly_id"].split(":", 1)[1])
            and seq_type == "genome"
        )
    elif row["record_type"] == "NUCLEOTIDE_SEQUENCE":
        valid = (
            row["record_id"].startswith("INSDC:")
            and NUCLEOTIDE.fullmatch(row["record_id"].split(":", 1)[1])
            and seq_type in {"gene", "rrnaop", "patent"}
        )
    else:
        key = {"STRAININFO_STRAIN": "strain_id", "STRAININFO_DEPOSIT": "deposit_id"}.get(row["record_type"])
        valid = key is not None and row["record_id"] == evidence[key] and seq_type is None
    if not valid or (
        seq_type
        and (
            evidence.get("sequence_deposit_id") != evidence["deposit_id"]
            or row["source_field"] != "strain.sequence.accessionNumber"
        )
    ):
        raise ValueError("StrainInfo target does not match its explicit source deposit/sequence type")
    return row["strain_id"], {
        **{k: v for k, v in row.items() if k not in {"strain_id", "straininfo_evidence_json"} and v},
        "straininfo_evidence": evidence,
    }


def record_links(
    directory: Path = DIRECTORY, *, root: Path = ROOT, config: dict | None = None
) -> tuple[dict, dict]:
    """Convert only links reproduced from the configured source and current strain inventory.

    Ordinary readers require the repository configuration. Generation can
    explicitly supply another configuration while preparing a new snapshot;
    the component's self-reported pin is never sufficient on its own.
    """
    source_config = settings(root / "conf/straininfo.yaml") if config is None else dict(config)
    manifest = _manifest(directory)
    if manifest["source"] != {k: v for k, v in source_config.items() if k != "snapshot_path"}:
        raise ValueError("StrainInfo source pin differs from configuration")
    _, assemblies, related, _ = _replay(directory, manifest, root)
    if config is None and settings(root / "conf/straininfo.yaml") != source_config:
        raise ValueError("StrainInfo configured source pin changed during conversion")
    result = []
    for rows, is_assembly in ((assemblies, True), (related, False)):
        grouped = defaultdict(list)
        for row in rows:
            sid, link = _link(row, assembly=is_assembly)
            grouped[sid].append(link)
        result.append(dict(grouped))
    return tuple(result)


def provenance_problems(root: Path = ROOT, *, reproduce: bool = True) -> list[str]:
    try:
        directory = root / "data/straininfo"
        manifest = _manifest(directory)
        config = settings(root / "conf/straininfo.yaml")
        failures = []
        if manifest["source"] != {k: v for k, v in config.items() if k != "snapshot_path"}:
            failures.append("StrainInfo source pin differs from configuration")
        if manifest["inputs"] != input_provenance(root):
            failures.append("StrainInfo input inventories changed; capture and rebuild the overlay")
        tracked = subprocess.check_output(["git", "ls-files", "--", "data/straininfo"], cwd=root, text=True)
        if {Path(name).name for name in tracked.splitlines()} != {*OUTPUT_NAMES, "MANIFEST.yaml"}:
            failures.append("StrainInfo manifest must cover all and only tracked component files")
        if failures:
            return failures
        if reproduce:
            _replay(directory, manifest, root)
        else:
            for _ in _checked_records(
                directory / "records.jsonl.gz", source_metadata(directory / "SOURCE.json")
            ):
                pass
        return failures
    except (OSError, ValueError, TypeError, KeyError, yaml.YAMLError) as exc:
        return [f"StrainInfo provenance missing or malformed: {exc}"]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG)
    parser.add_argument("--snapshot", type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)
    try:
        config = settings(args.config)
        result = generate(
            args.snapshot or ROOT / config["snapshot_path"],
            DIRECTORY,
            ROOT,
            config,
            apply=args.apply,
            config_path=args.config,
        )
        print(json.dumps(result["summary"], indent=2))
        print("StrainInfo component written." if args.apply else "Dry run: no component files written.")
    except (OSError, ValueError, TypeError, KeyError) as exc:
        parser.exit(1, f"StrainInfo: {exc}\n")
    return 0
