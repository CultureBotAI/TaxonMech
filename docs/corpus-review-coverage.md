# Full-Corpus Review Coverage

Every one of the **626,048** indexed taxon records in [`data/taxa/PATHS.tsv`](../data/taxa/PATHS.tsv) is accounted for across two disjoint, auditable review inventories (`0` overlap, `0` unreviewed records remaining):

1. **[Historical Review Archive](legacy-review-archive.md)** ([`docs/legacy-review-inventory.tsv`](legacy-review-inventory.tsv)): **23,883** distinct records with preserved pre-contract Markdown reports under `reports/yaml_record_review/` (imported in PR #115).
2. **Structured Review Inventory** ([`docs/structured-review-inventory/part-00.tsv`](structured-review-inventory/part-00.tsv) .. [`part-13.tsv`](structured-review-inventory/part-13.tsv) and [`docs/structured-review-batches.tsv`](structured-review-batches.tsv)): **602,165** distinct records reviewed under the structured review contract across **611** rounds (`pre-round`, `round13`, `round15`..`round24` in `part-00.tsv`, `round25-b01`..`round25-b598` across `part-01.tsv`..`part-12.tsv`, and `round26-b01` in `part-13.tsv`).

## Coverage By Domain

| Domain | Historical archive (`legacy-review-inventory.tsv`) | Structured inventory (`structured-review-inventory/part-*.tsv`) | Total indexed (`data/taxa/PATHS.tsv`) |
| --- | ---: | ---: | ---: |
| Archaea | 555 | 13,458 | 14,013 |
| Bacteria | 17,085 | 588,610 | 605,695 |
| Eukaryota | 6,243 | 88 | 6,331 |
| Other | 0 | 9 | 9 |
| **Total** | **23,883** | **602,165** | **626,048** |

## Coverage Is Not A Blanket Scientific Pass

Completing 100% review coverage (`626,048 / 626,048`) means every record in `data/taxa/` has an auditable review record and SHA-256 provenance attestation. **It does not promote any `PROPOSED` taxon to `REVIEWED`, nor does it close open curation findings.**

Across the 602,165 structured reviews in `docs/structured-review-inventory/part-00..13.tsv`:

| Verdict | Record count | Meaning |
| --- | ---: | --- |
| `pass` | 479,251 | Carried NCBI identity, lineage, nomenclature, and local strain/attestation routing match pinned `data/raw/` inputs without open findings. |
| `pass_with_limitations` | 27,118 | Carried fields match local raw tables, but manifest-pinned upstream `kg-microbe` edge tables (`GOLD`, `MEDIADIVE`, `MADIN`, `BACTOTRAITS`) are not committed locally (`completion: partial`). |
| `needs_curation` | 95,766 | Open scientific/grounding finding (primarily `src/taxonmech/seed.py` promoting `skos:closeMatch` GTDB species-cluster mappings to `EXACT_SYNONYM` and top-level `xrefs` without an explicit taxon-identity bridge; tracked in issue #124). |
| `blocked` | 30 | Early `pre-round` (`4`) and `round15` (`26`) reviews recorded as `blocked` pending check/dependency availability. |
| **Total** | **602,165** | **100% of records outside the historical archive** |

Per [`docs/record-review-profile.md`](record-review-profile.md), scientific findings in generated `data/taxa/<domain>/*.yaml` records must never be silenced by hand-editing generated YAML or `pages/`. They must be resolved through their maintained owners (`src/taxonmech/seed.py`, `curation/seed_scope.tsv`, `data/raw/`, etc.) followed by guarded regeneration and validation.

## Shard Architecture And Canonical Bundles

Storing 602,165 separate `review.yaml` + `review.md` directory pairs (1.2M+ files) directly under `reviews/structured/` would exceed practical Git tree/pack limits and CI runtime budgets. Instead:

- **Per-record structured inventory shards (`docs/structured-review-inventory/part-00.tsv` .. `part-13.tsv`)** record the exact `review_id`, `round_id`, `target_id`, `target_path`, `target_sha256` (matching the committed `data/taxa/<domain>/<slug>.yaml` bytes), `label`, `verdict`, `completion`, `scientific_review`, `finding_count`, `started_at`, and `finished_at` for all 602,165 records.
- **Per-round batch summary (`docs/structured-review-batches.tsv`)** aggregates all 611 review rounds (`pre-round` through `round26-b01`), recording the shard path(s), `record_count`, `pass_count`, `pass_with_limitations_count`, `needs_curation_count`, `blocked_count`, boundary `target_id`s, timestamps, and provenance notes (including the `round13-agent2` author-metadata erratum note).
- **Canonical structured bundles (`reviews/structured/`)** retain **14** `kind: batch` shard bundles (`*-structured-review-shard-part-00` .. `part-13`) that bind each shard TSV and `docs/structured-review-batches.tsv` by SHA-256 along with boundary and verdict-stratified target records, plus **25** representative single-record `kind: record` bundles spanning all four domains (`archaea`, `bacteria`, `eukaryota`, `other`).

## Verification

Run the reproducible full-corpus inventory checker and test suite from the repository root:

```bash
uv run python scripts/corpus_review_inventory.py --check
uv run pytest -q tests/test_corpus_review_inventory.py
```

To additionally recompute and verify the SHA-256 digest of all 602,165 target YAML files on disk against `target_sha256` in `docs/structured-review-inventory/part-*.tsv`:

```bash
uv run python scripts/corpus_review_inventory.py --check --verify-target-sha256
```
