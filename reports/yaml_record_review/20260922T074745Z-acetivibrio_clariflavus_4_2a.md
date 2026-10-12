# YAML Record Review: Acetivibrio clariflavus 4-2a

## Target

- File: `data/taxa/bacteria/acetivibrio_clariflavus_4_2a.yaml`
- Identifier: `NCBITaxon:1045012`
- PATHS.tsv row: 16993
- Label: `Acetivibrio clariflavus 4-2a`
- Rank/domain: `STRAIN` / `BACTERIA`
- Parent: `NCBITaxon:288965` (`Acetivibrio clariflavus`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_clariflavus_4_2a.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_clariflavus.yaml data/taxa/bacteria/acetivibrio_clariflavus_4_2a.yaml data/taxa/bacteria/acetivibrio_clariflavus_dsm_19732.yaml data/taxa/bacteria/acetivibrio_ethanolgignens.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial strain taxon under `Acetivibrio clariflavus`.
- `data/raw/ncbitaxon_taxa.tsv` line 224369 pins `NCBITaxon:1045012` to label `Acetivibrio clariflavus 4-2a`, rank `STRAIN`, parent `NCBITaxon:288965`, genetic code 11, exact NCBI strain synonyms for `Clostridium clariflavum 4-2a` and `Hungateiclostridium clariflavum 4-2a`, source set `ncbitaxon|gtdb|madin_etal`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the strain below `Acetivibrio clariflavus`, `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/gtdb_species.tsv` line 3277 and `data/raw/gtdb_mappings.tsv` line 1765 support the six-genome `GTDB:s__Acetivibrio_clariflavus` `skos:closeMatch` mapping to `NCBITaxon:1045012`.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_clariflavus_4_2a`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 36247 keeps this taxon in scope as `attested rule: Acetivibrio clariflavus 4-2a, 3 sources incl. NCBI`.
- The GTDB mapping row supplies the source label carried as the GTDB-sourced exact synonym `Acetivibrio clariflavus`.
- The compact strain record has no BacDive, GOLD, AllTheBacteria, NCBI Assembly, or StrainInfo rows to project; the available local evidence is represented by NCBI taxonomy, GTDB, and MADIN source attestations.

## Completeness

- NCBITAXON, GTDB, and MADIN attestations are represented with the expected assertion units and counts.
- The one local GTDB species mapping is represented as a strain-level `skos:closeMatch` with six genomes and an exact synonym carrying the GTDB source ID.
- `strain_count: 0` is consistent with the absence of same-strain BacDive or StrainInfo child entries in the reviewed source rows.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
