# YAML Record Review: Buttiauxella agrestis ATCC 33320

- Repository: TaxonMech
- Record: data/taxa/bacteria/buttiauxella_agrestis_atcc_33320.yaml
- Started UTC: 2026-09-23T03:47:32Z
- Finished UTC: 2026-09-23T03:47:32Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1006004`
- Label: `Buttiauxella agrestis ATCC 33320`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:82977` (`Buttiauxella agrestis`)
- Path registry row: `data/taxa/PATHS.tsv:2005`

## Validation

- `just validate-strict data/taxa/bacteria/buttiauxella_agrestis_atcc_33320.yaml data/taxa/archaea/metallosphaera_cuprina.yaml data/taxa/archaea/metallosphaera_cuprina_ar_4.yaml data/taxa/bacteria/priestia_megaterium_wsh_002.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/buttiauxella_agrestis_atcc_33320.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-buttiauxella_agrestis_atcc_33320.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, bacterial genetic code, and NCBI exact strain synonyms match `data/raw/ncbitaxon_taxa.tsv:210667`.
- The record is correctly grounded to the NCBI strain `NCBITaxon:1006004` under parent species `Buttiauxella agrestis`.
- The GTDB rows at `data/raw/gtdb_mappings.tsv:1052` and `data/raw/gtdb_mappings.tsv:1053` are intentionally carried as `skos:broadMatch` pooled species-cluster mappings, and they are not projected as exact GTDB synonyms.

## Evidence

- `data/raw/bacdive_strains.tsv:4207` supplies the BacDive strain, designation `Gavini-F-44, F44`, and eleven culture-collection identifiers for this record.
- `data/raw/strain_assemblies.tsv:125885` through `data/raw/strain_assemblies.tsv:125901` and `data/raw/strain_genome_records.tsv:101145` through `data/raw/strain_genome_records.tsv:101159` account for the local BacDive, BV-BRC, GOLD, GTDB, and NCBI Assembly payload.
- `data/straininfo/assemblies.tsv:9352` and `data/straininfo/strain_links.tsv:88903` independently support the ATCC 33320 StrainInfo match.
- `data/raw/gold_organisms.tsv:161`, `data/raw/mediadive_taxa.tsv:44`, and `data/raw/madin_taxa.tsv:353` supply the GOLD organism count, four MediaDive media, and one Madin trait assertion represented in source attestations.

## Completeness

- The record represents the expected NCBI, GTDB, BacDive, MediaDive, GOLD, Madin, BV-BRC, NCBI Assembly, and StrainInfo evidence for the ATCC 33320 culture.
- The broad GTDB mappings retain genome counts from `data/raw/gtdb_species.tsv:21058` and `data/raw/gtdb_species.tsv:21060` without creating exact species synonyms on the narrower strain record.

## Findings

- No curation findings.

## Recommended Edits

- None.

## Follow-up Checks

- Keep broad GTDB species-cluster mappings as `skos:broadMatch` unless upstream GTDB-to-NCBI projection logic can map a cluster exactly to a same-rank NCBI species.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
