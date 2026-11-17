# YAML Record Review: Streptococcus phocae subsp. salmonis
## Target
- Path: `data/taxa/bacteria/streptococcus_phocae_subsp_salmonis.yaml`
- Identifier: `NCBITaxon:1000562`
- Label: `Streptococcus phocae subsp. salmonis`
- Domain: `BACTERIA`
- Rank: `SUBSPECIES`

## Validation
- PASS: `just validate data/taxa/bacteria/streptococcus_phocae_subsp_salmonis.yaml`
- PASS: `just validate-strict data/taxa/bacteria/uncultured_marine_eubacterium_hstpl46.yaml data/taxa/bacteria/escherichia_coli_vdp.yaml data/taxa/bacteria/pseudomonas_aeruginosa_aes_1r.yaml data/taxa/bacteria/streptococcus_phocae_subsp_salmonis.yaml`
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
  - `NCBITaxon:1000562	Streptococcus phocae subsp. salmonis	SUBSPECIES	NCBITaxon:119224	11	...	ncbitaxon|gtdb|bacdive|mediadive|gold|madin_etal|bactotraits		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the NCBI and same-taxon auxiliary attestations.
- `mapping_status: SEEDED` accurately reflects a generated record that has not been manually curated beyond the source import.
- `parent_taxon: NCBITaxon:119224` is represented in the lineage as `Streptococcus phocae`, and the lineage is internally coherent:
  - `Bacteria` -> `Bacillati` -> `Bacillota` -> `Bacilli` -> `Lactobacillales` -> `Streptococcaceae` -> `Streptococcus` -> `Streptococcus phocae`
- The GTDB mapping is internally linked through `taxonomy_mappings`, `xrefs`, and `source_attestations`, and exact raw rows in `data/raw/gtdb_species.tsv` and `data/raw/gtdb_mappings.tsv` confirm `GTDB:s__Streptococcus_phocae` with two genomes.
- The three seeded synonyms match the pinned NCBI and GTDB source rows:
  - `Streptococcus phocae`
  - `Streptococcus phocae C-4`
  - `Streptococcus phocae subsp. salmonis Avendano-Herrara et al. 2014`
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` covers the seven expected source groups: `NCBITAXON` name count 1, `GTDB` genome count 2, `BACDIVE` strain count 1, `MEDIADIVE` medium count 2, `GOLD` organism count 5, `MADIN` trait assertion count 1, and `BACTOTRAITS` trait assertion count 1.
- `strain_count: 1` matches the exact `data/raw/bacdive_strains.tsv` row for strain `C-4`, with culture IDs `CECT-7921` and `DSM-24768`.
- The BacDive strain preserves its NCBI assembly `GCA_000772915`, IMG genome `img.taxon:2627853798`, and BV-BRC/PATRIC genome `patric:1000562.3` from exact rows in `data/raw/strain_assemblies.tsv` and `data/raw/strain_genome_records.tsv`.
- The related-record block is grounded by exact GOLD rows for `gold:Go0259479` and `gold:Go0259480`, plus two ignored-file-inclusive exact `data/straininfo/strain_links.tsv` rows for `straininfo.strain:393977`.
- Exact rows in `data/raw/mediadive_taxa.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/bactotraits_taxa.tsv` match the MediaDive, GOLD, Madin, and BactoTraits assertion counts.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- The record carries NCBI taxonomy, GTDB mapping, BacDive strain, MediaDive medium, GOLD organism, Madin trait, BactoTraits trait, and StrainInfo deposit evidence expected for this seven-source seeded subspecies.
- NCBI type material designations for `CECT 7921`, `DSM 24768`, and `C-4` are represented as culture collection IDs on the sole BacDive strain or as the BacDive designation itself.
- No causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding or scope expansion if future GTDB, BacDive, MediaDive, GOLD, StrainInfo, Madin, or BactoTraits snapshots add same-taxon evidence for `NCBITaxon:1000562`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
