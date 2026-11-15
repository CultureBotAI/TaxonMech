#!/usr/bin/env python3
"""Audit prior target-review coverage from immutable, tracked Git inputs.

This is a coverage ledger, not a scientific reassessment or a bundle validator.
Legacy report coverage excludes a target under the stated publication policy;
it does not confer structured scientific-review status. Captured working-tree
hashes remain attestations even when the recorded commit has different bytes.
"""

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
from pathlib import Path, PurePosixPath
from typing import Any

import yaml

POLICY = "any_prior_target_review_coverage"
LEGACY = "docs/legacy-review-inventory.tsv"
SHARD = re.compile(r"docs/structured-review-inventory/part-(\d+)\.tsv\Z")
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
COMMIT = re.compile(r"[0-9a-f]{40}\Z")
MAX_BLOB_BYTES = 64 * 1024 * 1024


class CoverageError(ValueError):
    """Missing, conflicting or unverifiable audit input."""


def require(condition: Any, message: str) -> None:
    if not condition:
        raise CoverageError(message)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def text(value: Any, label: str) -> str:
    require(isinstance(value, str) and bool(value.strip()), f"Missing/invalid {label}")
    return value


def relative_path(value: Any) -> str:
    value = text(value, "relative path")
    path = PurePosixPath(value)
    require(
        not path.is_absolute() and ".." not in path.parts and str(path) == value,
        f"Unsafe or ambiguous path: {value}",
    )
    return value


def hash_value(value: Any, label: str) -> str:
    require(isinstance(value, str) and SHA256.fullmatch(value), f"Invalid SHA256 for {label}")
    return value


class History:
    """Read only local Git objects; never fetch or consult checkout file contents."""

    def __init__(self, repository: Path):
        self.repository = repository
        self.env = {**os.environ, "GIT_NO_LAZY_FETCH": "1", "GIT_OPTIONAL_LOCKS": "0"}
        self.target_cache: dict[tuple[str, str], dict[str, str] | None] = {}
        self.revision_cache: dict[str, str] = {}

    def git(self, *args: str) -> bytes:
        result = subprocess.run(
            ["git", "-c", "core.fsmonitor=false", *args],
            cwd=self.repository,
            env=self.env,
            capture_output=True,
            check=False,
        )
        if result.returncode:
            raise CoverageError(f"Git {' '.join(args[:3])}: {result.stderr.decode().strip()}")
        return result.stdout

    def revision(self, value: str) -> str:
        if value not in self.revision_cache:
            self.revision_cache[value] = (
                self.git(
                    "rev-parse",
                    "--verify",
                    "--end-of-options",
                    value + "^{commit}",
                )
                .decode()
                .strip()
            )
        return self.revision_cache[value]

    def tracked(self, revision: str, *paths: str) -> dict[str, dict[str, Any]]:
        result = {}
        for item in self.git("ls-tree", "-r", "-z", "-l", revision, "--", *paths).split(b"\0"):
            if not item:
                continue
            metadata, path = item.decode().split("\t", 1)
            mode, kind, oid, size = metadata.split()
            require(kind == "blob" and mode in {"100644", "100755"}, f"Non-regular Git input: {path}")
            result[path] = {"path": path, "blob": oid, "mode": mode, "bytes": int(size)}
        return result

    def blob(self, entry: dict[str, Any]) -> bytes:
        require(entry["bytes"] <= MAX_BLOB_BYTES, f"Input exceeds size bound: {entry['path']}")
        data = self.git("cat-file", "blob", entry["blob"])
        require(len(data) == entry["bytes"], f"Git object size mismatch: {entry['path']}")
        return data

    def target(self, revision: str, path: str, *, optional: bool = False) -> dict[str, str] | None:
        key = (revision, path)
        if key not in self.target_cache:
            try:
                entry = self.tracked(revision, path).get(path)
            except CoverageError:
                if not optional:
                    raise
                entry = None
            if entry is None:
                require(optional, f"Missing target {revision}:{path}")
                self.target_cache[key] = None
            else:
                data = self.blob(entry)
                document = load_yaml(data, path)
                self.target_cache[key] = {
                    "blob": entry["blob"],
                    "sha256": digest(data),
                    "target_id": text(document.get("identifier"), f"target identifier in {revision}:{path}"),
                }
        result = self.target_cache[key]
        require(optional or result is not None, f"Missing target {revision}:{path}")
        return result


