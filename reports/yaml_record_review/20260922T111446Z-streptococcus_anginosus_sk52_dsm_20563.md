# YAML Record Review: Streptococcus anginosus SK52 = DSM 20563
## Target
- Path: `data/taxa/bacteria/streptococcus_anginosus_sk52_dsm_20563.yaml`
- Identifier: `NCBITaxon:1000570`
- Label: `Streptococcus anginosus SK52 = DSM 20563`
- Domain: `BACTERIA`
- Rank: `STRAIN`

## Validation
- PASS: `just validate data/taxa/bacteria/streptococcus_anginosus_sk52_dsm_20563.yaml`
- PASS: `just validate-strict data/taxa/bacteria/megasphaera_sp_upii_135_e.yaml data/taxa/bacteria/uncultured_marine_eubacterium_hstpl48.yaml data/taxa/bacteria/streptococcus_anginosus_sk52_dsm_20563.yaml data/taxa/bacteria/uncultured_marine_eubacterium_hstpl51.yaml`
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
  - `NCBITaxon:1000570	Streptococcus anginosus SK52 = DSM 20563	STRAIN	NCBITaxon:1328	11	...	ncbitaxon|gtdb|gold|madin_etal		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the NCBI, GTDB, GOLD, and Madin source attestations.
- `mapping_status: SEEDED` accurately reflects a generated record that has not been manually curated beyond the source import.
- `parent_taxon: NCBITaxon:1328` is represented in the lineage as `Streptococcus anginosus`, and the lineage is internally coherent:
  - `Bacteria` -> `Bacillati` -> `Bacillota` -> `Bacilli` -> `Lactobacillales` -> `Streptococcaceae` -> `Streptococcus` -> `Streptococcus anginosus group` -> `Streptococcus anginosus`
- The GTDB mapping is internally linked through `taxonomy_mappings`, `xrefs`, and `source_attestations`, and exact raw rows in `data/raw/gtdb_species.tsv` and `data/raw/gtdb_mappings.tsv` confirm `GTDB:s__Streptococcus_anginosus` with 51 genomes.
- The eight NCBI exact synonyms and the GTDB exact synonym match the pinned source rows, including `Streptococcus anginosus DSM 20563`, `Streptococcus anginosus DSM 20563 = SK52`, and `Streptococcus anginosus SK52`.
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` covers the four direct source groups: `NCBITAXON` name count 1, `GTDB` genome count 51, `GOLD` organism count 4, and `MADIN` trait assertion count 5.
- Exact rows in `data/raw/gold_organisms.tsv` and `data/raw/madin_taxa.tsv` match the GOLD and Madin assertion counts.
- Same-taxon raw assembly and ATB/StrainInfo rows for SK52 exist, but the exact `data/raw/bacdive_strains.tsv` row for `kgmicrobe.strain:bacdive_14717` is filed at `NCBITaxon:1328|NCBITaxon:1671923`; the generated exact SK52 record therefore has `strain_count: 0` and no BacDive or StrainInfo source attestation.
- An ignored-file-inclusive exact scan of `data/atb` found SK52 assemblies linked through the parent-keyed BacDive strain and no direct ATB source attestation on this record.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- The record carries the fields expected for an NCBI/GTDB/GOLD/Madin-seeded bacterial strain record.
- Exact synonyms from NCBI and GTDB are preserved; no direct same-taxon BacDive strain inventory, publications, or causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding or scope expansion if future BacDive, ATB, StrainInfo, GTDB, GOLD, or Madin snapshots link direct same-taxon evidence to `NCBITaxon:1000570`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
