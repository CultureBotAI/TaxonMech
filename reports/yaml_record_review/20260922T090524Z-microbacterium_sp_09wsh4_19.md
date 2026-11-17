# YAML Record Review: Microbacterium sp. 09WSH4-19
## Target
- Path: `data/taxa/bacteria/microbacterium_sp_09wsh4_19.yaml`
- Identifier: `NCBITaxon:1000119`
- Label: `Microbacterium sp. 09WSH4-19`
- Domain: `BACTERIA`
- Rank: `SPECIES`

## Validation
- PASS: `just validate data/taxa/bacteria/microbacterium_sp_09wsh4_19.yaml`
- PASS: `just validate-strict data/taxa/bacteria/microbacterium_sp_09wsh4_19.yaml data/taxa/bacteria/bartonella_sp_rr13863po.yaml data/taxa/bacteria/acidovorax_sp_09wsh4_20.yaml data/taxa/bacteria/sphingomonas_sp_09wsh4_21.yaml`
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
  - `NCBITaxon:1000119	Microbacterium sp. 09WSH4-19	SPECIES	NCBITaxon:2609290	11	...	ncbitaxon		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the source attestation.
- `mapping_status: SEEDED` accurately reflects a generated record that has not been manually curated beyond the source import.
- `parent_taxon: NCBITaxon:2609290` is represented in the lineage as `unclassified Microbacterium`, and the remaining lineage is internally coherent:
  - `Bacteria` -> `Actinomycetota` -> `Actinomycetes` -> `Micrococcales` -> `Microbacteriaceae` -> `Microbacterium` -> `unclassified Microbacterium`
- An ignored-file-inclusive `rg --no-ignore --hidden` check against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path entry and no curated seed-scope override.

## Evidence
- `source_attestations` contains one `NCBITAXON` name assertion for `NCBITaxon:1000119`, with `source_label: Microbacterium sp. 09WSH4-19` and `assertion_count: 1`.
- An ignored-file-inclusive exact scan of `data/raw`, `data/atb`, and `data/straininfo` for `NCBITaxon:1000119` found only the NCBI taxonomy row for this record; no same-taxon ATB or StrainInfo auxiliary rows were present.
- An ignored-file-inclusive exact scan of `data/raw/gtdb_mappings.tsv` and `data/raw/gtdb_species.tsv` for `NCBITaxon:1000119` and `Microbacterium sp. 09WSH4-19` found no GTDB crosswalk evidence.
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
- Re-run source seeding or scope expansion if a future ATB, StrainInfo, or GTDB snapshot links genomes or strains to `NCBITaxon:1000119`.

## Additional Notes
- Before this report was written, an exact `find reports/yaml_record_review -name '*microbacterium_sp_09wsh4_19.md' ...` probe found no prior report for this stem; `find` includes ignored report files.
