#!/usr/bin/env python3
"""Inventory historical Markdown observations, without inferring review outcomes."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORTS = Path("reports/yaml_record_review")
INDEX = Path("docs/legacy-review-inventory.tsv")
SECTIONS = (
    "Target", "Validation", "Identity and Grounding", "Evidence", "Completeness",
    "Findings", "Recommended Edits", "Follow-up Checks", "Additional Notes",
)
METADATA = ("Repository", "Started UTC", "Finished UTC", "Verdict")
COLUMNS = (
    "report_path", "target_id", "target_path", "reported_verdict",
    "reported_started_utc", "reported_finished_utc", "missing_metadata", "missing_sections",
    "report_sha256",
)


def field(text: str, name: str) -> str:
    values = re.findall(r"^- " + re.escape(name) + r":[ \t]*(.*)$", text, re.MULTILINE)
    if len(values) > 1:
        raise ValueError(f"duplicate metadata field: {name}")
    return values[0] if values else ""


def inventory(root: Path) -> list[dict[str, str]]:
    with (root / "data/taxa/PATHS.tsv").open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != ["identifier", "slug"]:
            raise ValueError("unexpected PATHS.tsv columns")
        targets = {}
        for row in reader:
            if row["slug"] in targets:
                raise ValueError(f"duplicate corpus slug: {row['slug']}")
            targets[row["slug"]] = row["identifier"]
    report_root = root / REPORTS
    if not report_root.is_dir() or report_root.is_symlink():
        raise ValueError("missing or symlinked report directory")
    paths = []
    # Filesystem enumeration deliberately includes hidden and ignored Markdown.
    for directory, dirs, files in os.walk(report_root):
        for name in dirs + files:
            path = Path(directory) / name
            if path.is_symlink():
                raise ValueError(f"symlink in archive: {path}")
        paths.extend(Path(directory) / name for name in files if name.endswith(".md"))
    if not paths:
        raise ValueError("empty historical archive")
    rows = []
    seen = set()
    for path in sorted(paths):
        match = re.fullmatch(r"(\d{8}T\d{6}Z)-([a-z0-9_]+)\.md", path.name)
        if not match:
            raise ValueError(f"invalid report filename: {path}")
        datetime.strptime(match[1], "%Y%m%dT%H%M%SZ")
        slug = match[2]
        if slug not in targets or slug in seen:
            raise ValueError(f"unmatched or duplicate report target: {slug}")
        seen.add(slug)
        content = path.read_bytes()
        text = content.decode("utf-8")
        locators = {
            value for value in re.findall(
                r"data/taxa/(?:archaea|bacteria|eukaryota|other)/[a-z0-9_]+\.yaml", text
            ) if Path(value).stem == slug
        }
        if len(locators) != 1:
            raise ValueError(f"missing or ambiguous report target path: {path}")
        locator = locators.pop()
        target = root / locator
        if not target.is_file() or target.is_symlink():
            raise ValueError(f"missing or symlinked corpus target: {locator}")
        if not re.search(r"(?<![A-Za-z0-9_])" + re.escape(targets[slug]) + r"(?![A-Za-z0-9_])", text):
            raise ValueError(f"report does not mention indexed target ID: {path}")
        metadata = {name: field(text, name) for name in METADATA}
        headings = re.findall(r"^## (.+)$", text, re.MULTILINE)
        rows.append({
            "report_path": path.relative_to(root).as_posix(),
            "report_sha256": hashlib.sha256(content).hexdigest(),
            "target_id": targets[slug],
            "target_path": locator,
            "reported_verdict": metadata["Verdict"],
            "reported_started_utc": metadata["Started UTC"],
            "reported_finished_utc": metadata["Finished UTC"],
            "missing_metadata": ";".join(name for name, value in metadata.items() if not value),
            "missing_sections": ";".join(name for name in SECTIONS if name not in headings),
        })
    return rows


def render(rows: list[dict[str, str]]) -> str:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def assert_preserved(root: Path, base: str) -> None:
    subprocess.run(
        ["git", "cat-file", "-e", f"{base}^{{commit}}"], cwd=root, check=True, capture_output=True,
    )
    result = subprocess.run(
        ["git", "diff", "--name-status", "--no-renames", "-z", base, "--", str(REPORTS)],
        cwd=root, check=True, capture_output=True, text=True,
    )
    parts = result.stdout.rstrip("\0").split("\0") if result.stdout else []
    for status, path in zip(parts[::2], parts[1::2], strict=True):
        if status != "A":
            raise ValueError(f"historical report changed relative to {base}: {status} {path}")


def check(root: Path, base: str) -> list[dict[str, str]]:
    assert_preserved(root, base)
    rows = inventory(root)
    if (root / INDEX).read_bytes() != render(rows).encode("utf-8"):
        raise ValueError("legacy review inventory drift: inspect changes before rebuilding the index")
    return rows


def summary(rows: list[dict[str, str]]) -> dict:
    return {
        "historical_reports": len(rows),
        "reports_by_domain": dict(sorted(Counter(Path(r["target_path"]).parts[2] for r in rows).items())),
        "reported_verdicts_not_reassessed": dict(sorted(Counter(
            r["reported_verdict"] or "NOT_RECORDED" for r in rows
        ).items())),
        "reports_missing_metadata": sum(bool(r["missing_metadata"]) for r in rows),
        "reports_missing_sections": sum(bool(r["missing_sections"]) for r in rows),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="rebuild only the inventory, never the reports")
    mode.add_argument("--check", action="store_true", help="verify inventory and preserved report bytes")
    parser.add_argument("--base", default=os.environ.get("RECORD_REVIEW_BASE") or "HEAD")
    args = parser.parse_args()
    try:
        if args.write:
            assert_preserved(ROOT, args.base)
            rows = inventory(ROOT)
            (ROOT / INDEX).write_text(render(rows), encoding="utf-8", newline="")
        else:
            rows = check(ROOT, args.base)
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        print(f"Legacy archive check failed: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(summary(rows), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
