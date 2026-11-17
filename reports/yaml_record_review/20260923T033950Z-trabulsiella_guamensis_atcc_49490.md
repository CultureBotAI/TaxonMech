# YAML Record Review: Trabulsiella guamensis ATCC 49490

- Repository: TaxonMech
- Record: data/taxa/bacteria/trabulsiella_guamensis_atcc_49490.yaml
- Started UTC: 2026-09-23T03:39:50Z
- Finished UTC: 2026-09-23T03:39:50Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1005994`
- Label: `Trabulsiella guamensis ATCC 49490`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:158852` (`Trabulsiella guamensis`)
- Path registry row: `data/taxa/PATHS.tsv:1998`

## Validation

- `just validate-strict data/taxa/eukaryota/ogataea_parapolymorpha.yaml data/taxa/bacteria/trabulsiella_guamensis_atcc_49490.yaml data/taxa/bacteria/tatumella_ptyseos_atcc_33301.yaml data/taxa/bacteria/klebsiella_planticola_atcc_33531.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/trabulsiella_guamensis_atcc_49490.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-trabulsiella_guamensis_atcc_49490.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, bacterial genetic code, and NCBI exact strain synonyms match `data/raw/ncbitaxon_taxa.tsv:210661`.
- The record is correctly grounded to the NCBI strain `NCBITaxon:1005994` under parent species `Trabulsiella guamensis`.
- The GTDB mapping from `data/raw/gtdb_mappings.tsv:1044` is a species cluster, `GTDB:s__Trabulsiella_guamensis`, projected as `skos:closeMatch` onto the narrower NCBI strain.
- The GTDB projection also contributes xref `GTDB:s__Trabulsiella_guamensis` and exact synonym `Trabulsiella guamensis`, which make the parent species label look exactly synonymous with the ATCC 49490 strain.

## Evidence

- `curation/seed_scope.tsv:14812` keeps this strain in scope through NCBI, GTDB, BacDive, MediaDive, and Madin evidence.
- `data/raw/bacdive_strains.tsv:5072` supplies BacDive strain `5181`, designation `370-85`, and seven culture-collection identifiers including `ATCC-49490`.
- `data/raw/strain_assemblies.tsv:129913` through `data/raw/strain_assemblies.tsv:129920` account for the BacDive, BV-BRC, GOLD, GTDB, and NCBI Assembly rows projected under the matched strain.
- `data/raw/strain_genome_records.tsv:104325` through `data/raw/strain_genome_records.tsv:104330` account for the GTDB, IMG, and PATRIC genome records.
- `data/raw/strain_related_records.tsv:374569` through `data/raw/strain_related_records.tsv:374590` account for the direct BioProject, BioSample, GOLD analysis, GOLD organism, and GOLD project rows, while the YAML also retains additional GOLD organism and StrainInfo deposit rows matched through the same BacDive strain.
- `data/straininfo/assemblies.tsv:9772` contributes the genome assembly for the `ATCC 49490` deposit, and the same StrainInfo strain supplies the projected deposit and rRNA sequence records.

## Completeness

- The BacDive and StrainInfo payloads are represented with `strain_count: 1`, seven culture-collection IDs, genome assemblies, genome records, and related records for the matched ATCC 49490 strain.
- The source attestations cover the expected NCBI, GTDB, BacDive, MediaDive, and Madin evidence for this strain.

## Findings

- Major: the GTDB species cluster `GTDB:s__Trabulsiella_guamensis` is projected as a `skos:closeMatch`, xref, and exact synonym onto the narrower NCBI strain `NCBITaxon:1005994`. The record should keep strain `Trabulsiella guamensis ATCC 49490` distinct from the parent species label `Trabulsiella guamensis`.

## Recommended Edits

- Owner: `data/raw/gtdb_mappings.tsv` generation and taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`. Suppress species-cluster exact synonyms and strain-level `skos:closeMatch` projections when a GTDB species maps to a narrower NCBI strain.

## Follow-up Checks

- After the GTDB projection is corrected, regenerate this YAML and verify that `Trabulsiella guamensis` is no longer an exact synonym of `Trabulsiella guamensis ATCC 49490`.
- Keep the existing BacDive, GOLD, NCBI Assembly, and StrainInfo strain payloads when regenerating.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
