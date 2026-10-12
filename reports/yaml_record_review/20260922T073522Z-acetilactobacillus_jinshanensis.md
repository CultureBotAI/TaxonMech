# YAML Record Review: Acetilactobacillus jinshanensis

## Target

- File: `data/taxa/bacteria/acetilactobacillus_jinshanensis.yaml`
- Identifier: `NCBITaxon:1720083`
- PATHS.tsv row: 255668
- Label: `Acetilactobacillus jinshanensis`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:2767874` (`Acetilactobacillus`)

## Validation

- `just validate data/taxa/bacteria/acetilactobacillus_jinshanensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/aceticella_sp_75b_ac.yaml data/taxa/bacteria/acetilactobacillus_jinshanensis.yaml data/taxa/bacteria/acetilactobacillus_sp.yaml data/taxa/bacteria/acetispira_formosa_nom_nud.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` species-level bacterial taxon.
- `data/raw/ncbitaxon_taxa.tsv` line 449397 pins `NCBITaxon:1720083` to label `Acetilactobacillus jinshanensis`, rank `SPECIES`, parent `NCBITaxon:2767874`, genetic code 11, exact synonym `Lactobacillus jinshani`, three NCBI related synonyms, source set `ncbitaxon|gtdb|bacdive|lpsn|gold`, and NCBI snapshot `2026-09-13`.
- `data/raw/lpsn_names.tsv` line 676 links `lpsn:5493` to the same NCBI taxon, the correct validly published species name, type strain designation `JCM-33270`, PMIDs/DOIs, sequence accession `INSDC:KT783533`, and `GTDB:s__Acetilactobacillus_jinshanensis`.
- The NCBI parent row for `NCBITaxon:2767874` and the higher parent rows for Lactobacillaceae, Lactobacillales, Bacilli, Bacillota, Bacillati, and Bacteria support the full YAML lineage.

## Evidence

- An exact `find` probe under `reports/yaml_record_review` found no existing report for `acetilactobacillus_jinshanensis`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 16213 keeps this taxon in scope as `attested rule: Acetilactobacillus jinshanensis, 5 sources incl. NCBI`.
- `data/raw/gtdb_species.tsv` lines 3272-3273 and `data/raw/gtdb_mappings.tsv` lines 51607-51608 support the two `skos:broadMatch` GTDB mappings, with `GTDB:s__Acetilactobacillus_jinshanensis` as the leading 3-genome row and one further pooled GTDB species.
- `data/raw/bacdive_strains.tsv` line 86727 supports the HSLZ-75 BacDive strain, BacDive source ID `bacdive:164491`, LPSN source ID `lpsn:5493`, BacDive `medium_count: 1`, and culture collection IDs `CICC%206269` and `JCM-33270`.
- `data/raw/culture_collection_strains.tsv` lines 42249 and 108462 map `CICC%206269` and `JCM-33270` to `NCBITaxon:1720083`; `data/raw/ncbi_type_material.tsv` lines 54913-54918 list CICC 6269, JCM 33270, and HSLZ-75 type-material synonyms.
- `data/raw/strain_assemblies.tsv` line 78518 and `data/raw/strain_genome_records.tsv` lines 61183-61184 support the BacDive INSDC, IMG, and BV-BRC genome accessions.
- `data/raw/gold_organisms.tsv` line 14935 supports the GOLD `assertion_count: 1`.

## Completeness

- All same-taxon local source rows found by the gitignore-independent bounded taxon/source-ID scan are represented in the YAML as NCBITAXON, LPSN, GTDB, BACDIVE, GOLD, strain, or genome evidence.
- The two pooled GTDB mappings, four NCBI synonyms, LPSN nomenclature block, and HSLZ-75 BacDive strain are internally consistent with their raw source rows.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
