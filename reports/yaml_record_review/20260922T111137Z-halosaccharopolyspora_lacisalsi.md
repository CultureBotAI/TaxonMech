# YAML Record Review: Halosaccharopolyspora lacisalsi
## Target
- Path: `data/taxa/bacteria/halosaccharopolyspora_lacisalsi.yaml`
- Identifier: `NCBITaxon:1000566`
- Label: `Halosaccharopolyspora lacisalsi`
- Domain: `BACTERIA`
- Rank: `SPECIES`

## Validation
- PASS: `just validate data/taxa/bacteria/halosaccharopolyspora_lacisalsi.yaml`
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
  - `NCBITaxon:1000566	Halosaccharopolyspora lacisalsi	SPECIES	NCBITaxon:2893577	11	...	ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the same-taxon source attestations.
- `mapping_status: SEEDED` accurately reflects a generated record that has not been manually curated beyond the source import.
- `parent_taxon: NCBITaxon:2893577` is represented in the lineage as `Halosaccharopolyspora`, and the lineage is internally coherent:
  - `Bacteria` -> `Bacillati` -> `Actinomycetota` -> `Actinomycetes` -> `Pseudonocardiales` -> `Pseudonocardiaceae` -> `Halosaccharopolyspora`
- The LPSN nomenclature block matches the local `data/raw/lpsn_names.tsv` row for `lpsn:19174`, including the GTDB cross-reference, DSM/KCTC type strain designations, two DOI/one PMID publication set, and `INSDC:JF411070` sequence accession.
- The GTDB mapping is internally linked through `taxonomy_mappings`, `xrefs`, and `source_attestations`, and exact raw rows in `data/raw/gtdb_species.tsv` and `data/raw/gtdb_mappings.tsv` confirm `GTDB:s__Halosaccharopolyspora_lacisalsi` with one genome.
- NCBI and LPSN synonyms are preserved, including `Saccharopolyspora lacisalsi Guan et al. 2013` as an NCBI exact synonym and `Saccharopolyspora lacisalsi` as an LPSN related synonym.
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` covers the six expected source groups: `NCBITAXON` name count 1, `LPSN` name count 1, `GTDB` genome count 1, `BACDIVE` strain count 2, `GOLD` organism count 4, and `MADIN` trait assertion count 1.
- `strain_count: 2` matches the exact `data/raw/bacdive_strains.tsv` rows for the DSM/KCTC/TRM type strain and the `H194` strain carrying `DSM-46688`.
- The type strain preserves assembly and genome evidence from BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo; exact raw rows in `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and ignored `data/straininfo/strain_links.tsv` match those same identifiers.
- Exact rows in `data/raw/gold_organisms.tsv` and `data/raw/madin_taxa.tsv` match the GOLD and Madin assertion counts.
- An ignored-file-inclusive exact scan of `data/atb` found no same-taxon ATB auxiliary rows.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- The record carries NCBI taxonomy, LPSN nomenclature, GTDB mapping, BacDive strain, GOLD organism, Madin trait, and StrainInfo deposit evidence expected for this six-source seeded species.
- The LPSN type designations are represented as culture collection IDs on the BacDive type strain, and the StrainInfo DSM 45975 sequence/deposit record is attached under that strain.
- No causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding or scope expansion if future GTDB, BacDive, GOLD, StrainInfo, Madin, or LPSN snapshots add same-taxon evidence for `NCBITaxon:1000566`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
