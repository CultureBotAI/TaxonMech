# YAML Record Review: Acetivibrio thermocellus YS

## Target

- File: `data/taxa/bacteria/acetivibrio_thermocellus_ys.yaml`
- Identifier: `NCBITaxon:1094188`
- PATHS.tsv row: 28774
- Label: `Acetivibrio thermocellus YS`
- Rank/domain: `STRAIN` / `BACTERIA`
- Parent: `NCBITaxon:1515` (`Acetivibrio thermocellus`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_thermocellus_ys.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_thermocellus_dsm_1313.yaml data/taxa/bacteria/acetivibrio_thermocellus_dsm_2360.yaml data/taxa/bacteria/acetivibrio_thermocellus_jw20.yaml data/taxa/bacteria/acetivibrio_thermocellus_ys.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial strain taxon under `Acetivibrio thermocellus`.
- `data/raw/ncbitaxon_taxa.tsv` line 235295 pins `NCBITaxon:1094188` to label `Acetivibrio thermocellus YS`, rank `STRAIN`, parent `NCBITaxon:1515`, genetic code 11, exact synonyms for the older `Clostridium`, `Hungateiclostridium`, and `Ruminiclostridium` YS combinations, source set `ncbitaxon|gtdb|gold|madin_etal`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the strain below `Acetivibrio thermocellus`, `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/gtdb_species.tsv` line 74478 and `data/raw/gtdb_mappings.tsv` line 3295 support the 13-genome `GTDB:s__Hungateiclostridium_thermocellum` `skos:closeMatch` mapping to `NCBITaxon:1094188`.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_thermocellus_ys`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 26391 keeps this taxon in scope as `attested rule: Acetivibrio thermocellus YS, 4 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv` line 1723 and `data/raw/madin_taxa.tsv` line 2143 supply the direct GOLD and MADIN source attestations represented on this compact child record.
- `data/raw/bacdive_strains.tsv` line 22771 files the YS / DSM 25991 BacDive strain under the parent species `NCBITaxon:1515`; its `data/raw/strain_assemblies.tsv` line 107781 and `data/raw/strain_genome_records.tsv` lines 86744-86745 are therefore represented on `acetivibrio_thermocellus.yaml`.

## Completeness

- NCBITAXON, GTDB, GOLD, and MADIN attestations are represented with the expected assertion units and counts.
- The one local GTDB species mapping is represented with 13 genomes, and its source label is carried as an exact synonym.
- `strain_count: 0` is consistent with BacDive YS being filed at the parent `Acetivibrio thermocellus` record rather than directly at this NCBI child strain.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
