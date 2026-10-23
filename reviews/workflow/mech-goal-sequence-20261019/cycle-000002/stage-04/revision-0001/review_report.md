# Stage 4 (`record_review`) Full-Corpus Review Report — TaxonMech (`mech-goal-sequence-20261019`, Cycle 2)

- **Repository**: `CultureBotAI/TaxonMech`
- **Source Revision**: `82a3ece85614bc6b975f7ed01850aa4f57207d71`
- **Previous Workflow Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-05/revision-0001/evidence.yaml` (`SHA256: 9cb21f3aea37f71bef99929badad120b34a52356b30d0821b6330c29e4b0ed95`)
- **Native Structured Review Bundle**: `reviews/structured/20261023T073200Z-cycle2-stage4-corpus-record-review/review.yaml` (`SHA256: 9e2dca9e61630c11ba99a43b54e3b880bc86db36e7a523d828beea5f2a01669a`)
- **Native Rendered Report**: `reviews/structured/20261023T073200Z-cycle2-stage4-corpus-record-review/review.md` (`SHA256: 25c9103077f2ec39dd60b274038a95e641d036b9705eb39bf4b11bf7fc5b3d93`)
- **Infrastructure Tasks Notebook**: `INFRA_TASKS.md` (`SHA256: 276aa7fa5439a3fac069798ca1b029d8a50b2cbcc47a74f7a3423f9847ba4fa0`; tracked tasks: `taxonmech-infra-0001..0004`)
- **Skills Executed**: `.claude/skills/review-yaml-record/SKILL.md`, `.claude/skills/review-yaml-category/SKILL.md`
- **Rubric**: `.claude/skills/curate-yaml-record/references/review-checklist.md`

> **Parent Workflow Schema Invariant Note**: `kg_microbe_workflows` (`validate-evidence` on Stage 4 `ReviewReport`) requires every path in `evidence.yaml:artifacts` to reside under `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-04/revision-0001/` and requires `evidence.yaml:infra_tasks` and `evidence.yaml:groups` to be `[]` on Stage 4 evidence manifests. The repository-root native review bundle (`reviews/structured/20261023T073200Z-cycle2-stage4-corpus-record-review/review.yaml`, `reviews/structured/20261023T073200Z-cycle2-stage4-corpus-record-review/review.md`) and `INFRA_TASKS.md` (`taxonmech-infra-0001..0004`) are therefore cross-referenced with exact SHA-256 digests in `corpus_coverage_summary.json`, `review_findings.yaml`, and this report.

## 1. Frozen Corpus Coverage & Post-Curation SHA-256 Inventory Audit

`.venv/bin/python scripts/corpus_review_inventory.py --check` verified **100.0% coverage** of all **626,048** in-scope `TaxonRecord` YAML files in `data/taxa/` (`data/taxa/PATHS.tsv` and `curation/seed_scope.tsv`), and `.venv/bin/python scripts/corpus_review_inventory.py --check --verify-target-sha256` audited per-record target SHA-256 alignment following Cycle 2 Stages 2–3 (`#155`, `#156`):

| Metric | Count | Notes |
| --- | ---: | --- |
| Total in-scope `TaxonRecord` files | `626,048` | `Bacteria: 605,695`, `Archaea: 14,013`, `Eukaryota: 6,331`, `other: 9` |
| Legacy-reviewed records (`docs/legacy-review-inventory.tsv`) | `23,883` | `Archaea: 555`, `Bacteria: 17,085`, `Eukaryota: 6,243`, `Other: 0` (including 5 Cycle 2 causal-graph records: `NCBITaxon:5207`, `235443`, `40410`, `283643`, `294750`) |
| Structured-reviewed records (`docs/structured-review-inventory/part-00.tsv`..`part-13.tsv`) | `602,165` | `611` batches in `docs/structured-review-batches.tsv` (`Archaea: 13,458`, `Bacteria: 588,610`, `Eukaryota: 88`, `other: 9`) |
| Unreviewed records | `0` | Verified against `data/taxa/PATHS.tsv` |
| Overlapping records between legacy and structured inventories | `0` | Disjoint partition |
| Unchanged records matching original inventory SHA-256 | `626,033` | Exact byte parity with Cycle 1 Stage 4 |
| Records updated by Cycle 2 Stages 2–3 `causal_graphs` + UniProtKB overlays | `15` | All 15 re-reviewed and hash-bound in `20261022T190800Z-cycle2-stage3-uniprot-protein-examples` and in this Stage 4 bundle (`10` in structured shards `part-02,05,08,12,13`; `5` in `docs/legacy-review-inventory.tsv`) |

