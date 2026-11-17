# YAML Record Review: Acetivibrio thermocellus JW20

## Target

- File: `data/taxa/bacteria/acetivibrio_thermocellus_jw20.yaml`
- Identifier: `NCBITaxon:492476`
- PATHS.tsv row: 519593
- Label: `Acetivibrio thermocellus JW20`
- Rank/domain: `STRAIN` / `BACTERIA`
- Parent: `NCBITaxon:1515` (`Acetivibrio thermocellus`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_thermocellus_jw20.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_thermocellus_dsm_1313.yaml data/taxa/bacteria/acetivibrio_thermocellus_dsm_2360.yaml data/taxa/bacteria/acetivibrio_thermocellus_jw20.yaml data/taxa/bacteria/acetivibrio_thermocellus_ys.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial strain taxon under `Acetivibrio thermocellus`.
- `data/raw/ncbitaxon_taxa.tsv` line 111402 pins `NCBITaxon:492476` to label `Acetivibrio thermocellus JW20`, rank `STRAIN`, parent `NCBITaxon:1515`, genetic code 11, exact synonyms for DSM 4150 / JW20 in the older `Clostridium`, `Hungateiclostridium`, and `Ruminiclostridium` combinations, source set `ncbitaxon|madin_etal`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the strain below `Acetivibrio thermocellus`, `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_thermocellus_jw20`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 55832 keeps this taxon in scope as `attested rule: Acetivibrio thermocellus JW20, 2 sources incl. NCBI`.
- `data/raw/madin_taxa.tsv` line 25417 supplies the direct MADIN source attestation represented on this compact child record.
- `data/raw/bacdive_strains.tsv` line 2632 files the JW20 / DSM 4150 BacDive strain under the parent species `NCBITaxon:1515`; its `data/raw/strain_assemblies.tsv` lines 117778-117781, `data/raw/strain_genome_records.tsv` lines 94686-94690, and `data/raw/strain_related_records.tsv` lines 340093-340101 are therefore represented on `acetivibrio_thermocellus.yaml`.

## Completeness

- NCBITAXON and MADIN attestations are represented with the expected assertion units and counts.
- The four older NCBI strain synonyms are present as exact synonyms.
- `strain_count: 0` is consistent with BacDive JW20 being filed at the parent `Acetivibrio thermocellus` record rather than directly at this NCBI child strain.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
