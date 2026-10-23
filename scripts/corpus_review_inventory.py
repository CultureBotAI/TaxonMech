#!/usr/bin/env python3
"""Verify full-corpus review coverage and structured review inventory integrity.

Audits that docs/legacy-review-inventory.tsv and docs/structured-review-inventory/part-*.tsv
form a complete, disjoint partition of data/taxa/PATHS.tsv without inferring scientific
verdicts or promoting PROPOSED records to REVIEWED.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import sys
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

ROOT = Path(__file__).resolve().parents[1]
PATHS_TSV = Path("data/taxa/PATHS.tsv")
LEGACY_TSV = Path("docs/legacy-review-inventory.tsv")
SHARD_DIR = Path("docs/structured-review-inventory")
BATCHES_TSV = Path("docs/structured-review-batches.tsv")
STRUCTURED_DIR = Path("reviews/structured")
DOMAINS = ("archaea", "bacteria", "eukaryota", "other")
LATEST_SHARD_LIVE_CONTEXT_PATHS = frozenset(
    {
        PATHS_TSV.as_posix(),
        LEGACY_TSV.as_posix(),
        BATCHES_TSV.as_posix(),
        "curation/seed_scope.tsv",
    }
)

INVENTORY_COLUMNS = (
    "review_id",
    "round_id",
    "target_id",
    "target_path",
    "target_sha256",
    "label",
    "verdict",
    "completion",
    "scientific_review",
    "finding_count",
    "started_at",
    "finished_at",
)

BATCH_COLUMNS = (
    "round_id",
    "shard_path",
    "record_count",
    "pass_count",
    "pass_with_limitations_count",
    "needs_curation_count",
    "blocked_count",
    "first_target_id",
    "last_target_id",
    "started_at",
    "finished_at",
    "notes",
)

ALLOWED_VERDICTS = ("pass", "pass_with_limitations", "needs_curation", "blocked")
ALLOWED_COMPLETIONS = ("completed", "partial", "blocked")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")

ERRATUM_REVIEW_IDS = {
    "20261013T061030Z-achromobacter_sp_r_17670-round13-agent2",
    "20261013T061030Z-achromobacter_sp_r_17671-round13-agent2",
    "20261013T061031Z-achromobacter_sp_r_17690-round13-agent2",
    "20261013T061031Z-achromobacter_sp_r_41384-round13-agent2",
    "20261013T061032Z-achromobacter_sp_r_41391-round13-agent2",
    "20261013T061032Z-achromobacter_sp_r_41395-round13-agent2",
    "20261013T061032Z-achromobacter_sp_r_90029-round13-agent2",
    "20261013T061033Z-achromobacter_sp_r_92577-round13-agent2",
    "20261013T061033Z-achromobacter_sp_r_92592-round13-agent2",
    "20261013T061034Z-achromobacter_sp_r_92754-round13-agent2",
    "20261013T061034Z-achromobacter_sp_r_92758-round13-agent2",
    "20261013T061034Z-achromobacter_sp_rau_832-round13-agent2",
    "20261013T061035Z-achromobacter_sp_rbc24-round13-agent2",
    "20261013T061035Z-achromobacter_sp_rbl15_5-round13-agent2",
    "20261013T061036Z-achromobacter_sp_rce_32-round13-agent2",
    "20261013T061036Z-achromobacter_sp_rd4-round13-agent2",
    "20261013T061036Z-achromobacter_sp_rd_matfa_09-round13-agent2",
    "20261013T061037Z-achromobacter_sp_red_4-round13-agent2",
    "20261013T061037Z-achromobacter_sp_rfr_5-round13-agent2",
    "20261013T061037Z-achromobacter_sp_rg14-round13-agent2",
    "20261013T061037Z-achromobacter_sp_rg16-round13-agent2",
    "20261013T061037Z-achromobacter_sp_rg_06_06-round13-agent2",
    "20261013T061037Z-achromobacter_sp_ri38-round13-agent2",
    "20261013T061038Z-achromobacter_sp_ri55-round13-agent2",
    "20261013T061038Z-achromobacter_sp_rifa_164-round13-agent2",
    "20261013T061038Z-achromobacter_sp_rl2c-round13-agent2",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def round_sort_key(round_id: str) -> tuple[int, int, str]:
    if round_id == "pre-round":
        return (0, 0, round_id)
    match = re.match(r"^round(\d+)(?:-b(\d+))?$", round_id)
    if match:
        return (int(match.group(1)), int(match.group(2) or 0), round_id)
    return (999, 0, round_id)


def parse_iso_utc(value: str) -> datetime:
    if not value or not value.endswith("Z"):
        raise ValueError(f"invalid UTC timestamp: {value!r}")
    return datetime.fromisoformat(value[:-1] + "+00:00")


def load_corpus_targets(root: Path) -> tuple[dict[str, str], set[str]]:
    paths_file = root / PATHS_TSV
    if not paths_file.is_file() or paths_file.is_symlink():
        raise ValueError("missing or symlinked data/taxa/PATHS.tsv")
    with paths_file.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != ["identifier", "slug"]:
            raise ValueError("unexpected PATHS.tsv columns")
        id_to_slug: dict[str, str] = {}
        seen_slugs: set[str] = set()
        for row in reader:
            ident = row["identifier"]
            slug = row["slug"]
            if not ident or not slug:
                raise ValueError("empty identifier or slug in PATHS.tsv")
            if ident in id_to_slug:
                raise ValueError(f"duplicate corpus identifier: {ident}")
            if slug in seen_slugs:
                raise ValueError(f"duplicate corpus slug: {slug}")
            id_to_slug[ident] = slug
            seen_slugs.add(slug)
    if not id_to_slug:
        raise ValueError("empty PATHS.tsv")

    existing_paths: set[str] = set()
    for domain in DOMAINS:
        dom_dir = root / "data" / "taxa" / domain
        if not dom_dir.is_dir():
            continue
        for name in os.listdir(dom_dir):
            if name.endswith(".yaml"):
                existing_paths.add(f"data/taxa/{domain}/{name}")
    return id_to_slug, existing_paths


def load_legacy_targets(
    root: Path, id_to_slug: dict[str, str], existing_paths: set[str]
) -> dict[str, dict[str, str]]:
    legacy_file = root / LEGACY_TSV
    if not legacy_file.is_file() or legacy_file.is_symlink():
        raise ValueError("missing or symlinked docs/legacy-review-inventory.tsv")
    legacy_by_id: dict[str, dict[str, str]] = {}
    with legacy_file.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            tid = row["target_id"]
            tpath = row["target_path"]
            if tid in legacy_by_id:
                raise ValueError(f"duplicate legacy target_id: {tid}")
            if tid not in id_to_slug:
                raise ValueError(f"legacy target_id not in PATHS.tsv: {tid}")
            if Path(tpath).stem != id_to_slug[tid]:
                raise ValueError(f"legacy target_path slug mismatch for {tid}: {tpath}")
            if tpath not in existing_paths:
                raise ValueError(f"missing corpus target file for legacy row: {tpath}")
            legacy_by_id[tid] = row
    return legacy_by_id


def load_latest_target_reviews(
    root: Path,
) -> tuple[
    dict[tuple[str, str], tuple[datetime, str, str, Path]],
    dict[str, tuple[datetime, str, str, Path]],
]:
    """Return latest completed scientific review target hashes from reviews/structured."""
    structured_root = root / STRUCTURED_DIR
    if not structured_root.is_dir() or structured_root.is_symlink():
        return {}, {}
    latest_by_target: dict[tuple[str, str], tuple[datetime, str, str, Path]] = {}
    latest_by_path: dict[str, tuple[datetime, str, str, Path]] = {}
    for bundle_yaml in sorted(structured_root.glob("*/review.yaml")):
        doc = yaml.load(bundle_yaml.read_bytes(), Loader=Loader)
        if not isinstance(doc, dict):
            continue
        review_id = doc.get("review_id")
        if (
            not isinstance(review_id, str)
            or not review_id
            or review_id != bundle_yaml.parent.name
        ):
            continue
        if (
            doc.get("completion") not in {"completed", "partial"}
            or doc.get("scientific_review") is not True
        ):
            continue
        if doc.get("verdict") not in ALLOWED_VERDICTS:
            continue
        started_raw = doc.get("started_at")
        finished_raw = doc.get("finished_at")
        if not isinstance(started_raw, str) or not isinstance(finished_raw, str):
            continue
        started_at = parse_iso_utc(started_raw)
        finished_at = parse_iso_utc(finished_raw)
        if finished_at < started_at:
            raise ValueError(f"bundle {bundle_yaml} finished_at precedes started_at")
        targets_by_path: dict[str, str] = {}
        for target in doc.get("targets") or []:
            if (
                isinstance(target, dict)
                and isinstance(target.get("target_id"), str)
                and isinstance(target.get("path"), str)
                and target["target_id"]
                and target["path"]
            ):
                targets_by_path[target["path"]] = target["target_id"]
        for inp in doc.get("source", {}).get("inputs", []):
            if not isinstance(inp, dict) or inp.get("role") != "target":
                continue
            rel_inp = inp.get("path")
            inp_sha = inp.get("sha256")
            if (
                not isinstance(rel_inp, str)
                or not isinstance(inp_sha, str)
                or not SHA256_RE.match(inp_sha)
                or rel_inp not in targets_by_path
            ):
                continue
            tid = targets_by_path[rel_inp]
            entry = (finished_at, review_id, inp_sha, bundle_yaml)
            prev_t = latest_by_target.get((tid, rel_inp))
            if (
                prev_t is not None
                and finished_at == prev_t[0]
                and inp_sha != prev_t[2]
            ):
                raise ValueError(
                    f"ambiguous equal finished_at for {tid} ({rel_inp}) across "
                    f"{prev_t[3]} and {bundle_yaml}"
                )
            if prev_t is None or (finished_at, review_id) >= (prev_t[0], prev_t[1]):
                latest_by_target[(tid, rel_inp)] = entry
            prev_p = latest_by_path.get(rel_inp)
            if (
                prev_p is not None
                and finished_at == prev_p[0]
                and inp_sha != prev_p[2]
            ):
                raise ValueError(
                    f"ambiguous equal finished_at for {rel_inp} across "
                    f"{prev_p[3]} and {bundle_yaml}"
                )
            if prev_p is None or (finished_at, review_id) >= (prev_p[0], prev_p[1]):
                latest_by_path[rel_inp] = entry
    return latest_by_target, latest_by_path


def load_structured_shards(
    root: Path,
    id_to_slug: dict[str, str],
    existing_paths: set[str],
    *,
    verify_target_sha256: bool = False,
) -> tuple[dict[str, list[dict[str, str]]], dict[str, dict[str, str]]]:
    shard_root = root / SHARD_DIR
    if not shard_root.is_dir() or shard_root.is_symlink():
        raise ValueError("missing or symlinked docs/structured-review-inventory directory")
    shard_files = sorted(shard_root.glob("part-*.tsv"))
    if not shard_files:
        raise ValueError("no shard files found in docs/structured-review-inventory")

    shard_rows_by_rel: dict[str, list[dict[str, str]]] = {}
    structured_by_id: dict[str, dict[str, str]] = {}

    for shard_file in shard_files:
        if shard_file.is_symlink():
            raise ValueError(f"symlinked shard file: {shard_file}")
        rel_path = shard_file.relative_to(root).as_posix()
        rows: list[dict[str, str]] = []
        with shard_file.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            if tuple(reader.fieldnames or ()) != INVENTORY_COLUMNS:
                raise ValueError(f"unexpected columns in {rel_path}: {reader.fieldnames}")
            for row in reader:
                tid = row["target_id"]
                tpath = row["target_path"]
                tsha = row["target_sha256"]
                verdict = row["verdict"]
                completion = row["completion"]
                sci = row["scientific_review"]
                fcount = row["finding_count"]

                if not row["review_id"] or not row["round_id"] or not row["label"]:
                    raise ValueError(f"missing required identity fields in {rel_path} for {tid}")
                if tid in structured_by_id:
                    raise ValueError(f"duplicate structured target_id: {tid}")
                if tid not in id_to_slug:
                    raise ValueError(f"structured target_id not in PATHS.tsv: {tid}")
                if Path(tpath).stem != id_to_slug[tid]:
                    raise ValueError(f"structured target_path slug mismatch for {tid}: {tpath}")
                if tpath not in existing_paths:
                    raise ValueError(f"missing corpus target file for structured row: {tpath}")
                if not SHA256_RE.match(tsha):
                    raise ValueError(f"invalid target_sha256 for {tid}: {tsha!r}")
                if verdict not in ALLOWED_VERDICTS:
                    raise ValueError(f"invalid verdict for {tid}: {verdict!r}")
                if completion not in ALLOWED_COMPLETIONS:
                    raise ValueError(f"invalid completion for {tid}: {completion!r}")
                if sci not in {"true", "false"}:
                    raise ValueError(f"invalid scientific_review flag for {tid}: {sci!r}")
                if not fcount.isdigit():
                    raise ValueError(f"invalid finding_count for {tid}: {fcount!r}")
                started = parse_iso_utc(row["started_at"])
                finished = parse_iso_utc(row["finished_at"])
                if finished < started:
                    raise ValueError(f"finished_at precedes started_at for {tid}")

                rows.append(row)
                structured_by_id[tid] = row
        if not rows:
            raise ValueError(f"empty structured review shard: {rel_path}")
        shard_rows_by_rel[rel_path] = rows

    if verify_target_sha256:
        latest_by_target, _ = load_latest_target_reviews(root)
        items = list(structured_by_id.values())

        def _check_one(item: dict[str, str]) -> None:
            tid = item["target_id"]
            tpath = item["target_path"]
            expected = item["target_sha256"]
            row_finished = parse_iso_utc(item["finished_at"])
            row_review_id = item["review_id"]
            latest = latest_by_target.get((tid, tpath))
            if latest is not None:
                bundle_finished, bundle_review_id, bundle_sha, bundle_yaml = latest
                if bundle_finished == row_finished and bundle_sha != expected:
                    raise ValueError(
                        f"ambiguous equal finished_at for {tid} ({tpath}) between "
                        f"shard row {row_review_id} and {bundle_yaml}"
                    )
                if (bundle_finished, bundle_review_id) > (row_finished, row_review_id):
                    expected = bundle_sha
            actual = sha256_file(root / tpath)
            if actual != expected:
                raise ValueError(
                    f"target_sha256 mismatch for {tid} ({tpath}): "
                    f"expected {expected}, got {actual}"
                )

        with ThreadPoolExecutor(max_workers=16) as executor:
            list(executor.map(_check_one, items))

    return shard_rows_by_rel, structured_by_id


def build_batch_rows(
    shard_rows_by_rel: dict[str, list[dict[str, str]]]
) -> list[dict[str, str]]:
    rows_by_round: dict[str, list[dict[str, str]]] = defaultdict(list)
    round_to_shards: dict[str, set[str]] = defaultdict(set)
    for rel_shard, srows in shard_rows_by_rel.items():
        for row in srows:
            rid = row["round_id"]
            rows_by_round[rid].append(row)
            round_to_shards[rid].add(rel_shard)

    batch_rows: list[dict[str, str]] = []
    for rid in sorted(rows_by_round.keys(), key=round_sort_key):
        rlist = rows_by_round[rid]
        vcounts = Counter(r["verdict"] for r in rlist)
        pass_c = vcounts.get("pass", 0)
        pwl_c = vcounts.get("pass_with_limitations", 0)
        nc_c = vcounts.get("needs_curation", 0)
        blk_c = vcounts.get("blocked", 0)
        if pass_c + pwl_c + nc_c + blk_c != len(rlist):
            raise ValueError(f"unaccounted verdict counts in round {rid}: {dict(vcounts)}")
        note = "Consolidated structured review batch inventory."
        if rid == "round13" and any(r["review_id"] in ERRATUM_REVIEW_IDS for r in rlist):
            note = (
                "Includes 26 round13-agent2 reviews covered by append-only author metadata erratum "
                "20261013T062322Z-round13-agent2-author-model-erratum (withdrawing GPT-6 label in "
                "favor of Codex/GPT-5 session identification)."
            )
        batch_rows.append(
            {
                "round_id": rid,
                "shard_path": ",".join(sorted(round_to_shards[rid])),
                "record_count": str(len(rlist)),
                "pass_count": str(pass_c),
                "pass_with_limitations_count": str(pwl_c),
                "needs_curation_count": str(nc_c),
                "blocked_count": str(blk_c),
                "first_target_id": rlist[0]["target_id"],
                "last_target_id": rlist[-1]["target_id"],
                "started_at": min(r["started_at"] for r in rlist),
                "finished_at": max(r["finished_at"] for r in rlist),
                "notes": note,
            }
        )
    return batch_rows


def render_batches(rows: list[dict[str, str]]) -> str:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(
        output, fieldnames=BATCH_COLUMNS, delimiter="\t", lineterminator="\n"
    )
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def verify_shard_bundles(
    root: Path,
    shard_rows_by_rel: dict[str, list[dict[str, str]]],
    *,
    verify_target_sha256: bool = False,
) -> None:
    structured_root = root / STRUCTURED_DIR
    if not structured_root.is_dir() or structured_root.is_symlink():
        raise ValueError("missing or symlinked reviews/structured directory")
    batches_sha = sha256_file(root / BATCHES_TSV)
    sha_cache: dict[str, str] = {BATCHES_TSV.as_posix(): batches_sha}

    latest_rel_shard = max(shard_rows_by_rel) if shard_rows_by_rel else None
    latest_bundle_yaml: Path | None = None
    for rel_shard, srows in shard_rows_by_rel.items():
        shard_name = Path(rel_shard).stem
        shard_sha = sha256_file(root / rel_shard)
        sha_cache[rel_shard] = shard_sha
        matches = sorted(
            structured_root.glob(f"*-structured-review-shard-{shard_name}/review.yaml")
        )
        if len(matches) != 1:
            raise ValueError(
                f"expected 1 shard bundle for {shard_name}, found {len(matches)}"
            )
        doc = yaml.load(matches[0].read_bytes(), Loader=Loader)
        if doc.get("kind") != "batch":
            raise ValueError(f"shard bundle {matches[0]} must have kind: batch")
        if doc.get("scope", {}).get("population_size") != len(srows):
            raise ValueError(
                f"shard bundle {matches[0]} population_size mismatch: "
                f"expected {len(srows)}, got {doc.get('scope', {}).get('population_size')}"
            )
        inputs_by_path = {
            inp["path"]: inp["sha256"]
            for inp in doc.get("source", {}).get("inputs", [])
        }
        if inputs_by_path.get(rel_shard) != shard_sha:
            raise ValueError(f"shard bundle {matches[0]} has stale SHA256 for {rel_shard}")
        if BATCHES_TSV.as_posix() not in inputs_by_path:
            raise ValueError(
                f"shard bundle {matches[0]} missing {BATCHES_TSV.as_posix()} input"
            )
        if rel_shard == latest_rel_shard:
            latest_bundle_yaml = matches[0]
            if inputs_by_path.get(BATCHES_TSV.as_posix()) != batches_sha:
                raise ValueError(
                    f"shard bundle {matches[0]} has stale SHA256 for {BATCHES_TSV.as_posix()}"
                )

    _, latest_by_path = (
        load_latest_target_reviews(root) if verify_target_sha256 else ({}, {})
    )

    for bundle_yaml in sorted(structured_root.glob("*/review.yaml")):
        doc = yaml.load(bundle_yaml.read_bytes(), Loader=Loader)
        is_latest_shard_bundle = bundle_yaml == latest_bundle_yaml
        bundle_finished = (
            parse_iso_utc(doc["finished_at"])
            if isinstance(doc.get("finished_at"), str) and doc.get("finished_at")
            else None
        )
        bundle_review_id = str(doc.get("review_id") or "")
        bundle_target_paths = {
            target["path"]
            for target in (doc.get("targets") or [])
            if isinstance(target, dict) and isinstance(target.get("path"), str)
        }
        for inp in doc.get("source", {}).get("inputs", []):
            rel_inp = inp["path"]
            if rel_inp not in sha_cache:
                inp_file = root / rel_inp
                if not inp_file.is_file() or inp_file.is_symlink():
                    raise ValueError(
                        f"bundle {bundle_yaml} references missing input {rel_inp}"
                    )
                sha_cache[rel_inp] = sha256_file(inp_file)
            is_live_inventory_context = is_latest_shard_bundle and (
                rel_inp in LATEST_SHARD_LIVE_CONTEXT_PATHS
                or rel_inp in shard_rows_by_rel
            )
            is_active_target_check = False
            if verify_target_sha256 and inp.get("role") == "target":
                latest = latest_by_path.get(rel_inp)
                is_superseded_target_snapshot = (
                    latest is not None
                    and rel_inp in bundle_target_paths
                    and bundle_finished is not None
                    and (latest[0], latest[1]) > (bundle_finished, bundle_review_id)
                )
                is_active_target_check = not is_superseded_target_snapshot
            if (is_live_inventory_context or is_active_target_check) and (
                inp["sha256"] != sha_cache[rel_inp]
            ):
                raise ValueError(
                    f"bundle {bundle_yaml} has stale SHA256 for {rel_inp}"
                )


def check(root: Path, *, verify_target_sha256: bool = False) -> dict[str, Any]:
    id_to_slug, existing_paths = load_corpus_targets(root)
    legacy_by_id = load_legacy_targets(root, id_to_slug, existing_paths)
    shard_rows_by_rel, structured_by_id = load_structured_shards(
        root, id_to_slug, existing_paths, verify_target_sha256=verify_target_sha256
    )

    overlap = set(legacy_by_id) & set(structured_by_id)
    if overlap:
        sample = ", ".join(sorted(overlap)[:5])
        raise ValueError(
            "overlap between legacy and structured review inventories "
            f"({len(overlap)} records, e.g. {sample})"
        )

    covered = set(legacy_by_id) | set(structured_by_id)
    missing = set(id_to_slug) - covered
    if missing:
        sample = ", ".join(sorted(missing)[:5])
        raise ValueError(
            f"unreviewed corpus records remaining ({len(missing)} records, e.g. {sample})"
        )

    expected_batches = build_batch_rows(shard_rows_by_rel)
    batches_file = root / BATCHES_TSV
    if not batches_file.is_file() or batches_file.is_symlink():
        raise ValueError("missing or symlinked docs/structured-review-batches.tsv")
    if batches_file.read_bytes() != render_batches(expected_batches).encode("utf-8"):
        raise ValueError(
            "structured-review-batches.tsv drift: rebuild with --write and update shard bundle digests"
        )

    verify_shard_bundles(
        root, shard_rows_by_rel, verify_target_sha256=verify_target_sha256
    )

    return {
        "corpus_records": len(id_to_slug),
        "legacy_records": len(legacy_by_id),
        "structured_records": len(structured_by_id),
        "overlap_records": len(overlap),
        "unreviewed_records": len(missing),
        "structured_shards": len(shard_rows_by_rel),
        "structured_batches": len(expected_batches),
        "structured_by_domain": dict(
            sorted(
                Counter(
                    Path(r["target_path"]).parts[2] for r in structured_by_id.values()
                ).items()
            )
        ),
        "structured_verdicts_not_promoted": dict(
            sorted(Counter(r["verdict"] for r in structured_by_id.values()).items())
        ),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--check",
        action="store_true",
        help="verify full-corpus partition, shard rows, batch summaries, and shard bundles",
    )
    mode.add_argument(
        "--write",
        action="store_true",
        help="rebuild docs/structured-review-batches.tsv from docs/structured-review-inventory/part-*.tsv",
    )
    parser.add_argument(
        "--verify-target-sha256",
        action="store_true",
        help="recompute SHA-256 of every target YAML file on disk",
    )
    args = parser.parse_args(argv)
    try:
        if args.write:
            id_to_slug, existing_paths = load_corpus_targets(ROOT)
            shard_rows_by_rel, _ = load_structured_shards(
                ROOT,
                id_to_slug,
                existing_paths,
                verify_target_sha256=args.verify_target_sha256,
            )
            batch_rows = build_batch_rows(shard_rows_by_rel)
            (ROOT / BATCHES_TSV).write_text(
                render_batches(batch_rows), encoding="utf-8", newline=""
            )
        result = check(ROOT, verify_target_sha256=args.verify_target_sha256)
    except (ValueError, OSError) as exc:
        print(f"Corpus review inventory check failed: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