### Structured Review Verdict Distribution (`602,165` records across `part-00.tsv`..`part-13.tsv`)

| Verdict | Record Count | Share | Primary Driver |
| --- | ---: | ---: | --- |
| `pass` | `479,251` | `79.59%` | Clean NCBI/BacDive/GTDB/LPSN/StrainInfo/ATB alignment |
| `needs_curation` | `95,766` | `15.90%` | `skos:closeMatch` GTDB species-cluster promotion to `EXACT_SYNONYM` and `xrefs` (`#124`, `#63`) |
| `pass_with_limitations` | `27,118` | `4.50%` | Uncommitted upstream `kg-microbe` raw edge tables for `GOLD`/`MEDIADIVE`/`MADIN`/`BACTOTRAITS` (`#8`) |
| `blocked` | `30` | `0.005%` | Multi-source attestation count verification blocked on uncommitted upstream raw edge tables (`#8`) |

## 2. Directly Bound Exemplar & Causal-Graph Records (`27` targets across all 4 domains)

The native bundle `reviews/structured/20261023T073200Z-cycle2-stage4-corpus-record-review/review.yaml` binds `27` representative `TaxonRecord` files (`role: target`) spanning `Bacteria` (13), `Archaea` (3), `Eukaryota` (8), and `other` (3), including all `15` records enriched with `causal_graphs` and live-verified `UniProtKB` `GENE_OR_PROTEIN` nodes in Cycle 2 Stages 2–3:
- **Bacteria (`13`)**: `NCBITaxon:562` (`Escherichia coli`), `NCBITaxon:83333` (`Escherichia coli K-12`), `NCBITaxon:511145` (`Escherichia coli str. K-12 substr. MG1655`), `NCBITaxon:1423` (`Bacillus subtilis`), `NCBITaxon:224308` (`Bacillus subtilis subsp. subtilis str. 168`), `NCBITaxon:287` (`Pseudomonas aeruginosa`), `NCBITaxon:208964` (`Pseudomonas aeruginosa PAO1`), `NCBITaxon:2940590` (`Achromobacter sp. JUb104`), `NCBITaxon:3121604` (`Acidaminobacteraceae bacterium`), `NCBITaxon:1435036` (`Acinetobacter bohemicus`), `NCBITaxon:209650` (`Acidicaldus organivorans`), `NCBITaxon:206` (`Campylobacter sputorum`), `NCBITaxon:33952` (`Acetobacterium woodii`).
- **Archaea (`3`)**: `NCBITaxon:2190` (`Methanocaldococcus jannaschii`), `NCBITaxon:243232` (`Methanocaldococcus jannaschii DSM 2661`), `NCBITaxon:2287` (`Saccharolobus solfataricus`).
- **Eukaryota (`8`)**: `NCBITaxon:4932` (`Saccharomyces cerevisiae`), `NCBITaxon:5207` (`Cryptococcus neoformans`), `NCBITaxon:235443` (`Cryptococcus neoformans H99`), `NCBITaxon:40410` (`Cryptococcus deneoformans`), `NCBITaxon:283643` (`Cryptococcus deneoformans B-3501A`), `NCBITaxon:1859096` (`Cryptococcus deuterogattii`), `NCBITaxon:294750` (`Cryptococcus deuterogattii R265`), `NCBITaxon:5755` (`Acanthamoeba castellanii`).
- **Other (`3`)**: `NCBITaxon:155900` (`uncultured organism`), `NCBITaxon:408170` (`human gut metagenome`), `NCBITaxon:32644` (`unidentified`).

