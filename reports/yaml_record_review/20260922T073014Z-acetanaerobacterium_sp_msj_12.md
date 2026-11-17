# YAML Record Review: Acetanaerobacterium sp. MSJ-12

## Target

- File: `data/taxa/bacteria/acetanaerobacterium_sp_msj_12.yaml`
- Identifier: `NCBITaxon:2841535`
- PATHS.tsv row: 383766
- Label: `Acetanaerobacterium sp. MSJ-12`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:2645644` (`unclassified Acetanaerobacterium`)

## Validation

- `just validate data/taxa/bacteria/acetanaerobacterium_sp_msj_12.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetanaerobacterium_sp_hmp_mda_pilot_jcvi_0107.yaml data/taxa/bacteria/acetanaerobacterium_sp_hmp_mda_pilot_jcvi_0109.yaml data/taxa/bacteria/acetanaerobacterium_sp_msj_12.yaml data/taxa/bacteria/acetatifactor_aquisgranensis.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` NCBI species-level bacterial taxon.
- `data/raw/ncbitaxon_taxa.tsv` line 563808 pins `NCBITaxon:2841535` to label `Acetanaerobacterium sp. MSJ-12`, rank `SPECIES`, parent `NCBITaxon:2645644`, genetic code 11, source set `ncbitaxon|gtdb`, and NCBI snapshot `2026-09-13`.
- The raw `NCBITaxon:2645644` row is `unclassified Acetanaerobacterium` under genus `Acetanaerobacterium`, matching the YAML `parent_taxon` and terminal no-rank lineage node.
- Higher NCBI rows for Oscillospiraceae, Eubacteriales, Clostridia, Bacillota, Bacillati, and Bacteria support the remainder of the lineage.

## Evidence

- An exact `find` probe under `reports/yaml_record_review` found no existing report for `acetanaerobacterium_sp_msj_12`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 106663 keeps this taxon in scope as `attested rule: Acetanaerobacterium sp. MSJ-12, 2 sources incl. NCBI`.
- `data/raw/gtdb_species.tsv` line 17991 and `data/raw/gtdb_mappings.tsv` line 226371 support the `GTDB:s__Bittarella_massiliensis` `skos:closeMatch` mapping to `NCBITaxon:2841535` with `genome_count: 14`.
- The GTDB source label `s__Bittarella_massiliensis` is represented as xref `GTDB:s__Bittarella_massiliensis` and as exact synonym `Bittarella massiliensis`.
- The gitignore-independent bounded exact-ID/source-ID scan across `data/raw`, `data/atb`, and `data/straininfo` found no BacDive, LPSN, MediaDive, GOLD, ATB, or StrainInfo evidence for this NCBI taxon.

## Completeness

- The NCBITAXON and GTDB attestations are both represented, and the record carries the GTDB close-match row found for `NCBITaxon:2841535`.
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