def load_yaml(data: bytes, label: str) -> dict[str, Any]:
    try:
        result = yaml.load(data, Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))
    except yaml.YAMLError as error:
        raise CoverageError(f"Invalid YAML {label}: {error}") from error
    require(isinstance(result, dict), f"Expected YAML mapping: {label}")
    return result


def bundle_targets(document: dict[str, Any], path: str) -> list[dict[str, Any]]:
    require(type(document.get("scientific_review")) is bool, f"Missing scientific status: {path}")
    scope = document.get("scope", {})
    require(isinstance(scope, dict), f"Invalid scope: {path}")
    reviewed = scope.get("reviewed_target_ids")
    require(
        isinstance(reviewed, list)
        and all(isinstance(value, str) for value in reviewed)
        and len(reviewed) == len(set(reviewed)),
        f"Invalid/duplicate reviewed target IDs: {path}",
    )
    targets = document.get("targets")
    require(isinstance(targets, list), f"Missing targets: {path}")
    by_id = {}
    for target in targets:
        require(isinstance(target, dict), f"Invalid target: {path}")
        identifier = text(target.get("target_id"), f"target ID in {path}")
        require(identifier not in by_id, f"Ambiguous target ID {identifier}: {path}")
        relative_path(target.get("path"))
        by_id[identifier] = target
    require(set(reviewed) <= by_id.keys(), f"Reviewed target missing from targets: {path}")
    return [by_id[identifier] for identifier in sorted(reviewed)]


def captured_target(document: dict[str, Any], target: dict[str, Any], path: str) -> dict[str, str]:
    source = document.get("source")
    require(isinstance(source, dict), f"Missing source: {path}")
    revision = source.get("git_revision")
    require(isinstance(revision, str) and COMMIT.fullmatch(revision), f"Invalid source revision: {path}")
    require(source.get("state") in {"git_commit", "working_tree"}, f"Unknown source state: {path}")
    inputs = source.get("inputs")
    require(
        isinstance(inputs, list) and all(isinstance(x, dict) for x in inputs),
        f"Missing/invalid source inputs: {path}",
    )
    matches = [item for item in inputs if item.get("path") == target["path"]]
    require(len(matches) == 1, f"Missing/ambiguous captured target hash: {path}: {target['path']}")
    return {
        "git_revision": revision,
        "state": source["state"],
        "target_sha256": hash_value(matches[0].get("sha256"), target["path"]),
    }


