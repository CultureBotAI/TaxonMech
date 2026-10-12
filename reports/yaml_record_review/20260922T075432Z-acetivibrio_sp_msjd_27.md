# YAML Record Review: Acetivibrio sp. MSJd-27

## Target

- File: `data/taxa/bacteria/acetivibrio_sp_msjd_27.yaml`
- Identifier: `NCBITaxon:2841523`
- PATHS.tsv row: 383754
- Label: `Acetivibrio sp. MSJd-27`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:2641281` (`unclassified Acetivibrio`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_sp_msjd_27.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_sp_fer_16.yaml data/taxa/bacteria/acetivibrio_sp_msjd_27.yaml data/taxa/bacteria/acetivibrio_straminisolvens.yaml data/taxa/bacteria/acetivibrio_straminisolvens_jcm_21531.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species placeholder below `unclassified Acetivibrio`.
- `data/raw/ncbitaxon_taxa.tsv` line 563796 pins `NCBITaxon:2841523` to label `Acetivibrio sp. MSJd-27`, rank `SPECIES`, parent `NCBITaxon:2641281`, genetic code 11, source set `ncbitaxon|gtdb`, and NCBI snapshot `2026-09-13`.
- `data/raw/ncbitaxon_taxa.tsv` line 539492 supports the immediate `unclassified Acetivibrio` parent, and the raw parent rows place that placeholder below `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/gtdb_species.tsv` line 71539 and `data/raw/gtdb_mappings.tsv` line 226342 support the five-genome `GTDB:s__HGM11507_sp900761005` `skos:closeMatch` mapping to `NCBITaxon:2841523`.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_sp_msjd_27`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 106653 keeps this taxon in scope as `attested rule: Acetivibrio sp. MSJd-27, 2 sources incl. NCBI`.
- The GTDB mapping row supplies the source label carried as the GTDB-sourced exact synonym `HGM11507 sp900761005`.
- A gitignore-independent exact scan for `NCBITaxon:2841523` under `data/raw`, `data/atb`, and `data/straininfo` found NCBI and GTDB evidence but no same-taxon BacDive, GOLD, AllTheBacteria, or StrainInfo rows.

## Completeness

- NCBITAXON and GTDB attestations are represented with the expected assertion units and counts.
- The one local GTDB species mapping is represented with five genomes, and its source label is carried as an exact synonym.
- `strain_count: 0` is consistent with the absence of same-taxon BacDive and StrainInfo rows in the gitignore-independent source scan.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
