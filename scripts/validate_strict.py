#!/usr/bin/env python3
"""Strict LinkML validation harness for TaxonMech instance records.

Wraps the in-process linkml.validator with JsonschemaValidationPlugin(closed=True)
so unknown fields are flagged (linkml-validate's default open mode silently lets
unknown fields pass). Emits a structured TSV of every ERROR result and exits
non-zero if any are found.

Usage:
    python scripts/validate_strict.py [PATH ...]
    python scripts/validate_strict.py --sample 5
    python scripts/validate_strict.py --out reports/instance_validation_failures.tsv

Paths may be files or directories; directories are walked for *.yaml.
Default scope when no paths given: data/taxa/
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from collections.abc import Iterable
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml.validator.report import Severity

_REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = _REPO_ROOT / "src" / "taxonmech" / "schema" / "taxonmech.yaml"
DEFAULT_ROOTS = [_REPO_ROOT / "data" / "taxa"]
TARGET_CLASS = "TaxonRecord"

_VALIDATOR: Validator | None = None


def _get_validator() -> Validator:
    global _VALIDATOR
    if _VALIDATOR is None:
        _VALIDATOR = Validator(
            schema=str(SCHEMA_PATH),
            validation_plugins=[JsonschemaValidationPlugin(closed=True)],
        )
    return _VALIDATOR


_CATEGORY_RULES: list[tuple[str, re.Pattern[str]]] = [
    ("unexpected_field",
     re.compile(r"Additional properties are not allowed \('(?P<key>[^']+)' was unexpected\) "
                r"in (?P<path>\S+)")),
    ("missing_required", re.compile(r"'(?P<key>[^']+)' is a required property in (?P<path>\S+)")),
    ("enum_mismatch", re.compile(r"'(?P<value>[^']+)' is not one of \[(?P<choices>[^\]]+)\]")),
    ("type_mismatch", re.compile(r"(?P<value>'[^']+'|\S+) is not of type '(?P<type>[^']+)'")),
    ("pattern_mismatch", re.compile(r"(?P<value>'[^']+'|\S+) does not match (?P<pattern>'[^']+')")),
    ("format_mismatch", re.compile(r"(?P<value>'[^']+'|\S+) is not a '(?P<format>[^']+)'")),
    ("range_violation", re.compile(r"(?P<value>\S+) is (less than|greater than) (?P<bound>\S+)")),
]


def classify(message: str) -> tuple[str, str]:
    for name, rule in _CATEGORY_RULES:
        m = rule.search(message)
        if m:
            return name, "|".join(f"{k}={v}" for k, v in m.groupdict().items())
    return "other", ""


def validate_one(path: Path) -> list[dict]:
    validator = _get_validator()
    try:
        with path.open() as f:
            instance = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return [{"file": str(path), "category": "yaml_parse_error", "detail": "", "path": "",
                 "message": str(e).splitlines()[0][:300]}]
    if instance is None:
        return [{"file": str(path), "category": "empty_file", "detail": "", "path": "",
                 "message": "file parsed as None"}]
    try:
        report = validator.validate(instance, target_class=TARGET_CLASS)
    except Exception as e:  # noqa: BLE001 — surface anything weird as a row
        return [{"file": str(path), "category": "validator_crash", "detail": type(e).__name__, "path": "",
                 "message": str(e)[:300]}]
    rows = []
    for result in report.results:
        if result.severity != Severity.ERROR:
            continue
        category, detail = classify(result.message)
        rows.append({"file": str(path), "category": category, "detail": detail,
                     "path": result.instance_index or "", "message": result.message[:300]})
    return rows


_YAML_SUFFIXES = {".yaml", ".yml"}


def iter_yaml_files(paths: Iterable[Path]) -> list[Path]:
    out: list[Path] = []
    for p in paths:
        if p.is_file():
            if p.suffix.lower() not in _YAML_SUFFIXES:
                print(f"Skipping non-YAML file: {p}", file=sys.stderr)
                continue
            out.append(p)
        elif p.is_dir():
            out.extend(sorted(p.rglob("*.yaml")))
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="Files or directories. Defaults to data/taxa/.")
    parser.add_argument("--out", type=Path, default=Path("reports/instance_validation_failures.tsv"))
    parser.add_argument("--sample", type=int, metavar="N", help="Validate only the first N files.")
    parser.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 4) - 1))
    parser.add_argument("--fail-on", choices=("error", "never"), default="error")
    parser.add_argument("--quiet", action="store_true", help="Suppress per-file progress.")
    args = parser.parse_args()

    files = iter_yaml_files(args.paths or DEFAULT_ROOTS)
    if args.sample:
        files = files[: args.sample]
    if not files:
        print("No YAML files found.", file=sys.stderr)
        return 2
    args.out.parent.mkdir(parents=True, exist_ok=True)
    print(f"Validating {len(files)} files with {args.workers} workers; schema={SCHEMA_PATH}", file=sys.stderr)

    all_rows: list[dict] = []
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(validate_one, p): p for p in files}
        for done, fut in enumerate(as_completed(futures), start=1):
            all_rows.extend(fut.result())
            if not args.quiet and done % 50 == 0:
                print(f"  {done}/{len(files)} files processed, {len(all_rows)} ERROR rows so far",
                      file=sys.stderr)

    all_rows.sort(key=lambda r: (r["file"], r["path"], r["category"], r["message"]))
    with args.out.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["file", "category", "detail", "path", "message"],
                                delimiter="\t", quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
        writer.writeheader()
        writer.writerows(all_rows)

    by_cat: dict[str, int] = {}
    files_with_errors: set[str] = set()
    for row in all_rows:
        by_cat[row["category"]] = by_cat.get(row["category"], 0) + 1
        files_with_errors.add(row["file"])
    print("\n=== validate-strict summary ===", file=sys.stderr)
    print(f"  files scanned:      {len(files)}", file=sys.stderr)
    print(f"  files with ERROR:   {len(files_with_errors)}", file=sys.stderr)
    print(f"  total ERROR rows:   {len(all_rows)}", file=sys.stderr)
    print(f"  TSV:                {args.out}", file=sys.stderr)
    for cat, count in sorted(by_cat.items(), key=lambda kv: -kv[1]):
        print(f"    {cat:24s} {count:>8d}", file=sys.stderr)
    return 1 if args.fail_on == "error" and all_rows else 0


if __name__ == "__main__":
    sys.exit(main())
