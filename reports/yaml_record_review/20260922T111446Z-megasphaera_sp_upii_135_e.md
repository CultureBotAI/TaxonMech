# YAML Record Review: Megasphaera sp. UPII 135-E
## Target
- Path: `data/taxa/bacteria/megasphaera_sp_upii_135_e.yaml`
- Identifier: `NCBITaxon:1000569`
- Label: `Megasphaera sp. UPII 135-E`
- Domain: `BACTERIA`
- Rank: `SPECIES`

## Validation
- PASS: `just validate data/taxa/bacteria/megasphaera_sp_upii_135_e.yaml`
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
  - `NCBITaxon:1000569	Megasphaera sp. UPII 135-E	SPECIES	NCBITaxon:2626256	11	...	ncbitaxon|gtdb|madin_etal		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the NCBI, GTDB, and Madin source attestations.
- `mapping_status: SEEDED` accurately reflects a generated record that has not been manually curated beyond the source import.
- `parent_taxon: NCBITaxon:2626256` is represented in the lineage as `unclassified Megasphaera`, and the lineage is internally coherent:
  - `Bacteria` -> `Bacillati` -> `Bacillota` -> `Negativicutes` -> `Veillonellales` -> `Veillonellaceae` -> `Megasphaera` -> `unclassified Megasphaera`
- The GTDB mapping is internally linked through `taxonomy_mappings`, `xrefs`, and `source_attestations`, and exact raw rows in `data/raw/gtdb_species.tsv` and `data/raw/gtdb_mappings.tsv` confirm `GTDB:s__Megasphaera_hutchinsoni` with 11 genomes.
- The GTDB exact synonym `Megasphaera hutchinsoni` is preserved.
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` covers the three expected source groups: `NCBITAXON` name count 1, `GTDB` genome count 11, and `MADIN` trait assertion count 1.
- The exact `data/raw/madin_taxa.tsv` row reports one direct trait assertion for `NCBITaxon:1000569`, matching the `MADIN` source attestation.
- An ignored-file-inclusive exact scan of `data/atb` and `data/straininfo` found no same-taxon ATB or StrainInfo auxiliary rows.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- The record carries the fields expected for an NCBI/GTDB/Madin-seeded bacterial species record.
- `strain_count: 0` is consistent with the absence of local BacDive, ATB, and StrainInfo same-taxon links.
- No strain inventory, publications, or causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding or scope expansion if a future BacDive, ATB, StrainInfo, GTDB, or Madin snapshot links additional same-taxon evidence to `NCBITaxon:1000569`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
