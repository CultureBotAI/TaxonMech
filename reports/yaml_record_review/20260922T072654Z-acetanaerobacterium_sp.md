# YAML Record Review: Acetanaerobacterium sp.

## Target

- File: `data/taxa/bacteria/acetanaerobacterium_sp.yaml`
- Identifier: `NCBITaxon:1872089`
- PATHS.tsv row: 296611
- Label: `Acetanaerobacterium sp.`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:2645644` (`unclassified Acetanaerobacterium`)

## Validation

- `just validate data/taxa/bacteria/acetanaerobacterium_sp.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetanaerobacter_sp.yaml data/taxa/bacteria/acetanaerobacterium_elongatum.yaml data/taxa/bacteria/acetanaerobacterium_sp.yaml data/taxa/bacteria/acetanaerobacterium_sp_hmp_mda_pilot_jcvi_0106.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` species-level bacterial taxon.
- `data/raw/ncbitaxon_taxa.tsv` line 489173 pins `NCBITaxon:1872089` to label `Acetanaerobacterium sp.`, rank `SPECIES`, parent `NCBITaxon:2645644`, genetic code 11, source set `ncbitaxon|bacdive|mediadive`, and NCBI snapshot `2026-09-13`.
- The raw `NCBITaxon:2645644` row is `unclassified Acetanaerobacterium` under genus `Acetanaerobacterium`, matching the YAML `parent_taxon` and terminal no-rank lineage node.
- Higher NCBI rows for Oscillospiraceae, Eubacteriales, Clostridia, Bacillota, Bacillati, and Bacteria support the remainder of the lineage.

## Evidence

- An exact `find` probe under `reports/yaml_record_review` found no existing report for `acetanaerobacterium_sp`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 30914 keeps this taxon in scope as `attested rule: Acetanaerobacterium sp., 3 sources incl. NCBI`.
- `data/raw/bacdive_strains.tsv` line 54339 supports the `Sanger 05` BacDive strain, BacDive source ID `bacdive:132028`, and culture collection ID `DSM-102114`.
- `data/raw/culture_collection_strains.tsv` line 58629 maps `DSM-102114` to `NCBITaxon:1872089`.
- `data/straininfo/strain_links.tsv` line 12607 supports the StrainInfo strain/deposit related records matched through `DSM-102114`; the raw StrainInfo taxon is genus-level `NCBITaxon:258514`, and the YAML preserves that source taxon in each related record.
- `data/raw/mediadive_taxa.tsv` line 5648 supports the MediaDive `assertion_count: 1`.
- The gitignore-independent bounded exact-ID/source-ID scan across `data/raw`, `data/atb`, and `data/straininfo` found no GTDB, LPSN, GOLD, MADIN, or ATB evidence for this NCBI taxon.

## Completeness

- The NCBITAXON, BACDIVE, MEDIADIVE, strain, and StrainInfo assertions are all represented.
- No same-taxon GTDB mapping, LPSN nomenclature row, GOLD organism row, MADIN trait row, or ATB row was present in the scanned local inventories, so those sections are appropriately absent.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
