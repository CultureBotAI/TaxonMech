# YAML Record Review: Acerihabitans arboris

## Target

- File: `data/taxa/bacteria/acerihabitans_arboris.yaml`
- Identifier: `NCBITaxon:2691583`
- PATHS.tsv row: 363818
- Label: `Acerihabitans arboris`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:2811373` (`Acerihabitans`)

## Validation

- `just validate data/taxa/bacteria/acerihabitans_arboris.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acer_platanoides_aster_yellows_phytoplasma.yaml data/taxa/bacteria/acerihabitans_arboris.yaml data/taxa/bacteria/acerihabitans_sp.yaml data/taxa/bacteria/acerihabitans_sp_bd602.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` species-level bacterial taxon.
- `data/raw/ncbitaxon_taxa.tsv` line 544243 pins `NCBITaxon:2691583` to label `Acerihabitans arboris`, rank `SPECIES`, parent `NCBITaxon:2811373`, genetic code 11, related synonyms `Acerihabitans arboris Lee et al. 2021` and `Enterobacteriales bacterium SAP-6`, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold`, and NCBI snapshot `2026-09-13`.
- `data/raw/lpsn_names.tsv` line 3293 links `lpsn:17738` to the same NCBI taxon, the correct validly published species name, type strain designations `DSM-104038` and `KCTC-52622`, PMIDs/DOIs, sequence accession `INSDC:MN737198`, and `GTDB:s__Acerihabitans_arboris`.
- The NCBI parent row for `NCBITaxon:2811373` and the higher parent rows for Pectobacteriaceae, Enterobacterales, Gammaproteobacteria, Pseudomonadota, Pseudomonadati, and Bacteria support the full YAML lineage.

## Evidence

- An exact `find` probe under `reports/yaml_record_review` found no existing report for `acerihabitans_arboris`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 13312 keeps this taxon in scope as `attested rule: Acerihabitans arboris, 6 sources incl. NCBI`.
- `data/raw/gtdb_species.tsv` line 2981 and `data/raw/gtdb_mappings.tsv` line 207879 support the single `GTDB:s__Acerihabitans_arboris` `skos:closeMatch` mapping with `genome_count: 1`.
- `data/raw/bacdive_strains.tsv` line 82562 supports the SAP-6 BacDive strain, BacDive source ID `bacdive:160325`, LPSN source ID `lpsn:17738`, and the two culture collection IDs.
- `data/raw/culture_collection_strains.tsv` lines 59914 and 120232 map `DSM-104038` and `KCTC-52622` to `NCBITaxon:2691583`.
- `data/raw/ncbi_type_material.tsv` lines 110407-110412 list DSM 104038, KCTC 52622, and SAP-6 type-material synonyms for the same NCBI taxon.
- `data/raw/strain_assemblies.tsv` line 69741 and `data/raw/strain_genome_records.tsv` lines 54386-54387 support the INSDC, IMG, and BV-BRC genome records attached to the BacDive strain.
- `data/straininfo/strain_links.tsv` line 59522 supports both StrainInfo related records on the `DSM-104038` culture identifier match.
- `data/raw/mediadive_taxa.tsv` line 7655 supports the MediaDive `assertion_count: 2`; `data/raw/gold_organisms.tsv` line 24838 supports the GOLD `assertion_count: 1`.

## Completeness

- All same-taxon local source rows found by the gitignore-independent ID/source-ID scan are represented in the YAML as NCBITAXON, LPSN, GTDB, BACDIVE, MEDIADIVE, GOLD, strain, type-material, genome, or StrainInfo assertions.
- The two NCBI related synonyms are both present as `RELATED_SYNONYM` entries, the GTDB and LPSN xrefs are present, and the only GTDB mapping for this NCBI taxon is present with the correct close-match predicate and genome count.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
