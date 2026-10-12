# YAML Record Review: Acetanaerobacterium elongatum

## Target

- File: `data/taxa/bacteria/acetanaerobacterium_elongatum.yaml`
- Identifier: `NCBITaxon:258515`
- PATHS.tsv row: 354588
- Label: `Acetanaerobacterium elongatum`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:258514` (`Acetanaerobacterium`)

## Validation

- `just validate data/taxa/bacteria/acetanaerobacterium_elongatum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetanaerobacter_sp.yaml data/taxa/bacteria/acetanaerobacterium_elongatum.yaml data/taxa/bacteria/acetanaerobacterium_sp.yaml data/taxa/bacteria/acetanaerobacterium_sp_hmp_mda_pilot_jcvi_0106.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` species-level bacterial taxon.
- `data/raw/ncbitaxon_taxa.tsv` line 52735 pins `NCBITaxon:258515` to label `Acetanaerobacterium elongatum`, rank `SPECIES`, parent `NCBITaxon:258514`, genetic code 11, related synonym `Acetanaerobacterium elongatum Chen and Dong 2004`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal`, and NCBI snapshot `2026-09-13`.
- `data/raw/lpsn_names.tsv` line 21351 links `lpsn:783232` to the same NCBI taxon, the correct validly published species name, type strain designation `JCM-12359`, PMIDs/DOIs, sequence accession `INSDC:AY487928`, and `GTDB:s__Acetanaerobacterium_elongatum`.
- The NCBI parent row for `NCBITaxon:258514` and the higher parent rows for Oscillospiraceae, Eubacteriales, Clostridia, Bacillota, Bacillati, and Bacteria support the full YAML lineage.

## Evidence

- An exact `find` probe under `reports/yaml_record_review` found no existing report for `acetanaerobacterium_elongatum`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 9605 keeps this taxon in scope as `attested rule: Acetanaerobacterium elongatum, 6 sources incl. NCBI`.
- `data/raw/gtdb_species.tsv` line 2991 and `data/raw/gtdb_mappings.tsv` line 200044 support the single `GTDB:s__Acetanaerobacterium_elongatum` `skos:closeMatch` mapping with `genome_count: 1`.
- `data/raw/bacdive_strains.tsv` line 56408 supports the Z7 BacDive strain, BacDive source ID `bacdive:134101`, LPSN source ID `lpsn:783232`, and culture collection IDs `AS-1.5012` and `JCM-12359`.
- `data/raw/culture_collection_strains.tsv` lines 603 and 99957 map `AS-1.5012` and `JCM-12359` to `NCBITaxon:258515`.
- `data/raw/ncbi_type_material.tsv` lines 103312-103319 list AS 1.5012, CGMCC 1.5012, JCM 12359, and Z7 type-material synonyms for the same NCBI taxon.
- `data/straininfo/strain_links.tsv` lines 15636-15637 support the AS 1.5012 and JCM 12359 StrainInfo deposit records.
- `data/raw/strain_related_records.tsv` line 91653 supports the `gold:Go0027238` GOLD related record matched through `JCM-12359`.
- `data/raw/gold_organisms.tsv` line 23652 supports the GOLD `assertion_count: 2`; `data/raw/madin_taxa.tsv` line 20128 supports the MADIN `assertion_count: 15`.

## Completeness

- All same-taxon local source rows found by the gitignore-independent bounded ID/source-ID scan are represented in the YAML as NCBITAXON, LPSN, GTDB, BACDIVE, GOLD, MADIN, strain, type-material, or StrainInfo evidence.
- The NCBI related synonym, LPSN nomenclature block, GTDB xref/mapping, BacDive strain, and StrainInfo deposit evidence are internally consistent with their raw source rows.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
