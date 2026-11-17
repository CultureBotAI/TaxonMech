# YAML Record Review: Pavlova granifera
## Target
- Path: `data/taxa/eukaryota/pavlova_granifera.yaml`
- Identifier: `NCBITaxon:1000983`
- Label: `Pavlova granifera`
- Domain: `EUKARYOTA`
- Rank: `SPECIES`

## Validation
- PASS: `just validate data/taxa/eukaryota/pavlova_granifera.yaml`
- PASS: `just validate-strict data/taxa/bacteria/uncultured_marine_eubacterium_hstpl71.yaml data/taxa/bacteria/uncultured_marine_eubacterium_hstpl75.yaml data/taxa/eukaryota/pavlova_granifera.yaml data/taxa/bacteria/uncultured_marine_eubacterium_hstpl77.yaml`
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
- `identifier`, `label`, `rank`, `parent_taxon`, `genetic_code`, exact synonym, and related synonyms match the pinned NCBI source row in `data/raw/ncbitaxon_taxa.tsv`:
  - `NCBITaxon:1000983	Pavlova granifera	SPECIES	NCBITaxon:2831	1	Chrysocapsa granifera	Chrysocapsa granifera B.Mack, 1954|Pavlova granifera (B.Mack) J.C.Green, 1973	...	2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the source attestation.
- `mapping_status: SEEDED` accurately reflects a generated record that has not been manually curated beyond the source import.
- `parent_taxon: NCBITaxon:2831` is represented in the lineage as `Pavlova`, and the haptophyte lineage is internally coherent:
  - `Eukaryota` -> `Haptista` -> `Haptophyta` -> `Pavlovophyceae` -> `Pavlovales` -> `Pavlovaceae` -> `Pavlova`
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` contains the two expected source rows from `curation/seed_scope.tsv`: NCBI name count 1 and GOLD organism count 1.
- An exact keyed scan of `data/raw/gold_organisms.tsv` found the same assertion count represented in the YAML.
- An ignored-file-inclusive exact scan of `data/atb`, `data/straininfo`, GTDB, and MADIN raw inputs found no same-taxon auxiliary strain, GTDB, or MADIN rows for `NCBITaxon:1000983`.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- The record carries the expected NCBI and GOLD seed evidence for this eukaryotic species.
- `strain_count: 0` is consistent with the absence of local ATB and StrainInfo same-taxon links.
- No GTDB mapping, MADIN trait count, strain inventory, publications, or causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding or scope expansion if a future ATB, StrainInfo, GTDB, or MADIN snapshot links rows to `NCBITaxon:1000983`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
