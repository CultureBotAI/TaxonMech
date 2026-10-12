# YAML Record Review: Nocardioides szechwanensis

- Repository: TaxonMech
- Record: data/taxa/bacteria/nocardioides_szechwanensis.yaml
- Started UTC: 2026-09-23T03:36:01Z
- Finished UTC: 2026-09-23T03:36:01Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1005944`
- Label: `Nocardioides szechwanensis`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1839` (`Nocardioides`)
- Path registry row: `data/taxa/PATHS.tsv:1994`

## Validation

- `just validate-strict data/taxa/bacteria/nocardioides_sp_cgmcc_1_09653.yaml data/taxa/bacteria/nocardioides_szechwanensis.yaml data/taxa/bacteria/nocardioides_psychrotolerans.yaml data/taxa/bacteria/iranian_hemp_witches_broom_phytoplasma.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/nocardioides_szechwanensis.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-nocardioides_szechwanensis.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, bacterial genetic code, and NCBI-derived related synonyms match `data/raw/ncbitaxon_taxa.tsv:210657`.
- The LPSN block matches `data/raw/lpsn_names.tsv:27401`: `lpsn:790445`, authority `Liu et al. 2013 emend. Nouioui et al. 2018`, correct-name status, type strains `DSM-27403` and `NBRC-108562`, DOI/PMID publications, and `INSDC:JF750424`.
- The `GTDB:s__Nocardioides_szechwanensis` mapping is species-level, has `genome_count: 2`, is linked by LPSN, and is backed by `data/raw/gtdb_mappings.tsv:1041`.
- `grounding_status: EXACT` is appropriate because all projected high-level taxonomy sources refer to `Nocardioides szechwanensis` at `NCBITaxon:1005944`.

## Evidence

- `curation/seed_scope.tsv:4028` keeps this taxon in scope through eight attesting sources: NCBI, LPSN, GTDB, BacDive, MediaDive, GOLD, Madin, and BactoTraits.
- `data/raw/bacdive_strains.tsv:23886` supplies BacDive strain `24250`, designation `RHLT1-17`, type-strain status, and culture collection IDs `CGMCC-1.11147`, `DSM-27403`, `JCM-19669`, and `NBRC-108562`.
- `data/raw/culture_collection_strains.tsv` backs all four culture-collection identifiers projected onto the BacDive strain.
- `data/raw/strain_assemblies.tsv:113756` through `data/raw/strain_assemblies.tsv:113772` account for the BacDive, BV-BRC, GOLD, GTDB, and NCBI Assembly rows projected under the matched strain.
- `data/raw/strain_genome_records.tsv:91388` through `data/raw/strain_genome_records.tsv:91400` account for the GTDB, IMG, and PATRIC genome records.
- `data/raw/strain_related_records.tsv:328128` through `data/raw/strain_related_records.tsv:328158` account for the projected BioProject, BioSample, GOLD analysis, GOLD organism, GOLD project, and StrainInfo records.
- `data/atb/strain_links.tsv:3744` contributes the `SAMN05192576` AllTheBacteria assembly link, and `data/straininfo/strain_links.tsv:82566` contributes the `DSM 27403` StrainInfo deposit link.

## Completeness

- The record projects every local strain-level evidence family found for `NCBITaxon:1005944`: one BacDive type strain, ATB evidence, assembly and genome records for the CGMCC and NBRC culture IDs, GOLD records, and StrainInfo records for `DSM-27403`.
- The record has eight `source_attestations`, matching the NCBI raw source list `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`.
- The NCBI authority strings and the CGMCC placeholder are retained as `RELATED_SYNONYM` values, which is consistent with local projection of NCBI related synonyms.

## Findings

- None.

## Recommended Edits

- None.

## Follow-up Checks

- Re-review the record if a future GTDB release changes `GTDB:s__Nocardioides_szechwanensis` away from the current species-level `skos:closeMatch`.
- Re-review the record if the LPSN type-strain list or emended authority changes in a future import.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
