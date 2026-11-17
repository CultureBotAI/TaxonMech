# YAML Record Review: Planococcus halocryophilus Or1

- Repository: TaxonMech
- Record: data/taxa/bacteria/planococcus_halocryophilus_or1.yaml
- Started UTC: 2026-09-23T03:32:53Z
- Finished UTC: 2026-09-23T03:32:53Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1005941`
- Label: `Planococcus halocryophilus Or1`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1215089` (`Planococcus halocryophilus`)
- Path registry row: `data/taxa/PATHS.tsv:1992`

## Validation

- `just validate-strict data/taxa/bacteria/rickettsia_sp_cyrtu43d.yaml data/taxa/bacteria/rickettsia_sp_cyrtu43s.yaml data/taxa/bacteria/rickettsia_sp_cyrtu43g.yaml data/taxa/bacteria/planococcus_halocryophilus_or1.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/planococcus_halocryophilus_or1.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-planococcus_halocryophilus_or1.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, bacterial genetic code, and NCBI exact synonym `Planococcus sp. Or1` match `data/raw/ncbitaxon_taxa.tsv:210655`.
- `grounding_status: EXACT` is appropriate for the NCBI strain identity because the YAML represents `NCBITaxon:1005941`, a strain under the `Planococcus halocryophilus` species.
- The `GTDB:s__Planococcus_halocryophilus` projection from `data/raw/gtdb_mappings.tsv:1040` is not strain-specific evidence: it is a two-genome GTDB species cluster mapped onto the narrower NCBI strain.
- The GTDB projection also contributes the xref `GTDB:s__Planococcus_halocryophilus` and exact synonym `Planococcus halocryophilus`, which make the parent species label look exactly synonymous with strain `Planococcus halocryophilus Or1`.

## Evidence

- `curation/seed_scope.tsv:36052` keeps this strain in scope through NCBI, GTDB, and Madin evidence.
- `data/raw/madin_taxa.tsv:343` supplies the three Madin trait assertions summarized by the `MADIN` source attestation.
- `data/raw/bacdive_strains.tsv:11811` supplies a matched BacDive strain, `bacdive:11967`, with designation `Or1` and culture collections `DSM-24743` and `JCM-17719` on parent species `NCBITaxon:1215089`.
- Local same-strain raw rows tied directly to `NCBITaxon:1005941` are not projected into the YAML: `data/raw/strain_assemblies.tsv:9405`, `data/raw/strain_assemblies.tsv:9406`, and `data/raw/strain_assemblies.tsv:9410`; `data/raw/strain_genome_records.tsv:7260` through `data/raw/strain_genome_records.tsv:7266`; and multiple BioProject, BioSample, GOLD analysis, GOLD organism, and GOLD project rows in `data/raw/strain_related_records.tsv:27594` through `data/raw/strain_related_records.tsv:27620`.
- `data/straininfo/assemblies.tsv:911` and `data/straininfo/strain_links.tsv:6336` additionally link the same BacDive strain to the `DSM 24743` deposit at species taxon `NCBITaxon:1215089`.

## Completeness

- The NCBI and Madin source attestations are complete for the fields projected into the YAML.
- The record is incomplete for local strain evidence because same-strain BacDive, GOLD, IMG, assembly, BioProject, BioSample, and StrainInfo rows are available locally but `strain_count` remains 0 and the record has no strain blocks or related accessions.

## Findings

- Major: the GTDB species cluster `GTDB:s__Planococcus_halocryophilus` is projected as a `skos:closeMatch`, xref, and exact synonym onto the narrower NCBI strain `NCBITaxon:1005941`. That makes the species name `Planococcus halocryophilus` exactly synonymous with strain `Planococcus halocryophilus Or1`.
- Major: local same-strain evidence for BacDive strain `11967` / `DSM-24743` / `JCM-17719` is omitted even though raw assembly, genome, and related-record rows exist around `data/raw/strain_assemblies.tsv:9405`, `data/raw/strain_genome_records.tsv:7260`, and `data/raw/strain_related_records.tsv:27594`.

## Recommended Edits

- Owner: `data/raw/gtdb_mappings.tsv` generation and taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`. Suppress species-cluster exact synonyms and strain-level `skos:closeMatch` projections when a GTDB species maps to a narrower NCBI strain.
- Owner: BacDive/GOLD/IMG strain projection in `src/taxonmech/seed.py`. Project the matched `bacdive:11967` strain evidence, culture-collection identifiers, assemblies, IMG/PATRIC genome records, and GOLD related records onto the strain record or document why same-strain rows are intentionally retained only at the parent species.

## Follow-up Checks

- After the GTDB projection is corrected, regenerate this YAML and verify that `Planococcus halocryophilus` is no longer an exact synonym of `Planococcus halocryophilus Or1`.
- After the strain projection is corrected, verify that `strain_count`, strain assemblies, genome records, and related GOLD/BioSample/BioProject records agree with the local rows for `kgmicrobe.strain:bacdive_11967`.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
