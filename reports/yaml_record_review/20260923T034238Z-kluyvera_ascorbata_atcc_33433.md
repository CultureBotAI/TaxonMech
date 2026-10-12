# YAML Record Review: Kluyvera ascorbata ATCC 33433

- Repository: TaxonMech
- Record: data/taxa/bacteria/kluyvera_ascorbata_atcc_33433.yaml
- Started UTC: 2026-09-23T03:42:38Z
- Finished UTC: 2026-09-23T03:42:38Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1006000`
- Label: `Kluyvera ascorbata ATCC 33433`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:51288` (`Kluyvera ascorbata`)
- Path registry row: `data/taxa/PATHS.tsv:2003`

## Validation

- `just validate-strict data/taxa/bacteria/leminorella_grimontii_atcc_33999_dsm_5078.yaml data/taxa/bacteria/marivirga_tractuosa.yaml data/taxa/bacteria/kluyvera_ascorbata_atcc_33433.yaml data/taxa/bacteria/citrobacter_freundii_atcc_8090_mtcc_1658_nbrc_12681.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/kluyvera_ascorbata_atcc_33433.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-kluyvera_ascorbata_atcc_33433.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, bacterial genetic code, and NCBI exact strain synonyms match `data/raw/ncbitaxon_taxa.tsv:210665`.
- The record is correctly grounded to the NCBI strain `NCBITaxon:1006000` under parent species `Kluyvera ascorbata`.
- The GTDB mapping from `data/raw/gtdb_mappings.tsv:1050` is a 29-genome species cluster, `GTDB:s__Kluyvera_ascorbata`, projected as `skos:closeMatch` onto the narrower NCBI strain.
- The GTDB projection also contributes xref `GTDB:s__Kluyvera_ascorbata` and exact synonym `Kluyvera ascorbata`, which make the parent species label look exactly synonymous with the ATCC 33433 strain.

## Evidence

- `data/raw/bacdive_strains.tsv:4864` supplies BacDive strain `4973`, designation `0648-74`, and eleven culture-collection identifiers including `ATCC-33433`.
- `data/raw/strain_genome_records.tsv:102920` through `data/raw/strain_genome_records.tsv:102926` account for the local GTDB, IMG, and PATRIC genome records under the matched strain.
- `data/straininfo/assemblies.tsv:9569` contributes the ATCC 33433 StrainInfo genome assembly retained in the strain payload.
- `data/raw/madin_taxa.tsv:351` supplies the three Madin trait assertions summarized by the `MADIN` source attestation.

## Completeness

- The BacDive and StrainInfo payloads are represented with `strain_count: 1`, eleven culture-collection IDs, the local assembly and genome records, and related records for the matched ATCC 33433 strain.
- The source attestations cover the expected NCBI, GTDB, BacDive, MediaDive, Madin, and BactoTraits evidence for this strain.

## Findings

- Major: the GTDB species cluster `GTDB:s__Kluyvera_ascorbata` is projected as a `skos:closeMatch`, xref, and exact synonym onto the narrower NCBI strain `NCBITaxon:1006000`. The record should keep strain `Kluyvera ascorbata ATCC 33433` distinct from the parent species label `Kluyvera ascorbata`.

## Recommended Edits

- Owner: `data/raw/gtdb_mappings.tsv` generation and taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`. Suppress species-cluster exact synonyms and strain-level `skos:closeMatch` projections when a GTDB species maps to a narrower NCBI strain.

## Follow-up Checks

- After the GTDB projection is corrected, regenerate this YAML and verify that `Kluyvera ascorbata` is no longer an exact synonym of `Kluyvera ascorbata ATCC 33433`.
- Keep the existing BacDive, NCBI Assembly, StrainInfo, and related strain payloads when regenerating.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
