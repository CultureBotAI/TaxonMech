# YAML Record Review: Rhodococcus sp. 1.3-VEs

## Target

- File: `data/taxa/bacteria/rhodococcus_sp_1_3_ves.yaml`
- Identifier: `NCBITaxon:1000016`
- PATHS.tsv row: 21
- Label: `Rhodococcus sp. 1.3-VEs`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:192944` (`unclassified Rhodococcus (in: high G+C Gram-positive bacteria)`)

## Validation

- `just validate data/taxa/bacteria/rhodococcus_sp_1_3_ves.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/pseudomonas_sp_5t_vpa.yaml data/taxa/bacteria/pseudomonas_sp_6s_vpa.yaml data/taxa/bacteria/rhodococcus_sp_1_15_ves.yaml data/taxa/bacteria/rhodococcus_sp_1_3_ves.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species-level placeholder under the no-rank NCBI `unclassified Rhodococcus (in: high G+C Gram-positive bacteria)` node.
- `data/raw/ncbitaxon_taxa.tsv` line 208817 pins `NCBITaxon:1000016` to label `Rhodococcus sp. 1.3-VEs`, rank `SPECIES`, parent `NCBITaxon:192944`, genetic code 11, source set `ncbitaxon`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the record under `unclassified Rhodococcus (in: high G+C Gram-positive bacteria)`, `Rhodococcus`, Nocardiaceae, Mycobacteriales, Actinomycetes, Actinomycetota, Bacillati, and Bacteria, matching the YAML lineage.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `rhodococcus_sp_1_3_ves`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 309931 keeps this taxon in scope as `attested rule: Rhodococcus sp. 1.3-VEs, 1 sources incl. NCBI`.
- A gitignore-independent `rg --no-ignore --hidden` scan of `data/raw`, `data/atb`, and `data/straininfo` found only the NCBI taxonomy row for `NCBITaxon:1000016`.

## Completeness

- The sole NCBITAXON source attestation is represented with one `NAME` assertion and the pinned NCBI snapshot date.
- The record has no GTDB or LPSN cross-reference in the local source inventories, and the YAML correspondingly has no `taxonomy_mappings`, `nomenclature`, or `xrefs` block.
- `strain_count: 0` is consistent with the lack of direct BacDive, GOLD, AllTheBacteria, or StrainInfo rows for this NCBI taxon in the local source inventories.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
