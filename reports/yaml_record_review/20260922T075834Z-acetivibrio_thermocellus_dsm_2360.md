# YAML Record Review: Acetivibrio thermocellus DSM 2360

## Target

- File: `data/taxa/bacteria/acetivibrio_thermocellus_dsm_2360.yaml`
- Identifier: `NCBITaxon:572545`
- PATHS.tsv row: 543972
- Label: `Acetivibrio thermocellus DSM 2360`
- Rank/domain: `STRAIN` / `BACTERIA`
- Parent: `NCBITaxon:1515` (`Acetivibrio thermocellus`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_thermocellus_dsm_2360.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_thermocellus_dsm_1313.yaml data/taxa/bacteria/acetivibrio_thermocellus_dsm_2360.yaml data/taxa/bacteria/acetivibrio_thermocellus_jw20.yaml data/taxa/bacteria/acetivibrio_thermocellus_ys.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial strain taxon under `Acetivibrio thermocellus`.
- `data/raw/ncbitaxon_taxa.tsv` line 135030 pins `NCBITaxon:572545` to label `Acetivibrio thermocellus DSM 2360`, rank `STRAIN`, parent `NCBITaxon:1515`, genetic code 11, exact synonyms for the older `Clostridium`, `Hungateiclostridium`, and `Ruminiclostridium` DSM 2360 combinations, source set `ncbitaxon|gtdb|bacdive|mediadive|gold|madin_etal|bactotraits`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the strain below `Acetivibrio thermocellus`, `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/gtdb_species.tsv` line 74478 and `data/raw/gtdb_mappings.tsv` line 297067 support the 13-genome `GTDB:s__Hungateiclostridium_thermocellum` `skos:closeMatch` mapping to `NCBITaxon:572545`.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_thermocellus_dsm_2360`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 6723 keeps this taxon in scope as `attested rule: Acetivibrio thermocellus DSM 2360, 7 sources incl. NCBI`.
- `data/raw/bacdive_strains.tsv` line 2631 ties `bacdive:2730` directly to `NCBITaxon:572545`, LPSN name `lpsn:5956`, designation LQR1, and ATCC 35609, DSM 2360, and JCM 9323 collection IDs.
- `data/raw/strain_assemblies.tsv` lines 117772-117777, `data/straininfo/assemblies.tsv` line 8573, and `data/raw/strain_genome_records.tsv` lines 94678-94685 support the BacDive, BV-BRC, GOLD, and StrainInfo genome evidence for the contig and complete DSM 2360 assemblies.
- `data/raw/strain_related_records.tsv` lines 340082-340092 support the BioProject, BioSample, GOLD analysis, GOLD organism, and GOLD project records.
- `data/straininfo/strain_links.tsv` lines 84426-84428 support the ATCC 35609, DSM 2360, and JCM 9323 StrainInfo deposits projected under `straininfo.strain:41192`.

## Completeness

- NCBITAXON, GTDB, BACDIVE, MEDIADIVE, GOLD, MADIN, and BACTOTRAITS attestations are represented with the expected assertion units and counts.
- The `GTDB:s__Hungateiclostridium_thermocellum` mapping and older NCBI strain synonyms are present, and the parent species carries the corresponding LPSN nomenclatural rows.
- The DSM 2360 BacDive strain is represented with culture-collection IDs, local genome assemblies, local genome records, GOLD project/sample/analysis records, and StrainInfo deposits.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
