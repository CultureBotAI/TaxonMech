# YAML Record Review: Acetivibrio straminisolvens JCM 21531

## Target

- File: `data/taxa/bacteria/acetivibrio_straminisolvens_jcm_21531.yaml`
- Identifier: `NCBITaxon:1294263`
- PATHS.tsv row: 102150
- Label: `Acetivibrio straminisolvens JCM 21531`
- Rank/domain: `STRAIN` / `BACTERIA`
- Parent: `NCBITaxon:253314` (`Acetivibrio straminisolvens`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_straminisolvens_jcm_21531.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_sp_fer_16.yaml data/taxa/bacteria/acetivibrio_sp_msjd_27.yaml data/taxa/bacteria/acetivibrio_straminisolvens.yaml data/taxa/bacteria/acetivibrio_straminisolvens_jcm_21531.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial strain taxon under `Acetivibrio straminisolvens`.
- `data/raw/ncbitaxon_taxa.tsv` line 304298 pins `NCBITaxon:1294263` to label `Acetivibrio straminisolvens JCM 21531`, rank `STRAIN`, parent `NCBITaxon:253314`, genetic code 11, exact NCBI synonyms for the older `Clostridium` and `Hungateiclostridium` combinations, source set `ncbitaxon|gtdb|bacdive|mediadive|madin_etal|bactotraits`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the strain below `Acetivibrio straminisolvens`, `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/gtdb_species.tsv` line 74477 and `data/raw/gtdb_mappings.tsv` line 16977 support the four-genome `GTDB:s__Hungateiclostridium_straminisolvens` `skos:closeMatch` mapping to `NCBITaxon:1294263`.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_straminisolvens_jcm_21531`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 12047 keeps this taxon in scope as `attested rule: Acetivibrio straminisolvens JCM 21531, 6 sources incl. NCBI`.
- `data/raw/bacdive_strains.tsv` line 2727 ties `bacdive:2827` directly to `NCBITaxon:1294263`, LPSN name `lpsn:5955`, designation CSK1, and collection IDs DSM 16021, IAM 15070, JCM 21531, and NBRC 103399.
- `data/raw/strain_assemblies.tsv` lines 118638-118648, `data/straininfo/assemblies.tsv` line 8664, and `data/raw/strain_genome_records.tsv` lines 95376-95383 support the BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo genome evidence.
- `data/raw/strain_related_records.tsv` lines 342575-342599 support the NCBI, BV-BRC, GTDB, GOLD, and StrainInfo BioProject/BioSample/GOLD related records.
- `data/straininfo/strain_links.tsv` lines 84731-84734 support the DSM 16021, IAM 15070, JCM 21531, and NBRC 103399 StrainInfo deposits projected under `straininfo.strain:134417`.

## Completeness

- NCBITAXON, GTDB, BACDIVE, MEDIADIVE, MADIN, and BACTOTRAITS attestations are represented with the expected assertion units and counts.
- The `GTDB:s__Hungateiclostridium_straminisolvens` mapping and older NCBI strain synonyms are present, and the parent species carries the corresponding LPSN nomenclatural rows.
- The BacDive type strain is represented with collection identifiers, local genome assemblies, local genome records, GOLD/NCBI project records, and StrainInfo deposits.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
