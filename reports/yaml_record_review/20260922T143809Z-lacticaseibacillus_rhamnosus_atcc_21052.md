# YAML Record Review: Lacticaseibacillus rhamnosus ATCC 21052

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/lacticaseibacillus_rhamnosus_atcc_21052.yaml`
- Started UTC: 2026-09-22T14:36:50Z
- Finished UTC: 2026-09-22T14:38:09Z
- Verdict: needs curation

## Target

- Record: `data/taxa/bacteria/lacticaseibacillus_rhamnosus_atcc_21052.yaml`
- Identifier: `NCBITaxon:1002365`
- Slug: `lacticaseibacillus_rhamnosus_atcc_21052`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:47715` (`Lacticaseibacillus rhamnosus`)

## Validation

- `just validate data/taxa/bacteria/lacticaseibacillus_rhamnosus_atcc_21052.yaml`: passed.
- `just validate-strict data/taxa/bacteria/uncultured_actinomycete.yaml data/taxa/bacteria/rickettsiella_armadillidii.yaml data/taxa/bacteria/hafnia_alvei_atcc_51873.yaml data/taxa/bacteria/lacticaseibacillus_rhamnosus_atcc_21052.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The NCBI strain identity is exact for `NCBITaxon:1002365` / `Lacticaseibacillus rhamnosus ATCC 21052`.

- `identifier`, `label`, `rank: STRAIN`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:47715` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Bacillota`, `Bacilli`, `Lactobacillales`, `Lactobacillaceae`, `Lacticaseibacillus`, then `Lacticaseibacillus rhamnosus`.
- The NCBI exact synonyms `Lactobacillus rhamnosus BCRC 14029`, `Lactobacillus rhamnosus str. ATCC 21052`, and `Lactobacillus rhamnosus strain ATCC 21052` are represented.
- `grounding_status: EXACT` is correct for the NCBI strain seed itself.
- The GTDB-derived close match and exact synonym need curation review because `GTDB:s__Lacticaseibacillus_rhamnosus`, a 480-genome species cluster that also maps to many other NCBI taxa and to the parent species `NCBITaxon:47715`, is grafted directly onto one ATCC strain.

## Evidence

The local exact-ID search found the NCBI row, one GTDB `skos:closeMatch` row, and four MADIN trait assertions keyed directly to `NCBITaxon:1002365`. The reviewed YAML carries those same source attestations plus the GTDB taxonomy mapping, GTDB xref, GTDB-derived exact synonym, and NCBI exact synonyms.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found no ATB, BacDive, GOLD, LPSN, or strain-info rows keyed to this identifier. An exact GTDB ID search found `GTDB:s__Lacticaseibacillus_rhamnosus` mapped to many NCBI taxa, including the parent species `NCBITaxon:47715`.

## Completeness

The record represents all direct local source rows keyed to `NCBITaxon:1002365`. It has no `strains`, `equivalent_identifiers`, `comments`, or product-level sections; none are required by the reviewed same-taxon evidence.

## Findings

- Major: a species-scale GTDB mapping is attached directly to the `Lacticaseibacillus rhamnosus ATCC 21052` strain seed. `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Lacticaseibacillus_rhamnosus` to `NCBITaxon:1002365` with `skos:closeMatch` and `genome_count: 480`, and the generator turns that row into a taxonomy mapping, a GTDB xref, and an `EXACT_SYNONYM` of `Lacticaseibacillus rhamnosus`. Owner: the GTDB mapping import behind `data/raw/gtdb_mappings.tsv` and the generated `data/taxa` emission of GTDB close-match synonyms.

## Recommended Edits

- Review whether the `GTDB:s__Lacticaseibacillus_rhamnosus` close match and its derived parent-species exact synonym should remain on this strain record, be represented only as a broader species-cluster relationship, or be moved to the `Lacticaseibacillus rhamnosus` species record or another aggregate that does not make one ATCC strain denote the whole 480-genome GTDB species.

## Follow-up Checks

- After curation, rerun `just validate data/taxa/bacteria/lacticaseibacillus_rhamnosus_atcc_21052.yaml` and `just validate-strict data/taxa/bacteria/lacticaseibacillus_rhamnosus_atcc_21052.yaml`.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- `just validate-history` was not run because this read-only review did not add a `history/` decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `lacticaseibacillus_rhamnosus_atcc_21052` review.
