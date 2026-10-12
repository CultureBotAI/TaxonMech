# YAML Record Review: Herbaspirillum sp. BA134

## Target

- File: `data/taxa/bacteria/herbaspirillum_sp_ba134.yaml`
- Identifier: `NCBITaxon:100004`
- PATHS.tsv row: 47
- Label: `Herbaspirillum sp. BA134`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:2624150` (`unclassified Herbaspirillum`)

## Validation

- `just validate data/taxa/bacteria/herbaspirillum_sp_ba134.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/sphingomonas_sp_09wsh1_7.yaml data/taxa/bacteria/herbaspirillum_sp_ba134.yaml data/taxa/bacteria/sphingomonas_sp_09wsh1_8.yaml data/taxa/bacteria/sphingomonas_sp_09wsh1_9.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species-level placeholder under the no-rank NCBI `unclassified Herbaspirillum` node.
- `data/raw/ncbitaxon_taxa.tsv` line 17108 pins `NCBITaxon:100004` to label `Herbaspirillum sp. BA134`, rank `SPECIES`, parent `NCBITaxon:2624150`, genetic code 11, exact synonym `Herbispirillum sp. BA134`, source set `ncbitaxon`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the record under `unclassified Herbaspirillum`, `Herbaspirillum`, Oxalobacteraceae, Burkholderiales, Betaproteobacteria, Pseudomonadota, Pseudomonadati, and Bacteria, matching the YAML lineage.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `herbaspirillum_sp_ba134`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 142937 keeps this taxon in scope as `attested rule: Herbaspirillum sp. BA134, 1 sources incl. NCBI`.
- A gitignore-independent `rg --no-ignore --hidden` scan of `data/raw`, `data/atb`, and `data/straininfo` found only the NCBI taxonomy row for `NCBITaxon:100004`.

## Completeness

- The sole NCBITAXON source attestation is represented with one `NAME` assertion and the pinned NCBI snapshot date.
- The NCBITAXON synonym `Herbispirillum sp. BA134` is represented as one `EXACT_SYNONYM` sourced to `NCBITaxon`.
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
