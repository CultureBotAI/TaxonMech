# YAML Record Review: Staphylococcus epidermidis 14.1.R1.SE
## Target
- Path: `data/taxa/bacteria/staphylococcus_epidermidis_14_1_r1_se.yaml`
- Identifier: `NCBITaxon:1000590`
- Label: `Staphylococcus epidermidis 14.1.R1.SE`
- Domain: `BACTERIA`
- Rank: `STRAIN`

## Validation
- PASS: `just validate data/taxa/bacteria/staphylococcus_epidermidis_14_1_r1_se.yaml`
- PASS: `just validate-strict data/taxa/bacteria/streptococcus_mitis_bv_2_str_sk95.yaml data/taxa/bacteria/streptococcus_dysgalactiae_subsp_equisimilis_sk1249.yaml data/taxa/bacteria/uncultured_marine_eubacterium_hstpl78.yaml data/taxa/bacteria/staphylococcus_epidermidis_14_1_r1_se.yaml`
  - `files scanned: 4`
  - `files with ERROR: 0`
  - `total ERROR rows: 0`
- SKIPPED: `just validate-history`
  - This was a read-only review of a generated record and did not add a `history/` decision.
- SKIPPED: `just verify-corpus`
  - The record was unchanged; full-corpus verification was not rerun for this four-record review batch.
- NOT APPLICABLE: `just validate-products`
  - The record has no `causal_graphs`.

## Identity and Grounding
- `identifier`, `label`, `rank`, `parent_taxon`, and `genetic_code` match the pinned NCBI source row in `data/raw/ncbitaxon_taxa.tsv`:
  - `NCBITaxon:1000590	Staphylococcus epidermidis 14.1.R1.SE	STRAIN	NCBITaxon:1282	11	...	ncbitaxon|gtdb|madin_etal		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the NCBI, GTDB, and Madin source attestations.
- `mapping_status: SEEDED` accurately reflects a generated record that has not been manually curated beyond the source import.
- `parent_taxon: NCBITaxon:1282` is represented in the lineage as `Staphylococcus epidermidis`, and the lineage is internally coherent:
  - `Bacteria` -> `Bacillati` -> `Bacillota` -> `Bacilli` -> `Caryophanales` -> `Staphylococcaceae` -> `Staphylococcus` -> `Staphylococcus epidermidis`
- The GTDB mapping is internally linked through `taxonomy_mappings`, `xrefs`, and `source_attestations`, and exact raw rows in `data/raw/gtdb_species.tsv` and `data/raw/gtdb_mappings.tsv` confirm `GTDB:s__Staphylococcus_epidermidis` with 2165 genomes.
- The two NCBI exact synonyms and one GTDB exact synonym match the pinned source rows:
  - `Staphylococcus epidermidis`
  - `Staphylococcus epidermidis str. 14.1.R1.SE`
  - `Staphylococcus epidermidis strain 14.1.R1.SE`
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` covers the three expected source groups: `NCBITAXON` name count 1, `GTDB` genome count 2165, and `MADIN` trait assertion count 1.
- The exact `data/raw/madin_taxa.tsv` row reports one direct trait assertion for `NCBITaxon:1000590`, matching the `MADIN` source attestation.
- Raw GOLD assembly and related-record rows exist for this strain label, but the exact `data/raw/bacdive_strains.tsv` row for `kgmicrobe.strain:bacdive_156546` is filed at parent species `NCBITaxon:1282`; the generated exact strain record therefore has `strain_count: 0` and no BacDive or GOLD source attestation.
- An ignored-file-inclusive exact scan of `data/atb` and `data/straininfo` found no same-taxon ATB or StrainInfo auxiliary rows.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- The record carries the fields expected for an NCBI/GTDB/Madin-seeded bacterial strain record.
- Exact synonyms from NCBI and GTDB are preserved; no direct same-taxon BacDive strain inventory, publications, or causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding or scope expansion if a future BacDive, ATB, StrainInfo, GTDB, GOLD, or Madin snapshot links additional direct same-taxon evidence to `NCBITaxon:1000590`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
