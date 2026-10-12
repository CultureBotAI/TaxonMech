# YAML Record Review: Acetivibrio thermocellus ATCC 27405

## Target

- File: `data/taxa/bacteria/acetivibrio_thermocellus_atcc_27405.yaml`
- Identifier: `NCBITaxon:203119`
- PATHS.tsv row: 321599
- Label: `Acetivibrio thermocellus ATCC 27405`
- Rank/domain: `STRAIN` / `BACTERIA`
- Parent: `NCBITaxon:1515` (`Acetivibrio thermocellus`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_thermocellus_atcc_27405.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_thermocellus.yaml data/taxa/bacteria/acetivibrio_thermocellus_ad2.yaml data/taxa/bacteria/acetivibrio_thermocellus_atcc_27405.yaml data/taxa/bacteria/acetivibrio_thermocellus_bc1.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial strain taxon under `Acetivibrio thermocellus`.
- `data/raw/ncbitaxon_taxa.tsv` line 40060 pins `NCBITaxon:203119` to label `Acetivibrio thermocellus ATCC 27405`, rank `STRAIN`, parent `NCBITaxon:1515`, genetic code 11, exact synonyms for ATCC 27405 / DSM 1237 in the older `Clostridium`, `Hungateiclostridium`, and `Ruminiclostridium` combinations, source set `ncbitaxon|gtdb|bacdive|mediadive|gold|madin_etal|bactotraits`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the strain below `Acetivibrio thermocellus`, `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/gtdb_species.tsv` line 74478 and `data/raw/gtdb_mappings.tsv` line 145341 support the 13-genome `GTDB:s__Hungateiclostridium_thermocellum` `skos:closeMatch` mapping to `NCBITaxon:203119`.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_thermocellus_atcc_27405`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 6092 keeps this taxon in scope as `attested rule: Acetivibrio thermocellus ATCC 27405, 7 sources incl. NCBI`.
- `data/raw/bacdive_strains.tsv` line 2630 ties `bacdive:2729` directly to `NCBITaxon:203119`, LPSN name `lpsn:5956`, and ten culture collection identifiers including ATCC 27405 and DSM 1237.
- `data/raw/strain_assemblies.tsv` lines 117755-117763, `data/straininfo/assemblies.tsv` line 8572, and the `bacdive:2729` rows in `data/raw/strain_genome_records.tsv` support the BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo genome evidence for the complete ASM1586v1 genome.
- `data/raw/strain_related_records.tsv` carries the BioProject, BioSample, GOLD, NCBI Assembly, and StrainInfo related records for the type strain, including a large set of ATCC 27405 transcriptome GOLD projects filed at the parent species.
- `data/straininfo/strain_links.tsv` lines 84412-84419 support the JCM 9322, CECT 593, LMG 10435, ATCC 27405, NCIMB 10682, NRRL B-4536, NBRC 103400, and DSM 1237 StrainInfo deposits projected under `straininfo.strain:10383`.

## Completeness

- NCBITAXON, GTDB, BACDIVE, MEDIADIVE, GOLD, MADIN, and BACTOTRAITS attestations are represented with the expected assertion units and counts.
- The `GTDB:s__Hungateiclostridium_thermocellum` mapping and older NCBI strain synonyms are present, and the parent species carries the corresponding LPSN nomenclatural rows.
- The ATCC 27405 type-strain evidence is represented with culture-collection IDs, local genome assemblies, local genome records, GOLD/NCBI project records, and StrainInfo deposits.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
