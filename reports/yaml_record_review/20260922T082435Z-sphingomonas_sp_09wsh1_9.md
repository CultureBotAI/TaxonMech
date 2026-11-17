# YAML Record Review: Sphingomonas sp. 09WSH1-9

## Target

- File: `data/taxa/bacteria/sphingomonas_sp_09wsh1_9.yaml`
- Identifier: `NCBITaxon:1000041`
- PATHS.tsv row: 49
- Label: `Sphingomonas sp. 09WSH1-9`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:196159` (`unclassified Sphingomonas`)

## Validation

- `just validate data/taxa/bacteria/sphingomonas_sp_09wsh1_9.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/sphingomonas_sp_09wsh1_7.yaml data/taxa/bacteria/herbaspirillum_sp_ba134.yaml data/taxa/bacteria/sphingomonas_sp_09wsh1_8.yaml data/taxa/bacteria/sphingomonas_sp_09wsh1_9.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species-level placeholder under the no-rank NCBI `unclassified Sphingomonas` node.
- `data/raw/ncbitaxon_taxa.tsv` line 208842 pins `NCBITaxon:1000041` to label `Sphingomonas sp. 09WSH1-9`, rank `SPECIES`, parent `NCBITaxon:196159`, genetic code 11, source set `ncbitaxon`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the record under `unclassified Sphingomonas`, `Sphingomonas`, Sphingomonadaceae, Sphingomonadales, Alphaproteobacteria, Pseudomonadota, Pseudomonadati, and Bacteria, matching the YAML lineage.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `sphingomonas_sp_09wsh1_9`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 309956 keeps this taxon in scope as `attested rule: Sphingomonas sp. 09WSH1-9, 1 sources incl. NCBI`.
- A gitignore-independent `rg --no-ignore --hidden` scan of `data/raw`, `data/atb`, and `data/straininfo` found only the NCBI taxonomy row for `NCBITaxon:1000041`.

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
