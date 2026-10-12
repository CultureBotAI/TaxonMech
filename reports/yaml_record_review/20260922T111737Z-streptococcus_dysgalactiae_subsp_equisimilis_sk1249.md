# YAML Record Review: Streptococcus dysgalactiae subsp. equisimilis SK1249
## Target
- Path: `data/taxa/bacteria/streptococcus_dysgalactiae_subsp_equisimilis_sk1249.yaml`
- Identifier: `NCBITaxon:1000589`
- Label: `Streptococcus dysgalactiae subsp. equisimilis SK1249`
- Domain: `BACTERIA`
- Rank: `STRAIN`

## Validation
- PASS: `just validate data/taxa/bacteria/streptococcus_dysgalactiae_subsp_equisimilis_sk1249.yaml`
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
  - `NCBITaxon:1000589	Streptococcus dysgalactiae subsp. equisimilis SK1249	STRAIN	NCBITaxon:119602	11	...	ncbitaxon|gtdb|gold|madin_etal		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the NCBI, GTDB, GOLD, and Madin source attestations.
- `mapping_status: SEEDED` accurately reflects a generated record that has not been manually curated beyond the source import.
- `parent_taxon: NCBITaxon:119602` is represented in the lineage as `Streptococcus dysgalactiae subsp. equisimilis`, and the lineage is internally coherent:
  - `Bacteria` -> `Bacillati` -> `Bacillota` -> `Bacilli` -> `Lactobacillales` -> `Streptococcaceae` -> `Streptococcus` -> `Streptococcus dysgalactiae group` -> `Streptococcus dysgalactiae` -> `Streptococcus dysgalactiae subsp. equisimilis`
- The GTDB mapping is internally linked through `taxonomy_mappings`, `xrefs`, and `source_attestations`, and exact raw rows in `data/raw/gtdb_species.tsv` and `data/raw/gtdb_mappings.tsv` confirm `GTDB:s__Streptococcus_dysgalactiae` with 268 genomes.
- The two NCBI exact synonyms and one GTDB exact synonym match the pinned source rows:
  - `Streptococcus dysgalactiae`
  - `Streptococcus dysgalactiae subsp. equisimilis str. SK1249`
  - `Streptococcus dysgalactiae subsp. equisimilis strain SK1249`
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` covers the four expected source groups: `NCBITAXON` name count 1, `GTDB` genome count 268, `GOLD` organism count 1, and `MADIN` trait assertion count 1.
- Exact rows in `data/raw/gold_organisms.tsv` and `data/raw/madin_taxa.tsv` match the GOLD and Madin assertion counts.
- Raw assembly rows for SK1249 exist, but the exact `data/raw/bacdive_strains.tsv` row for `kgmicrobe.strain:bacdive_14801` is filed at parent subspecies `NCBITaxon:119602`; the generated exact SK1249 record therefore has `strain_count: 0` and no BacDive source attestation.
- An ignored-file-inclusive exact scan of `data/atb` and `data/straininfo` found no same-taxon ATB or StrainInfo auxiliary rows.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- The record carries the fields expected for an NCBI/GTDB/GOLD/Madin-seeded bacterial strain record.
- Exact synonyms from NCBI and GTDB are preserved; no direct same-taxon BacDive strain inventory, publications, or causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding or scope expansion if a future BacDive, ATB, StrainInfo, GTDB, GOLD, or Madin snapshot links additional direct same-taxon evidence to `NCBITaxon:1000589`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
