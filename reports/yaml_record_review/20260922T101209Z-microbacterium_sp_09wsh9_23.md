# YAML Record Review: Microbacterium sp. 09WSH9-23
## Target
- Path: `data/taxa/bacteria/microbacterium_sp_09wsh9_23.yaml`
- Identifier: `NCBITaxon:1000232`
- Label: `Microbacterium sp. 09WSH9-23`
- Domain: `BACTERIA`
- Rank: `SPECIES`

## Validation
- PASS: `just validate data/taxa/bacteria/microbacterium_sp_09wsh9_23.yaml`
- PASS: `just validate-strict data/taxa/bacteria/microbacterium_sp_09wsh9_23.yaml data/taxa/bacteria/sphingomonas_sp_09wsh9_24.yaml data/taxa/bacteria/methylobacterium_sp_09wsh9_25.yaml data/taxa/bacteria/sphingomonas_sp_09wsh9_27.yaml`
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
  - `NCBITaxon:1000232	Microbacterium sp. 09WSH9-23	SPECIES	NCBITaxon:2609290	11	...	ncbitaxon		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the source attestation.
- `mapping_status: SEEDED` accurately reflects a generated record that has not been manually curated beyond the source import.
- `parent_taxon: NCBITaxon:2609290` is represented in the lineage as `unclassified Microbacterium`, and the remaining lineage is internally coherent:
  - `Bacteria` -> `Actinomycetota` -> `Actinomycetes` -> `Micrococcales` -> `Microbacteriaceae` -> `Microbacterium` -> `unclassified Microbacterium`
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` contains one `NCBITAXON` name assertion for `NCBITaxon:1000232`, with `source_label: Microbacterium sp. 09WSH9-23` and `assertion_count: 1`.
- An exact keyed scan of `data/raw/ncbitaxon_taxa.tsv`, plus an ignored-file-inclusive exact scan of `data/atb` and `data/straininfo`, found only the NCBI taxonomy row for this record; no same-taxon ATB or StrainInfo auxiliary rows were present.
- An ignored-file-inclusive exact scan of `data/raw/gtdb_mappings.tsv` and `data/raw/gtdb_species.tsv` for `NCBITaxon:1000232` and `Microbacterium sp. 09WSH9-23` found no GTDB crosswalk evidence.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- The record carries the fields expected for a minimal NCBI-only seeded bacterial species placeholder.
- `strain_count: 0` is consistent with the absence of local ATB and StrainInfo same-taxon links.
- No GTDB mapping, strain inventory, synonyms, publications, or causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding or scope expansion if a future ATB, StrainInfo, or GTDB snapshot links genomes or strains to `NCBITaxon:1000232`.

## Additional Notes
- Before this report was written, an exact `find reports/yaml_record_review` probe for this stem and its batchmates found no prior report; `find` includes ignored report files.
