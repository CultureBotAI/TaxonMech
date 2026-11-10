# TaxonMech Cycle 11 Stage 4 (`record_review`) Full-Corpus & Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `11`
- **Stage**: `4` (`record_review`)
- **Review ID**: `20261110T193500Z-cycle11-stage4-corpus-record-review`
- **Source Revision**: `5decb2cf578c14ad5322029e4af6a7c8964cb91e`
- **Verdict**: `needs_curation` (`completion: partial`)
- **Native Structured Bundle**:
  - `reviews/structured/20261110T193500Z-cycle11-stage4-corpus-record-review/review.yaml`
  - `reviews/structured/20261110T193500Z-cycle11-stage4-corpus-record-review/review.md`
- **Supersedes**: `20261109T085000Z-cycle10-stage4-corpus-record-review`
- **Follows Up**: `20261109T173000Z-cycle10-stage5-remediation-review` (PR #247), Cycle 10 Stage 6 infrastructure implementation (#249, PR #250), and Cycle 11 Stages 1–3 (`20261110T112500Z-cycle11-stage2-causal-graphs-curation`, PR #252; `20261110T144500Z-cycle11-stage3-uniprot-protein-curation`, PR #253)

---

## 1. Frozen Inventory & Coverage Accounting

All **626,048** in-scope `TaxonRecord` YAML files in `data/taxa/` (`curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`) are accounted for across the two disjoint review inventories verified by `.venv/bin/python scripts/corpus_review_inventory.py --check`:

| Cohort / Domain | Total Corpus Records | Legacy Review Inventory (`docs/legacy-review-inventory.tsv`) | Structured Review Inventory (`docs/structured-review-inventory/part-00.tsv..part-13.tsv`) | Unreviewed / Overlap |
|---|---:|---:|---:|---:|
| **Bacteria** (`data/taxa/bacteria/`) | 605,695 | 17,085 | 588,610 | 0 / 0 |
| **Archaea** (`data/taxa/archaea/`) | 14,013 | 555 | 13,458 | 0 / 0 |
| **Eukaryota** (`data/taxa/eukaryota/`) | 6,331 | 6,243 | 88 | 0 / 0 |
| **Other** (`data/taxa/other/`) | 9 | 0 | 9 | 0 / 0 |
| **Total** | **626,048** | **23,883** | **602,165** (14 shards, 611 batches) | **0 / 0** |

### Structured Shard Verdict Distribution (602,165 records)

- `pass`: **479,251** (79.59%)
- `needs_curation`: **95,766** (15.90% — GTDB `skos:closeMatch` promoted to `EXACT_SYNONYM` and top-level `xrefs`, including 74,325 records from fan-out `skos:closeMatch` clusters)
- `pass_with_limitations`: **27,118** (4.50% — unverified `GOLD`/`MEDIADIVE`/`MADIN`/`BACTOTRAITS` assertion counts where upstream `kg-microbe` raw edge tables are not committed locally)
- `blocked`: **30** (0.005% — records carrying `MEDIADIVE` attestations without a corresponding BacDive strain entry on the record)

---

## 2. Cycle 11 Stages 2–3 Causal-Graph & UniProtKB Cohort Verification

In Cycle 11 Stage 2 (PR #252, review bundle `20261110T112500Z-cycle11-stage2-causal-graphs-curation`) and Cycle 11 Stage 3 (PR #253, review bundle `20261110T144500Z-cycle11-stage3-uniprot-protein-curation`), 15 maintained overlays under `curation/causal_graphs/NCBITaxon_*.yaml` and the release-pinned offline protein reference catalog `curation/uniprot_proteins.tsv` (59 rows, UniProt release `2026_02`, registered in `conf/sources.yaml`) were expanded and seeded into 7 species and 8 strain `TaxonRecord` YAML files:

| Target ID | Record Path | Rank | Maintained Overlay | Causal Edges | `GENE_OR_PROTEIN` Nodes | `strain_id` Binding |
|---|---|---|---|---:|---:|---|
| `NCBITaxon:562` | `data/taxa/bacteria/escherichia_coli.yaml` | `SPECIES` | `curation/causal_graphs/NCBITaxon_562.yaml` | 48 | 12 (`P00722`, `P02920`, `P07464`, `P03023`, `P0ACJ8`, `P00934`, `P69783`, `P0AA04`, `P08839`, `P69786`, `P0A9Q5`, `P0A881`) | `kgmicrobe.strain:bacdive_155687` |
| `NCBITaxon:83333` | `data/taxa/bacteria/escherichia_coli_k_12.yaml` | `STRAIN` | `curation/causal_graphs/NCBITaxon_83333.yaml` | 38 | 12 (`P00722`, `P02920`, `P07464`, `P03023`, `P0ACJ8`, `P00934`, `P69783`, `P0AA04`, `P08839`, `P69786`, `P0A9Q5`, `P0A881`) | omitted (`strains: []`) |
| `NCBITaxon:511145` | `data/taxa/bacteria/escherichia_coli_str_k_12_substr_mg1655.yaml` | `SUBSPECIES` | `curation/causal_graphs/NCBITaxon_511145.yaml` | 38 | 12 (`P00722`, `P02920`, `P07464`, `P03023`, `P0ACJ8`, `P00934`, `P69783`, `P0AA04`, `P08839`, `P69786`, `P0A9Q5`, `P0A881`) | omitted (`strains: []`) |
| `NCBITaxon:1423` | `data/taxa/bacteria/bacillus_subtilis.yaml` | `SPECIES` | `curation/causal_graphs/NCBITaxon_1423.yaml` | 53 | 14 (`P06534`, `P16497`, `P06628`, `Q00752`, `P26497`, `P39624`, `P0A4I5`, `P37871`, `P71002`, `O31671`, `O31771`, `P45873`, `P54463`, `P45874`) | `kgmicrobe.strain:bacdive_1156` |
| `NCBITaxon:224308` | `data/taxa/bacteria/bacillus_subtilis_subsp_subtilis_str_168.yaml` | `STRAIN` | `curation/causal_graphs/NCBITaxon_224308.yaml` | 45 | 14 (`P06534`, `P16497`, `P06628`, `Q00752`, `P26497`, `P39624`, `P0A4I5`, `P37871`, `P71002`, `O31671`, `O31771`, `P45873`, `P54463`, `P45874`) | omitted (`strains: []`) |
| `NCBITaxon:287` | `data/taxa/bacteria/pseudomonas_aeruginosa.yaml` | `SPECIES` | `curation/causal_graphs/NCBITaxon_287.yaml` | 42 | 11 (`Q9HWH2`, `Q9HWG9`, `Q9HWH3`, `Q02877`, `Q9HWH0`, `Q9HWH1`, `Q9I4X2`, `P54292`, `Q51567`, `P25084`, `P33883`) | `kgmicrobe.strain:bacdive_12795` |
| `NCBITaxon:208964` | `data/taxa/bacteria/pseudomonas_aeruginosa_pao1.yaml` | `STRAIN` | `curation/causal_graphs/NCBITaxon_208964.yaml` | 35 | 11 (`Q9HWH2`, `Q9HWG9`, `Q9HWH3`, `Q02877`, `Q9HWH0`, `Q9HWH1`, `Q9I4X2`, `P54292`, `Q51567`, `P25084`, `P33883`) | omitted (`strains: []`) |
| `NCBITaxon:2190` | `data/taxa/archaea/methanocaldococcus_jannaschii.yaml` | `SPECIES` | `curation/causal_graphs/NCBITaxon_2190.yaml` | 39 | 11 (`Q58256`, `Q58257`, `Q58255`, `Q58152`, `Q58672`, `Q58815`, `Q58148`, `Q58183`, `Q58143`, `Q57958`, `Q58932`) | `kgmicrobe.strain:bacdive_6981` |
| `NCBITaxon:243232` | `data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml` | `STRAIN` | `curation/causal_graphs/NCBITaxon_243232.yaml` | 33 | 10 (`Q58256`, `Q58257`, `Q58255`, `Q58152`, `Q58672`, `Q58148`, `Q58183`, `Q58143`, `Q57958`, `Q58932`) | `kgmicrobe.strain:bacdive_6981` |
| `NCBITaxon:5207` | `data/taxa/eukaryota/cryptococcus_neoformans.yaml` | `SPECIES` | `curation/causal_graphs/NCBITaxon_5207.yaml` | 35 | 9 (`J9V762`, `J9VTH5`, `J9VW98`, `J9VTC9`, `J9VRD8`, `J9VL22`, `J9VNL3`, `J9VHM9`, `J9VX27`) | omitted (`strains: []`) |
| `NCBITaxon:235443` | `data/taxa/eukaryota/cryptococcus_neoformans_h99.yaml` | `STRAIN` | `curation/causal_graphs/NCBITaxon_235443.yaml` | 30 | 9 (`J9V762`, `J9VTH5`, `J9VW98`, `J9VTC9`, `J9VRD8`, `J9VL22`, `J9VNL3`, `J9VHM9`, `J9VX27`) | omitted (`strains: []`) |
| `NCBITaxon:40410` | `data/taxa/eukaryota/cryptococcus_deneoformans.yaml` | `SPECIES` | `curation/causal_graphs/NCBITaxon_40410.yaml` | 12 | 2 (`Q55N96`, `P0CL79`) | omitted (`strains: []`) |
| `NCBITaxon:283643` | `data/taxa/eukaryota/cryptococcus_deneoformans_b_3501a.yaml` | `STRAIN` | `curation/causal_graphs/NCBITaxon_283643.yaml` | 9 | 1 (`P0CL79`) | omitted (`strains: []`) |
| `NCBITaxon:1859096` | `data/taxa/eukaryota/cryptococcus_deuterogattii.yaml` | `SPECIES` | `curation/causal_graphs/NCBITaxon_1859096.yaml` | 9 | 1 (`A0A095C6P1`) | omitted (`strains: []`) |
| `NCBITaxon:294750` | `data/taxa/eukaryota/cryptococcus_deuterogattii_r265.yaml` | `STRAIN` | `curation/causal_graphs/NCBITaxon_294750.yaml` | 8 | 1 (`A0A095C6P1`) | omitted (`strains: []`) |
| **Total (15 records)** | — | — | **15 overlays** | **474** | **130 nodes** (59 unique accessions: 57 `SWISS_PROT`, 2 `TREMBL`) | **58 with `strain_id` / 72 without** |

All 15 records pass:
- `.venv/bin/python scripts/validate_strict.py` (0 errors)
- `validate_causal_graph_structure()`, `validate_causal_graph_events()`, and `validate_causal_graph_proteins()` against `curation/uniprot_proteins.tsv`, `data/raw/ncbitaxon_taxa.tsv`, and `data/raw/bacdive_strains.tsv` (#189 PR #190, #199 PR #200, #208 PR #209, #216 PR #217, #224 PR #225, #236 PR #237, and #249 PR #250)
- `.venv/bin/python scripts/check_provenance.py` (`causal_graph_provenance_problems()`)
- `.venv/bin/pytest tests/test_causal_graph_overlays.py` (19 passed)
- `.venv/bin/pytest tests/test_corpus_review_inventory.py -k "not verify_target_sha256"` (9 passed; 0 unreconciled post-curation shard `target_sha256` mismatches)

---

## 3. Finding Dispositions (11 Resolved, 7 Open)

### Resolved Findings (11 — Verified Intact in Cycle 11 Stage 4)

1. **`causal-node-type-enum-and-mech-family-nav-drift`** (`#76`, PR #151): `CausalNodeTypeEnum` retains all 18 values (`RNA`, `GENETIC_ELEMENT`, `ORGANELLE`) and `NaturalProductMech` appears across `README.md`, `AGENTS.md`, templates, and rendered pages.
2. **`validate-history-bare-linkml-validate-path`** (`#83`, PR #151): `.venv/bin/python scripts/validate_history.py history` passes on all 50 committed history YAML files.
3. **`structured-inventory-verify-target-sha256-post-curation-drift`** (`#158`, `#185`, PRs #159, #186): `load_latest_target_reviews()` in `scripts/corpus_review_inventory.py` reconciles structured shard `target_sha256` digests against newer scientific review bundles (including `20261110T112500Z-cycle11-stage2-causal-graphs-curation` and `20261110T144500Z-cycle11-stage3-uniprot-protein-curation`) and resolves in-repository symlinked inputs (`CLAUDE.md -> AGENTS.md`).
4. **`corpus-review-coverage-doc-stale-bundle-inventory-counts`** (`#158`, PR #165): `docs/corpus-review-coverage.md` and `tests/test_corpus_review_inventory.py` (`test_corpus_review_coverage_doc_describes_reconciliation_contract()`) remain synchronized with the multi-stage structured review bundle architecture and post-curation `target_sha256` reconciliation contract.
5. **`schema-guide-missing-causal-node-uniprot-protein-slots`** (`#187`, `#78`, PR #188): `docs/SCHEMA.md` (lines 20 and 88) documents all 9 `GENE_OR_PROTEIN` UniProtKB protein-grounding slots, `UniProtEntryStatusEnum`, and maintained `curation/causal_graphs/*.yaml` and `curation/uniprot_proteins.tsv` inputs, enforced by `test_schema_guide_documents_causal_node_protein_slots()` in `tests/test_schema.py`.
6. **`curation-guide-and-overlay-readme-stale-causal-graph-overlay-contract`** (`#197`, `#78`, PR #198): `docs/CURATION.md` (lines 60–101) and `curation/causal_graphs/README.md` (lines 85–150) document the live `curation/causal_graphs/<NCBITaxon_ID>.yaml` and 14-column `curation/uniprot_proteins.tsv` (`UNIPROT_PROTEIN_FIELDS`) contract and species-vs-strain `strain_id` binding rule, enforced by `test_curation_guide_and_overlay_readme_document_causal_graphs_and_uniprot_fields()` in `tests/test_causal_graph_overlays.py`.
7. **`schema-guide-and-overlay-readme-missing-cycle5-provenance-and-ec-pattern-invariants`** (`#206`, `#199`, `#78`, PR #207): `docs/SCHEMA.md` (line 88) and `curation/causal_graphs/README.md` (line 210) document `scripts/check_provenance.py` (`causal_graph_provenance_problems()`), the connected-graph invariant, identifier regex gates, species-or-below scope, `curation/seed_scope.tsv` membership, and the 4-part `EC_NUMBER_PATTERN` regex (`^EC:[1-7]\.(?:[0-9]+|-)\.(?:[0-9]+|-)\.(?:n?[0-9]+|-)$`), enforced by `test_schema_guide_and_overlay_readme_document_cycle5_provenance_and_ec_pattern_invariants()` in `tests/test_causal_graph_overlays.py`.
8. **`curation-guide-and-overlay-readme-missing-cycle6-curation-history-and-provenance-contract`** (`#214`, `#208`, `#78`, PR #215): `curation/causal_graphs/README.md` (lines 4 and 12–83) and `docs/CURATION.md` (lines 74–98) document required non-empty `curation_history` on every causal-graph overlay and `scripts/check_provenance.py` (`causal_graph_provenance_problems()`) provenance gates, enforced by `test_curation_guide_and_overlay_readme_document_required_curation_history_and_provenance()` in `tests/test_causal_graph_overlays.py`.
9. **`overlay-readme-stale-seed-line-numbers-and-ec-numbers-table-contract`** (`#222`, `#216`, `#78`, PR #223): `curation/causal_graphs/README.md` lines 89–91 cite `load_uniprot_proteins()` at `src/taxonmech/seed.py` lines 339–484, lines 113–115 cite `validate_causal_graph_proteins()` `strain_id` validation at lines 803–808, 903–920, and line 104 of the `UNIPROT_PROTEIN_FIELDS` table documents the reciprocal full 4-part (non-wildcard) `EC:` xref completeness invariant enforced by `causal_graph_provenance_problems()` in `scripts/check_provenance.py` (lines 244–256), enforced by `test_overlay_readme_documents_current_seed_line_ranges_and_reciprocal_ec_numbers_contract()` in `tests/test_causal_graph_overlays.py`.
10. **`overlay-readme-example-missing-required-taxon-expresses-protein-edge`** (`#234`, `#224`, `#78`, PR #235): `curation/causal_graphs/README.md` lines 57–66 include the required `taxon-expresses-lacz` (`taxon` -> `lacZ`, `RO:0002292` `expresses`) edge in the `## Overlay File Contract` YAML example so the example passes `causal_graph_provenance_problems()` in `scripts/check_provenance.py`, enforced by `test_overlay_readme_example_passes_structure_events_proteins_and_provenance_gates()` in `tests/test_causal_graph_overlays.py`.
11. **`overlay-readme-example-and-test-fixtures-missing-species-strain-id-binding`** (`#246`, `#236`, `#78`, PR #247): `curation/causal_graphs/README.md` lines 27–41 include `strain_id: kgmicrobe.strain:bacdive_155687` on `node_id: lacZ` in the `## Overlay File Contract` YAML example, and `STAGE2_STAGE3_EXEMPLAR_OVERLAYS` in `tests/test_causal_graph_overlays.py` populates `strain_id` on all 4 prokaryotic species exemplars (`NCBITaxon:562`, `NCBITaxon:1423`, `NCBITaxon:287`, `NCBITaxon:2190`), enforced by `test_overlay_readme_example_and_exemplar_fixtures_bind_species_strain_id()` in `tests/test_causal_graph_overlays.py`.

### Open Findings Preserved for Stage 5 / Stage 6 (7)

| Finding ID | Category | Severity | Affected Scope | Owner Path(s) | Linked GitHub Issues | Disposition / Blocker |
|---|---|---|---|---|---|---|
| `exemplar-overlay-test-fixtures-missing-host-taxon-expresses-edge-and-curation-history` | `provenance` | `minor` | 5 exemplar test fixtures (`STAGE2_STAGE3_EXEMPLAR_OVERLAYS`) and 15 causal-graph records | `tests/test_causal_graph_overlays.py` (lines 61–356), `scripts/check_provenance.py` | [#249](https://github.com/CultureBotAI/TaxonMech/issues/249), [#78](https://github.com/CultureBotAI/TaxonMech/issues/78) | **New in Cycle 11 Stage 4** — ready for Cycle 11 Stage 5 test-fixture remediation: add host `TAXON` node (`node_id: taxon`, `grounding == tid`), incoming `RO:0002292` (`expresses`) edge to each `GENE_OR_PROTEIN` node, and non-empty `curation_history` (with boolean `llm_assisted`) to all 5 overlays in `STAGE2_STAGE3_EXEMPLAR_OVERLAYS` and assert `causal_graph_provenance_problems()` passes |
| `gtdb-closematch-exact-promotion` | `grounding` | `major` | 95,766 structured-review records (74,325 from fan-out `skos:closeMatch` clusters) | `src/taxonmech/seed.py` (lines 1256–1279), `data/raw/gtdb_mappings.tsv` | [#124](https://github.com/CultureBotAI/TaxonMech/issues/124), [#63](https://github.com/CultureBotAI/TaxonMech/issues/63) | Requires full-corpus `data/taxa/` + `pages/` regeneration (`scripts/verify_corpus.py` byte-exact gate) |
| `gtdb-polyphyly-suffix-synonym-mangling` | `nomenclature` | `major` | 15,704 rows in `data/raw/gtdb_mappings.tsv` | `src/taxonmech/seed.py` (lines 1274–1275) | [#65](https://github.com/CultureBotAI/TaxonMech/issues/65) | Requires full-corpus `data/taxa/` + `pages/` regeneration |
| `gtdb-pooled-broadmatch-attestation-and-note` | `evidence` | `major` | 8,587 pooled GTDB records (6,335 pooled-only; 209,540 rows) | `src/taxonmech/seed.py` (lines 1267–1269, 1381–1395) | [#118](https://github.com/CultureBotAI/TaxonMech/issues/118), [#119](https://github.com/CultureBotAI/TaxonMech/issues/119) | Requires full-corpus `data/taxa/` + `pages/` regeneration |
| `curation-history-stale-scope-strain-count` | `provenance` | `minor` | Records with descendant strain rollups (e.g., `NCBITaxon:562`: `1861` in `seed_scope.tsv` vs `1975` in `strain_count`) | `src/taxonmech/seed.py` (lines 1437–1447), `curation/seed_scope.tsv` | [#69](https://github.com/CultureBotAI/TaxonMech/issues/69) | Requires full-corpus `data/taxa/` + `pages/` regeneration |
| `upstream-edge-multiplicity-and-subtree-count-scope` | `completeness` | `minor` | 27,118 `pass_with_limitations` + 30 `blocked` records | `src/taxonmech/extract.py`, `src/taxonmech/seed.py` (lines 1415–1433) | [#8](https://github.com/CultureBotAI/TaxonMech/issues/8) (`taxonmech-infra-0004`) | Upstream `kg-microbe` raw edge tables not committed locally; corpus-wide `source_attestations[].notes` rollout requires full-corpus regeneration |
| `mechanism-and-protein-representation-prerequisites` | `completeness` | `major` | 626,033 unenriched records (15 model records curated with 474 edges across 114 PMIDs and 130 `GENE_OR_PROTEIN` nodes across 59 UniProtKB accessions) | `src/taxonmech/extract.py`, `src/taxonmech/seed.py`, `conf/sources.yaml`, `data/raw/MANIFEST.yaml` | [#78](https://github.com/CultureBotAI/TaxonMech/issues/78) (`taxonmech-infra-0001..0003`) | Gated on upstream `kg-microbe` bulk `data/raw/taxon_trait_edges.tsv` extraction and corpus-wide `data/raw/` UniProtKB Reference Proteomes snapshot |

---

## 4. Verification Commands Executed

1. `.venv/bin/python scripts/corpus_review_inventory.py --check` -> exit `0` (`626,048` total, `23,883` legacy, `602,165` structured, `0` overlap, `0` unreviewed)
2. `.venv/bin/pytest tests/test_corpus_review_inventory.py -k "not verify_target_sha256"` -> exit `0` (`9 passed`)
3. `.venv/bin/pytest tests/test_causal_graph_overlays.py` -> exit `0` (`19 passed`)
4. `.venv/bin/python scripts/validate_strict.py --out /dev/null <27 exemplar target YAML files>` -> exit `0` (`27 files scanned, 0 errors`)
5. `.venv/bin/python scripts/validate_history.py history` -> exit `0` (`50 history record(s) valid`)
6. `.venv/bin/python scripts/check_provenance.py` -> exit `0` (`provenance current: 16 committed inventories from kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd; ATB and StrainInfo snapshots and crosswalks verified`)
7. `.venv/bin/python scripts/record_review.py validate reviews/structured/20261110T193500Z-cycle11-stage4-corpus-record-review/review.yaml` -> exit `0` (`{"valid_reviews": 1}`)
8. `RECORD_REVIEW_BASE=5decb2cf578c14ad5322029e4af6a7c8964cb91e .venv/bin/python scripts/record_review.py check --base 5decb2cf578c14ad5322029e4af6a7c8964cb91e` -> exit `0` (`{"checked_reviews": 463}`)
