# Stage 4 (`record_review`) Full-Corpus Review Report — TaxonMech (`mech-goal-sequence-20261019`, Cycle 1)

- **Repository**: `CultureBotAI/TaxonMech`
- **Source Revision**: `a4696c9f0cb7400fb95ffd7ce1bfc9bff9eae520`
- **Native Structured Review Bundle**: `reviews/structured/20261021T163800Z-stage4-corpus-record-review/review.yaml` (`SHA256: dffeef8bb90f373e6f5e07eeb00eb004db9959bb363afe50a0dabf641a6e1c73`)
- **Native Rendered Report**: `reviews/structured/20261021T163800Z-stage4-corpus-record-review/review.md` (`SHA256: d52d4ebeba57083148669dd43e8ce813c63f94726311e6ce19a7064763ad5222`)
- **Infrastructure Tasks Notebook**: `INFRA_TASKS.md` (`SHA256: bd905426fcef930be22a4c7f878278a60f629a9e2106521380577ee6bb62efb4`; Stage 4 originated task: `taxonmech-infra-0004`)
- **Skills Executed**: `.claude/skills/review-yaml-record/SKILL.md`, `.claude/skills/review-yaml-category/SKILL.md`
- **Rubric**: `.claude/skills/curate-yaml-record/references/review-checklist.md`

> **Parent Workflow Schema Invariant Note**: `kg_microbe_workflows` (`validate-evidence` on Stage 4 `ReviewReport`) requires every path in `evidence.yaml:artifacts` to reside under `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/` and requires `evidence.yaml:infra_tasks` to be `[]` on non-Stage-6 evidence manifests. The repository-root native review bundle (`reviews/structured/20261021T163800Z-stage4-corpus-record-review/review.yaml`, `review.md`) and `INFRA_TASKS.md` (`taxonmech-infra-0004`) are therefore cross-referenced with exact SHA-256 digests in `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/corpus_coverage_summary.json`, `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/review_findings.yaml`, and this report.

## 1. Frozen Corpus Coverage & SHA-256 Inventory Verification

`.venv/bin/python scripts/corpus_review_inventory.py --check --verify-target-sha256` verified **100.0% coverage** of all **626,048** in-scope `TaxonRecord` YAML files in `data/taxa/` (`data/taxa/PATHS.tsv` and `curation/seed_scope.tsv`):

| Metric | Count | Notes |
| --- | ---: | --- |
| Total in-scope `TaxonRecord` files | `626,048` | `Bacteria: 605,695`, `Archaea: 14,013`, `Eukaryota: 6,331`, `other: 9` |
| Legacy-reviewed records (`docs/legacy-review-inventory.tsv`) | `23,883` | `Archaea: 555`, `Bacteria: 17,085`, `Eukaryota: 6,243`, `Other: 0` |
| Structured-reviewed records (`docs/structured-review-inventory/part-00.tsv`..`part-13.tsv`) | `602,165` | `611` batches in `docs/structured-review-batches.tsv` (`Archaea: 13,458`, `Bacteria: 588,610`, `Eukaryota: 88`, `other: 9`) |
| Unreviewed records | `0` | Verified against `data/taxa/PATHS.tsv` |
| Overlapping records between legacy and structured inventories | `0` | Disjoint partition |
| Target YAML SHA-256 mismatches | `0` | All 626,048 files verified on disk |

### Structured Review Verdict Distribution (`602,165` records across `part-00.tsv`..`part-13.tsv`)

| Verdict | Record Count | Share | Primary Driver |
| --- | ---: | ---: | --- |
| `pass` | `479,251` | `79.59%` | Clean NCBI/BacDive/GTDB/LPSN/StrainInfo/ATB alignment |
| `needs_curation` | `95,766` | `15.90%` | `skos:closeMatch` GTDB species-cluster promotion to `EXACT_SYNONYM` and `xrefs` (`#124`, `#63`) |
| `pass_with_limitations` | `27,118` | `4.50%` | Uncommitted upstream `kg-microbe` raw edge tables for `GOLD`/`MEDIADIVE`/`MADIN`/`BACTOTRAITS` (`#8`) |
| `blocked` | `30` | `0.005%` | Multi-source attestation count verification blocked on uncommitted upstream raw edge tables (`#8`) |

## 2. Directly Bound Exemplar Records (`20` targets across all 4 domains)

