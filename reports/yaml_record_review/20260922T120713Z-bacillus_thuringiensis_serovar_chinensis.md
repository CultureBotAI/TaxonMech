# YAML Record Review: Bacillus thuringiensis serovar chinensis
## Target
- Path: `data/taxa/bacteria/bacillus_thuringiensis_serovar_chinensis.yaml`
- Identifier: `NCBITaxon:1001229`
- Label: `Bacillus thuringiensis serovar chinensis`
- Domain: `BACTERIA`
- Rank: `NO_RANK`

## Validation
- PASS: `just validate data/taxa/bacteria/bacillus_thuringiensis_serovar_chinensis.yaml`
- PASS: `just validate-strict data/taxa/bacteria/francisella_endosymbiont_of_ornitnodoros_porcinus.yaml data/taxa/bacteria/avibacterium_paragallinarum_72c.yaml data/taxa/bacteria/avibacterium_paragallinarum_72c1.yaml data/taxa/bacteria/bacillus_thuringiensis_serovar_chinensis.yaml`
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
- `identifier`, `label`, `rank`, `parent_taxon`, `genetic_code`, and exact synonym match the pinned NCBI source row in `data/raw/ncbitaxon_taxa.tsv`:
  - `NCBITaxon:1001229	Bacillus thuringiensis serovar chinensis	NO_RANK	NCBITaxon:1428	11	Bacillus thuringiensis subsp. chinensis	...	ncbitaxon		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the source attestation.
- `mapping_status: SEEDED` accurately reflects a generated NCBI-only seed.
- The `NO_RANK` target is an ancestry-dependent infraspecific record under parent species `NCBITaxon:1428` / `Bacillus thuringiensis`, which keeps it inside TaxonMech's species-and-below scope.
- The lineage is internally coherent for a Bacillus thuringiensis serovar:
  - `Bacteria` -> `Bacillati` -> `Bacillota` -> `Bacilli` -> `Caryophanales` -> `Bacillaceae` -> `Bacillus` -> `Bacillus cereus group` -> `Bacillus thuringiensis`
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` contains the expected NCBI-only name assertion.
- The exact synonym `Bacillus thuringiensis subsp. chinensis` is present in the NCBI row and is represented in the YAML as an `EXACT_SYNONYM`.
- `curation_history` is consistent with `curation/seed_scope.tsv`: the record was in scope as an attested NCBI-only seed on `2026-09-13`.
- The related child strain `NCBITaxon:541229` / `Bacillus thuringiensis serovar chinensis CT-43` has separate local source rows and a separate record; no CT-43 evidence is incorrectly attached to this broader serovar record.
- An ignored-file-inclusive exact CURIE scan of local BacDive, GOLD, LPSN, MediaDive, MADIN, GTDB, StrainInfo, and NCBI merge raw inputs found no same-taxon auxiliary evidence for `NCBITaxon:1001229`.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- `strain_count: 0` is consistent with the absence of local BacDive and StrainInfo same-taxon rows.
- No LPSN nomenclature, GTDB mapping, GOLD organism row, MADIN trait assertion, publications, strain inventory, source-related strain records, or causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.
- No major findings.
- No minor findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding if a future source snapshot adds non-NCBI attestations or a rank update for `NCBITaxon:1001229`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
