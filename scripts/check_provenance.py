#!/usr/bin/env python3
"""Verify hashes and coverage for every committed data/raw inventory.

Every tracked TSV under data/raw/ must be listed in MANIFEST.yaml with matching
row count, byte count and sha256, and every manifest output must be tracked.
A committed inventory nobody can trace to an extraction is the failure this
guards against.
"""

from __future__ import annotations

import csv
import hashlib
import re
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = REPO_ROOT / "data" / "raw"
MANIFEST = RAW_DIR / "MANIFEST.yaml"
SHA256_RE = re.compile(r"[0-9a-f]{64}")
SOURCE_RE = re.compile(r"kg-microbe@[0-9a-f]{40}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tsv_rows(path: Path) -> int:
    csv.field_size_limit(min(sys.maxsize, 2**31 - 1))
    with path.open(newline="", encoding="utf-8") as fh:
        return sum(1 for _row in csv.reader(fh, delimiter="\t")) - 1


def tracked_raw_tsvs() -> set[str]:
    completed = subprocess.run(["git", "ls-files", "--", "data/raw/*.tsv"], cwd=REPO_ROOT,
                               check=True, capture_output=True, text=True)
    return {Path(line).name for line in completed.stdout.splitlines() if line}


def manifest_contract_problems(manifest: dict) -> list[str]:
    failures = []
    if not SOURCE_RE.fullmatch(str(manifest.get("kg_microbe_source", ""))):
        failures.append("MANIFEST: kg_microbe_source must be kg-microbe@<40-character commit>")
    if not manifest.get("extracted_at"):
        failures.append("MANIFEST: extracted_at missing")
    for entry in manifest.get("inputs", []):
        for key in ("path", "bytes", "mtime"):
            if entry.get(key) in (None, ""):
                failures.append(f"MANIFEST input {entry.get('path', '<unnamed>')}: missing {key}")
        if entry.get("sha256") is not None and not SHA256_RE.fullmatch(str(entry["sha256"])):
            failures.append(f"MANIFEST input {entry.get('path')}: malformed sha256")
    paths = []
    for entry in manifest.get("outputs", []):
        for key in ("path", "rows", "bytes", "sha256"):
            if entry.get(key) in (None, ""):
                failures.append(f"MANIFEST output {entry.get('path', '<unnamed>')}: missing {key}")
        if not SHA256_RE.fullmatch(str(entry.get("sha256", ""))):
            failures.append(f"MANIFEST output {entry.get('path')}: malformed sha256")
        paths.append(entry.get("path"))
    if len(paths) != len(set(paths)):
        failures.append("MANIFEST: duplicate output paths")
    return failures


def problems() -> list[str]:
    if not MANIFEST.exists():
        return [f"{MANIFEST.relative_to(REPO_ROOT)} is missing"]
    manifest = yaml.safe_load(MANIFEST.read_text(encoding="utf-8")) or {}
    failures = manifest_contract_problems(manifest)
    outputs = {e["path"]: e for e in manifest.get("outputs", []) if e.get("path")}
    tracked = tracked_raw_tsvs()
    uncovered = sorted(tracked - outputs.keys())
    stale = sorted(outputs.keys() - tracked)
    if uncovered:
        failures.append(f"committed raw TSVs without provenance: {', '.join(uncovered)}")
    if stale:
        failures.append(f"manifest outputs not committed as raw TSVs: {', '.join(stale)}")
    for name in sorted(tracked & outputs.keys()):
        entry, path = outputs[name], RAW_DIR / name
        if tsv_rows(path) != int(entry["rows"]):
            failures.append(f"{name}: row count differs from its manifest")
        if path.stat().st_size != int(entry["bytes"]):
            failures.append(f"{name}: byte count differs from its manifest")
        if sha256(path) != entry["sha256"]:
            failures.append(f"{name}: sha256 differs from its manifest")
    return failures


def main() -> int:
    failures = problems()
    if failures:
        print("provenance check failed:\n  " + "\n  ".join(failures), file=sys.stderr)
        return 1
    manifest = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    print(f"provenance current: {len(manifest.get('outputs', []))} committed inventories from "
          f"{manifest.get('kg_microbe_source')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
