# YAML Record Review: Ancylobacter aquaticus

## Target

- File: `data/taxa/bacteria/ancylobacter_aquaticus.yaml`
- Identifier: `NCBITaxon:100`
- PATHS.tsv row: 2
- Label: `Ancylobacter aquaticus`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:99` (`Ancylobacter`)

## Validation

- `just validate data/taxa/bacteria/ancylobacter_aquaticus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/ancylobacter_aquaticus.yaml data/taxa/bacteria/herbaspirillum_sp_ba12.yaml data/taxa/bacteria/microbacterium_sp_6_11_vpa.yaml data/taxa/bacteria/mycobacterium_sp_1_1_ves.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species taxon under `Ancylobacter`.
- `data/raw/ncbitaxon_taxa.tsv` line 74 pins `NCBITaxon:100` to label `Ancylobacter aquaticus`, rank `SPECIES`, parent `NCBITaxon:99`, genetic code 11, exact synonym `Microcyclus aquaticus`, related `Ancylobacter` and `Microcyclus` authority strings, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the record under `Ancylobacter`, Xanthobacteraceae, Hyphomicrobiales, Alphaproteobacteria, Pseudomonadota, Pseudomonadati, and Bacteria, matching the YAML lineage.
- `data/raw/lpsn_names.tsv` line 15330 identifies `lpsn:773268` as the legitimate, validly published, correct species name with authority `(Ørskov 1928) Raj 1983 emend. Hördt et al. 2020`, type culture identifiers including ATCC 25396, DSM 101, JCM 20518, LMG 4052, and NBRC 102453, sequence `INSDC:M62790`, and NCBITaxon/GTDB cross-references.
- `data/raw/gtdb_species.tsv` lines 9944 and 9960 and `data/raw/gtdb_mappings.tsv` lines 2-3 support both 1-genome `GTDB:s__Ancylobacter_aquaticus` and 2-genome `GTDB:s__Ancylobacter_rudongensis` as `skos:broadMatch` mappings to `NCBITaxon:100`.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `ancylobacter_aquaticus`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 533 keeps this taxon in scope as `attested rule: Ancylobacter aquaticus, 8 sources incl. NCBI`.
- `data/raw/bacdive_strains.tsv` lines 17194, 17196-17197, and 17202-17203 supply the five BacDive strains represented in the YAML: M, B, the ATCC 25396 / DSM 101 type strain, H, and W.
- `data/raw/ncbi_type_material.tsv` lines 2-21 list type-material variants for ATCC 25396, CCUG 1820, CCUG 30551, DSM 101, JCM 20518, LMG 4052, NBRC 102453, VKM B-1287, Ørskov, and `strain rskov`.
- The DSM 101 type-strain genome evidence is present in `data/raw/strain_assemblies.tsv` lines 96922-96930, `data/raw/strain_genome_records.tsv` lines 78112-78118, `data/raw/strain_related_records.tsv` lines 281698-281723, and StrainInfo assembly line 6930.

## Completeness

- NCBITAXON, LPSN, GTDB, BACDIVE, MEDIADIVE, GOLD, MADIN, and BACTOTRAITS source attestations are represented with the expected assertion units and counts.
- The LPSN block captures the correct-name status, `Microcyclus aquaticus` synonym, type culture identifiers, publication DOI, and 16S sequence accession.
- `strain_count: 5` is consistent with the five BacDive strain rows, and the DSM 101 type strain carries the local genome assemblies, genome records, and related BioProject/BioSample/GOLD/StrainInfo records from the local source inventories.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