## 3. Consolidated Findings & Dispositions (`2` Resolved, `7` Carried Forward to Cycle 2 Stage 5)

| `finding_id` | Issue | Category | Severity | Status | Summary & Stage 5 / Stage 6 Disposition |
| --- | --- | --- | --- | --- | --- |
| `causal-node-type-enum-and-mech-family-nav-drift` | [#76](https://github.com/CultureBotAI/TaxonMech/issues/76) | `schema` | `minor` | `resolved` | Resolved in Cycle 1 Stage 5 (`#151`) and verified intact at `82a3ece85614bc6b975f7ed01850aa4f57207d71`. |
| `validate-history-bare-linkml-validate-path` | [#83](https://github.com/CultureBotAI/TaxonMech/issues/83) | `provenance` | `minor` | `resolved` | Resolved in Cycle 1 Stage 5 (`#151`) and verified across all 23 history records at `82a3ece85614bc6b975f7ed01850aa4f57207d71`. |
| `gtdb-closematch-exact-promotion` | [#124](https://github.com/CultureBotAI/TaxonMech/issues/124) | `grounding` | `major` | `open` | `95,766` records carry `needs_curation` from `skos:closeMatch` GTDB promotion (`src/taxonmech/seed.py` lines 508–535; `#124`, `#63`). Carry forward to Stage 5. |
| `gtdb-polyphyly-suffix-synonym-mangling` | [#65](https://github.com/CultureBotAI/TaxonMech/issues/65) | `nomenclature` | `major` | `open` | `src/taxonmech/seed.py` line 529 mangles 15,704 GTDB polyphyly suffixes into fake trinomials (`#65`). Carry forward to Stage 5. |
| `gtdb-pooled-broadmatch-attestation-and-note` | [#118](https://github.com/CultureBotAI/TaxonMech/issues/118) | `evidence` | `major` | `open` | 6,335 pooled-only GTDB records report largest pooled cluster's genome count (`seed.py` lines 636–650; `#118`) and 8,587 pooled records invert the `broadMatch` direction note (`seed.py` lines 522–524; `#119`). Carry forward to Stage 5. |
| `curation-history-stale-scope-strain-count` | [#69](https://github.com/CultureBotAI/TaxonMech/issues/69) | `provenance` | `minor` | `open` | `SEEDED_FROM_SOURCES` `curation_history` (`seed.py` lines 691–702) embeds static `curation/seed_scope.tsv` strain count (`1861` vs `1975` on `NCBITaxon:562`; `#69`). Carry forward to Stage 5. |
| `upstream-edge-multiplicity-and-subtree-count-scope` | [#8](https://github.com/CultureBotAI/TaxonMech/issues/8) | `completeness` | `minor` | `open` | `27,118` `pass_with_limitations` and `30` `blocked` records reflect uncommitted upstream `kg-microbe` raw edge tables and direct-only non-BacDive counts (`#8`; `taxonmech-infra-0004`). Carry forward to Stage 5 / Stage 6. |
| `mechanism-and-protein-representation-prerequisites` | [#78](https://github.com/CultureBotAI/TaxonMech/issues/78) | `completeness` | `major` | `open` | `15` records now carry `causal_graphs` (83 edges, 28 `UniProtKB` `GENE_OR_PROTEIN` nodes), while `626,033` records await bulk `kg-microbe` trait-edge extraction (`taxonmech-infra-0002`) and a pinned `data/raw/` UniProtKB snapshot + offline validator (`taxonmech-infra-0003`; `#78`). Carry forward to Stage 5 / Stage 6. |
| `structured-inventory-verify-target-sha256-post-curation-drift` | [#78](https://github.com/CultureBotAI/TaxonMech/issues/78) | `provenance` | `major` | `open` | `scripts/corpus_review_inventory.py --check --verify-target-sha256` exits `1` on the 10 structured-shard records curated in Cycle 2 Stages 2–3 (`part-02,05,08,12,13`) and on historical append-only review bundles. Carry forward to Stage 5 for direct remediation. |
