# YAML Record Review: Leminorella grimontii ATCC 33999 = DSM 5078

- Repository: TaxonMech
- Record: data/taxa/bacteria/leminorella_grimontii_atcc_33999_dsm_5078.yaml
- Started UTC: 2026-09-23T03:42:38Z
- Finished UTC: 2026-09-23T03:42:38Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1005999`
- Label: `Leminorella grimontii ATCC 33999 = DSM 5078`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:82981` (`Leminorella grimontii`)
- Path registry row: `data/taxa/PATHS.tsv:2001`

## Validation

- `just validate-strict data/taxa/bacteria/leminorella_grimontii_atcc_33999_dsm_5078.yaml data/taxa/bacteria/marivirga_tractuosa.yaml data/taxa/bacteria/kluyvera_ascorbata_atcc_33433.yaml data/taxa/bacteria/citrobacter_freundii_atcc_8090_mtcc_1658_nbrc_12681.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/leminorella_grimontii_atcc_33999_dsm_5078.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-leminorella_grimontii_atcc_33999_dsm_5078.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, bacterial genetic code, and NCBI exact strain synonyms match `data/raw/ncbitaxon_taxa.tsv:210664`.
- The record is correctly grounded to the NCBI strain `NCBITaxon:1005999` under parent species `Leminorella grimontii`.
- The GTDB mapping from `data/raw/gtdb_mappings.tsv:1047` is an eight-genome species cluster, `GTDB:s__Leminorella_grimontii`, projected as `skos:closeMatch` onto the narrower NCBI strain.
- The GTDB projection also contributes xref `GTDB:s__Leminorella_grimontii` and exact synonym `Leminorella grimontii`, which make the parent species label look exactly synonymous with the ATCC 33999 / DSM 5078 strain.

## Evidence

- `curation/seed_scope.tsv` keeps this strain in scope through NCBI, GTDB, BacDive, MediaDive, GOLD, and Madin evidence.
- `data/raw/bacdive_strains.tsv:4872` supplies BacDive strain `4981`, designation `81H-380`, and eight culture-collection identifiers including `ATCC-33999` and `DSM-5078`.
- `data/raw/strain_genome_records.tsv:102980` through `data/raw/strain_genome_records.tsv:102996` account for the local GTDB, IMG, and PATRIC genome records under the matched strain.
- `data/raw/strain_related_records.tsv:369662` through `data/raw/strain_related_records.tsv:369711` account for the local BioProject, BioSample, GOLD analysis, GOLD organism, and GOLD project records.
- `data/straininfo/assemblies.tsv:9579` through `data/straininfo/assemblies.tsv:9582` contribute the ATCC 33999 and DSM 5078 StrainInfo assemblies that are retained in the strain payload.

## Completeness

- The BacDive and StrainInfo payloads are represented with `strain_count: 1`, eight culture-collection IDs, assembly rows for the ATCC and DSM aliases, genome records, and related BioProject, BioSample, GOLD, and StrainInfo records.
- The source attestations cover the expected NCBI, GTDB, BacDive, MediaDive, GOLD, and Madin evidence for this strain.

## Findings

- Major: the GTDB species cluster `GTDB:s__Leminorella_grimontii` is projected as a `skos:closeMatch`, xref, and exact synonym onto the narrower NCBI strain `NCBITaxon:1005999`. The record should keep strain `Leminorella grimontii ATCC 33999 = DSM 5078` distinct from the parent species label `Leminorella grimontii`.

## Recommended Edits

- Owner: `data/raw/gtdb_mappings.tsv` generation and taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`. Suppress species-cluster exact synonyms and strain-level `skos:closeMatch` projections when a GTDB species maps to a narrower NCBI strain.

## Follow-up Checks

- After the GTDB projection is corrected, regenerate this YAML and verify that `Leminorella grimontii` is no longer an exact synonym of `Leminorella grimontii ATCC 33999 = DSM 5078`.
- Keep the existing BacDive, GOLD, NCBI Assembly, and StrainInfo strain payloads when regenerating.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
