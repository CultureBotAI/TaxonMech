# YAML Record Review: Nocardioides psychrotolerans

- Repository: TaxonMech
- Record: data/taxa/bacteria/nocardioides_psychrotolerans.yaml
- Started UTC: 2026-09-23T03:36:01Z
- Finished UTC: 2026-09-23T03:36:01Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1005945`
- Label: `Nocardioides psychrotolerans`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1839` (`Nocardioides`)
- Path registry row: `data/taxa/PATHS.tsv:1995`

## Validation

- `just validate-strict data/taxa/bacteria/nocardioides_sp_cgmcc_1_09653.yaml data/taxa/bacteria/nocardioides_szechwanensis.yaml data/taxa/bacteria/nocardioides_psychrotolerans.yaml data/taxa/bacteria/iranian_hemp_witches_broom_phytoplasma.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/nocardioides_psychrotolerans.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-nocardioides_psychrotolerans.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, bacterial genetic code, and NCBI-derived related synonyms match `data/raw/ncbitaxon_taxa.tsv:210658`.
- The LPSN block matches `data/raw/lpsn_names.tsv:27402`: `lpsn:790446`, authority `Liu et al. 2013 emend. Nouioui et al. 2018`, correct-name status, type strains `DSM-27452` and `NBRC-108563`, DOI/PMID publications, and `INSDC:JF750425`.
- The YAML contains both local GTDB mappings for the NCBI species, `GTDB:s__Nocardioides_psychrotolerans` and `GTDB:s__Nocardioides_psychrotolerans_A`, with explicit `skos:broadMatch` predicates and notes rather than exact synonyms.
- `grounding_status: EXACT` is appropriate because the record is grounded to the current NCBI species and LPSN correct-name entry; the pooled GTDB projections are explicitly marked as broad mappings.

## Evidence

- `curation/seed_scope.tsv:4029` keeps this taxon in scope through eight attesting sources: NCBI, LPSN, GTDB, BacDive, MediaDive, GOLD, Madin, and BactoTraits.
- `data/raw/bacdive_strains.tsv:23887` supplies BacDive strain `24251`, designation `RHLT2-1`, type-strain status, and culture collection IDs `CGMCC-1.11156`, `DSM-27452`, `JCM-19668`, and `NBRC-108563`.
- `data/raw/culture_collection_strains.tsv` backs all four culture-collection identifiers projected onto the BacDive strain.
- `data/raw/strain_assemblies.tsv:113773` and following rows account for the BacDive, BV-BRC, GOLD, GTDB, and NCBI Assembly rows projected under the matched strain.
- `data/raw/strain_genome_records.tsv:91401` through `data/raw/strain_genome_records.tsv:91413` account for the GTDB, IMG, and PATRIC genome records.
- `data/raw/strain_related_records.tsv:328159` through `data/raw/strain_related_records.tsv:328200` account for the projected BioProject, BioSample, GOLD analysis, GOLD organism, GOLD project, and StrainInfo records.
- `data/atb/strain_links.tsv:3745` contributes the `SAMN05216561` AllTheBacteria assembly link, and `data/straininfo/strain_links.tsv:82567` contributes the `DSM 27452` StrainInfo deposit link.

## Completeness

- The record projects every local strain-level evidence family found for `NCBITaxon:1005945`: one BacDive type strain, ATB evidence, assembly and genome records for the CGMCC and NBRC culture IDs, GOLD records, and StrainInfo records for `DSM-27452`.
- The record has eight `source_attestations`, matching the NCBI raw source list `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`.
- The NCBI authority strings and the CGMCC placeholder are retained as `RELATED_SYNONYM` values, which is consistent with local projection of NCBI related synonyms.

## Findings

- None.

## Recommended Edits

- None.

## Follow-up Checks

- Re-review the record if a future GTDB release collapses or renames the `Nocardioides psychrotolerans` and `Nocardioides psychrotolerans_A` broad mappings.
- Re-review the record if the LPSN type-strain list or emended authority changes in a future import.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
