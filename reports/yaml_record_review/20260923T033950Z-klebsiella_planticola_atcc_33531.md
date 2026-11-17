# YAML Record Review: Klebsiella planticola ATCC 33531

- Repository: TaxonMech
- Record: data/taxa/bacteria/klebsiella_planticola_atcc_33531.yaml
- Started UTC: 2026-09-23T03:39:50Z
- Finished UTC: 2026-09-23T03:39:50Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1005996`
- Label: `Klebsiella planticola ATCC 33531`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:575` (`Klebsiella planticola`)
- Path registry row: `data/taxa/PATHS.tsv:2000`

## Validation

- `just validate-strict data/taxa/eukaryota/ogataea_parapolymorpha.yaml data/taxa/bacteria/trabulsiella_guamensis_atcc_49490.yaml data/taxa/bacteria/tatumella_ptyseos_atcc_33301.yaml data/taxa/bacteria/klebsiella_planticola_atcc_33531.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/klebsiella_planticola_atcc_33531.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-klebsiella_planticola_atcc_33531.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, bacterial genetic code, and NCBI exact strain synonyms match `data/raw/ncbitaxon_taxa.tsv:210663`.
- The record is correctly grounded to the NCBI strain `NCBITaxon:1005996` under parent species `Klebsiella planticola`.
- The GTDB mapping from `data/raw/gtdb_mappings.tsv:1046` is a 120-genome species cluster, `GTDB:s__Klebsiella_planticola`, projected as `skos:closeMatch` onto the narrower NCBI strain.
- The GTDB projection also contributes xref `GTDB:s__Klebsiella_planticola` and exact synonym `Klebsiella planticola`, which make the parent species label look exactly synonymous with the ATCC 33531 strain.

## Evidence

- `curation/seed_scope.tsv:7198` keeps this strain in scope through NCBI, GTDB, MediaDive, GOLD, Madin, and BactoTraits evidence.
- The same-strain raw evidence is available locally under the matched BacDive strain `bacdive:5097`: `data/raw/strain_assemblies.tsv:128990` through `data/raw/strain_assemblies.tsv:129001`, `data/raw/strain_genome_records.tsv:103661` through `data/raw/strain_genome_records.tsv:103666`, and `data/raw/strain_related_records.tsv:372198` through `data/raw/strain_related_records.tsv:372243`.
- `data/raw/bacdive_strains.tsv:4988` and `data/straininfo/strain_links.tsv:91186` tie culture collection `ATCC-33531` to BacDive strain `5097` at parent species taxon `NCBITaxon:575`.
- `data/straininfo/assemblies.tsv:9675` contributes the matching `GCA_000735435` genome assembly for `Raoultella planticola ATCC 33531`.
- `data/raw/gold_organisms.tsv:157` and `data/raw/madin_taxa.tsv:348` supply the GOLD and Madin evidence summarized by source attestations.

## Completeness

- The NCBI, MediaDive, GOLD, Madin, and BactoTraits source attestations are present.
- The record is incomplete for local strain evidence because ATCC 33531 assembly, genome, BioProject, BioSample, GOLD analysis, GOLD project, BacDive, and StrainInfo rows are locally available but `strain_count` remains 0 and no strain block is projected.

## Findings

- Major: the GTDB species cluster `GTDB:s__Klebsiella_planticola` is projected as a `skos:closeMatch`, xref, and exact synonym onto the narrower NCBI strain `NCBITaxon:1005996`. The record should keep strain `Klebsiella planticola ATCC 33531` distinct from the parent species label `Klebsiella planticola`.
- Major: local same-strain ATCC 33531 evidence is omitted even though raw BacDive, GOLD, IMG, PATRIC, NCBI Assembly, GTDB genome, BioProject, BioSample, and StrainInfo rows are available for the same culture identifier.

## Recommended Edits

- Owner: `data/raw/gtdb_mappings.tsv` generation and taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`. Suppress species-cluster exact synonyms and strain-level `skos:closeMatch` projections when a GTDB species maps to a narrower NCBI strain.
- Owner: BacDive/GOLD/IMG/StrainInfo strain projection in `src/taxonmech/seed.py`. Project the matched `ATCC-33531` strain evidence into this strain record or document why same-strain rows are intentionally retained only at parent species `NCBITaxon:575`.

## Follow-up Checks

- After the GTDB projection is corrected, regenerate this YAML and verify that `Klebsiella planticola` is no longer an exact synonym of `Klebsiella planticola ATCC 33531`.
- After the strain projection is corrected, verify that `strain_count`, strain assemblies, genome records, and related GOLD/BioSample/BioProject records agree with the local rows for `kgmicrobe.strain:bacdive_5097`.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
