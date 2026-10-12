# YAML Record Review: Azospirillum sp. Ala

## Target

- File: `data/taxa/bacteria/azospirillum_sp_ala.yaml`
- Identifier: `NCBITaxon:100006`
- PATHS.tsv row: 69
- Label: `Azospirillum sp. Ala`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:2630922` (`unclassified Azospirillum`)

## Validation

- `just validate data/taxa/bacteria/azospirillum_sp_ala.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/sphingomonas_sp_09wsh1_26.yaml data/taxa/bacteria/sphingomonas_sp_09wsh1_27.yaml data/taxa/bacteria/sphingomonas_sp_09wsh1_29.yaml data/taxa/bacteria/azospirillum_sp_ala.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species-level placeholder under the no-rank NCBI `unclassified Azospirillum` node.
- `data/raw/ncbitaxon_taxa.tsv` line 17110 pins `NCBITaxon:100006` to label `Azospirillum sp. Ala`, rank `SPECIES`, parent `NCBITaxon:2630922`, genetic code 11, source set `ncbitaxon`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the record under `unclassified Azospirillum`, `Azospirillum`, Azospirillaceae, Rhodospirillales, Alphaproteobacteria, Pseudomonadota, Pseudomonadati, and Bacteria, matching the YAML lineage.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `azospirillum_sp_ala`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 142939 keeps this taxon in scope as `attested rule: Azospirillum sp. Ala, 1 sources incl. NCBI`.
- A gitignore-independent `rg --no-ignore --hidden` scan of `data/raw`, `data/atb`, and `data/straininfo` found only the NCBI taxonomy row for `NCBITaxon:100006`.

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
