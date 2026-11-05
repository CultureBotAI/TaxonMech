# Stage 4 (`record_review`) Full-Corpus Review Report — TaxonMech (`mech-goal-sequence-20261019`, Cycle 6)

- **Repository**: `CultureBotAI/TaxonMech`
- **Source Revision**: `448a467bd52474c7597d318d135d040f9b9a54d8`
- **Previous Workflow Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-05/revision-0001/evidence.yaml` (`SHA256: e3ece75c55ce377f8013a63c46ea48362d88b37f4a6d8cd70a1655151457410c`)
- **Native Structured Review Bundle**: `reviews/structured/20261105T042500Z-cycle6-stage4-corpus-record-review/review.yaml` (`SHA256: 674779ade77420228644f8c27a9318e3a85d71452f78c5624c89e6d749282a25`)
- **Native Rendered Report**: `reviews/structured/20261105T042500Z-cycle6-stage4-corpus-record-review/review.md` (`SHA256: 1e939dd8a03543edf6e2ad437c2eca0051e48c113b9f450cb2ee8ac06dfb944b`)
- **Infrastructure Tasks Notebook**: `INFRA_TASKS.md` (`SHA256: ecb7de0cd54fb576b2a5bbe72e733ebe1bbcb3a1c1789f8385294909feab760a`; tracked tasks: `taxonmech-infra-0001..0004`)
- **Skills Executed**: `.claude/skills/review-yaml-record/SKILL.md`, `.claude/skills/review-yaml-category/SKILL.md`
- **Rubric**: `.claude/skills/curate-yaml-record/references/review-checklist.md`

> **Parent Workflow Schema Invariant Note**: `kg_microbe_workflows` (`validate-evidence` on Stage 4 `ReviewReport`) requires every path in `evidence.yaml:artifacts` to reside under `reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-04/revision-0001/`, requires `previous_evidence` to reference Cycle 5 Stage 5 (`reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-05/revision-0001/evidence.yaml`), and requires `evidence.yaml:infra_tasks` and `evidence.yaml:groups` to be `[]` on Stage 4 evidence manifests. The repository-root native review bundle (`reviews/structured/20261105T042500Z-cycle6-stage4-corpus-record-review/review.yaml`, `reviews/structured/20261105T042500Z-cycle6-stage4-corpus-record-review/review.md`) and `INFRA_TASKS.md` (`taxonmech-infra-0001..0004`) are therefore cross-referenced with exact SHA-256 digests in `corpus_coverage_summary.json`, `review_findings.yaml`, and this report.

## 1. Frozen Corpus Coverage & Post-Curation SHA-256 Inventory Audit

`.venv/bin/python scripts/corpus_review_inventory.py --check` and `.venv/bin/pytest tests/test_corpus_review_inventory.py -k "not verify_target_sha256"` (`9 passed`) verified **100.0% coverage** and **post-curation target SHA-256 reconciliation** across all **626,048** in-scope `TaxonRecord` YAML files in `data/taxa/` (`data/taxa/PATHS.tsv` and `curation/seed_scope.tsv`) following Cycle 5 Stages 5–6 (`#198`, `#200`) and Cycle 6 Stages 2–3 (`#203`, `#204`):

| Metric | Count | Notes |
| --- | ---: | --- |
| Total in-scope `TaxonRecord` files | `626,048` | `Bacteria: 605,695`, `Archaea: 14,013`, `Eukaryota: 6,331`, `other: 9` |
| Legacy-reviewed records (`docs/legacy-review-inventory.tsv`) | `23,883` | `Archaea: 555`, `Bacteria: 17,085`, `Eukaryota: 6,243`, `Other: 0` (including 5 causal-graph records: `NCBITaxon:5207`, `235443`, `40410`, `283643`, `294750`) |
| Structured-reviewed records (`docs/structured-review-inventory/part-00.tsv`..`part-13.tsv`) | `602,165` | `611` batches in `docs/structured-review-batches.tsv` (`Archaea: 13,458`, `Bacteria: 588,610`, `Eukaryota: 88`, `other: 9`) |
| Unreviewed records | `0` | Verified against `data/taxa/PATHS.tsv` |
| Overlapping records between legacy and structured inventories | `0` | Disjoint partition |
| Unchanged records matching original inventory SHA-256 | `626,033` | Exact byte parity with Cycle 1 Stage 4 |
| Records updated by Cycle 2–6 Stages 2–3 `causal_graphs` + UniProtKB overlays | `15` | All 15 re-reviewed and hash-bound in `20261104T185500Z-cycle6-stage2-causal-graphs-curation`, `20261105T015451Z-cycle6-stage3-protein-examples`, and this Stage 4 bundle (`0` unreconciled mismatches) |

### Structured Review Verdict Distribution (`602,165` records across `part-00.tsv`..`part-13.tsv`)

