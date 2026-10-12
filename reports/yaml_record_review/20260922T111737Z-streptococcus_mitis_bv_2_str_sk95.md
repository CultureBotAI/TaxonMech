# YAML Record Review: Streptococcus mitis bv. 2 str. SK95
## Target
- Path: `data/taxa/bacteria/streptococcus_mitis_bv_2_str_sk95.yaml`
- Identifier: `NCBITaxon:1000588`
- Label: `Streptococcus mitis bv. 2 str. SK95`
- Domain: `BACTERIA`
- Rank: `STRAIN`

## Validation
- PASS: `just validate data/taxa/bacteria/streptococcus_mitis_bv_2_str_sk95.yaml`
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
  - `NCBITaxon:1000588	Streptococcus mitis bv. 2 str. SK95	STRAIN	NCBITaxon:1458253	11	...	ncbitaxon|gtdb|gold|madin_etal		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the NCBI, GTDB, GOLD, and Madin source attestations.
- `mapping_status: SEEDED` accurately reflects a generated record that has not been manually curated beyond the source import.
- `parent_taxon: NCBITaxon:1458253` is represented in the lineage as `Streptococcus oralis subsp. dentisani`, and the lineage is internally coherent:
  - `Bacteria` -> `Bacillati` -> `Bacillota` -> `Bacilli` -> `Lactobacillales` -> `Streptococcaceae` -> `Streptococcus` -> `Streptococcus oralis` -> `Streptococcus oralis subsp. dentisani`
- The GTDB mapping is internally linked through `taxonomy_mappings`, `xrefs`, and `source_attestations`, and exact raw rows in `data/raw/gtdb_species.tsv` and `data/raw/gtdb_mappings.tsv` confirm `GTDB:s__Streptococcus_mitis_AY` with one genome.
- The NCBI exact synonym `Streptococcus mitis bv. 2 strain SK95` and the GTDB exact synonym `Streptococcus mitis AY` match the pinned source rows.
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` covers the four expected source groups: `NCBITAXON` name count 1, `GTDB` genome count 1, `GOLD` organism count 1, and `MADIN` trait assertion count 1.
- Exact rows in `data/raw/gold_organisms.tsv` and `data/raw/madin_taxa.tsv` match the GOLD and Madin assertion counts.
- An ignored-file-inclusive exact scan of `data/atb` and `data/straininfo` found no same-taxon ATB or StrainInfo auxiliary rows.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- The record carries the fields expected for an NCBI/GTDB/GOLD/Madin-seeded bacterial strain record.
- `strain_count: 0` is consistent with the absence of local BacDive, ATB, and StrainInfo same-taxon links.
- Exact synonyms from NCBI and GTDB are preserved; no direct strain inventory, publications, or causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding or scope expansion if a future BacDive, ATB, StrainInfo, GTDB, GOLD, or Madin snapshot links additional direct same-taxon evidence to `NCBITaxon:1000588`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
