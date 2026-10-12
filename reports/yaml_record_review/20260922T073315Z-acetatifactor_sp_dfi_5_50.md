# YAML Record Review: Acetatifactor sp. DFI.5.50

## Target

- File: `data/taxa/bacteria/acetatifactor_sp_dfi_5_50.yaml`
- Identifier: `NCBITaxon:2908897`
- PATHS.tsv row: 391039
- Label: `Acetatifactor sp. DFI.5.50`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:2633901` (`unclassified Acetatifactor`)

## Validation

- `just validate data/taxa/bacteria/acetatifactor_sp_dfi_5_50.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetatifactor_muris.yaml data/taxa/bacteria/acetatifactor_sp.yaml data/taxa/bacteria/acetatifactor_sp_dfi_5_50.yaml data/taxa/bacteria/aceticella_autotrophica.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` NCBI species-level bacterial placeholder.
- `data/raw/ncbitaxon_taxa.tsv` line 570323 pins `NCBITaxon:2908897` to label `Acetatifactor sp. DFI.5.50`, rank `SPECIES`, parent `NCBITaxon:2633901`, genetic code 11, source set `ncbitaxon|gtdb`, and NCBI snapshot `2026-09-13`.
- The raw `NCBITaxon:2633901` row is `unclassified Acetatifactor` under genus `Acetatifactor`, matching the YAML `parent_taxon` and terminal no-rank lineage node.
- Higher NCBI rows for Lachnospiraceae, Lachnospirales, Clostridia, Bacillota, Bacillati, and Bacteria support the remainder of the lineage.

## Evidence

- An exact `find` probe under `reports/yaml_record_review` found no existing report for `acetatifactor_sp_dfi_5_50`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 108765 keeps this taxon in scope as `attested rule: Acetatifactor sp. DFI.5.50, 2 sources incl. NCBI`.
- `data/raw/gtdb_species.tsv` line 3001 and `data/raw/gtdb_mappings.tsv` line 232663 support the `GTDB:s__Acetatifactor_acetigignens` `skos:closeMatch` mapping to `NCBITaxon:2908897` with `genome_count: 222`.
- The GTDB source label `s__Acetatifactor_acetigignens` is represented as xref `GTDB:s__Acetatifactor_acetigignens` and as exact synonym `Acetatifactor acetigignens`.
- The gitignore-independent bounded exact-ID/source-ID scan across `data/raw`, `data/atb`, and `data/straininfo` found no BacDive, LPSN, MediaDive, GOLD, ATB, or StrainInfo evidence for this NCBI taxon.

## Completeness

- The NCBITAXON and GTDB attestations are both represented, and the record carries the only GTDB close-match row found for `NCBITaxon:2908897`.
- No same-taxon strain, nomenclature, medium, GOLD, or ATB rows were present in the scanned local inventories, so the empty `strains` and `nomenclature` surfaces are consistent with the source evidence.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
