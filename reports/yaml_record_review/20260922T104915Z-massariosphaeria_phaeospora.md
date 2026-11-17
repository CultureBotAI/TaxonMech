# YAML Record Review: Massariosphaeria phaeospora
## Target
- Path: `data/taxa/eukaryota/massariosphaeria_phaeospora.yaml`
- Identifier: `NCBITaxon:100035`
- Label: `Massariosphaeria phaeospora`
- Domain: `EUKARYOTA`
- Rank: `SPECIES`

## Validation
- PASS: `just validate data/taxa/eukaryota/massariosphaeria_phaeospora.yaml`
- PASS: `just validate-strict data/taxa/bacteria/arcanobacterium_sp_3656_05.yaml data/taxa/bacteria/arcanobacterium_sp_5773_06.yaml data/taxa/bacteria/arcanobacterium_sp_6462_07.yaml data/taxa/eukaryota/massariosphaeria_phaeospora.yaml`
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
  - `NCBITaxon:100035	Massariosphaeria phaeospora	SPECIES	NCBITaxon:100034	1	...	gold		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the NCBI and GOLD source attestations.
- `mapping_status: SEEDED` accurately reflects a generated record that has not been manually curated beyond the source import.
- `parent_taxon: NCBITaxon:100034` is represented in the lineage as `Massariosphaeria`, and the lineage is internally coherent down to `Pleosporales incertae sedis` -> `Massariosphaeria`.
- The three seeded synonyms match the NCBI synonym fields in `data/raw/ncbitaxon_taxa.tsv`:
  - `Leptosphaeria phaeospora`
  - `Leptosphaeria phaeospora E. Mull., 1950`
  - `Massariosphaeria phaeospora (E. Mull.) Crivelli, 1983`
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` contains one `NCBITAXON` name assertion for `NCBITaxon:100035`, with `source_label: Massariosphaeria phaeospora` and `assertion_count: 1`.
- `source_attestations` also contains a `GOLD` organism assertion for `NCBITaxon:100035`, and the exact `data/raw/gold_organisms.tsv` row reports `organism_count: 2`.
- An ignored-file-inclusive exact scan of `data/atb` and `data/straininfo` found no same-taxon bacterial auxiliary rows for this eukaryotic record.
- An ignored-file-inclusive exact scan of `data/raw/gtdb_mappings.tsv` and `data/raw/gtdb_species.tsv` for `NCBITaxon:100035` and `Massariosphaeria phaeospora` found no GTDB crosswalk evidence.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- The record carries the fields expected for an NCBI-and-GOLD-seeded fungal species.
- `strain_count: 0` is consistent with the absence of local ATB and StrainInfo same-taxon links.
- Synonyms from NCBI are preserved; no strain inventory, publications, or causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding or scope expansion if a future GOLD, ATB, StrainInfo, or GTDB snapshot links additional genomes or strains to `NCBITaxon:100035`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
