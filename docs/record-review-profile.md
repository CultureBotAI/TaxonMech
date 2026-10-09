# TaxonMech review profile

New record reviews follow [the shared contract](record-reviews.md), with
authoritative YAML and derived Markdown under
`reviews/structured/<YYYYMMDDTHHMMSSZ>-<slug>/`. Historical ad hoc reports remain
historical evidence and need no migration. `conf/record_review.yaml` lists the
active routes and local rubrics.

## Routes and output

- `.claude/skills/review-yaml-record/SKILL.md`: one resolved record.
- `.claude/skills/review-yaml-category/SKILL.md`: a coherent category with
  explicit lump/split/retain/defer decisions; sampled coverage keeps its method,
  denominator, inspected members and limitations. Explicit batches use `kind: batch`.
- `.claude/skills/curate-yaml-record/SKILL.md`: the audit-only route uses the
  same output contract and retains the native scientific checklist.

Run from the repository root using its own Python environment (LinkML,
linkml-runtime, jsonschema and PyYAML; pytest in the dev extra):

```bash
uv run python scripts/record_review.py inspect --targets /tmp/review-targets.yaml
just review-validate /tmp/completed-review.yaml
just review-save /tmp/completed-review.yaml
just review-check
```

Use session-unique temporary inputs and add `--input <path>` to inspect for each
additional rubric/schema/source/overlay used. Retain the captured Git revision
and hashes. Checks record actual commands and exit codes, never invented
success. New observations are immutable; link both saved files in the final
response. Missing dependencies or required checks are an explicit blocked output
step or partial assessment, not permission to save unvalidated prose.

## Native questions and generated ownership

Review generated `data/taxa/<domain>/` records at species rank or below.
Higher taxa belong only in lineage. Inspect exact NCBI taxon identity/rank,
carried NCBI lineage, LPSN nomenclature, GTDB mapping predicates, source
attestations, strain/deposit identities and genome links. Use
`docs/CURATION.md`, `docs/HARMONIZATION.md`, `docs/SCHEMA.md`, the local checklist,
and the source/strain guides listed in `conf/record_review.yaml`.

Keep strain identity, taxon classification and genome-record identity separate.
CAFI authority and complete deposit accession must match; preserve source
accession versions, GOLD organism/project/analysis chains, StrainInfo SI-DP
links and ATB sample evidence. Shared taxonomy, strain names or BioSamples do
not establish assembly equivalence. Retain taxon rank, deposit authority,
source snapshot/version and assertion units as evidence-linked dimensions.
Preserve all classified strains in records; page pagination is not a data cap.

Set target kind to `generated`; inspect the exact source rows and hash every
input used. Scientific fixes belong in committed `data/raw/`, `data/atb/`,
`data/straininfo/`, `curation/seed_scope.tsv`, source catalog/overlay inputs, the
extractor/seeder, or the specifically identified kg-microbe upstream owner.
Report precise source row locators; if upstream ownership cannot be resolved,
state that limitation. Never fix generated YAML or `pages/` to silence a
finding. A snapshot-row target needs an exact selector.

NCBI lineage is carried, not reconciled with GTDB or LPSN here. Agent-authored
changes remain PROPOSED; REVIEWED requires a human. Shared validation neither
promotes native status nor appends history. Existing guarded writers and
curation-event requirements remain applicable to future authorized changes.

## Native checks

```bash
just validate-strict <record-path> --out /tmp/taxonmech-record-validation.tsv
just verify-corpus
just validate-history
just validate-products
just qc
```

Corpus reproduction is a full-corpus check; report its actual execution/scope
instead of inventing a focused equivalent. Source catalog queries and
`just propose-scope` are lookup/selection aids, not scientific review.
Save assessed output using the shared validator/saver. Deterministic-only
inspection uses `scientific_review: false`; blocked checks and uninspected
members remain visible in limitations. Legacy ignored `reports/` output remains
unchanged; new structured bundles live in the separate Git-visible
`reviews/structured/` path.

## Validation and ownership of the contract

`schema/record_review.yaml`, `scripts/record_review.py`,
`docs/record-reviews.md`, and `tests/test_record_review_contract.py` are copied
byte-identically from CLAW. Canonical marked skill regions are rendered with
the native sections preserved. Edit the shared contract upstream and re-adopt;
the local profile, rubrics and scientific status gates remain repository-owned.
`just review-check` validates retained bundles and runs the profile/roundtrip
contract tests. The existing PR and merge-group quality workflow also runs the
contract test alongside its unchanged native checks. Zero structured reviews
means missing coverage, not a scientific pass. The new path is Git-visible
without opening ignored legacy report directories.

CI fetches full history and sets `RECORD_REVIEW_BASE` from the trusted PR base,
merge-group base, or push-before SHA. It requires that commit to exist before
running the canonical test, which rejects changes or deletions to previously
saved bundles. Local `just review-check` defaults to HEAD; set
`RECORD_REVIEW_BASE=<base-commit>` when checking a branch's committed changes.
There is no automatic CI fallback to an already modified HEAD.
