"""Transport native GTDB mappings with exact orientation and unavailable review.

The complete committed mapping inventory is an extracted source surface. It
does not contain exact assertion-level native approval proofs. Every row is
therefore unassessed, preserving mapping predicate, taxonomy, parent and genome
count without inferring strain identity, genome equivalence or function.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import multiprocessing
import os
import re
import subprocess
import tempfile
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from itertools import islice
from pathlib import Path

import yaml

from taxonmech.edge_publication import publish_stage

REPOSITORY = "CultureBotAI/TaxonMech"
SOURCE = "data/raw/gtdb_mappings.tsv"
MANIFEST = "data/raw/MANIFEST.yaml"
SCHEMA = "src/taxonmech/schema/taxonmech.yaml"
SEMANTICS = "docs/CURATION.md"
CLAW_COMMIT = "6141da81dc521d776e1ebcff1c4e63824313a9a1"
PREDICATES = {"skos:exactMatch", "skos:broadMatch", "skos:narrowMatch", "skos:closeMatch"}
VALIDATION_BATCH_SIZE = 64


def sha(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def adapt_mapping(
    row: dict, *, position: int, commit: str, hashes: dict, prefixes: dict, provenance: str
) -> dict:
    """Keep an extracted mapping unassessed even if a parent record is reviewed."""
    from kg_microbe_curation.identity import sha256_json
    from kg_microbe_curation.native import NATIVE_CONTRACT, native_assertion_id, validate_native_assertion

    if row.get("predicate") not in PREDICATES or not row.get("gtdb_id") or not row.get("ncbitaxon_id"):
        raise ValueError("Incomplete or unsupported native taxonomy mapping")
    if not row.get("genome_count", "").isdigit():
        raise ValueError("Native genome_count must remain an explicit nonnegative count")

    def locator(path, selector=None):
        return {"repository": REPOSITORY, "commit": commit, "path": path, "selector": selector or {}}

    payload_sha = sha256_json(row)
    assertion = {
        "contract": NATIVE_CONTRACT,
        "native_locator": {
            **locator(SOURCE, {"source_position": position}),
            "source_sha256": hashes[SOURCE],
            "payload_sha256": payload_sha,
        },
        "payload": {
            "subject": row["gtdb_id"],
            "predicate": row["predicate"],
            "object": row["ncbitaxon_id"],
            "native_payload": row,
            "context": {
                "scope": "native_taxonomy_mapping_only",
                "taxonomy_source": "GTDB",
                "upstream_snapshot": provenance,
                "review_evidence_status": "unavailable_exact_native_assertion_review",
                "matching_policy": "exact_native_payload_and_dependency_bindings",
                "match_selector": {
                    "subject": row["gtdb_id"],
                    "predicate": row["predicate"],
                    "object": row["ncbitaxon_id"],
                    "native_payload_sha256": payload_sha,
                    "source_sha256": hashes[SOURCE],
                },
            },
            "interpretation": {
                "normalization_contract": "taxonmech-native-gtdb-mapping-exact-lexical/v1",
                "normalizer_contract_sha256": hashes[SEMANTICS],
                "schema_sha256": hashes[SCHEMA],
                "prefix_map_sha256": sha256_json(prefixes),
            },
        },
        "evidence": [
            {"evidence_id": "native-file:" + path, "locator": locator(path), "sha256": digest, "ancestry": []}
            for path, digest in sorted(hashes.items())
        ],
        "native_review": {
            "status": "unassessed",
            "locator": None,
            "sha256": None,
            "payload": {},
            "payload_sha256": sha256_json({}),
            "rationale": (
                "The native inventory contains extracted mappings, not exact assertion-level "
                "approval proofs. "
                "Generated record statuses and corpus review coverage are not inherited as mapping approval."
            ),
        },
        "assurance": "unassessed",
        "limitations": [
            (
                "Exact GTDB-to-NCBI mapping orientation and original predicate are retained; "
                "close or broad matches are never identity equivalence."
            ),
            (
                "Taxon classification, strain/deposit identity and genome-record identity remain separate. "
                "Genome counts do not identify a strain or establish assembly equivalence."
            ),
            (
                "Native source inventory bytes and manifest were verified; "
                "external primary-source files named by the manifest were not fetched."
            ),
            "No independent scientific review or current KG occurrence approval is supplied.",
        ],
        "independent_scientific_review": False,
    }
    assertion["assertion_id"] = native_assertion_id(assertion)
    validate_native_assertion(assertion)
    return assertion


def _adapt_batch(jobs: list[tuple[int, dict]], common: dict) -> list[tuple[int, dict]]:
    """Spawn-safe worker validates every generated envelope with the shared contract."""
    return [(position, adapt_mapping(row, position=position, **common)) for position, row in jobs]


def _validated_assertions(rows, common: dict, workers: int):
    """Keep at most workers * 64 rows submitted, yielding original source order."""
    if type(workers) is not int or not 1 <= workers <= 4:
        raise ValueError("workers must be an integer between 1 and 4")
    if workers == 1:
        for position, row in rows:
            yield position, adapt_mapping(row, position=position, **common)
        return
    context = multiprocessing.get_context("spawn")
    with ProcessPoolExecutor(max_workers=workers, mp_context=context) as executor:
        while True:
            window = list(islice(rows, workers * VALIDATION_BATCH_SIZE))
            if not window:
                break
            futures = [
                executor.submit(_adapt_batch, window[start : start + VALIDATION_BATCH_SIZE], common)
                for start in range(0, len(window), VALIDATION_BATCH_SIZE)
            ]
            for future in futures:
                yield from future.result()


def export_assertions(
    root: Path, commit: str, output: Path, positions: list[int] | None, *, workers: int = 1
) -> dict:
    """Stream selected or all immutable mapping rows into one atomic JSONL export."""
    from kg_microbe_curation.identity import canonical_json

    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("An immutable source commit is required")
    if type(workers) is not int or not 1 <= workers <= 4:
        raise ValueError("workers must be an integer between 1 and 4")
    if output.exists() or output.is_symlink():
        raise ValueError("Output must be a new directory")
    origin = subprocess.check_output(
        ["git", "-C", str(root), "remote", "get-url", "origin"], text=True
    ).strip()
    if origin not in {
        f"https://github.com/{REPOSITORY}.git",
        f"https://github.com/{REPOSITORY}",
        f"git@github.com:{REPOSITORY}.git",
    }:
        raise ValueError("Native Git origin identity mismatch")
    sources = {
        path: subprocess.check_output(["git", "-C", str(root), "show", f"{commit}:{path}"])
        for path in (SOURCE, MANIFEST, SCHEMA, SEMANTICS)
    }
    hashes = {path: sha(content) for path, content in sources.items()}
    source_manifest, schema = yaml.safe_load(sources[MANIFEST]), yaml.safe_load(sources[SCHEMA])
    entries = [item for item in source_manifest["outputs"] if item["path"] == Path(SOURCE).name]
    if (
        len(entries) != 1
        or entries[0]["sha256"] != hashes[SOURCE]
        or entries[0]["bytes"] != len(sources[SOURCE])
    ):
        raise ValueError("Native source inventory differs from its provenance manifest")
    reader = csv.DictReader(io.StringIO(sources[SOURCE].decode()), delimiter="\t", strict=True)
    required = {"gtdb_id", "gtdb_label", "gtdb_parent", "ncbitaxon_id", "predicate", "genome_count"}
    if (
        not reader.fieldnames
        or len(reader.fieldnames) != len(set(reader.fieldnames))
        or not required.issubset(reader.fieldnames)
    ):
        raise ValueError("Invalid native taxonomy TSV header")
    selected = set(positions) if positions is not None else None
    if positions is not None and (
        not positions
        or len(selected) != len(positions)
        or any(type(i) is not int or i < 1 for i in positions)
    ):
        raise ValueError("Positions must be unique positive source rows")
    output.parent.mkdir(parents=True, exist_ok=True)
    counts, source_rows, written = Counter(), 0, 0

    def selected_rows():
        nonlocal source_rows
        for source_rows, row in enumerate(reader, 1):
            if None in row or any(value is None for value in row.values()):
                raise ValueError("Malformed native taxonomy row")
            if selected is None or source_rows in selected:
                yield source_rows, row

    common = {
        "commit": commit,
        "hashes": hashes,
        "prefixes": schema["prefixes"],
        "provenance": source_manifest["kg_microbe_source"],
    }
    with tempfile.TemporaryDirectory(prefix=".native-assertions-", dir=output.parent) as temporary:
        stage = Path(temporary) / "export"
        stage.mkdir()
        content_hash = hashlib.sha256()
        membership_hash = hashlib.sha256()
        with (stage / "assertions.jsonl").open("wb") as stream:
            for position, assertion in _validated_assertions(selected_rows(), common, workers):
                data = canonical_json(assertion) + b"\n"
                stream.write(data)
                content_hash.update(data)
                membership_hash.update(canonical_json([assertion["assertion_id"], position]) + b"\n")
                counts["unassessed"] += 1
                written += 1
            stream.flush()
            os.fsync(stream.fileno())
        if (
            source_rows != entries[0]["rows"]
            or selected is not None
            and (max(selected) > source_rows or written != len(selected))
        ):
            raise ValueError("Native source or selected row count differs")
        persisted = Counter()
        persisted_hash, persisted_membership = hashlib.sha256(), hashlib.sha256()
        with (stage / "assertions.jsonl").open("rb") as stream:
            for line in stream:
                persisted_hash.update(line)
                assertion = json.loads(line)
                persisted[assertion["native_review"]["status"]] += 1
                persisted_membership.update(
                    canonical_json(
                        [
                            assertion["assertion_id"],
                            assertion["native_locator"]["selector"]["source_position"],
                        ]
                    )
                    + b"\n"
                )
        if (
            persisted != counts
            or persisted_hash.digest() != content_hash.digest()
            or persisted_membership.digest() != membership_hash.digest()
        ):
            raise ValueError("Persisted native bytes, identity membership or counters differ")
        # Every generated envelope was shared-contract validated. Only the exact
        # byte/membership equality above admits persisted schema validity; a
        # second 322k-row JSON Schema pass would prove the same bytes again.
        manifest = {
            "schema_version": 1,
            "contract": "kg-microbe-native-assertion/v1",
            "repository": REPOSITORY,
            "source_commit": commit,
            "claw_contract_commit": CLAW_COMMIT,
            "validation_workers": workers,
            "validation_batch_size": VALIDATION_BATCH_SIZE,
            "source_positions": positions,
            "source_rows": source_rows,
            "rows": written,
            "native_status_counts": dict(counts),
            "assertions_sha256": content_hash.hexdigest(),
            "assertion_membership_sha256": membership_hash.hexdigest(),
            "assertions_bytes": (stage / "assertions.jsonl").stat().st_size,
            "source_files": hashes,
            "independent_scientific_reviews": 0,
            "kg_occurrences_approved": 0,
            "scope": (
                "Complete committed GTDB-to-NCBI mapping inventory; "
                "bounded positions only when explicitly selected."
            ),
            "review_evidence_status": "unavailable_exact_native_assertion_review",
            "excluded_surfaces": [
                (
                    "Strain/deposit identities, assembly/genome links and nomenclature assertions "
                    "require distinct native evidence bindings and are not covered by this mapping adapter."
                )
            ],
        }
        (stage / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
        publish_stage(stage, output)
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=1, choices=range(1, 5))
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--positions", nargs="+", type=int)
    selection.add_argument("--all", action="store_true")
    args = parser.parse_args()
    print(
        json.dumps(
            export_assertions(
                args.root, args.source_commit, args.output, args.positions, workers=args.workers
            ),
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
