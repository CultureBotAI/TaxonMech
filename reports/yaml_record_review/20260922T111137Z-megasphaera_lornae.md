# YAML Record Review: Megasphaera lornae
## Target
- Path: `data/taxa/bacteria/megasphaera_lornae.yaml`
- Identifier: `NCBITaxon:1000568`
- Label: `Megasphaera lornae`
- Domain: `BACTERIA`
- Rank: `SPECIES`

## Validation
- PASS: `just validate data/taxa/bacteria/megasphaera_lornae.yaml`
- PASS: `just validate-strict data/taxa/bacteria/methyloversatilis_universalis_fam5.yaml data/taxa/bacteria/halosaccharopolyspora_lacisalsi.yaml data/taxa/bacteria/bifidobacterium_longum_3_1_37dfaab.yaml data/taxa/bacteria/megasphaera_lornae.yaml`
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
  - `NCBITaxon:1000568	Megasphaera lornae	SPECIES	NCBITaxon:906	11	...	ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the same-taxon source attestations.
- `mapping_status: SEEDED` accurately reflects a generated record that has not been manually curated beyond the source import.
- `parent_taxon: NCBITaxon:906` is represented in the lineage as `Megasphaera`, and the lineage is internally coherent:
  - `Bacteria` -> `Bacillati` -> `Bacillota` -> `Negativicutes` -> `Veillonellales` -> `Veillonellaceae` -> `Megasphaera`
- The LPSN nomenclature block matches the local `data/raw/lpsn_names.tsv` row for `lpsn:18684`, including the GTDB cross-reference, ATCC/DSM type strain designations, two DOI/one PMID publication set, and `INSDC:MT906439` sequence accession.
- The GTDB mapping is internally linked through `taxonomy_mappings`, `xrefs`, and `source_attestations`, and exact raw rows in `data/raw/gtdb_species.tsv` and `data/raw/gtdb_mappings.tsv` confirm `GTDB:s__Megasphaera_lornae` with 16 genomes.
- The six seeded synonyms match the NCBI synonym fields in `data/raw/ncbitaxon_taxa.tsv`.
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` covers the seven expected source groups: `NCBITAXON` name count 1, `LPSN` name count 1, `GTDB` genome count 16, `BACDIVE` strain count 1, `MEDIADIVE` medium count 2, `GOLD` organism count 2, and `MADIN` trait assertion count 1.
- `strain_count: 1` matches the exact `data/raw/bacdive_strains.tsv` row for type strain `UPII 199-6, Type1`, with culture IDs `ATCC-TSD-205` and `DSM-111201`.
- The type strain preserves BacDive assembly `GCA_000214495`, IMG genome `img.taxon:651324070`, BV-BRC/PATRIC genome `patric:1000568.3`, and StrainInfo DSM 111201 deposit links from exact raw rows.
- Exact rows in `data/raw/mediadive_taxa.tsv`, `data/raw/gold_organisms.tsv`, and `data/raw/madin_taxa.tsv` match the MediaDive, GOLD, and Madin assertion counts.
- An ignored-file-inclusive exact scan of `data/atb` found no same-taxon ATB auxiliary rows.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- The record carries NCBI taxonomy, LPSN nomenclature, GTDB mapping, BacDive strain, MediaDive medium, GOLD organism, Madin trait, and StrainInfo deposit evidence expected for this seven-source seeded species.
- LPSN type designations are represented as culture collection IDs on the BacDive type strain, and the DSM 111201 StrainInfo records are attached under that strain.
- No causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding or scope expansion if future GTDB, BacDive, MediaDive, GOLD, StrainInfo, Madin, or LPSN snapshots add same-taxon evidence for `NCBITaxon:1000568`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
