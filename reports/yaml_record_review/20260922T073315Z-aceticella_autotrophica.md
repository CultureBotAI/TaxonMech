# YAML Record Review: Aceticella autotrophica

## Target

- File: `data/taxa/bacteria/aceticella_autotrophica.yaml`
- Identifier: `NCBITaxon:2755338`
- PATHS.tsv row: 371342
- Label: `Aceticella autotrophica`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:3051499` (`Aceticella`)

## Validation

- `just validate data/taxa/bacteria/aceticella_autotrophica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetatifactor_muris.yaml data/taxa/bacteria/acetatifactor_sp.yaml data/taxa/bacteria/acetatifactor_sp_dfi_5_50.yaml data/taxa/bacteria/aceticella_autotrophica.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` species-level bacterial taxon.
- `data/raw/ncbitaxon_taxa.tsv` line 551244 pins `NCBITaxon:2755338` to label `Aceticella autotrophica`, rank `SPECIES`, parent `NCBITaxon:3051499`, genetic code 11, three NCBI related synonyms, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive`, and NCBI snapshot `2026-09-13`.
- `data/raw/lpsn_names.tsv` line 7797 links `lpsn:46550` to the same NCBI taxon, the correct validly published species name, authority `Frolov et al. 2024`, type strain designation `DSM-108286`, PMIDs/DOIs, sequence accession `INSDC:CP060096`, and `GTDB:s__Aceticella_autotrophica`.
- The NCBI parent row for `NCBITaxon:3051499` and the higher parent rows for Thermoanaerobacteraceae, Thermoanaerobacterales, Clostridia, Bacillota, Bacillati, and Bacteria support the full YAML lineage.

## Evidence

- An exact `find` probe under `reports/yaml_record_review` found no existing report for `aceticella_autotrophica`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 18911 keeps this taxon in scope as `attested rule: Aceticella autotrophica, 5 sources incl. NCBI`.
- `data/raw/gtdb_species.tsv` line 3271 and `data/raw/gtdb_mappings.tsv` line 213607 support the `GTDB:s__Aceticella_autotrophica` `skos:closeMatch` mapping to `NCBITaxon:2755338` with `genome_count: 2`.
- `data/raw/bacdive_strains.tsv` line 97346 supports the `3443-3AC` BacDive strain, BacDive source ID `bacdive:175115`, LPSN source ID `lpsn:46550`, and culture collection IDs `DSM-108286` and `VKM-B-3415`.
- `data/raw/culture_collection_strains.tsv` lines 61480 and 153347 map `DSM-108286` and `VKM-B-3415` to `NCBITaxon:2755338`; `data/raw/ncbi_type_material.tsv` lines 117659-117668 list DSM 108286, VKM B-3415, and 3443-3Ac type-material synonyms.
- `data/straininfo/strain_links.tsv` line 75848 supports the StrainInfo deposit/strain related records matched through `DSM-108286`.
- `data/raw/mediadive_taxa.tsv` line 7841 supports the MediaDive `assertion_count: 1`.

## Completeness

- All same-taxon local source rows found by the gitignore-independent bounded taxon/source-ID scan are represented in the YAML as NCBITAXON, LPSN, GTDB, BACDIVE, MEDIADIVE, strain, type-material, or StrainInfo evidence.
- The three NCBI related synonyms, LPSN nomenclature block, GTDB xref/mapping, and BacDive/StrainInfo strain material are internally consistent with their raw source rows.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
