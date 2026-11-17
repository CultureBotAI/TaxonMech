# YAML Record Review: Acetatifactor aquisgranensis

## Target

- File: `data/taxa/bacteria/acetatifactor_aquisgranensis.yaml`
- Identifier: `NCBITaxon:2941233`
- PATHS.tsv row: 395924
- Label: `Acetatifactor aquisgranensis`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:1427378` (`Acetatifactor`)

## Validation

- `just validate data/taxa/bacteria/acetatifactor_aquisgranensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetanaerobacterium_sp_hmp_mda_pilot_jcvi_0107.yaml data/taxa/bacteria/acetanaerobacterium_sp_hmp_mda_pilot_jcvi_0109.yaml data/taxa/bacteria/acetanaerobacterium_sp_msj_12.yaml data/taxa/bacteria/acetatifactor_aquisgranensis.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` species-level bacterial taxon.
- `data/raw/ncbitaxon_taxa.tsv` line 574779 pins `NCBITaxon:2941233` to label `Acetatifactor aquisgranensis`, rank `SPECIES`, parent `NCBITaxon:1427378`, genetic code 11, three NCBI related synonyms, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold`, and NCBI snapshot `2026-09-13`.
- `data/raw/lpsn_names.tsv` line 7494 links `lpsn:43744` to the same NCBI taxon, the correct validly published species name, authority `Afrizal et al. 2024`, type strain designations `DSM-110981` and `JCM-36051`, PMIDs/DOIs, and `GTDB:s__Acetatifactor_aquisgranensis`.
- The NCBI parent row for `NCBITaxon:1427378` and the higher parent rows for Lachnospiraceae, Lachnospirales, Clostridia, Bacillota, Bacillati, and Bacteria support the full YAML lineage.

## Evidence

- An exact `find` probe under `reports/yaml_record_review` found no existing report for `acetatifactor_aquisgranensis`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 13545 keeps this taxon in scope as `attested rule: Acetatifactor aquisgranensis, 6 sources incl. NCBI`.
- `data/raw/gtdb_species.tsv` line 3002 and `data/raw/gtdb_mappings.tsv` line 236969 support the `GTDB:s__Acetatifactor_aquisgranensis` `skos:closeMatch` mapping to `NCBITaxon:2941233` with `genome_count: 22`.
- `data/raw/bacdive_strains.tsv` line 91974 supports the `CLA-AA-M01, SCP101-BHI2-D7` BacDive strain, BacDive source ID `bacdive:169741`, LPSN source ID `lpsn:43744`, and the two culture collection IDs.
- `data/raw/culture_collection_strains.tsv` lines 62517 and 109666 map `DSM-110981` and `JCM-36051` to `NCBITaxon:2941233`; `data/raw/ncbi_type_material.tsv` lines 145318-145327 list DSM 110981, JCM 36051, and CLA-AA-M01 type-material synonyms for the same NCBI taxon.
- `data/raw/strain_assemblies.tsv` lines 91711-91717, `data/straininfo/assemblies.tsv` line 6468, and `data/raw/strain_genome_records.tsv` lines 73591-73595 support the BacDive, GOLD, GTDB, NCBI Assembly, and StrainInfo assembly and genome entries attached to DSM 110981.
- `data/raw/strain_related_records.tsv` lines 268994-269009 support the GOLD, GTDB, NCBI Assembly, BioProject, and BioSample related records.
- `data/straininfo/strain_links.tsv` line 72151 supports the StrainInfo deposit/strain related records, and compressed StrainInfo source rows `data/straininfo/records.jsonl.gz` line 294475 and `data/straininfo/related_records.tsv.gz` line 170875 support the `INSDC:OM658548` nucleotide related record.
- `data/raw/mediadive_taxa.tsv` line 8435 supports the MediaDive `assertion_count: 1`; `data/raw/gold_organisms.tsv` line 29151 supports the GOLD `assertion_count: 1`.

## Completeness

- All same-taxon local source rows found by the gitignore-independent bounded taxon/source-ID scan are represented in the YAML as NCBITAXON, LPSN, GTDB, BACDIVE, MEDIADIVE, GOLD, strain, assembly, genome, BioProject/BioSample, or StrainInfo evidence.
- The three NCBI related synonyms, LPSN nomenclature block, GTDB xref/mapping, DSM 110981 BacDive strain, and replicated GOLD/GTDB/NCBI Assembly accessions are internally consistent with their raw source rows.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
