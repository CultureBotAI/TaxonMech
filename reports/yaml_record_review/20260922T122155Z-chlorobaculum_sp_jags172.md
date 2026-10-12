# YAML Record Review: Chlorobaculum sp. JAGS172
## Target
- Path: `data/taxa/bacteria/chlorobaculum_sp_jags172.yaml`
- Identifier: `NCBITaxon:1001363`
- Label: `Chlorobaculum sp. JAGS172`
- Domain: `BACTERIA`
- Rank: `SPECIES`

## Validation
- PASS: `just validate data/taxa/bacteria/chlorobaculum_sp_jags172.yaml`
- PASS: `just validate-strict data/taxa/bacteria/prosthecochloris_sp_jags170.yaml data/taxa/bacteria/chlorobaculum_sp_jags171.yaml data/taxa/bacteria/chlorobaculum_sp_jags172.yaml data/taxa/bacteria/chlorobaculum_sp_jags173.yaml`
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
  - `NCBITaxon:1001363	Chlorobaculum sp. JAGS172	SPECIES	NCBITaxon:2685250	11	...	ncbitaxon		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the source attestation.
- `mapping_status: SEEDED` accurately reflects a generated NCBI-only seed.
- `parent_taxon: NCBITaxon:2685250` is represented in the lineage as `unclassified Chlorobaculum`.
- The lineage is internally coherent for a Chlorobaculum record:
  - `Bacteria` -> `Pseudomonadati` -> `FCB group` -> `Bacteroidota/Chlorobiota group` -> `Chlorobiota` -> `Chlorobiia` -> `Chlorobiales` -> `Chlorobiaceae` -> `Chlorobaculum` -> `unclassified Chlorobaculum`
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` contains the expected NCBI-only name assertion.
- `curation_history` is consistent with `curation/seed_scope.tsv`: the record was in scope as an attested NCBI-only seed on `2026-09-13`.
- An ignored-file-inclusive exact CURIE scan of local BacDive, GOLD, LPSN, MediaDive, MADIN, GTDB, StrainInfo, and NCBI merge raw inputs found no same-taxon auxiliary evidence for `NCBITaxon:1001363`.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- `strain_count: 0` is consistent with the absence of local BacDive and StrainInfo same-taxon rows.
- No synonyms, LPSN nomenclature, GTDB mapping, GOLD organism row, MADIN trait assertion, publications, strain inventory, source-related strain records, or causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.
- No major findings.
- No minor findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding if a future source snapshot adds non-NCBI attestations for `NCBITaxon:1001363`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