def incoming_reviews(history: History, base: str, publication: str) -> tuple[list[dict], list[dict]]:
    tree = history.tracked(publication, "reviews/structured")
    fields = (
        history.git(
            "diff",
            "--no-ext-diff",
            "--no-textconv",
            "--no-renames",
            "--name-status",
            "-z",
            base,
            publication,
            "--",
            "reviews/structured",
        )
        .decode()
        .split("\0")[:-1]
    )
    require(len(fields) % 2 == 0, "Unrecognized publication diff")
    added = set()
    for status, path in zip(fields[::2], fields[1::2], strict=True):
        require(status == "A", f"Historical review changed/deleted: {status} {path}")
        require(path.endswith(("/review.yaml", "/review.md")), f"Unexpected review addition: {path}")
        added.add(path)
    require(added, "No added publication reviews")
    incoming, excluded = [], []
    for path in sorted(added):
        if not path.endswith("/review.yaml"):
            require(path.removesuffix(".md") + ".yaml" in added, f"Orphan Markdown: {path}")
            continue
        require(path.removesuffix(".yaml") + ".md" in added, f"Missing rendered Markdown: {path}")
        data = history.blob(tree[path])
        document = load_yaml(data, path)
        identifier = text(document.get("review_id"), f"review ID in {path}")
        require(PurePosixPath(path).parent.name == identifier, f"Review ID/path mismatch: {path}")
        targets = bundle_targets(document, path)
        reference = {
            "review_id": identifier,
            "path": path,
            "blob": tree[path]["blob"],
            "sha256": digest(data),
        }
        if not document["scientific_review"]:
            excluded.append(
                {**reference, "reason": "scientific_review_false_metadata_or_process_observation"}
            )
            continue
        require(
            document.get("kind") == "record"
            and len(targets) == 1
            and document["scope"].get("coverage") == "full"
            and document["scope"].get("population_size") == 1,
            f"Incoming scientific scope must be one fully reviewed record: {path}",
        )
        for target in targets:
            captured = captured_target(document, target, path)
            history.revision(captured["git_revision"])
            observed = history.target(
                captured["git_revision"],
                target["path"],
                optional=captured["state"] == "working_tree",
            )
            if captured["state"] == "git_commit":
                require(
                    observed is not None and observed["target_id"] == target["target_id"],
                    f"Source target identity mismatch: {path}",
                )
                require(
                    observed is not None and observed["sha256"] == captured["target_sha256"],
                    f"Captured git_commit target hash mismatch: {path}",
                )
            at_base = history.target(base, target["path"])
            require(
                at_base is not None and at_base["target_id"] == target["target_id"],
                f"Baseline target identity mismatch: {path}",
            )
            incoming.append(
                {
                    **reference,
                    "target_id": target["target_id"],
                    "target_path": target["path"],
                    "target_label": target.get("label"),
                    "captured_target": captured,
                    "source_commit_target": observed,
                    "captured_hash_matches_source_commit": (
                        observed["sha256"] == captured["target_sha256"] if observed else None
                    ),
                    "source_commit_identity_matches_target": (
                        observed["target_id"] == target["target_id"] if observed else None
                    ),
                    "base_target": at_base,
                    "working_tree_limitation": (
                        "Captured hash attests working-tree bytes; "
                        "commit comparison does not verify those bytes."
                        if captured["state"] == "working_tree"
                        else None
                    ),
                }
            )
    require(incoming, "No scientific publication targets")
    require(len({r["target_id"] for r in incoming}) == len(incoming), "Duplicate incoming target IDs")
    require(len({r["target_path"] for r in incoming}) == len(incoming), "Ambiguous incoming target paths")
    return incoming, excluded


