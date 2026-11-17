# YAML Record Review: Methylobacterium sp. 09WSH1-18

## Target

- File: `data/taxa/bacteria/methylobacterium_sp_09wsh1_18.yaml`
- Identifier: `NCBITaxon:1000050`
- PATHS.tsv row: 59
- Label: `Methylobacterium sp. 09WSH1-18`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:2615210` (`unclassified Methylobacterium`)

## Validation

- `just validate data/taxa/bacteria/methylobacterium_sp_09wsh1_18.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/herbaspirillum_sp_ba161.yaml data/taxa/bacteria/methylobacterium_sp_09wsh1_18.yaml data/taxa/bacteria/sphingomonas_sp_09wsh1_19.yaml data/taxa/bacteria/sphingomonas_sp_09wsh1_20.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species-level placeholder under the no-rank NCBI `unclassified Methylobacterium` node.
- `data/raw/ncbitaxon_taxa.tsv` line 208851 pins `NCBITaxon:1000050` to label `Methylobacterium sp. 09WSH1-18`, rank `SPECIES`, parent `NCBITaxon:2615210`, genetic code 11, source set `ncbitaxon`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the record under `unclassified Methylobacterium`, `Methylobacterium`, Methylobacteriaceae, Hyphomicrobiales, Alphaproteobacteria, Pseudomonadota, Pseudomonadati, and Bacteria, matching the YAML lineage.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `methylobacterium_sp_09wsh1_18`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 309965 keeps this taxon in scope as `attested rule: Methylobacterium sp. 09WSH1-18, 1 sources incl. NCBI`.
- A gitignore-independent `rg --no-ignore --hidden` scan of `data/raw`, `data/atb`, and `data/straininfo` found only the NCBI taxonomy row for `NCBITaxon:1000050`.

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
