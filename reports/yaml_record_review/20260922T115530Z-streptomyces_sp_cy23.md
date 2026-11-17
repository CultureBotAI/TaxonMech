# YAML Record Review: Streptomyces sp. CY23
## Target
- Path: `data/taxa/bacteria/streptomyces_sp_cy23.yaml`
- Identifier: `NCBITaxon:1001155`
- Label: `Streptomyces sp. CY23`
- Domain: `BACTERIA`
- Rank: `SPECIES`

## Validation
- PASS: `just validate data/taxa/bacteria/streptomyces_sp_cy23.yaml`
- PASS: `just validate-strict data/taxa/bacteria/rhodococcus_sp_cy17.yaml data/taxa/bacteria/streptomyces_sp_126_7.yaml data/taxa/bacteria/streptomyces_sp_cy23.yaml data/taxa/bacteria/streptomyces_sp_ed4.yaml`
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
  - `NCBITaxon:1001155	Streptomyces sp. CY23	SPECIES	NCBITaxon:2593676	11	...	ncbitaxon		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the source attestation.
- `mapping_status: SEEDED` accurately reflects a generated NCBI-only seed.
- `parent_taxon: NCBITaxon:2593676` is represented in the lineage as `unclassified Streptomyces`.
- The lineage is internally coherent for a Streptomyces record:
  - `Bacteria` -> `Bacillati` -> `Actinomycetota` -> `Actinomycetes` -> `Kitasatosporales` -> `Streptomycetaceae` -> `Streptomyces` -> `unclassified Streptomyces`
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` contains the expected NCBI-only name assertion.
- `curation_history` is consistent with `curation/seed_scope.tsv`: the record was in scope as an attested NCBI-only seed on `2026-09-13`.
- An ignored-file-inclusive exact CURIE scan of BacDive, GOLD, LPSN, MediaDive, MADIN, GTDB, ATB, and StrainInfo raw inputs found no same-taxon auxiliary evidence for `NCBITaxon:1001155`; label-neighbor `CY23` rows belonged to different NCBITaxon identifiers.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- `strain_count: 0` is consistent with the absence of local BacDive, ATB, and StrainInfo same-taxon rows.
- No synonyms, LPSN nomenclature, GTDB mapping, publications, strain inventory, source-related strain records, or causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding if a future source snapshot adds non-NCBI attestations or a more resolved parent for `NCBITaxon:1001155`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
