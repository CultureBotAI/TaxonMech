# YAML Record Review: Acetivibrio cellulolyticus

## Target

- File: `data/taxa/bacteria/acetivibrio_cellulolyticus.yaml`
- Identifier: `NCBITaxon:35830`
- PATHS.tsv row: 470889
- Label: `Acetivibrio cellulolyticus`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:35829` (`Acetivibrio`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_cellulolyticus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_alkalicellulosi.yaml data/taxa/bacteria/acetivibrio_alkalicellulosi_dsm_17461.yaml data/taxa/bacteria/acetivibrio_cellulolyticus.yaml data/taxa/bacteria/acetivibrio_cellulolyticus_cd2.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species for the validly published correct name `Acetivibrio cellulolyticus`.
- `data/raw/ncbitaxon_taxa.tsv` line 4018 pins `NCBITaxon:35830` to label `Acetivibrio cellulolyticus`, rank `SPECIES`, parent `NCBITaxon:35829`, genetic code 11, NCBI exact synonyms for `Acetivibrio cellulosolvens` and `Hungateiclostridium cellulolyticum`, related synonyms, source set `ncbitaxon|bacdive|lpsn|gold|madin_etal`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place `NCBITaxon:35830` under `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/lpsn_names.tsv` lines 14791, 21352, and 33533 support the LPSN correct name `lpsn:772481`, the `Acetivibrio cellulosolvens` and `Hungateiclostridium cellulolyticum` synonym rows, the type-strain designations, and the `GTDB:s__Acetivibrio_cellulolyticus` xref.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_cellulolyticus`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 13790 keeps this taxon in scope as `attested rule: Acetivibrio cellulolyticus, 5 sources incl. NCBI`.
- `data/raw/bacdive_strains.tsv` lines 17485 and 92113 support the two BacDive strains, `bacdive:17674` for child strain CD2 and `bacdive:169880` for the synonym-linked BAS / NRC 2936 strain at `NCBITaxon:35830`.
- `data/raw/ncbi_type_material.tsv` lines 193132-193148 list NCBI type-material variants for both the `Acetivibrio cellulolyticus` CD2 / ATCC 33288 / DSM 1870 / LMG 8466 / NRC 2248 set and the `Acetivibrio cellulosolvens` BAS / ATCC 35928 / NRC 2936 set.
- `data/raw/strain_assemblies.tsv` lines 99905-99906 and `data/raw/strain_genome_records.tsv` lines 80462-80464 support the CD2 BacDive/GOLD assembly and IMG/BV-BRC genome rows projected through `classified_as: NCBITaxon:509191`.
- `data/raw/strain_related_records.tsv` lines 289818-289824 support the CD2 GOLD project/sample/analysis/organism related records plus the direct ATCC 33288 GOLD organism row, and line 269733 supports the BAS / ATCC 35928 GOLD organism.
- `data/straininfo/strain_links.tsv` lines 76877-76878 and 72284 support the StrainInfo deposits for ATCC 33288, DSM 1870, and ATCC 35928.

## Completeness

- NCBITAXON, LPSN, BACDIVE, GOLD, and MADIN attestations are represented with explicit notes that the CD2 BacDive child is rolled up and direct GOLD/MADIN rows are counted separately.
- Both local BacDive strains are represented: CD2 carries the type-strain genome and the child taxon link, while BAS carries the `Acetivibrio cellulosolvens` synonym strain and its ATCC 35928 StrainInfo/GOLD evidence.
- The GTDB species is present as an LPSN cross-reference; the separate GTDB mapping inventory maps `GTDB:s__Acetivibrio_cellulolyticus` to the child strain `NCBITaxon:509191`, so the species-level record appropriately does not assert a direct `taxonomy_mappings` row.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
