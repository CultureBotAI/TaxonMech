# Review publication corrections

These corrections describe publication eligibility. They do not replace scientific
reviews, erase their findings, or promote taxon status. Committed review bundles
remain immutable; a correction adds a linked observation and a reproducible ledger.

## PR 169: batches 0014–0051

[PR 169](https://github.com/CultureBotAI/TaxonMech/pull/169) published 380 historical
record-review observations. Its original duplicate check inspected only the targets
explicitly listed in canonical bundles. It missed the per-record structured and
legacy inventories. This did not satisfy the publication task's requirement to
exclude records already reviewed on the original main base. The owner requested a
corrective follow-up on 2026-11-15; [issue 179](https://github.com/CultureBotAI/TaxonMech/issues/179)
tracks the correction.

The corrected selection applies **any prior target-review coverage**, irrespective
of whether the incoming observation has a different review ID or verdict. It uses
base `a050e29c140f7ca7e74432e364b10d732e2922f1` and publication merge
`bc4f9b4c1cb44a87acd830dd96e7b8ba2f36f6b5`, never today's inventory in place of
the historical base.

| Disposition in the original selection | Targets |
| --- | ---: |
| Excluded: prior completed scientific structured review | 149 |
| Excluded: prior legacy report | 231 |
| Eligible as a previously unreviewed target | 0 |
| Historical incoming observations preserved | 380 |

[The machine-readable ledger](pr-169.json) names every incoming observation and
target, the prior inventory row or canonical review that covers it, the exact
source revisions and hashes, and its corrected eligibility. The 149 structured
rows and incoming reviews capture matching native target hashes; this proves
neither equivalence of other inputs nor equivalence of scientific assessments.
Legacy report hashes describe the reports, not the native taxon bytes. Legacy
coverage remains separate from structured scientific-review coverage.

All 380 incoming targets are excluded from the task's previously-unreviewed
selection. The 380 published observations and their eight scientific findings
remain historical evidence. **Zero bundles were physically dropped by PR 169 or
this correction.** This correction does not retroactively make the original
pre-publication exclusion check correct. It replaces the eligibility result and
retains the record of the publication error.

The metadata-only supplement added with PR 169 is identified separately by the
ledger; it is not an additional incoming scientific record review.

The linked correction observation is available as
[YAML](../../reviews/structured/20261115T100241Z-pr-169-publication-eligibility-correction/review.yaml)
and [Markdown](../../reviews/structured/20261115T100241Z-pr-169-publication-eligibility-correction/review.md).
It assesses all 380 publication metadata targets with `scientific_review: false`
and `verdict: not_assessed`; it does not supersede the scientific observations.

## Reproduce and verify

From a checkout with the two historical revisions available:

```bash
uv run python scripts/review_publication_coverage.py --check docs/review-publication-corrections/pr-169.json
uv run pytest -q tests/test_review_publication_coverage.py
RECORD_REVIEW_BASE=origin/main just review-check
```

The audit enumerates committed Git trees, including tracked files that match
ignore patterns. It checks canonical bundles and all structured inventory shards
and legacy inventory rows. It does not execute commands recorded inside old
reviews or use uncommitted local reports to reconstruct a historical base.

The checker fails when the ledger differs from the independently reconstructed
result. Its tests cover inventory-only overlaps, distinct observations of the
same target, legacy coverage, metadata-only additions, and invalid provenance.
Passing this audit verifies selection metadata, not the reviewed science.
