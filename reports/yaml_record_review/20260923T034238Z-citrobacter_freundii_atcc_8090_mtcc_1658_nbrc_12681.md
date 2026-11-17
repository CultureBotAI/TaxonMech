# YAML Record Review: Citrobacter freundii ATCC 8090 = MTCC 1658 = NBRC 12681

- Repository: TaxonMech
- Record: data/taxa/bacteria/citrobacter_freundii_atcc_8090_mtcc_1658_nbrc_12681.yaml
- Started UTC: 2026-09-23T03:42:38Z
- Finished UTC: 2026-09-23T03:42:38Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1006003`
- Label: `Citrobacter freundii ATCC 8090 = MTCC 1658 = NBRC 12681`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:546` (`Citrobacter freundii`)
- Path registry row: `data/taxa/PATHS.tsv:2004`

## Validation

- `just validate-strict data/taxa/bacteria/leminorella_grimontii_atcc_33999_dsm_5078.yaml data/taxa/bacteria/marivirga_tractuosa.yaml data/taxa/bacteria/kluyvera_ascorbata_atcc_33433.yaml data/taxa/bacteria/citrobacter_freundii_atcc_8090_mtcc_1658_nbrc_12681.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/citrobacter_freundii_atcc_8090_mtcc_1658_nbrc_12681.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-citrobacter_freundii_atcc_8090_mtcc_1658_nbrc_12681.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, bacterial genetic code, and NCBI exact and related strain synonyms match `data/raw/ncbitaxon_taxa.tsv:210666`.
- The record is correctly grounded to the NCBI strain `NCBITaxon:1006003` under parent species `Citrobacter freundii`.
- The GTDB mapping from `data/raw/gtdb_mappings.tsv:1051` is a 1,691-genome species cluster, `GTDB:s__Citrobacter_freundii`, projected as `skos:closeMatch` onto the narrower NCBI strain.
- The GTDB projection also contributes xref `GTDB:s__Citrobacter_freundii` and exact synonym `Citrobacter freundii`, which make the parent species label look exactly synonymous with the ATCC 8090 / MTCC 1658 / NBRC 12681 strain.

## Evidence

- `data/raw/bacdive_strains.tsv:4221` supplies BacDive strain `4325` and eighteen culture-collection identifiers including `ATCC-8090`, `MTCC-1658`, and `NBRC-12681`.
- `data/raw/strain_assemblies.tsv:126024` and following rows account for the local BacDive, BV-BRC, GOLD, GTDB, and NCBI Assembly rows projected under the matched strain.
- `data/raw/strain_genome_records.tsv:101269` through `data/raw/strain_genome_records.tsv:101293` account for the local GTDB, IMG, and PATRIC genome records under the matched strain.
- `data/straininfo/assemblies.tsv:9368` through `data/straininfo/assemblies.tsv:9372` contribute StrainInfo assembly rows for the ATCC and NBRC deposits retained in the strain payload.
- `data/raw/gold_organisms.tsv:160`, `data/raw/madin_taxa.tsv:352`, and the BactoTraits rows supply the non-taxonomic source attestations.

## Completeness

- The BacDive and StrainInfo payloads are represented with `strain_count: 1`, eighteen culture-collection IDs, assembly and genome records for several equivalent accessions, and related records for the matched ATCC/MTCC/NBRC strain.
- The source attestations cover the expected NCBI, GTDB, BacDive, MediaDive, GOLD, Madin, and BactoTraits evidence for this strain.

## Findings

- Major: the GTDB species cluster `GTDB:s__Citrobacter_freundii` is projected as a `skos:closeMatch`, xref, and exact synonym onto the narrower NCBI strain `NCBITaxon:1006003`. The record should keep strain `Citrobacter freundii ATCC 8090 = MTCC 1658 = NBRC 12681` distinct from the parent species label `Citrobacter freundii`.

## Recommended Edits

- Owner: `data/raw/gtdb_mappings.tsv` generation and taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`. Suppress species-cluster exact synonyms and strain-level `skos:closeMatch` projections when a GTDB species maps to a narrower NCBI strain.

## Follow-up Checks

- After the GTDB projection is corrected, regenerate this YAML and verify that `Citrobacter freundii` is no longer an exact synonym of `Citrobacter freundii ATCC 8090 = MTCC 1658 = NBRC 12681`.
- Keep the existing BacDive, GOLD, NCBI Assembly, StrainInfo, and related strain payloads when regenerating.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