| Verdict | Record Count | Share | Primary Driver |
| --- | ---: | ---: | --- |
| `pass` | `479,251` | `79.59%` | Clean NCBI/BacDive/GTDB/LPSN/StrainInfo/ATB alignment |
| `needs_curation` | `95,766` | `15.90%` | `skos:closeMatch` GTDB species-cluster promotion to `EXACT_SYNONYM` and `xrefs` (`#124`, `#63`) |
| `pass_with_limitations` | `27,118` | `4.50%` | Uncommitted upstream `kg-microbe` raw edge tables for `GOLD`/`MEDIADIVE`/`MADIN`/`BACTOTRAITS` (`#8`) |
| `blocked` | `30` | `0.005%` | Multi-source attestation count verification blocked on uncommitted upstream raw edge tables (`#8`) |

## 2. Directly Bound Exemplar & Causal-Graph Records (`27` targets across all 4 domains)

The native bundle `reviews/structured/20261105T042500Z-cycle6-stage4-corpus-record-review/review.yaml` binds `27` representative `TaxonRecord` files (`role: target`) spanning `Bacteria` (13), `Archaea` (3), `Eukaryota` (8), and `other` (3), including all `15` records enriched with `causal_graphs` (`246` edges across `48` `PMID`s) and live-verified + offline-validated `UniProtKB` `GENE_OR_PROTEIN` nodes (`75` nodes across `34` unique accessions—`32` `SWISS_PROT` and `2` `TREMBL`—in `curation/uniprot_proteins.tsv`):
- **Bacteria (`13`)**: `NCBITaxon:562` (`Escherichia coli`), `NCBITaxon:83333` (`Escherichia coli K-12`), `NCBITaxon:511145` (`Escherichia coli str. K-12 substr. MG1655`), `NCBITaxon:1423` (`Bacillus subtilis`), `NCBITaxon:224308` (`Bacillus subtilis subsp. subtilis str. 168`), `NCBITaxon:287` (`Pseudomonas aeruginosa`), `NCBITaxon:208964` (`Pseudomonas aeruginosa PAO1`), `NCBITaxon:2940590` (`Achromobacter sp. JUb104`), `NCBITaxon:3121604` (`Acidaminobacteraceae bacterium`), `NCBITaxon:1435036` (`Acinetobacter bohemicus`), `NCBITaxon:209650` (`Acidicaldus organivorans`), `NCBITaxon:206` (`Campylobacter sputorum`), `NCBITaxon:33952` (`Acetobacterium woodii`).
- **Archaea (`3`)**: `NCBITaxon:2190` (`Methanocaldococcus jannaschii`), `NCBITaxon:243232` (`Methanocaldococcus jannaschii DSM 2661`), `NCBITaxon:2287` (`Saccharolobus solfataricus`).
- **Eukaryota (`8`)**: `NCBITaxon:4932` (`Saccharomyces cerevisiae`), `NCBITaxon:5207` (`Cryptococcus neoformans`), `NCBITaxon:235443` (`Cryptococcus neoformans H99`), `NCBITaxon:40410` (`Cryptococcus deneoformans`), `NCBITaxon:283643` (`Cryptococcus deneoformans B-3501A`), `NCBITaxon:1859096` (`Cryptococcus deuterogattii`), `NCBITaxon:294750` (`Cryptococcus deuterogattii R265`), `NCBITaxon:5755` (`Acanthamoeba castellanii`).
- **Other (`3`)**: `NCBITaxon:155900` (`uncultured organism`), `NCBITaxon:408170` (`human gut metagenome`), `NCBITaxon:32644` (`unidentified`).

## 3. Consolidated Findings & Dispositions (`6` Resolved, `7` Carried Forward to Cycle 6 Stage 5)

