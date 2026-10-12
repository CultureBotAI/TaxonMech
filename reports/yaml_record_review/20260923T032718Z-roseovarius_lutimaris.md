# YAML Record Review: Roseovarius lutimaris

- Repository: TaxonMech
- Record: data/taxa/bacteria/roseovarius_lutimaris.yaml
- Started UTC: 2026-09-23T03:27:18Z
- Finished UTC: 2026-09-23T03:27:18Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1005928`
- Label: `Roseovarius lutimaris`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:74030` (`Roseovarius`)
- Path registry row: `data/taxa/PATHS.tsv:1983`

## Validation

- `just validate-strict data/taxa/bacteria/flagellimonas_taeanensis.yaml data/taxa/bacteria/pusillimonas_sp_208.yaml data/taxa/bacteria/roseovarius_lutimaris.yaml data/taxa/bacteria/vibrio_sp_la1.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/roseovarius_lutimaris.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-roseovarius_lutimaris.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, bacterial genetic code, and NCBI-derived related synonyms match `data/raw/ncbitaxon_taxa.tsv:210646`.
- The LPSN block matches the local correct-name evidence for `lpsn:791174`: authority `Choi et al. 2013 emend. Hördt et al. 2020`, type strains `DSM-28463` and `JCM-17743`, DOI/PMID publication accessions, `INSDC:JF714703`, and correct-name status.
- The projected NCBI related synonyms preserve the duplicated authority-style label `Roseovarius lutimaris Roseovarius lutimaris Choi et al. 2013` and the placeholder `Roseovarius sp. 112`.
- The projected `GTDB:s__Roseovarius_lutimaris` mapping is backed by `data/raw/gtdb_mappings.tsv:1016`, stays at the species level for `NCBITaxon:1005928`, and carries `genome_count: 1`.
- `grounding_status: EXACT` is appropriate because the record is grounded directly to the current NCBI taxon and the LPSN correct-name entry for `Roseovarius lutimaris`.

## Evidence

- `curation/seed_scope.tsv:4027` keeps this taxon in scope through NCBI, LPSN, GTDB, BacDive, GOLD, Madin, and BactoTraits evidence.
- `data/raw/bacdive_strains.tsv` supplies BacDive strain `24500`, designation `112`, type-strain status, and culture collection IDs `DSM-28463`, `JCM-17743`, and `KACC-16185`.
- Local `data/raw/culture_collection_strains.tsv` rows back all three culture-collection identifiers projected into the BacDive strain block.
- `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` account for the ATB, BacDive, BV-BRC, GOLD, GTDB, IMG, NCBI Assembly, BioProject, BioSample, and strain-related accessions linked to the local type strain.
- `data/raw/madin_taxa.tsv:342`, `data/raw/gold_organisms.tsv:153`, and the BactoTraits source rows account for the non-taxonomic source-attestation counts.
- The local ATB assembly row for BioSample `SAMN04487859`, plus StrainInfo rows for `DSM-28463` and `JCM-17743`, are represented by the matched strain evidence.

## Completeness

- The record projects every local strain-level evidence family found for the same taxon: one BacDive strain, culture-collection identifiers, assembly and genome records, related strain records, and imported ATB/StrainInfo accessions.
- The record has the eight expected source attestations: NCBI name evidence, LPSN name evidence, one GTDB genome, one BacDive strain, two MediaDive media, four GOLD organisms, thirteen Madin trait assertions, and twenty-four BactoTraits trait assertions.
- The NCBI authority string and strain placeholder are retained as `RELATED_SYNONYM` entries, which is consistent with local projection of NCBI related synonyms.

## Findings

- None.

## Recommended Edits

- None.

## Follow-up Checks

- Re-review the record if a future GTDB release adds more genomes to `GTDB:s__Roseovarius_lutimaris` or changes the mapped NCBI species.
- Re-review the record if the LPSN type-strain list or emended authority changes in a future import.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
