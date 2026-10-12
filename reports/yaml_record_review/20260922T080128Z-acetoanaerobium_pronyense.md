# YAML Record Review: Acetoanaerobium pronyense

## Target

- File: `data/taxa/bacteria/acetoanaerobium_pronyense.yaml`
- Identifier: `NCBITaxon:1482736`
- PATHS.tsv row: 182202
- Label: `Acetoanaerobium pronyense`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:186831` (`Acetoanaerobium`)

## Validation

- `just validate data/taxa/bacteria/acetoanaerobium_pronyense.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrionales_bacterium.yaml data/taxa/bacteria/acetoanaerobium_noterae.yaml data/taxa/bacteria/acetoanaerobium_pronyense.yaml data/taxa/bacteria/acetoanaerobium_sp.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species taxon under `Acetoanaerobium`.
- `data/raw/ncbitaxon_taxa.tsv` line 379369 pins `NCBITaxon:1482736` to label `Acetoanaerobium pronyense`, rank `SPECIES`, parent `NCBITaxon:186831`, genetic code 11, related synonyms for `Acetoanaerobium pronyense Bes et al. 2015` and `Clostridium sp. ST07-YE`, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|bactotraits`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the record under `Acetoanaerobium`, Filifactoraceae, Peptostreptococcales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/lpsn_data.tsv` line 29751 identifies `lpsn:793068` as the legitimate, validly published, correct species name with authority `Bes et al. 2015`, type strains `DSM 27512` and `JCM 19400`, sequence `INSDC:KJ174056`, DOI/PMID publication references, and NCBITaxon/GTDB cross-references.
- `data/raw/gtdb_species.tsv` line 3284 and `data/raw/gtdb_mappings.tsv` line 31961 support the 1-genome `GTDB:s__Acetoanaerobium_pronyense` `skos:closeMatch` mapping to `NCBITaxon:1482736`.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetoanaerobium_pronyense`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 7969 keeps this taxon in scope as `attested rule: Acetoanaerobium pronyense, 7 sources incl. NCBI`.
- `data/raw/bacdive_strains.tsv` line 53703 supplies the ST07-YE / DSM 27512 / JCM 19400 type strain represented as `kgmicrobe.strain:bacdive_131392`.
- `data/raw/ncbi_type_material.tsv` lines 35340-35345 list the DSM 27512, JCM 19400, and ST07-YE variants for the same taxon.
- The strain-level genome and cross-reference rows are present in `data/raw/strain_assemblies.tsv` lines 20044-20052, `data/raw/strain_genome_records.tsv` lines 15550-15556, `data/raw/strain_related_records.tsv` lines 57465-57484, StrainInfo line 1933, and StrainInfo link line 11546.

## Completeness

- NCBITAXON, LPSN, GTDB, BACDIVE, MEDIADIVE, GOLD, and BACTOTRAITS source attestations are represented with the expected assertion units and counts.
- The LPSN block captures the correct-name status, both type culture identifiers, publications, and sequence accession.
- `strain_count: 1` is consistent with the single BacDive strain, and the DSM 27512 strain carries the local genome assemblies, genome records, and related BioProject/BioSample/GOLD/StrainInfo records from the local source inventories.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
