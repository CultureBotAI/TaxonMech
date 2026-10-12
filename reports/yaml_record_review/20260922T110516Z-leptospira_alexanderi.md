# YAML Record Review: Leptospira alexanderi
## Target
- Path: `data/taxa/bacteria/leptospira_alexanderi.yaml`
- Identifier: `NCBITaxon:100053`
- Label: `Leptospira alexanderi`
- Domain: `BACTERIA`
- Rank: `SPECIES`

## Validation
- PASS: `just validate data/taxa/bacteria/leptospira_alexanderi.yaml`
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
  - `NCBITaxon:100053	Leptospira alexanderi	SPECIES	NCBITaxon:171	11	...	ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the NCBI and same-taxon auxiliary attestations.
- `mapping_status: SEEDED` accurately reflects a generated record that has not been manually curated beyond the source import.
- `parent_taxon: NCBITaxon:171` is represented in the lineage as `Leptospira`, and the lineage is internally coherent:
  - `Bacteria` -> `Pseudomonadati` -> `Spirochaetota` -> `Leptospiria` -> `Leptospirales` -> `Leptospiraceae` -> `Leptospira`
- The LPSN nomenclature block matches the local `data/raw/lpsn_names.tsv` row for `lpsn:784131`, including the GTDB cross-reference, ATCC/DSM type strain designations, two DOI/one PMID publication set, and `INSDC:AY631880` sequence accession.
- The GTDB mapping is internally linked through `taxonomy_mappings`, `xrefs`, and `source_attestations`, and exact raw rows in `data/raw/gtdb_species.tsv` and `data/raw/gtdb_mappings.tsv` confirm `GTDB:s__Leptospira_alexanderi` with six genomes.
- The four NCBI-seeded synonyms match `data/raw/ncbitaxon_taxa.tsv`: `Leptospira alexanderi Brenner et al. 1999`, `Leptospira genomosp. 2`, `Leptospira genomospecies 2`, and `Leptospira genospecies 2`.
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` covers the six expected source groups: `NCBITAXON` name count 1, `LPSN` name count 1, `GTDB` genome count 6, `BACDIVE` strain count 5, `GOLD` organism count 11, and `MADIN` trait assertion count 2.
- `strain_count: 5` matches the five exact `data/raw/bacdive_strains.tsv` rows for `NCBITaxon:100053`, including the `L 60, Manhao 3` type strain and four CRBIP strains.
- The type strain related-record block is grounded by exact `data/raw/strain_related_records.tsv` rows for GOLD organisms `gold:Go0610162` and `gold:Go0610163`, plus the ignored-file-inclusive exact `data/straininfo/strain_links.tsv` row for `straininfo.strain:46965`.
- `data/raw/gold_organisms.tsv` reports 11 same-taxon GOLD organisms for `NCBITaxon:100053`, matching the `GOLD` source attestation.
- `data/raw/madin_taxa.tsv` reports two direct Madin trait assertions for `NCBITaxon:100053`, matching the `MADIN` source attestation.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- The record carries NCBI taxonomy, LPSN nomenclature, GTDB mapping, BacDive strain, GOLD organism, Madin trait, and StrainInfo type-strain evidence expected for this six-source seeded species.
- LPSN type designations are represented as culture collection IDs on the type strain, and the ATCC 700520 StrainInfo sequence/deposit records are attached under the BacDive type strain as related records.
- No causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding or scope expansion if future LPSN, GTDB, BacDive, GOLD, StrainInfo, or Madin snapshots add same-taxon evidence for `NCBITaxon:100053`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