def audit(repository: Path, base: str, publication: str) -> dict[str, Any]:
    history = History(repository)
    base, publication = history.revision(base), history.revision(publication)
    history.git("merge-base", "--is-ancestor", base, publication)
    incoming, excluded = incoming_reviews(history, base, publication)
    by_id = {row["target_id"]: row for row in incoming}
    by_path = {row["target_path"]: row for row in incoming}
    prior: dict[str, list[dict[str, Any]]] = {identifier: [] for identifier in by_id}
    files = history.tracked(base, "reviews/structured", "docs/structured-review-inventory", LEGACY)
    shards = sorted(path for path in files if SHARD.fullmatch(path))
    require(shards and LEGACY in files, "Missing required structured or legacy coverage inventory")
    indices = sorted(int(SHARD.fullmatch(path)[1]) for path in shards)
    require(indices == list(range(len(indices))), "Missing or duplicate structured inventory shard")
    bundles = sorted(p for p in files if p.startswith("reviews/structured/") and p.endswith("/review.yaml"))
    require(bundles, "Missing canonical baseline bundles")
    inputs, counts = (
        [],
        {
            "canonical_bundles": 0,
            "structured_rows": 0,
            "legacy_rows": 0,
            "excluded_baseline_metadata_bundles": 0,
        },
    )
    excluded_baseline = []
    excluded_baseline_targets = []

    def match(identifier: str, path: str) -> dict[str, Any] | None:
        row = by_id.get(identifier) or by_path.get(path)
        if row is not None:
            require(
                row["target_id"] == identifier and row["target_path"] == path,
                f"Ambiguous prior target identity: {identifier} {path}",
            )
        return row

    def source(path: str) -> bytes:
        data = history.blob(files[path])
        inputs.append({**files[path], "sha256": digest(data)})
        return data

    for path in bundles:
        data = source(path)
        document = load_yaml(data, path)
        targets = bundle_targets(document, path)
        counts["canonical_bundles"] += 1
        # Coverage concerns native taxon records, regardless of scientific status.
        # Metadata observations can reuse a native target ID for a review artifact;
        # classify the actual path before attempting a native identity match.
        native_targets = []
        for target in targets:
            if target["path"].startswith("data/taxa/") and target["path"].endswith(".yaml"):
                native_targets.append(target)
            else:
                excluded_baseline_targets.append(
                    {
                        "review_id": text(document.get("review_id"), path),
                        "path": path,
                        "target_id": target["target_id"],
                        "target_path": target["path"],
                        "scientific_review": document["scientific_review"],
                        "reason": "target_path_is_not_a_native_taxon_record",
                    }
                )
        if not native_targets:
            excluded_baseline.append(
                {
                    "review_id": text(document.get("review_id"), path),
                    "path": path,
                    "blob": files[path]["blob"],
                    "sha256": digest(data),
                    "reason": "no_explicit_native_taxon_record_targets",
                }
            )
            counts["excluded_baseline_metadata_bundles"] += 1
            continue
        for item in document.get("source", {}).get("inputs", []):
            if isinstance(item, dict) and SHARD.fullmatch(str(item.get("path", ""))):
                require(
                    item["path"] in files, f"Canonical bundle references missing inventory: {item['path']}"
                )
        for target in native_targets:
            row = match(target["target_id"], target["path"])
            if row is None:
                continue
            captured = captured_target(document, target, path)
            prior[row["target_id"]].append(
                {
                    "type": "canonical",
                    "path": path,
                    "line": 1,
                    "record_id": text(document.get("review_id"), path),
                    "blob": files[path]["blob"],
                    "sha256": digest(data),
                    "scientific_review": document["scientific_review"],
                    "completion": text(document.get("completion"), path),
                    "verdict": text(document.get("verdict"), path),
                    "target_sha256": captured["target_sha256"],
                    "source": captured,
                }
            )

    headers = {
        "structured": {
            "review_id",
            "round_id",
            "target_id",
            "target_path",
            "target_sha256",
            "verdict",
            "completion",
            "scientific_review",
        },
        "legacy": {"report_path", "target_id", "target_path", "reported_verdict", "report_sha256"},
    }
    for path in [*shards, LEGACY]:
        kind = "legacy" if path == LEGACY else "structured"
        reader = csv.DictReader(io.StringIO(source(path).decode()), delimiter="\t")
        require(
            reader.fieldnames is not None and headers[kind] <= set(reader.fieldnames),
            f"Missing inventory columns: {path}",
        )
        require(len(reader.fieldnames) == len(set(reader.fieldnames)), f"Duplicate inventory headers: {path}")
        for item in reader:
            counts[kind + "_rows"] += 1
            require(
                None not in item and all(value is not None for value in item.values()),
                f"Malformed inventory row: {path}:{reader.line_num}",
            )
            identifier = text(item["target_id"], f"{path}:{reader.line_num} target ID")
            target_path = relative_path(item["target_path"])
            row = match(identifier, target_path)
            if kind == "structured":
                hash_value(item["target_sha256"], f"{path}:{reader.line_num}")
                require(
                    item["scientific_review"] in {"true", "false"},
                    f"Unknown scientific status: {path}:{reader.line_num}",
                )
                require(
                    item["completion"] in {"completed", "partial", "blocked"},
                    f"Unknown completion: {path}:{reader.line_num}",
                )
                text(item["review_id"], f"{path}:{reader.line_num} review ID")
                text(item["verdict"], f"{path}:{reader.line_num} verdict")
            else:
                hash_value(item["report_sha256"], f"{path}:{reader.line_num}")
                relative_path(item["report_path"])
            if row is None:
                continue
            evidence = {
                "type": kind,
                "path": path,
                "line": reader.line_num,
                "record_id": item["review_id"] if kind == "structured" else item["report_path"],
                "scientific_review": item["scientific_review"] == "true" if kind == "structured" else None,
                "completion": item.get("completion"),
                "verdict": item.get("verdict") if kind == "structured" else item["reported_verdict"] or None,
                "target_sha256": item.get("target_sha256"),
                "row": item,
            }
            if kind == "legacy":
                report_path = item["report_path"]
                report_entry = history.tracked(base, report_path).get(report_path)
                require(report_entry is not None, f"Missing indexed legacy report: {report_path}")
                report_data = history.blob(report_entry)
                require(
                    digest(report_data) == item["report_sha256"],
                    f"Legacy report hash mismatch: {report_path}",
                )
                evidence["report"] = {**report_entry, "sha256": digest(report_data)}
            prior[identifier].append(evidence)

    targets = []
    for row in incoming:
        evidence = sorted(prior[row["target_id"]], key=lambda e: (e["type"], e["path"], e["line"]))
        for entry in evidence:
            entry["target_hash_matches_incoming_capture"] = (
                entry["target_sha256"] == row["captured_target"]["target_sha256"]
                if entry["target_sha256"]
                else None
            )
        flags = {
            "prior_" + kind: any(e["type"] == kind for e in evidence)
            for kind in ("structured", "legacy", "canonical")
        }
        targets.append(
            {
                **row,
                **flags,
                "prior_records": evidence,
                "eligible": not evidence,
                "eligibility_reason": "prior_target_review_coverage"
                if evidence
                else "no_prior_coverage_in_inputs",
                "structured_only_eligible_informative": not (
                    flags["prior_structured"] or flags["prior_canonical"]
                ),
            }
        )
    targets.sort(key=lambda row: (row["target_id"], row["path"]))
    return {
        "schema_version": 1,
        "base": base,
        "publication": publication,
        "policy": {
            "name": POLICY,
            "predicate": "eligible iff no prior canonical, structured-inventory or legacy record",
            "unit": "target_id and unambiguous target_path, independent of review_id and target hash",
            "legacy_is_scientific_equivalence": False,
            "hash_equality_is_scientific_equivalence": False,
            "structured_only_counts": "Informative alternative only; not the eligibility predicate.",
        },
        "inputs": sorted(inputs, key=lambda entry: entry["path"]),
        "input_counts": counts,
        "summary": {
            "incoming_scientific_reviews": len({row["review_id"] for row in targets}),
            "incoming_targets": len(targets),
            "excluded_metadata_bundles": len(excluded),
            "eligible": sum(row["eligible"] for row in targets),
            "excluded_prior_coverage": sum(not row["eligible"] for row in targets),
            **{
                field: sum(row[field] for row in targets)
                for field in ("prior_structured", "prior_legacy", "prior_canonical")
            },
            "structured_only_eligible_informative": sum(
                row["structured_only_eligible_informative"] for row in targets
            ),
        },
        "excluded_incoming_bundles": excluded,
        "excluded_baseline_bundles": excluded_baseline,
        "excluded_baseline_targets": excluded_baseline_targets,
        "targets": targets,
        "limitations": [
            "This deterministic inventory does not reassess evidence, verdicts, "
            "completion or scientific quality.",
            "Legacy rows preserve unknown scientific/completion/target-hash values; "
            "report hashes hash reports.",
            "Working-tree target hashes are declarations, "
            "not proof that those bytes exist at the recorded commit.",
            "Coverage inputs come from the entire tracked baseline tree, independently of ignore rules.",
        ],
    }


def render(ledger: dict[str, Any]) -> str:
    return json.dumps(ledger, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--base", help="Required for output; otherwise defaults to the checked ledger's pin")
    parser.add_argument("--publication", help="Required for output; otherwise uses the checked ledger's pin")
    destination = parser.add_mutually_exclusive_group(required=True)
    destination.add_argument("--output", type=Path)
    destination.add_argument(
        "--check", type=Path, help="Regenerate and require exact deterministic ledger bytes"
    )
    args = parser.parse_args(argv)
    try:
        existing = json.loads(args.check.read_text()) if args.check else {}
        require(isinstance(existing, dict), "Expected ledger JSON mapping")
        base = args.base or existing.get("base")
        publication = args.publication or existing.get("publication")
        require(base and publication, "--base and --publication are required when creating a ledger")
        ledger = audit(args.repo, text(base, "base revision"), text(publication, "publication revision"))
        content = render(ledger)
        if args.check:
            require(args.check.read_text() == content, f"Coverage ledger drift: {args.check}")
        else:
            args.output.write_text(content)
        print(json.dumps(ledger["summary"], sort_keys=True))
    except (CoverageError, OSError, UnicodeError, csv.Error, json.JSONDecodeError) as error:
        print(f"publication coverage audit failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
