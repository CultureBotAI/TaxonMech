# YAML Record Review: Flagellimonas taeanensis

- Repository: TaxonMech
- Record: data/taxa/bacteria/flagellimonas_taeanensis.yaml
- Started UTC: 2026-09-23T03:27:18Z
- Finished UTC: 2026-09-23T03:27:18Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1005926`
- Label: `Flagellimonas taeanensis`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1005924` (`Flagellimonas`)
- Path registry row: `data/taxa/PATHS.tsv:1981`

## Validation

- `just validate-strict data/taxa/bacteria/flagellimonas_taeanensis.yaml data/taxa/bacteria/pusillimonas_sp_208.yaml data/taxa/bacteria/roseovarius_lutimaris.yaml data/taxa/bacteria/vibrio_sp_la1.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/flagellimonas_taeanensis.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-flagellimonas_taeanensis.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, bacterial genetic code, and NCBI-derived related synonyms match `data/raw/ncbitaxon_taxa.tsv:210644`.
- The LPSN block matches the local correct-name evidence for `lpsn:45088`: authority `(Kim et al. 2013) Molinari Novoa et al. 2024`, type strain `JCM-17757`, DOI/PMID publication accessions, `INSDC:JF714702`, and correct-name status.
- The synonym set preserves the expected Allomuricauda antarctica, Allomuricauda taeanensis, Flagellimonas antarctica, Muricauda antarctica, Muricauda taeanensis, Muricauda sp. 105, and Muricauda sp. Ar-22 names supplied by NCBI and LPSN.
- The projected `GTDB:s__Flagellimonas_taeanensis` mapping is backed by `data/raw/gtdb_mappings.tsv:1015`, stays at the species level for `NCBITaxon:1005926`, and carries `genome_count: 6`.
- `grounding_status: EXACT` is appropriate because the record is grounded directly to the current NCBI taxon and the LPSN correct-name entry for `Flagellimonas taeanensis`.

## Evidence

- `curation/seed_scope.tsv:1525` keeps this taxon in scope through NCBI, LPSN, GTDB, BacDive, GOLD, Madin, and BactoTraits evidence.
- `data/raw/bacdive_strains.tsv` supplies two strain records: BacDive `133943` for type strain `105`, with culture collections `JCM-17757` and `KACC-16195`, and BacDive `24031` for strain `Ar-22`, with culture collections `CGMCC-1.12174`, `DSM-26351`, and `JCM-18450`.
- Local `data/raw/culture_collection_strains.tsv` rows back all five culture-collection identifiers projected into those two BacDive strain blocks.
- `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` account for the ATB, BacDive, BV-BRC, GOLD, GTDB, IMG, NCBI Assembly, BioProject, BioSample, and strain-related accessions linked to the two local strains.
- `data/raw/madin_taxa.tsv:341`, `data/raw/gold_organisms.tsv:152`, `data/raw/gold_organisms.tsv:153`, and the BactoTraits source rows account for the non-taxonomic source-attestation counts.
- Local ATB assembly rows for BioSamples `SAMN04487891` and `SAMN05216293`, plus StrainInfo rows for `JCM-17757` and `JCM-18450`, are represented by the matched strain evidence.

## Completeness

- The record projects every local strain-level evidence family found for the same taxon: two BacDive strains, culture-collection identifiers, assembly and genome records, related strain records, and imported ATB/StrainInfo accessions.
- The record has the eight expected source attestations: NCBI name evidence, LPSN name evidence, six GTDB genomes, two BacDive strains, two MediaDive media, six GOLD organisms, fourteen Madin trait assertions, and twenty-seven BactoTraits trait assertions.
- The historical and placeholder names are retained as `RELATED_SYNONYM` entries, which is consistent with local projection of NCBI authority strings, LPSN synonyms, and strain placeholders.

## Findings

- None.

## Recommended Edits

- None.

## Follow-up Checks

- Re-review the record if a future GTDB release changes the `GTDB:s__Flagellimonas_taeanensis` species cluster or removes the current mapping to `NCBITaxon:1005926`.
- Re-review the record if the raw LPSN import changes the post-2024 synonym relationship with Allomuricauda antarctica or Muricauda taeanensis.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
