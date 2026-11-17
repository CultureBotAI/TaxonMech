"""Export typed native strain links without inferring identity or scientific review.

The flat committed inventories are distinct from nested ATB/StrainInfo overlays.
Every source qualifier and exact owner row remains bound to its immutable file.
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
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
from itertools import islice
from pathlib import Path

import yaml

from taxonmech.edge_curation import CLAW_COMMIT, MANIFEST, REPOSITORY, SCHEMA, SEMANTICS, sha
from taxonmech.edge_publication import publish_stage

OWNERS = ("data/raw/bacdive_strains.tsv", "data/raw/culture_collection_strains.tsv")
SEMANTIC_FILES = (SEMANTICS, "docs/STRAIN_GENOMES.md", "src/taxonmech/genome_sources.py")
BATCH_ROWS = 64
SURFACES = {
    "assemblies": {
        "source": "data/raw/strain_assemblies.tsv",
        "target": "assembly_id",
        "class": "GenomeAssemblyLink",
        "slot": "genome_assemblies",
    },
    "genomes": {
        "source": "data/raw/strain_genome_records.tsv",
        "target": "genome_id",
        "class": "GenomeRecordLink",
        "slot": "genome_records",
    },
    "related": {
        "source": "data/raw/strain_related_records.tsv",
        "target": "record_id",
        "class": "GenomeRelatedRecordLink",
        "slot": "related_records",
    },
}
EXCLUDED_SOURCES = {"ALLTHEBACTERIA", "STRAININFO"}


def table_rows(data, required):
    reader = csv.DictReader(io.StringIO(data.decode("utf-8")), delimiter="\t", strict=True)
    if (
        not reader.fieldnames
        or len(reader.fieldnames) != len(set(reader.fieldnames))
        or not required.issubset(reader.fieldnames)
    ):
        raise ValueError("Missing or ambiguous native link columns")
    for position, row in enumerate(reader, 1):
        if None in row or any(value is None for value in row.values()):
            raise ValueError("Malformed native link row")
        yield position, row


def constraints(schema, surface):
    """Extract flat lexical and type constraints from the pinned native schema."""
    native = schema["classes"][SURFACES[surface]["class"]]
    attributes = {**schema["classes"]["StrainLinkEvidence"]["attributes"], **native["attributes"]}
    checks = {}
    for field, definition in attributes.items():
        values = schema.get("enums", {}).get(definition.get("range"), {}).get("permissible_values")
        checks[field] = {
            "required": definition.get("required", False),
            "pattern": definition.get("pattern"),
            "values": list(values) if values else None,
        }
    checks["strain_id"] = {"required": True, "pattern": r"^kgmicrobe\.strain:\S+$", "values": None}
    conditional = []
    for rule in native.get("rules", []):
        condition = rule["preconditions"]["slot_conditions"]
        if len(condition) != 1:
            continue
        field, value = next(iter(condition.items()))
        if field in {"source_database", "record_type"} and "equals_string" in value:
            target_rule = rule["postconditions"]["slot_conditions"].get(SURFACES[surface]["target"], {})
            if "pattern" in target_rule:
                conditional.append([field, value["equals_string"], target_rule["pattern"]])
    return {"fields": checks, "conditional": conditional}


def validate_row(row, rules, surface):
    if row.get("source") in EXCLUDED_SOURCES or row.get("record_type", "").startswith("STRAININFO"):
        raise ValueError("Nested overlay evidence requires a separate native adapter")
    if row.get("record_type") == "NUCLEOTIDE_SEQUENCE":
        raise ValueError("Nested sequence evidence requires a separate native adapter")
    for field, check in rules["fields"].items():
        value = row.get(field, "")
        if check["required"] and not value:
            raise ValueError(f"Missing required native link field: {field}")
        if value and (
            (check["pattern"] and not re.fullmatch(check["pattern"], value))
            or (check["values"] and value not in check["values"])
        ):
            raise ValueError(f"Invalid native link field: {field}")
    for field, value, pattern in rules["conditional"]:
        if row.get(field) == value and not re.fullmatch(pattern, row[SURFACES[surface]["target"]]):
            raise ValueError("Native target namespace conflicts with its source type")


def owner_matches(row, owners):
    """Exact lexical lookup only; neither aliases nor co-occurrence imply identity."""
    bindings, missing = [], []
    for role in ("strain_id", "matched_strain_id"):
        key = row.get(role)
        if key:
            matches = owners.get(key, [])
            if not matches:
                missing.append({"role": role, "strain_id": key})
            for path, position, payload in matches:
                bindings.append((role, path, position, payload))
    return bindings, missing


def prepare(root, commit, surface):
    if not re.fullmatch(r"[0-9a-f]{40}", commit) or surface not in SURFACES:
        raise ValueError("An immutable native commit and known surface are required")
    origin = subprocess.check_output(
        ["git", "-C", str(root), "remote", "get-url", "origin"], text=True
    ).strip()
    if origin not in {
        f"https://github.com/{REPOSITORY}.git",
        f"https://github.com/{REPOSITORY}",
        f"git@github.com:{REPOSITORY}.git",
    }:
        raise ValueError("Native Git origin identity mismatch")
    profile = SURFACES[surface]
    paths = (profile["source"], *OWNERS, MANIFEST, SCHEMA, *SEMANTIC_FILES)
    sources = {
        path: subprocess.check_output(["git", "-C", str(root), "show", f"{commit}:{path}"]) for path in paths
    }
    hashes = {path: sha(content) for path, content in sources.items()}
    provenance, schema = yaml.safe_load(sources[MANIFEST]), yaml.safe_load(sources[SCHEMA])
    rules = constraints(schema, surface)
    required = {field for field, check in rules["fields"].items() if check["required"]}
    owners, source_counts, missing_counts, row_counts = defaultdict(list), Counter(), Counter(), {}
    for path in OWNERS:
        count, seen = 0, set()
        for position, row in table_rows(sources[path], {"strain_id", "taxon_ids"}):
            count += 1
            if not re.fullmatch(r"kgmicrobe\.strain:\S+", row["strain_id"]) or row["strain_id"] in seen:
                raise ValueError("Missing, duplicate or malformed native owner")
            seen.add(row["strain_id"])
            owners[row["strain_id"]].append((path, position, row))
        row_counts[path] = count
    count = 0
    for _position, row in table_rows(sources[profile["source"]], required):
        validate_row(row, rules, surface)
        count += 1
        source_counts[row["source"]] += 1
        _bindings, missing = owner_matches(row, owners)
        missing_counts.update(entry["role"] for entry in missing)
    row_counts[profile["source"]] = count
    for path, count in row_counts.items():
        entries = [entry for entry in provenance["outputs"] if entry["path"] == Path(path).name]
        if (
            len(entries) != 1
            or entries[0]["rows"] != count
            or entries[0]["bytes"] != len(sources[path])
            or entries[0]["sha256"] != hashes[path]
        ):
            raise ValueError("Native inventory differs from its provenance manifest")
    return {
        "source": sources[profile["source"]],
        "owners": owners,
        "required": required,
        "source_rows": row_counts[profile["source"]],
        "owner_rows": {path: row_counts[path] for path in OWNERS},
        "source_counts": dict(source_counts),
        "missing_owner_counts": dict(missing_counts),
        "common": {
            "commit": commit,
            "surface": surface,
            "hashes": hashes,
            "rules": rules,
            "prefixes": schema["prefixes"],
            "upstream": provenance["kg_microbe_source"],
        },
    }


def adapt_link(row, *, position, owners, missing, commit, surface, hashes, rules, prefixes, upstream):
    from kg_microbe_curation.identity import sha256_json
    from kg_microbe_curation.native import NATIVE_CONTRACT, native_assertion_id, validate_native_assertion

    validate_row(row, rules, surface)
    profile = SURFACES[surface]
    predicate = "taxonmech:" + profile["slot"]

    def locator(path, selector=None):
        return {"repository": REPOSITORY, "commit": commit, "path": path, "selector": selector or {}}

    payload_sha = sha256_json(row)
    bindings = []
    for role, path, owner_position, payload in owners:
        if payload["strain_id"] != row[role] or path not in OWNERS:
            raise ValueError("Native owner binding differs from its source link")
        bindings.append(
            {
                "role": role,
                "locator": locator(path, {"source_position": owner_position}),
                "source_sha256": hashes[path],
                "payload_sha256": sha256_json(payload),
                "native_payload": payload,
            }
        )
    assertion = {
        "contract": NATIVE_CONTRACT,
        "native_locator": {
            **locator(profile["source"], {"source_position": position}),
            "source_sha256": hashes[profile["source"]],
            "payload_sha256": payload_sha,
        },
        "payload": {
            "subject": row["strain_id"],
            "predicate": predicate,
            "object": row[profile["target"]],
            "native_payload": row,
            "context": {
                "scope": "native_typed_strain_link_only",
                "native_class": profile["class"],
                "native_slot": profile["slot"],
                "upstream_snapshot": upstream,
                "owner_bindings": bindings,
                "unavailable_owner_bindings": missing,
                "review_evidence_status": "unavailable_exact_native_link_review",
                "matching_policy": "exact_native_payload_and_dependency_bindings",
                "match_selector": {
                    "subject": row["strain_id"],
                    "predicate": predicate,
                    "object": row[profile["target"]],
                    "native_payload_sha256": payload_sha,
                    "source_sha256": hashes[profile["source"]],
                },
            },
            "interpretation": {
                "normalization_contract": "taxonmech-native-typed-link-exact-lexical/v1",
                "normalizer_contract_sha256": sha256_json({p: hashes[p] for p in SEMANTIC_FILES}),
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
            "rationale": "The extracted link has no exact native assertion review proof. "
            "Owner, cohort and generated-record review do not approve this link.",
        },
        "assurance": "unassessed",
        "limitations": [
            "Source-reported strain links are not strain/deposit, taxon or genome equivalence assertions.",
            "Accession versions, source taxonomy and GOLD organism/project/analysis keys retain their "
            "native meaning; source taxonomy does not override strain classification.",
            "Owner rows are exact lexical provenance, not new collection-identity validation or joins. "
            "Missing owners remain explicitly unavailable; no alias normalization is inferred.",
            "Genome records can describe plasmids or draft scopes; "
            "complete cellular genomes are not inferred.",
            "Only flat committed inventories are exported. Nested ATB/StrainInfo and nomenclature need "
            "separate scoped adapters. External primary-source files were not fetched or reverified.",
            "No independent scientific review, KG predicate projection "
            "or KG occurrence approval is supplied.",
        ],
        "independent_scientific_review": False,
    }
    assertion["assertion_id"] = native_assertion_id(assertion)
    validate_native_assertion(assertion)
    return assertion


def _adapt_batch(jobs, common):
    return [
        (position, adapt_link(row, position=position, owners=owners, missing=missing, **common))
        for position, row, owners, missing in jobs
    ]


def _validated(jobs, common, workers):
    if workers == 1:
        for job in jobs:
            yield from _adapt_batch([job], common)
        return
    with ProcessPoolExecutor(
        max_workers=workers, mp_context=multiprocessing.get_context("spawn")
    ) as executor:
        while window := list(islice(jobs, workers * BATCH_ROWS)):
            pending = [
                executor.submit(_adapt_batch, window[i : i + BATCH_ROWS], common)
                for i in range(0, len(window), BATCH_ROWS)
            ]
            for future in pending:
                yield from future.result()


def export_links(root, commit, surface, output, positions, *, workers=1):
    from kg_microbe_curation.identity import canonical_json

    if type(workers) is not int or not 1 <= workers <= 4:
        raise ValueError("workers must be an integer from 1 to 4")
    if output.exists() or output.is_symlink():
        raise ValueError("Output must be a new directory")
    prepared = prepare(root, commit, surface)
    if positions is not None and (
        not positions
        or len(set(positions)) != len(positions)
        or any(type(i) is not int or not 1 <= i <= prepared["source_rows"] for i in positions)
    ):
        raise ValueError("Positions must be unique valid native source rows")
    selected = set(positions) if positions is not None else None

    def jobs():
        for position, row in table_rows(prepared["source"], prepared["required"]):
            if selected is None or position in selected:
                bindings, missing = owner_matches(row, prepared["owners"])
                yield position, row, bindings, missing

    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".native-links-", dir=output.parent) as temporary:
        stage = Path(temporary) / "export"
        stage.mkdir()
        content_hash, membership_hash, written = hashlib.sha256(), hashlib.sha256(), 0
        with (stage / "assertions.jsonl").open("wb") as handle:
            for position, assertion in _validated(jobs(), prepared["common"], workers):
                line = canonical_json(assertion) + b"\n"
                handle.write(line)
                content_hash.update(line)
                membership_hash.update(canonical_json([assertion["assertion_id"], position]) + b"\n")
                written += 1
            handle.flush()
            os.fsync(handle.fileno())
        if written != (len(positions) if positions is not None else prepared["source_rows"]):
            raise ValueError("Export did not preserve selected native membership")
        persisted_hash, persisted_membership, statuses = hashlib.sha256(), hashlib.sha256(), Counter()
        with (stage / "assertions.jsonl").open("rb") as handle:
            for line in handle:
                persisted_hash.update(line)
                assertion = json.loads(line)
                statuses[assertion["native_review"]["status"]] += 1
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
            persisted_hash.digest() != content_hash.digest()
            or persisted_membership.digest() != membership_hash.digest()
            or statuses != Counter({"unassessed": written})
        ):
            raise ValueError("Persisted native bytes, membership or counters differ")
        manifest = {
            "schema_version": 1,
            "contract": "kg-microbe-native-assertion/v1",
            "repository": REPOSITORY,
            "source_commit": commit,
            "claw_contract_commit": CLAW_COMMIT,
            "surface": surface,
            "source_positions": positions,
            "source_rows": prepared["source_rows"],
            "rows": written,
            "source_owner_rows": prepared["owner_rows"],
            "source_database_counts": prepared["source_counts"],
            "source_missing_owner_counts": prepared["missing_owner_counts"],
            "native_status_counts": {"unassessed": written},
            "assertions_sha256": content_hash.hexdigest(),
            "assertion_membership_sha256": membership_hash.hexdigest(),
            "assertions_bytes": (stage / "assertions.jsonl").stat().st_size,
            "source_files": prepared["common"]["hashes"],
            "validation_workers": workers,
            "validation_batch_size": BATCH_ROWS,
            "independent_scientific_reviews": 0,
            "kg_occurrences_approved": 0,
            "scope": "Complete committed flat typed strain-link inventory; no identity or KG projection.",
            "predicate": "taxonmech:" + SURFACES[surface]["slot"],
            "review_evidence_status": "unavailable_exact_native_link_review",
            "excluded_surfaces": [
                "Nested AllTheBacteria and StrainInfo overlays, including their evidence chains.",
                "Nomenclature, strain/deposit equivalence and new joins.",
                "Exact assertion review and approved KG predicate projections.",
            ],
        }
        (stage / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
        publish_stage(stage, output)
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--surface", choices=SURFACES, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--workers", type=int, choices=range(1, 5), default=1)
    parser.add_argument("--plan", action="store_true")
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--positions", type=int, nargs="+")
    selection.add_argument("--all", action="store_true")
    args = parser.parse_args()
    if args.plan:
        prepared = prepare(args.root, args.source_commit, args.surface)
        result = {
            key: prepared[key]
            for key in ("source_rows", "owner_rows", "source_counts", "missing_owner_counts")
        }
        result.update(
            surface=args.surface,
            predicate="taxonmech:" + SURFACES[args.surface]["slot"],
            workers=args.workers,
            status="unassessed",
            source_files=prepared["common"]["hashes"],
        )
    else:
        result = export_links(
            args.root, args.source_commit, args.surface, args.output, args.positions, workers=args.workers
        )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
