# YAML Record Review: Acetanaerobacter sp.

## Target

- File: `data/taxa/bacteria/acetanaerobacter_sp.yaml`
- Identifier: `NCBITaxon:2912264`
- PATHS.tsv row: 391569
- Label: `Acetanaerobacter sp.`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:2912263` (`unclassified Acetanaerobacter`)

## Validation

- `just validate data/taxa/bacteria/acetanaerobacter_sp.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetanaerobacter_sp.yaml data/taxa/bacteria/acetanaerobacterium_elongatum.yaml data/taxa/bacteria/acetanaerobacterium_sp.yaml data/taxa/bacteria/acetanaerobacterium_sp_hmp_mda_pilot_jcvi_0106.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` NCBI species-level bacterial taxon.
- `data/raw/ncbitaxon_taxa.tsv` line 570852 pins `NCBITaxon:2912264` to label `Acetanaerobacter sp.`, rank `SPECIES`, parent `NCBITaxon:2912263`, genetic code 11, source set `ncbitaxon`, and NCBI snapshot `2026-09-13`.
- The raw `NCBITaxon:2912263` row is `unclassified Acetanaerobacter` under genus `Acetanaerobacter`, matching the YAML `parent_taxon` and terminal no-rank lineage node.
- Higher NCBI rows for Oscillospiraceae, Eubacteriales, Clostridia, Bacillota, Bacillati, and Bacteria support the remainder of the lineage.

## Evidence

- An exact `find` probe under `reports/yaml_record_review` found no existing report for `acetanaerobacter_sp`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 580751 keeps this taxon in scope as `attested rule: Acetanaerobacter sp., 1 sources incl. NCBI`.
- A gitignore-independent, bounded exact-ID scan across `data/raw`, `data/atb`, and `data/straininfo` found no same-taxon auxiliary source rows beyond the NCBI row, matching the YAML's single NCBITAXON `source_attestations` entry and absence of `taxonomy_mappings`, `nomenclature`, and `strains`.
- The YAML `genetic_code: 11` and `strain_count: 0` are consistent with the pinned raw NCBI row and the absence of matching strain inventories.

## Completeness

- The available local evidence for this leaf consists of the seeded NCBI name row and its NCBI lineage; all of those facts are represented in the YAML.
- No GTDB, LPSN, BacDive, MediaDive, GOLD, MADIN, ATB, or StrainInfo evidence was present for `NCBITaxon:2912264` in the exact same-taxon local scans, so the record does not appear to be omitting structured auxiliary assertions.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
