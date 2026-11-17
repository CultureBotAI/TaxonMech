# YAML Record Review: Garritya polymorpha
## Target
- Path: `data/taxa/bacteria/garritya_polymorpha.yaml`
- Identifier: `NCBITaxon:1001`
- Label: `Garritya polymorpha`
- Domain: `BACTERIA`
- Rank: `SPECIES`

## Validation
- PASS: `just validate data/taxa/bacteria/garritya_polymorpha.yaml`
- PASS: `just validate-strict data/taxa/bacteria/garritya_polymorpha.yaml data/taxa/bacteria/uncultured_marine_eubacterium_hstpl8.yaml data/taxa/bacteria/bacterium_ahbyk2010rs_1.yaml data/taxa/bacteria/uncultured_marine_eubacterium_hstpl81.yaml`
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
- `identifier`, `label`, `rank`, `parent_taxon`, `genetic_code`, synonyms, and the six-source scope match the pinned NCBI source row in `data/raw/ncbitaxon_taxa.tsv`:
  - `NCBITaxon:1001	Garritya polymorpha	SPECIES	NCBITaxon:1937995	11	Flexibacter polymorphus	...	ncbitaxon|bacdive|lpsn|mediadive|gold|madin_etal	...	2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the NCBI source attestation.
- `mapping_status: SEEDED` accurately reflects a generated record that has not been manually curated beyond the source import.
- `parent_taxon: NCBITaxon:1937995` is represented in the lineage as `Garritya`, and the bacterial lineage is internally coherent:
  - `Bacteria` -> `Pseudomonadati` -> `FCB group` -> `Bacteroidota/Chlorobiota group` -> `Bacteroidota` -> `Cytophagia` -> `Cytophagales` -> `Bernardetiaceae` -> `Garritya`
- The LPSN `lpsn:795343` source row supports the species name, `(Lewin 1974) Hahnke et al. 2017` authority, validly published and correct-name flags, five type-strain designations, three publications, and `INSDC:AB078059`.
- The LPSN `lpsn:776296` row supports `Flexibacter polymorphus` as a synonym that redirects to `lpsn:795343`.
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` is consistent with `curation/seed_scope.tsv` and the pinned raw inventories: NCBI name count 1, LPSN name count 1, BacDive strain count 1, MediaDive medium count 1, GOLD organism count 5, and MADIN trait assertion count 1.
- The BacDive row for `kgmicrobe.strain:bacdive_3794` links `NCBITaxon:1001`, `lpsn:795343`, and the ATCC 27820, DSM 9678, IFO 16703, and NBRC 16703 culture collection identifiers represented on the YAML strain.
- `data/straininfo/strain_links.tsv` corroborates the StrainInfo deposits for IFO 16703, ATCC 27820, DSM 9678, and NBRC 16703 against BacDive ID `3794` and `NCBITaxon:1001`.
- `data/raw/strain_related_records.tsv` supports the GOLD related records attached under the BacDive strain for `Garritya polymorpha ATCC 27820` and the `Flexibacter polymorphus` NBRC 16703, IFO 16703, and DSM 9678 records.
- The type-material strings imported from NCBI include ATCC 27820, DSM 9678, IFO 16703, LMG 13859, and NBRC 16703 variants, matching the same type-strain set LPSN exposes.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- The record carries the expected NCBI, LPSN, BacDive, MediaDive, GOLD, MADIN, and StrainInfo evidence available locally for this species.
- `strain_count: 1` is consistent with the single BacDive strain seed; the strain aggregates additional GOLD and StrainInfo related records rather than creating separate strain entries.
- No GTDB mapping or causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding if a future StrainInfo or BacDive snapshot exposes LMG 13859 as a same-taxon strain link rather than only as LPSN and NCBI type material.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