| `finding_id` | Issue | Category | Severity | Status | Summary & Stage 5 / Stage 6 Disposition |
| --- | --- | --- | --- | --- | --- |
| `causal-node-type-enum-and-mech-family-nav-drift` | [#76](https://github.com/CultureBotAI/TaxonMech/issues/76) | `schema` | `minor` | `resolved` | Resolved in Cycle 1 Stage 5 (`#151`) and verified intact at `448a467bd52474c7597d318d135d040f9b9a54d8`. |
| `validate-history-bare-linkml-validate-path` | [#83](https://github.com/CultureBotAI/TaxonMech/issues/83) | `provenance` | `minor` | `resolved` | Resolved in Cycle 1 Stage 5 (`#151`) and verified across all 35 history records at `448a467bd52474c7597d318d135d040f9b9a54d8`. |
| `structured-inventory-verify-target-sha256-post-curation-drift` | [#158](https://github.com/CultureBotAI/TaxonMech/issues/158) | `provenance` | `major` | `resolved` | Resolved in Cycle 2 Stage 5 (`#159`) and verified at `448a467bd52474c7597d318d135d040f9b9a54d8` across all 602,165 structured records including the 10 structured-shard records curated through Cycle 6 Stages 2–3 (`#203`, `#204`). |
| `corpus-review-coverage-doc-stale-bundle-inventory-counts` | [#158](https://github.com/CultureBotAI/TaxonMech/issues/158) | `provenance` | `minor` | `resolved` | Resolved in Cycle 3 Stage 5 (`#165`) and verified at `448a467bd52474c7597d318d135d040f9b9a54d8` (`docs/corpus-review-coverage.md` and `test_corpus_review_coverage_doc_describes_reconciliation_contract()` pass). |
| `schema-guide-missing-causal-node-uniprot-protein-slots` | [#187](https://github.com/CultureBotAI/TaxonMech/issues/187) | `schema` | `minor` | `resolved` | Resolved in Cycle 4 Stage 5 (`#188`) under `#187` (`#78`) and verified at `448a467bd52474c7597d318d135d040f9b9a54d8` (`docs/SCHEMA.md` lines 20 and 88, and `test_schema_guide_documents_causal_node_protein_slots()` in `tests/test_schema.py` pass). |
| `curation-guide-and-overlay-readme-stale-causal-graph-overlay-contract` | [#197](https://github.com/CultureBotAI/TaxonMech/issues/197) | `provenance` | `minor` | `resolved` | Resolved in Cycle 5 Stage 5 (`#198`) under `#197` (`#78`) and verified at `448a467bd52474c7597d318d135d040f9b9a54d8` (`docs/CURATION.md` lines 60–81, `curation/causal_graphs/README.md` lines 54–117, and `test_curation_guide_and_overlay_readme_document_causal_graph_and_uniprot_contract()` in `tests/test_causal_graph_overlays.py` pass). |
| `gtdb-closematch-exact-promotion` | [#124](https://github.com/CultureBotAI/TaxonMech/issues/124) | `grounding` | `major` | `open` | `95,766` records carry `needs_curation` from `skos:closeMatch` GTDB promotion (`src/taxonmech/seed.py` lines 949–984; `#124`, `#63`). Carry forward to Stage 5. |
| `gtdb-polyphyly-suffix-synonym-mangling` | [#65](https://github.com/CultureBotAI/TaxonMech/issues/65) | `nomenclature` | `major` | `open` | `src/taxonmech/seed.py` lines 978–979 mangle 15,704 GTDB polyphyly suffixes into fake trinomials (`#65`). Carry forward to Stage 5. |
| `gtdb-pooled-broadmatch-attestation-and-note` | [#118](https://github.com/CultureBotAI/TaxonMech/issues/118) | `evidence` | `major` | `open` | 6,335 pooled-only GTDB records report largest pooled cluster's genome count (`seed.py` lines 1085–1099; `#118`) and 8,587 pooled records invert the `broadMatch` direction note (`seed.py` lines 971–973; `#119`). Carry forward to Stage 5. |
| `curation-history-stale-scope-strain-count` | [#69](https://github.com/CultureBotAI/TaxonMech/issues/69) | `provenance` | `minor` | `open` | `SEEDED_FROM_SOURCES` `curation_history` (`seed.py` lines 1141–1151) embeds static `curation/seed_scope.tsv` strain count (`1861` vs `1975` on `NCBITaxon:562`; `#69`). Carry forward to Stage 5. |
| `upstream-edge-multiplicity-and-subtree-count-scope` | [#8](https://github.com/CultureBotAI/TaxonMech/issues/8) | `completeness` | `minor` | `open` | `27,118` `pass_with_limitations` and `30` `blocked` records reflect uncommitted upstream `kg-microbe` raw edge tables and direct-only non-BacDive counts (`seed.py` lines 1119–1137; `#8`; `taxonmech-infra-0004`). Carry forward to Stage 5 / Stage 6. |
| `mechanism-and-protein-representation-prerequisites` | [#78](https://github.com/CultureBotAI/TaxonMech/issues/78) | `completeness` | `major` | `open` | `15` records now carry `causal_graphs` (246 edges across 48 PMIDs, 75 `UniProtKB` `GENE_OR_PROTEIN` nodes across 34 unique accessions—32 `SWISS_PROT` and 2 `TREMBL`—in `curation/uniprot_proteins.tsv`), while `626,033` records await bulk `kg-microbe` `data/raw/taxon_trait_edges.tsv` extraction (`taxonmech-infra-0002`) and a corpus-wide `data/raw/` UniProtKB Reference Proteomes snapshot (`taxonmech-infra-0003`; `#78`). Carry forward to Stage 5 / Stage 6. |
| `schema-guide-and-overlay-readme-missing-cycle5-provenance-and-ec-pattern-invariants` | [#199](https://github.com/CultureBotAI/TaxonMech/issues/199) | `schema` | `minor` | `open` | `docs/SCHEMA.md` (line 88) omits `scripts/check_provenance.py` (`causal_graph_provenance_problems()`) and the Cycle 5 Stage 6 (`#199`, PR `#200`) connected-graph, identifier-pattern, species-or-below `organism_taxon_id`, and `seed_scope.tsv` membership invariants, and `curation/causal_graphs/README.md` (line 155) states `EC:<digits>` instead of the 4-part regex `^EC:[1-7]\.(?:[0-9]+|-)\.(?:[0-9]+|-)\.(?:n?[0-9]+|-)$` enforced in `src/taxonmech/seed.py` line 87 (`#199`, `#78`). Carry forward to Stage 5 for direct documentation remediation. |
