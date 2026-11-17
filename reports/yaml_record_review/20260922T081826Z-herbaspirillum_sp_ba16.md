# YAML Record Review: Herbaspirillum sp. BA16

## Target

- File: `data/taxa/bacteria/herbaspirillum_sp_ba16.yaml`
- Identifier: `NCBITaxon:100003`
- PATHS.tsv row: 36
- Label: `Herbaspirillum sp. BA16`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:2624150` (`unclassified Herbaspirillum`)

## Validation

- `just validate data/taxa/bacteria/herbaspirillum_sp_ba16.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/bacillus_sp_enrichment_culture_clone_w_181.yaml data/taxa/bacteria/pseudomonas_sp_mbyd_1.yaml data/taxa/bacteria/herbaspirillum_sp_ba16.yaml data/taxa/bacteria/agrobacterium_sp_g21_07.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species-level placeholder under the no-rank NCBI `unclassified Herbaspirillum` node.
- `data/raw/ncbitaxon_taxa.tsv` line 17107 pins `NCBITaxon:100003` to label `Herbaspirillum sp. BA16`, rank `SPECIES`, parent `NCBITaxon:2624150`, genetic code 11, exact synonym `Herbispirillum sp. BA16`, source set `ncbitaxon`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the record under `unclassified Herbaspirillum`, `Herbaspirillum`, Oxalobacteraceae, Burkholderiales, Betaproteobacteria, Pseudomonadota, Pseudomonadati, and Bacteria, matching the YAML lineage.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `herbaspirillum_sp_ba16`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 142936 keeps this taxon in scope as `attested rule: Herbaspirillum sp. BA16, 1 sources incl. NCBI`.
- A gitignore-independent `rg --no-ignore --hidden` scan of `data/raw`, `data/atb`, and `data/straininfo` found only the NCBI taxonomy row for `NCBITaxon:100003`.

## Completeness

- The sole NCBITAXON source attestation is represented with one `NAME` assertion and the pinned NCBI snapshot date.
- The NCBI exact synonym is preserved in `synonyms`.
- `strain_count: 0` is consistent with the lack of direct GTDB, BacDive, GOLD, AllTheBacteria, or StrainInfo rows for this NCBI taxon in the local source inventories.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
