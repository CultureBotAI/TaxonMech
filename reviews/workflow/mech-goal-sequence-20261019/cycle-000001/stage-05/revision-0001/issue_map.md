# Cycle 1 Stage 5 Issue Map and Grouped Finding Dispositions (`resolve_review_findings`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: `cycle 1`, `stage 5` (`resolve_review_findings`), `revision 1`
- **Repository**: `CultureBotAI/TaxonMech`
- **Source Revision**: `5bab842c1acde531640142f784b013af168b9a0f`
- **Consumed Stage 4 Workflow Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml` (`sha256: 4d5428357f5317ef1faad82e61541ba4496e5ba417423473094a2da677ba062b`)
- **Consumed Stage 4 Structured Review**: `reviews/structured/20261021T163800Z-stage4-corpus-record-review/review.yaml`
- **Linked Stage 5 Post-Remediation Structured Review**: `reviews/structured/20261022T012228Z-stage5-remediation-review/review.yaml`

---

## 1. Grouped Finding Triage, Issue Deduplication, and Dispositions

All 8 consolidated findings carried forward from Cycle 1 Stage 4 (`reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml`) were grouped by shared root cause and repair ownership, deduplicated against canonical GitHub issues in `CultureBotAI/TaxonMech`, and triaged into **2 resolved groups** and **6 deferred groups**:

| Group ID | Finding ID | Canonical GitHub Issue | Related Issues / Infra Tasks | Repair Ownership | Stage 5 Status | Disposition Summary |
|---|---|---|---|---|---|---|
| `group-schema-enum-and-mech-family-nav` | `causal-node-type-enum-and-mech-family-nav-drift` | [#76](https://github.com/CultureBotAI/TaxonMech/issues/76) | — | `src/taxonmech/schema/taxonmech.yaml`, `README.md`, `CLAUDE.md`, `src/taxonmech/templates/{base,index}.html`, `pages/*.html` | `resolved` | Restored `RNA`, `GENETIC_ELEMENT`, and `ORGANELLE` to `CausalNodeTypeEnum` (matching the 18-value superset of `TraitMech` and `HabitatMech`), and added `NaturalProductMech` across `README.md`, `CLAUDE.md`, `src/taxonmech/templates/{base,index}.html`, and all 6,372 rendered HTML pages under `pages/`. |
| `group-validate-history-linkml-executable` | `validate-history-bare-linkml-validate-path` | [#83](https://github.com/CultureBotAI/TaxonMech/issues/83) | — | `scripts/validate_history.py`, `tests/test_new_history_record.py` | `resolved` | Added `linkml_validate()` helper in `scripts/validate_history.py` resolving `Path(sys.executable).with_name("linkml-validate")` when present on disk and falling back to `"linkml-validate"` on `PATH`. |
| `group-gtdb-closematch-exact-promotion` | `gtdb-closematch-exact-promotion` | [#124](https://github.com/CultureBotAI/TaxonMech/issues/124) | [#63](https://github.com/CultureBotAI/TaxonMech/issues/63) | `src/taxonmech/seed.py` (lines 443–478), `data/taxa/**/*.yaml` (95,766 records), `pages/taxon-details/*.json.gz` | `deferred` | Deferred: `scripts/verify_corpus.py` in `just qc` enforces byte-for-byte identity between `src/taxonmech/seed.py` and all 626,048 YAML files in `data/taxa/`. Gating `skos:closeMatch` promotion requires a dedicated full-corpus YAML and page-shard regeneration pass across 95,766 records and 2,909 `.json.gz` shards. |
| `group-gtdb-polyphyly-suffix-mangling` | `gtdb-polyphyly-suffix-synonym-mangling` | [#65](https://github.com/CultureBotAI/TaxonMech/issues/65) | — | `src/taxonmech/seed.py` (lines 470–473), `data/taxa/**/*.yaml` (15,704 rows), `pages/taxon-details/*.json.gz` | `deferred` | Deferred: preserving GTDB polyphyly suffix formatting (`_A`, `_F`) in `src/taxonmech/seed.py` alters generated `synonyms` across 15,704 GTDB mapping rows, requiring a coordinated full-corpus YAML and page-shard regeneration pass to satisfy `scripts/verify_corpus.py` and `scripts/render_pages.py --check`. |
| `group-gtdb-pooled-broadmatch-semantics` | `gtdb-pooled-broadmatch-attestation-and-note` | [#118](https://github.com/CultureBotAI/TaxonMech/issues/118) | [#119](https://github.com/CultureBotAI/TaxonMech/issues/119) | `src/taxonmech/seed.py` (lines 465–467, 579–593), `data/taxa/**/*.yaml` (8,587 records), `pages/taxon-details/*.json.gz` | `deferred` | Deferred: aligning pooled GTDB `skos:broadMatch` genome-count attestations (`6,335` pooled-only records) and mapping-direction notes (`8,587` records / `209,540` rows) in `src/taxonmech/seed.py` requires regenerating all 8,587 affected `TaxonRecord` YAML files and rendered shards in a dedicated corpus-regeneration batch. |
| `group-curation-history-scope-strain-count` | `curation-history-stale-scope-strain-count` | [#69](https://github.com/CultureBotAI/TaxonMech/issues/69) | — | `src/taxonmech/seed.py` (lines 635–645), `curation/seed_scope.tsv`, `data/taxa/**/*.yaml` | `deferred` | Deferred: updating `SEEDED_FROM_SOURCES` `curation_history` notes in `src/taxonmech/seed.py` and `curation/seed_scope.tsv` alters generated `curation_history` across `data/taxa/`, requiring full-corpus YAML and page-shard regeneration under `scripts/verify_corpus.py`. |
| `group-upstream-edge-multiplicity-and-subtree-counts` | `upstream-edge-multiplicity-and-subtree-count-scope` | [#8](https://github.com/CultureBotAI/TaxonMech/issues/8) | `INFRA_TASKS.md` (`taxonmech-infra-0004`) | `src/taxonmech/extract.py`, `src/taxonmech/seed.py`, `docs/record-review-profile.md` | `deferred` | Deferred to Stage 6 (`implement_infra_tasks`): requires reproducible upstream kg-microbe edge-multiplicity provenance for `GOLD`, `MEDIADIVE`, `MADIN`, and `BACTOTRAITS` and direct-vs-subtree count documentation/alignment tracked in `INFRA_TASKS.md` (`taxonmech-infra-0004`) and `#8`. |
| `group-mechanism-and-protein-infra-prerequisites` | `mechanism-and-protein-representation-prerequisites` | [#78](https://github.com/CultureBotAI/TaxonMech/issues/78) | `INFRA_TASKS.md` (`taxonmech-infra-0001`, `taxonmech-infra-0002`, `taxonmech-infra-0003`) | `src/taxonmech/seed.py`, `src/taxonmech/extract.py`, `src/taxonmech/schema/taxonmech.yaml`, `conf/id_label_targets.yaml` | `deferred` | Deferred to Stage 6 (`implement_infra_tasks`): populating `causal_graphs` and `GENE_OR_PROTEIN` `UniProtKB:` references is gated on maintained overlay merging in `src/taxonmech/seed.py` (`taxonmech-infra-0001`), granular trait/pathway extraction in `src/taxonmech/extract.py` (`taxonmech-infra-0002`), and a pinned UniProtKB snapshot plus `UniProtKB`/`EC` prefix and scope validation (`taxonmech-infra-0003`). |

---

## 2. Detailed Remediation Notes for Resolved Groups

### 2.1 `group-schema-enum-and-mech-family-nav` ([#76](https://github.com/CultureBotAI/TaxonMech/issues/76))

- **Root Cause**:
  1. `CausalNodeTypeEnum` in `src/taxonmech/schema/taxonmech.yaml` documented that it was a superset of TraitMech's `CausalNodeTypeEnum` to allow lossless instantiation of TraitMech `MechanismTemplate` graphs, but omitted three TraitMech node types (`RNA`, `GENETIC_ELEMENT`, and `ORGANELLE`).
  2. The Mech suite navigation in `README.md`, `CLAUDE.md`, `src/taxonmech/templates/base.html`, `src/taxonmech/templates/index.html`, and the rendered HTML pages in `pages/` omitted `NaturalProductMech` (`https://culturebotai.github.io/NaturalProductMech/`).
- **Native Writer Fixes**:
  - Added `RNA`, `GENETIC_ELEMENT`, and `ORGANELLE` (with TraitMech's exact definitions) to `CausalNodeTypeEnum` in `src/taxonmech/schema/taxonmech.yaml` (now 18 permissible values).
  - Added `NaturalProductMech` to the Mech suite tables in `README.md` and `CLAUDE.md` and to the footer navigation in `src/taxonmech/templates/base.html` and `src/taxonmech/templates/index.html`.
  - Updated all 6,372 rendered HTML files in `pages/*.html` and `pages/domain/*.html` to match `src/taxonmech/templates/{base,index}.html` byte-for-byte (`pages/taxon-details/*.json.gz` shards do not inherit `base.html` and remain untouched).
  - Added regression tests `test_causal_node_type_enum_is_superset_of_traitmech_and_habitatmech` in `tests/test_schema.py` and `test_mech_family_navigation_and_docs_include_naturalproductmech` in `tests/test_html_navigation.py`.

### 2.2 `group-validate-history-linkml-executable` ([#83](https://github.com/CultureBotAI/TaxonMech/issues/83))

- **Root Cause**:
  - `scripts/validate_history.py` invoked `subprocess.run(["linkml-validate", ...])` using a bare executable name. When invoked via `.venv/bin/python scripts/validate_history.py history` in non-interactive shells or subagent environments where `.venv/bin` is not prepended to `PATH`, `subprocess.run` raised `FileNotFoundError` even though `linkml-validate` was installed alongside `sys.executable`.
- **Native Writer Fixes**:
  - Added `linkml_validate()` helper in `scripts/validate_history.py` that checks `Path(sys.executable).with_name("linkml-validate")` and returns its full path when present as a file on disk, falling back to `"linkml-validate"` on `PATH`.
  - Added unit test `test_validate_history_resolves_linkml_validate_beside_interpreter` in `tests/test_new_history_record.py`.
