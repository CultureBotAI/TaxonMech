# YAML Record Review: Acetivibrio straminisolvens

## Target

- File: `data/taxa/bacteria/acetivibrio_straminisolvens.yaml`
- Identifier: `NCBITaxon:253314`
- PATHS.tsv row: 349126
- Label: `Acetivibrio straminisolvens`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:35829` (`Acetivibrio`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_straminisolvens.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_sp_fer_16.yaml data/taxa/bacteria/acetivibrio_sp_msjd_27.yaml data/taxa/bacteria/acetivibrio_straminisolvens.yaml data/taxa/bacteria/acetivibrio_straminisolvens_jcm_21531.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species for the validly published correct name `Acetivibrio straminisolvens`.
- `data/raw/ncbitaxon_taxa.tsv` line 51321 pins `NCBITaxon:253314` to label `Acetivibrio straminisolvens`, rank `SPECIES`, parent `NCBITaxon:35829`, genetic code 11, NCBI exact synonyms for `Clostridium straminisolvens` and `Hungateiclostridium straminisolvens`, related authority-string synonyms, source set `ncbitaxon|gtdb|lpsn|gold|madin_etal`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the species below `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/lpsn_names.tsv` lines 1125, 16369, and 33501 support the LPSN correct name `lpsn:5955`, the `Clostridium straminisolvens` and `Hungateiclostridium straminisolvens` synonym rows, type-strain designations DSM 16021, IAM 15070, JCM 21531, and NBRC 103399, sequence accession `INSDC:AB125279`, and the synonym-side `GTDB:s__Hungateiclostridium_straminisolvens` xref.
- `data/raw/gtdb_species.tsv` line 74477 and `data/raw/gtdb_mappings.tsv` line 197625 support the four-genome `GTDB:s__Hungateiclostridium_straminisolvens` `skos:closeMatch` mapping to `NCBITaxon:253314`.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_straminisolvens`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 21206 keeps this taxon in scope as `attested rule: Acetivibrio straminisolvens, 5 sources incl. NCBI`.
- `data/raw/bacdive_strains.tsv` line 2727 ties `bacdive:2827` to child taxon `NCBITaxon:1294263`, LPSN name `lpsn:5955`, designation CSK1, and collection IDs DSM 16021, IAM 15070, JCM 21531, and NBRC 103399.
- `data/raw/ncbi_type_material.tsv` lines 100212-100221 list the DSM 16021, IAM 15070, JCM 21531, NBRC 103399, and CSK1 type-material variants.
- `data/raw/strain_assemblies.tsv` lines 118638-118648, `data/straininfo/assemblies.tsv` line 8664, and `data/raw/strain_genome_records.tsv` lines 95376-95383 support the BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo genome evidence projected from JCM 21531.
- `data/raw/strain_related_records.tsv` lines 342575-342599 support the NCBI, BV-BRC, GTDB, GOLD, and StrainInfo BioProject/BioSample/GOLD related records.
- `data/straininfo/strain_links.tsv` lines 84731-84734 support the DSM 16021, IAM 15070, JCM 21531, and NBRC 103399 StrainInfo deposits projected under `straininfo.strain:134417`.

## Completeness

- NCBITAXON, LPSN, GTDB, BACDIVE, GOLD, and MADIN attestations are represented with the expected assertion units and counts, including direct-only notes for GOLD and MADIN and a descendant note for the BacDive type strain.
- The LPSN correct/synonym names, NCBI exact/related synonyms, and GTDB `Hungateiclostridium` species mapping are present.
- The JCM 21531 type-strain child evidence is represented with BacDive, collection identifiers, local genome assemblies, local genome records, GOLD/NCBI project records, and StrainInfo deposits.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
