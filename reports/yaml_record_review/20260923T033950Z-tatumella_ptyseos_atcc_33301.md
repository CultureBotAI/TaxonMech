# YAML Record Review: Tatumella ptyseos ATCC 33301

- Repository: TaxonMech
- Record: data/taxa/bacteria/tatumella_ptyseos_atcc_33301.yaml
- Started UTC: 2026-09-23T03:39:50Z
- Finished UTC: 2026-09-23T03:39:50Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1005995`
- Label: `Tatumella ptyseos ATCC 33301`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:82987` (`Tatumella ptyseos`)
- Path registry row: `data/taxa/PATHS.tsv:1999`

## Validation

- `just validate-strict data/taxa/eukaryota/ogataea_parapolymorpha.yaml data/taxa/bacteria/trabulsiella_guamensis_atcc_49490.yaml data/taxa/bacteria/tatumella_ptyseos_atcc_33301.yaml data/taxa/bacteria/klebsiella_planticola_atcc_33531.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/tatumella_ptyseos_atcc_33301.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-tatumella_ptyseos_atcc_33301.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, bacterial genetic code, and NCBI exact strain synonyms match `data/raw/ncbitaxon_taxa.tsv:210662`.
- The record is correctly grounded to the NCBI strain `NCBITaxon:1005995` under parent species `Tatumella ptyseos`.
- The GTDB mapping from `data/raw/gtdb_mappings.tsv:1045` is a six-genome species cluster, `GTDB:s__Tatumella_ptyseos`, projected as `skos:closeMatch` onto the narrower NCBI strain.
- The GTDB projection also contributes xref `GTDB:s__Tatumella_ptyseos` and exact synonym `Tatumella ptyseos`, which make the parent species label look exactly synonymous with the ATCC 33301 strain.

## Evidence

- `curation/seed_scope.tsv:10774` keeps this strain in scope through NCBI, GTDB, BacDive, MediaDive, Madin, and BactoTraits evidence.
- `data/raw/bacdive_strains.tsv:5067` supplies BacDive strain `5176`, designation `H36`, and seven culture-collection identifiers including `ATCC-33301`, `DSM-5000`, `LMG-7888`, and `NCTC-11468`.
- `data/raw/strain_assemblies.tsv:129831` through `data/raw/strain_assemblies.tsv:129851` account for the local BacDive, BV-BRC, GOLD, GTDB, and NCBI Assembly assembly rows projected under the matched BacDive strain.
- `data/raw/strain_genome_records.tsv:104266` through `data/raw/strain_genome_records.tsv:104281` account for the local GTDB, IMG, and PATRIC genome records under the matched strain.
- `data/raw/strain_related_records.tsv:374352` and following rows account for the projected BioProject, BioSample, GOLD analysis, GOLD organism, and GOLD project records.
- `data/straininfo/assemblies.tsv:9766` and `data/straininfo/assemblies.tsv:9767` contribute the ATCC 33301 assembly evidence that the YAML retains as StrainInfo assembly rows.

## Completeness

- The BacDive and StrainInfo payloads are represented with `strain_count: 1`, seven culture-collection IDs, genome assemblies, genome records, and related records for the matched ATCC 33301/NCTC 11468 strain evidence.
- The source attestations cover the expected NCBI, GTDB, BacDive, MediaDive, Madin, and BactoTraits evidence for this strain.

## Findings

- Major: the GTDB species cluster `GTDB:s__Tatumella_ptyseos` is projected as a `skos:closeMatch`, xref, and exact synonym onto the narrower NCBI strain `NCBITaxon:1005995`. The record should keep strain `Tatumella ptyseos ATCC 33301` distinct from the parent species label `Tatumella ptyseos`.

## Recommended Edits

- Owner: `data/raw/gtdb_mappings.tsv` generation and taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`. Suppress species-cluster exact synonyms and strain-level `skos:closeMatch` projections when a GTDB species maps to a narrower NCBI strain.

## Follow-up Checks

- After the GTDB projection is corrected, regenerate this YAML and verify that `Tatumella ptyseos` is no longer an exact synonym of `Tatumella ptyseos ATCC 33301`.
- Keep the existing BacDive, GOLD, NCBI Assembly, and StrainInfo strain payloads when regenerating.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
