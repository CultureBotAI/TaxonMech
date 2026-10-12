# YAML Record Review: Acetoanaerobium noterae

## Target

- File: `data/taxa/bacteria/acetoanaerobium_noterae.yaml`
- Identifier: `NCBITaxon:745369`
- PATHS.tsv row: 583338
- Label: `Acetoanaerobium noterae`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:186831` (`Acetoanaerobium`)

## Validation

- `just validate data/taxa/bacteria/acetoanaerobium_noterae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrionales_bacterium.yaml data/taxa/bacteria/acetoanaerobium_noterae.yaml data/taxa/bacteria/acetoanaerobium_pronyense.yaml data/taxa/bacteria/acetoanaerobium_sp.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species taxon under `Acetoanaerobium`.
- `data/raw/ncbitaxon_taxa.tsv` line 171882 pins `NCBITaxon:745369` to label `Acetoanaerobium noterae`, rank `SPECIES`, parent `NCBITaxon:186831`, genetic code 11, the related synonym `Acetoanaerobium noterae Sleat et al. 1985`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the record under `Acetoanaerobium`, Filifactoraceae, Peptostreptococcales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/lpsn_data.tsv` line 21353 identifies `lpsn:783234` as the legitimate, validly published, correct species name with authority `Sleat et al. 1985`, type strain `ATCC 35199`, sequence `INSDC:GU562448`, DOI `10.1099/00207713-35-1-10`, and NCBITaxon/GTDB cross-references.
- `data/raw/gtdb_species.tsv` line 3283 and `data/raw/gtdb_mappings.tsv` line 305767 support the 12-genome `GTDB:s__Acetoanaerobium_noterae` `skos:closeMatch` mapping to `NCBITaxon:745369`.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetoanaerobium_noterae`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 10495 keeps this taxon in scope as `attested rule: Acetoanaerobium noterae, 6 sources incl. NCBI`.
- `data/raw/bacdive_strains.tsv` line 90564 supplies the NOT-3 / ATCC 35199 type strain represented as `kgmicrobe.strain:bacdive_168331`.
- `data/raw/ncbi_type_material.tsv` lines 261548-261551 list ATCC 35199 and NOT-3 variants for the same taxon.
- The strain-level genome and cross-reference rows are present in `data/raw/strain_assemblies.tsv` lines 87471-87478, `data/raw/strain_genome_records.tsv` lines 69864-69869, `data/raw/strain_related_records.tsv` lines 259886-259903, StrainInfo line 6187, StrainInfo link line 70216, AllTheBacteria strain-link line 2741, and AllTheBacteria genome-link lines 11570-11574.

## Completeness

- NCBITAXON, LPSN, GTDB, BACDIVE, GOLD, and MADIN source attestations are represented with the expected assertion units and counts.
- The LPSN block captures the correct-name status, publication, sequence accession, and `ATCC-35199` type strain.
- `strain_count: 1` is consistent with the single BacDive strain, and the ATCC 35199 strain carries the local genome assemblies, genome records, and related BioProject/BioSample/GOLD/StrainInfo records from the local source inventories.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
