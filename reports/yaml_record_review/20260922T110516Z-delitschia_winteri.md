# YAML Record Review: Delitschia winteri
## Target
- Path: `data/taxa/eukaryota/delitschia_winteri.yaml`
- Identifier: `NCBITaxon:100052`
- Label: `Delitschia winteri`
- Domain: `EUKARYOTA`
- Rank: `SPECIES`

## Validation
- PASS: `just validate data/taxa/eukaryota/delitschia_winteri.yaml`
- PASS: `just validate-strict data/taxa/eukaryota/melanomma_pulvis_pyrius.yaml data/taxa/eukaryota/delitschia_winteri.yaml data/taxa/bacteria/leptospira_alexanderi.yaml data/taxa/bacteria/uncultured_marine_eubacterium_hstpl2.yaml`
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
  - `NCBITaxon:100052	Delitschia winteri	SPECIES	NCBITaxon:100051	1	...	gold		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the NCBI and GOLD source attestations.
- `mapping_status: SEEDED` accurately reflects a generated record that has not been manually curated beyond the source import.
- `parent_taxon: NCBITaxon:100051` is represented in the lineage as `Delitschia`, and the lineage is internally coherent down to `Delitschiaceae` -> `Delitschia`.
- The seeded synonym `Delitschia winteri Plowr. ex G. Winter, 1874` matches the NCBI related-synonym field in `data/raw/ncbitaxon_taxa.tsv`.
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` contains one `NCBITAXON` name assertion for `NCBITaxon:100052`, with `source_label: Delitschia winteri` and `assertion_count: 1`.
- `source_attestations` also contains a `GOLD` organism assertion for `NCBITaxon:100052`, and the exact `data/raw/gold_organisms.tsv` row reports `organism_count: 1`.
- An ignored-file-inclusive exact scan of `data/atb` and `data/straininfo` found no same-taxon bacterial auxiliary rows for this eukaryotic record.
- An ignored-file-inclusive exact scan of GTDB raw inputs for `NCBITaxon:100052` and `Delitschia winteri` found no GTDB crosswalk evidence.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- The record carries the fields expected for an NCBI-and-GOLD-seeded fungal species.
- `strain_count: 0` is consistent with the absence of local ATB and StrainInfo same-taxon links.
- The NCBI related synonym is preserved; no strain inventory, publications, or causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding or scope expansion if a future GOLD, ATB, StrainInfo, or GTDB snapshot links additional genomes or strains to `NCBITaxon:100052`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
