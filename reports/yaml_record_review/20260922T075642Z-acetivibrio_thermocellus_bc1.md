# YAML Record Review: Acetivibrio thermocellus BC1

## Target

- File: `data/taxa/bacteria/acetivibrio_thermocellus_bc1.yaml`
- Identifier: `NCBITaxon:1349417`
- PATHS.tsv row: 124549
- Label: `Acetivibrio thermocellus BC1`
- Rank/domain: `ISOLATE` / `BACTERIA`
- Parent: `NCBITaxon:1515` (`Acetivibrio thermocellus`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_thermocellus_bc1.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_thermocellus.yaml data/taxa/bacteria/acetivibrio_thermocellus_ad2.yaml data/taxa/bacteria/acetivibrio_thermocellus_atcc_27405.yaml data/taxa/bacteria/acetivibrio_thermocellus_bc1.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial isolate taxon under `Acetivibrio thermocellus`.
- `data/raw/ncbitaxon_taxa.tsv` line 324928 pins `NCBITaxon:1349417` to label `Acetivibrio thermocellus BC1`, rank `ISOLATE`, parent `NCBITaxon:1515`, genetic code 11, exact synonyms for the older `Clostridium`, `Hungateiclostridium`, and `Ruminiclostridium` BC1 combinations, source set `ncbitaxon|gtdb`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the isolate below `Acetivibrio thermocellus`, `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/gtdb_species.tsv` line 74478 and `data/raw/gtdb_mappings.tsv` line 20424 support the 13-genome `GTDB:s__Hungateiclostridium_thermocellum` `skos:closeMatch` mapping to `NCBITaxon:1349417`.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_thermocellus_bc1`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 68532 keeps this taxon in scope as `attested rule: Acetivibrio thermocellus BC1, 2 sources incl. NCBI`.
- The GTDB mapping row supplies the source label carried as the GTDB-sourced exact synonym `Hungateiclostridium thermocellum`.
- A gitignore-independent exact scan for `NCBITaxon:1349417` under `data/raw`, `data/atb`, and `data/straininfo` found NCBI and GTDB evidence but no same-taxon BacDive, GOLD, AllTheBacteria, or StrainInfo rows.

## Completeness

- NCBITAXON and GTDB attestations are represented with the expected assertion units and counts.
- The one local GTDB species mapping is represented with 13 genomes, and its source label is carried as an exact synonym.
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
