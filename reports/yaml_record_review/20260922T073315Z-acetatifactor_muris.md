# YAML Record Review: Acetatifactor muris

## Target

- File: `data/taxa/bacteria/acetatifactor_muris.yaml`
- Identifier: `NCBITaxon:879566`
- PATHS.tsv row: 601450
- Label: `Acetatifactor muris`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:1427378` (`Acetatifactor`)

## Validation

- `just validate data/taxa/bacteria/acetatifactor_muris.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetatifactor_muris.yaml data/taxa/bacteria/acetatifactor_sp.yaml data/taxa/bacteria/acetatifactor_sp_dfi_5_50.yaml data/taxa/bacteria/aceticella_autotrophica.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` species-level bacterial taxon.
- `data/raw/ncbitaxon_taxa.tsv` line 187089 pins `NCBITaxon:879566` to label `Acetatifactor muris`, rank `SPECIES`, parent `NCBITaxon:1427378`, genetic code 11, related synonyms `Acetatifactor muris Pfeiffer et al. 2013` and `bacterium CT-m2`, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|bactotraits`, and NCBI snapshot `2026-09-13`.
- `data/raw/lpsn_names.tsv` line 27234 links `lpsn:790255` to the same NCBI taxon, the correct validly published species name, type strain designations `ATCC-BAA-2170` and `DSM-23669`, PMIDs/DOIs, sequence accession `INSDC:HM989805`, and `GTDB:s__Acetatifactor_muris`.
- The NCBI parent row for `NCBITaxon:1427378` and the higher parent rows for Lachnospiraceae, Lachnospirales, Clostridia, Bacillota, Bacillati, and Bacteria support the full YAML lineage.

## Evidence

- An exact `find` probe under `reports/yaml_record_review` found no existing report for `acetatifactor_muris`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 7043 keeps this taxon in scope as `attested rule: Acetatifactor muris, 7 sources incl. NCBI`.
- `data/raw/gtdb_mappings.tsv` lines 316407-316412 support the six `skos:broadMatch` GTDB mappings, with `GTDB:s__Acetatifactor_muris` as the leading 4-genome row and five further pooled GTDB species.
- `data/raw/bacdive_strains.tsv` line 17898 supports the CT-m2 BacDive strain, BacDive source ID `bacdive:18089`, LPSN source ID `lpsn:790255`, and culture collection IDs `ATCC-BAA-2170` and `DSM-23669`.
- `data/raw/culture_collection_strains.tsv` lines 7694 and 72671 map `ATCC-BAA-2170` and `DSM-23669` to `NCBITaxon:879566`; `data/raw/ncbi_type_material.tsv` lines 270419-270426 list ATCC BAA-2170, DSM 23669, and CT-m2 type-material synonyms.
- `data/raw/strain_assemblies.tsv` lines 103443-103449, `data/straininfo/assemblies.tsv` line 7436, and `data/raw/strain_genome_records.tsv` lines 83297-83300 support the BacDive, BV-BRC, GTDB, NCBI Assembly, and StrainInfo assembly/genome entries attached to DSM 23669.
- `data/raw/strain_related_records.tsv` lines 299335-299352 support the GTDB, BV-BRC, NCBI Assembly, GOLD, BioProject, and BioSample related records; `data/straininfo/strain_links.tsv` line 78039 supports the StrainInfo deposit/strain related records.
- `data/raw/mediadive_taxa.tsv` line 13629 supports the MediaDive `assertion_count: 2`; `data/raw/gold_organisms.tsv` line 43730 supports the GOLD `assertion_count: 4`; `data/raw/bactotraits_taxa.tsv` line 9204 supports the BacToTraits `assertion_count: 2`.

## Completeness

- All same-taxon local source rows found by the gitignore-independent bounded taxon/source-ID scan are represented in the YAML as NCBITAXON, LPSN, GTDB, BACDIVE, MEDIADIVE, GOLD, BACTOTRAITS, strain, assembly, genome, BioProject/BioSample, or StrainInfo evidence.
- The six pooled GTDB mappings, two NCBI related synonyms, LPSN nomenclature block, CT-m2 BacDive strain, and DSM 23669 accession records are internally consistent with their raw source rows.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
