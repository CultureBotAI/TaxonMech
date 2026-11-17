# YAML Record Review: Acetitomaculum ruminis DSM 5522

## Target

- File: `data/taxa/bacteria/acetitomaculum_ruminis_dsm_5522.yaml`
- Identifier: `NCBITaxon:1120918`
- PATHS.tsv row: 35981
- Label: `Acetitomaculum ruminis DSM 5522`
- Rank/domain: `STRAIN` / `BACTERIA`
- Parent: `NCBITaxon:2382` (`Acetitomaculum ruminis`)

## Validation

- `just validate data/taxa/bacteria/acetitomaculum_ruminis_dsm_5522.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetitomaculum_ruminis.yaml data/taxa/bacteria/acetitomaculum_ruminis_dsm_5522.yaml data/taxa/bacteria/acetitomaculum_sp.yaml data/taxa/bacteria/acetivibrio_aldrichii.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial strain taxon for `Acetitomaculum ruminis DSM 5522`.
- `data/raw/ncbitaxon_taxa.tsv` line 241897 pins `NCBITaxon:1120918` to label `Acetitomaculum ruminis DSM 5522`, rank `STRAIN`, parent `NCBITaxon:2382`, genetic code 11, source set `ncbitaxon|gtdb|bacdive|mediadive|madin_etal|bactotraits`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the strain below `Acetitomaculum ruminis`, `Acetitomaculum`, Lachnospiraceae, Lachnospirales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/gtdb_species.tsv` line 3275 and `data/raw/gtdb_mappings.tsv` line 4393 support the one-genome `GTDB:s__Acetitomaculum_ruminis` `skos:closeMatch` mapping to `NCBITaxon:1120918`.

## Evidence

- An exact `find` probe under `reports/yaml_record_review` found no existing report for `acetitomaculum_ruminis_dsm_5522`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 10942 keeps this taxon in scope as `attested rule: Acetitomaculum ruminis DSM 5522, 6 sources incl. NCBI`.
- `data/raw/bacdive_strains.tsv` line 6222 ties `bacdive:6338` directly to `NCBITaxon:1120918`, `lpsn:772479`, and collection IDs ATCC 43876 and DSM 5522.
- `data/raw/strain_assemblies.tsv` lines 139776-139784 and `data/raw/strain_genome_records.tsv` lines 111963-111969 support the BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo assembly/genome blocks for DSM 5522.
- `data/atb/assemblies.tsv` line 4375, `data/atb/strain_links.tsv` line 4850, and `data/atb/genome_links.tsv` lines 21217-21221 support `atb.assembly:202505.SAMN05216249`, BioSample `SAMN05216249`, `SRR4228327`, ENA analysis `ERZ4270441`, and the same-strain links back to BV-BRC, GOLD, GTDB, and NCBI Assembly sources.
- `data/raw/strain_related_records.tsv` lines 400995-401016 support the BioProject, BioSample, GOLD, and StrainInfo related-record rows projected for `kgmicrobe.strain:bacdive_6338`.
- `data/straininfo/strain_links.tsv` lines 96174-96175 support the ATCC 43876 and DSM 5522 StrainInfo deposits that are retained under this BacDive strain.

## Completeness

- NCBITAXON, GTDB, BACDIVE, MEDIADIVE, MADIN, and BACTOTRAITS attestations are represented with the expected assertion units and counts.
- The one GTDB mapping in the local mapping table is represented, and its source label is carried as the GTDB-sourced exact synonym `Acetitomaculum ruminis`.
- The complete local genome trail for DSM 5522 is present across assemblies, genome IDs, related BioProject/BioSample/GOLD records, ATB sample links, and the matching StrainInfo deposits.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
