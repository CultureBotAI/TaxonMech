# YAML Record Review: Kordiimonas aestuarii

- Repository: TaxonMech
- Record: data/taxa/bacteria/kordiimonas_aestuarii.yaml
- Started UTC: 2026-09-23T03:23:19Z
- Finished UTC: 2026-09-23T03:23:19Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1005925`
- Label: `Kordiimonas aestuarii`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:288021` (`Kordiimonas`)
- Path registry row: `data/taxa/PATHS.tsv:1980`

## Validation

- `just validate-strict data/taxa/bacteria/clostridium_sp_nan076.yaml data/taxa/bacteria/clostridium_sp_nan123.yaml data/taxa/bacteria/bacillus_sp_3_10.yaml data/taxa/bacteria/kordiimonas_aestuarii.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/kordiimonas_aestuarii.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-kordiimonas_aestuarii.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, bacterial genetic code, and NCBI-derived related synonyms match `data/raw/ncbitaxon_taxa.tsv:210643`.
- The LPSN block matches `data/raw/lpsn_names.tsv:27303`: `lpsn:790326`, authority `Math et al. 2012`, correct-name status, DOI/PMID publications, sequence accession `INSDC:JF714701`, and type strain `kgmicrobe.strain:JCM-17742`.
- The `GTDB:s__Kordiimonas_aestuarii` mapping is species-level, has `genome_count: 1`, and is backed by both the LPSN GTDB link and `data/raw/gtdb_mappings.tsv:1014`.
- `grounding_status: EXACT` is appropriate because all projected high-level sources refer to `Kordiimonas aestuarii` at `NCBITaxon:1005925`.

## Evidence

- `curation/seed_scope.tsv:10773` keeps this taxon in scope through six attesting sources: NCBI, LPSN, GTDB, BacDive, GOLD, and Madin.
- `data/raw/bacdive_strains.tsv:56122` contributes BacDive strain `133812`, designation `101-1`, type-strain status, and culture collection IDs `JCM-17742` and `KACC-16184`.
- `data/raw/culture_collection_strains.tsv:103263` and `data/raw/culture_collection_strains.tsv:113328` back the two culture-collection identifiers projected onto the BacDive strain.
- `data/raw/strain_assemblies.tsv:32316` through `data/raw/strain_assemblies.tsv:32324` account for the nine assembly projections from BacDive, BV-BRC, GOLD, GTDB, and NCBI Assembly.
- `data/raw/strain_genome_records.tsv:25467` through `data/raw/strain_genome_records.tsv:25473` account for the seven GTDB, IMG, and PATRIC genome records under `kgmicrobe.strain:bacdive_133812`.
- `data/raw/strain_related_records.tsv:87188` through `data/raw/strain_related_records.tsv:87207` account for the two BioProject accessions, BioSample `SAMN30733096`, and GOLD analysis, organism, and project records projected under the same matched JCM 17742 strain.
- `data/raw/madin_taxa.tsv:340` supplies the `MADIN` source attestation with 27 trait assertions, and `data/raw/gold_organisms.tsv:151` supplies the GOLD organism count.
- A gitignore-independent `rg --no-ignore --hidden` scan of `data/atb` and `data/straininfo` found no extra same-ID, same-label, or same-slug rows outside the pinned raw rows.

## Completeness

- The record projects every local strain-level evidence family found for `NCBITaxon:1005925`: one BacDive type strain, nine assemblies, seven genome records, and twenty related BioProject/BioSample/GOLD records.
- The NCBI authority and strain-name synonyms are retained as `RELATED_SYNONYM` values, which is consistent with local handling of NCBI authority strings and strain placeholders.
- The record has six `source_attestations`, matching the NCBI raw source list `ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal`.

## Findings

- None.

## Recommended Edits

- None.

## Follow-up Checks

- Re-review the record if a future GTDB release adds multiple genomes or changes the species assignment away from `GTDB:s__Kordiimonas_aestuarii`.
- Re-review the record if Madin trait rows are projected into inline trait blocks rather than summarized through the current `MADIN` source attestation.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
