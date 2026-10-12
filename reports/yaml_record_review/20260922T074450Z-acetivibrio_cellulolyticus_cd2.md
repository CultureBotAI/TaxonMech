# YAML Record Review: Acetivibrio cellulolyticus CD2

## Target

- File: `data/taxa/bacteria/acetivibrio_cellulolyticus_cd2.yaml`
- Identifier: `NCBITaxon:509191`
- PATHS.tsv row: 523995
- Label: `Acetivibrio cellulolyticus CD2`
- Rank/domain: `STRAIN` / `BACTERIA`
- Parent: `NCBITaxon:35830` (`Acetivibrio cellulolyticus`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_cellulolyticus_cd2.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_alkalicellulosi.yaml data/taxa/bacteria/acetivibrio_alkalicellulosi_dsm_17461.yaml data/taxa/bacteria/acetivibrio_cellulolyticus.yaml data/taxa/bacteria/acetivibrio_cellulolyticus_cd2.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial strain taxon for `Acetivibrio cellulolyticus CD2`.
- `data/raw/ncbitaxon_taxa.tsv` line 115694 pins `NCBITaxon:509191` to label `Acetivibrio cellulolyticus CD2`, rank `STRAIN`, parent `NCBITaxon:35830`, genetic code 11, three exact strain synonyms from NCBI, source set `ncbitaxon|gtdb|bacdive|mediadive|madin_etal|bactotraits`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the strain below `Acetivibrio cellulolyticus`, `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/gtdb_species.tsv` line 3276 and `data/raw/gtdb_mappings.tsv` line 293698 support the one-genome `GTDB:s__Acetivibrio_cellulolyticus` `skos:closeMatch` mapping to `NCBITaxon:509191`.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_cellulolyticus_cd2`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 10084 keeps this taxon in scope as `attested rule: Acetivibrio cellulolyticus CD2, 6 sources incl. NCBI`.
- `data/raw/bacdive_strains.tsv` line 17485 ties `bacdive:17674` directly to `NCBITaxon:509191`, LPSN name `lpsn:772481`, designation `CD2`, and collection IDs ATCC 33288, DSM 1870, and NRC 2248.
- `data/raw/strain_assemblies.tsv` lines 99905-99906 and `data/raw/strain_genome_records.tsv` lines 80462-80464 support the BacDive INSDC assembly, GOLD assembly, BacDive IMG genome, GOLD IMG genome, and BacDive BV-BRC genome rows for CD2.
- `data/raw/strain_related_records.tsv` lines 289818-289824 support the GOLD BioProject `PRJNA45843`, BioSample `SAMN02256541`, analysis `Ga0025127`, organism `Go0004748`, project `Gp0004748`, and same-type-strain ATCC 33288 organism `Go0605150`.
- `data/straininfo/strain_links.tsv` lines 76877-76878 support the ATCC 33288 and DSM 1870 StrainInfo deposits projected under `straininfo.strain:10241`.

## Completeness

- NCBITAXON, GTDB, BACDIVE, MEDIADIVE, MADIN, and BACTOTRAITS attestations are represented with the expected assertion units and counts.
- The one local GTDB species mapping is represented, and its source label is carried as the GTDB-sourced exact synonym `Acetivibrio cellulolyticus`.
- The strain record carries the CD2 BacDive strain, its ATCC/DSM/NRC collection identifiers, its available local genome records, the GOLD project/sample/analysis records, and the matching StrainInfo ATCC 33288 / DSM 1870 deposit rows.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
