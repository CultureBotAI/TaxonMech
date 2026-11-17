# YAML Record Review: Acetivibrio thermocellus

## Target

- File: `data/taxa/bacteria/acetivibrio_thermocellus.yaml`
- Identifier: `NCBITaxon:1515`
- PATHS.tsv row: 193941
- Label: `Acetivibrio thermocellus`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:35829` (`Acetivibrio`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_thermocellus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_thermocellus.yaml data/taxa/bacteria/acetivibrio_thermocellus_ad2.yaml data/taxa/bacteria/acetivibrio_thermocellus_atcc_27405.yaml data/taxa/bacteria/acetivibrio_thermocellus_bc1.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species for the validly published correct name `Acetivibrio thermocellus`.
- `data/raw/ncbitaxon_taxa.tsv` line 1182 pins `NCBITaxon:1515` to label `Acetivibrio thermocellus`, rank `SPECIES`, parent `NCBITaxon:35829`, genetic code 11, exact synonyms for `Clostridium thermocellum`, `Hungateiclostridium thermocellum`, and `Ruminiclostridium thermocellum`, related authority-string synonyms, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the species below `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/lpsn_names.tsv` lines 1126, 16380, and 33504 support the LPSN correct name `lpsn:5956`, the `Clostridium thermocellum` and `Hungateiclostridium thermocellum` synonym rows, type-strain designations, sequence accession `INSDC:AB558166`, and the synonym-side `GTDB:s__Hungateiclostridium_thermocellum` xref.
- `data/raw/gtdb_species.tsv` line 74478 and `data/raw/gtdb_mappings.tsv` line 33160 support the 13-genome `GTDB:s__Hungateiclostridium_thermocellum` `skos:closeMatch` mapping to `NCBITaxon:1515`.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_thermocellus`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 641 keeps this taxon in scope as `attested rule: Acetivibrio thermocellus, 8 sources incl. NCBI`.
- `data/raw/bacdive_strains.tsv` lines 2629-2632, 22771-22772, and 96633 support the seven BacDive strain blocks in the YAML: DSM 1313, ATCC 27405, DSM 2360, JW20, YS, AD2, and BC 1 / DSM 29190.
- `data/raw/ncbi_type_material.tsv` lines 38471-38487 list the ATCC 27405, DSM 1237, JCM 9322, LMG 10435, NBRC 103400, NCIMB 10682, and NRRL B-4536 type-material variants.
- `data/raw/strain_assemblies.tsv` and `data/raw/strain_genome_records.tsv` support the local BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo genome evidence for the 7 projected BacDive strains, with `bacdive:2729` alone contributing 10 assemblies and 9 genome records for the ATCC 27405 type strain.
- `data/raw/strain_related_records.tsv`, `data/atb/strain_links.tsv`, and `data/atb/genome_links.tsv` carry the BioProject, BioSample, GOLD, and AllTheBacteria related records; the parent species intentionally accumulates several hundred direct GOLD organism/project rows.
- `data/straininfo/strain_links.tsv` lines 74892, 80180-80181, 84411-84419, and 84426-84430 support StrainInfo deposits for the DSM 29190, DSM 25991, DSM 25992, DSM 1313, ATCC 27405 family, DSM 2360, and JW20 family strains.

## Completeness

- NCBITAXON, LPSN, GTDB, BACDIVE, MEDIADIVE, GOLD, MADIN, and BACTOTRAITS attestations are represented with the expected assertion units and counts.
- The LPSN correct/synonym names, NCBI exact/related synonyms, and GTDB `Hungateiclostridium` species mapping are present.
- All seven local BacDive strains are represented with the expected collection identifiers, genome evidence, and related records available for each source strain.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