The native bundle `reviews/structured/20261021T163800Z-stage4-corpus-record-review/review.yaml` binds 20 representative `TaxonRecord` files (`role: target`) spanning `Bacteria` (10), `Archaea` (3), `Eukaryota` (4), and `other` (3):
- **Bacteria (`10`)**: `NCBITaxon:562` (`Escherichia coli`), `NCBITaxon:83333` (`Escherichia coli K-12`), `NCBITaxon:1423` (`Bacillus subtilis`), `NCBITaxon:287` (`Pseudomonas aeruginosa`), `NCBITaxon:2940590` (`Achromobacter sp. JUb104`, `needs_curation` `skos:closeMatch` promotion exemplar), `NCBITaxon:3121604` (`Acidaminobacteraceae bacterium`, `needs_curation` pooled-only `skos:broadMatch` exemplar), `NCBITaxon:1435036` (`Acinetobacter bohemicus`, 8-source `pass_with_limitations` exemplar), `NCBITaxon:209650` (`Acidicaldus organivorans`, 8-source `blocked` exemplar), `NCBITaxon:206` (`Campylobacter sputorum`, `needs_curation` `skos:closeMatch` + polyphyly suffix exemplar), `NCBITaxon:33952` (`Acetobacterium woodii`, legacy-reviewed `skos:closeMatch` + polyphyly suffix exemplar).
- **Archaea (`3`)**: `NCBITaxon:2190` (`Methanocaldococcus jannaschii`), `NCBITaxon:243232` (`Methanocaldococcus jannaschii DSM 2661`), `NCBITaxon:2287` (`Saccharolobus solfataricus`).
- **Eukaryota (`4`)**: `NCBITaxon:4932` (`Saccharomyces cerevisiae`), `NCBITaxon:5207` (`Cryptococcus neoformans`), `NCBITaxon:5755` (`Acanthamoeba castellanii`, Stage 1 part-13 `pass` expansion), `NCBITaxon:1859096` (`Cryptococcus deuterogattii`, Stage 1 part-13 `pass` expansion).
- **Other (`3`)**: `NCBITaxon:155900` (`uncultured organism`), `NCBITaxon:408170` (`human gut metagenome`), `NCBITaxon:32644` (`unidentified`).

## 3. Consolidated Findings Carried Forward to Stage 5 (`resolve_review_findings`)

| `finding_id` | Issue | Category | Severity | Status | Summary & Stage 5 / Stage 6 Disposition |
| --- | --- | --- | --- | --- | --- |
| `causal-node-type-enum-and-mech-family-nav-drift` | [#76](https://github.com/CultureBotAI/TaxonMech/issues/76) | `schema` | `minor` | `open` | `CausalNodeTypeEnum` (`src/taxonmech/schema/taxonmech.yaml` lines 1467–1504) omits `GENETIC_ELEMENT`, `ORGANELLE`, `RNA`; Mech family nav omits `NaturalProductMech`. Remediate directly in Stage 5. |
| `validate-history-bare-linkml-validate-path` | [#83](https://github.com/CultureBotAI/TaxonMech/issues/83) | `provenance` | `minor` | `open` | `scripts/validate_history.py` `main()` (lines 47–51) invokes `linkml-validate` by bare name instead of checking `Path(sys.executable).with_name("linkml-validate")`. Remediate directly in Stage 5. |
| `gtdb-closematch-exact-promotion` | [#124](https://github.com/CultureBotAI/TaxonMech/issues/124) | `grounding` | `major` | `open` | `95,766` records across `part-00.tsv`..`part-13.tsv` carry `needs_curation` from `skos:closeMatch` GTDB promotion to `EXACT_SYNONYM` and `xrefs` (`src/taxonmech/seed.py` lines 443–478; `#124`, `#63`). Requires full-corpus regeneration. |
| `gtdb-polyphyly-suffix-synonym-mangling` | [#65](https://github.com/CultureBotAI/TaxonMech/issues/65) | `nomenclature` | `major` | `open` | `src/taxonmech/seed.py` lines 470–473 mangle 15,704 GTDB polyphyly suffixes into fake trinomials (`Campylobacter F sputorum`, `Acetobacterium woodii A`). Requires corpus regeneration. |
| `gtdb-pooled-broadmatch-attestation-and-note` | [#118](https://github.com/CultureBotAI/TaxonMech/issues/118) | `evidence` | `major` | `open` | 6,335 pooled-only GTDB records (e.g., `NCBITaxon:3121604`) report largest pooled cluster's genome count (`seed.py` lines 579–593; `#118`) and 8,587 pooled records invert the `broadMatch` direction note (`seed.py` lines 465–467; `#119`). Requires corpus regeneration. |
| `curation-history-stale-scope-strain-count` | [#69](https://github.com/CultureBotAI/TaxonMech/issues/69) | `provenance` | `minor` | `open` | `SEEDED_FROM_SOURCES` `curation_history` (`seed.py` lines 635–645) embeds static `curation/seed_scope.tsv` strain count (`1861` vs `1975` on `NCBITaxon:562`). Requires corpus regeneration. |
| `upstream-edge-multiplicity-and-subtree-count-scope` | [#8](https://github.com/CultureBotAI/TaxonMech/issues/8) | `completeness` | `minor` | `open` | `27,118` `pass_with_limitations` (`NCBITaxon:1435036`) and `30` `blocked` (`NCBITaxon:209650`) records reflect uncommitted upstream `kg-microbe` raw edge tables and direct-only non-BacDive counts (`#8`; `taxonmech-infra-0004`). |
| `mechanism-and-protein-representation-prerequisites` | [#78](https://github.com/CultureBotAI/TaxonMech/issues/78) | `completeness` | `major` | `open` | `0` of `626,048` records populate `causal_graphs` or `UniProtKB:` `GENE_OR_PROTEIN` nodes pending `INFRA_TASKS.md` `taxonmech-infra-0001..0003` (Stage 6). |
