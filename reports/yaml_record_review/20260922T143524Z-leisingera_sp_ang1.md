# YAML Record Review: Leisingera sp. ANG1

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/leisingera_sp_ang1.yaml`
- Started UTC: 2026-09-22T14:31:12Z
- Finished UTC: 2026-09-22T14:35:24Z
- Verdict: needs curation

## Target

- Record: `data/taxa/bacteria/leisingera_sp_ang1.yaml`
- Identifier: `NCBITaxon:1002340`
- Slug: `leisingera_sp_ang1`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2614906` (`unclassified Leisingera`)

## Validation

- `just validate data/taxa/bacteria/leisingera_sp_ang1.yaml`: passed.
- `just validate-strict data/taxa/bacteria/bordetella_petrii_104.yaml data/taxa/bacteria/psychrobacter_sp_1501_2011.yaml data/taxa/bacteria/uncultured_verrucomicrobiales_bacterium.yaml data/taxa/bacteria/leisingera_sp_ang1.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The NCBI placeholder identity is exact for `NCBITaxon:1002340` / `Leisingera sp. ANG1`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:2614906` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Pseudomonadota`, `Alphaproteobacteria`, `Rhodobacterales`, `Roseobacteraceae`, `Leisingera`, then `unclassified Leisingera`.
- The NCBI exact synonym `Phaeobacter gallaeciensis ANG1` is represented.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.
- The GTDB-derived close match and exact synonym need curation review because `GTDB:s__Leisingera_sp000203975`, a six-genome GTDB species cluster, is grafted directly onto this NCBI `Leisingera sp.` placeholder.

## Evidence

The local exact-ID search found the NCBI row, one GTDB `skos:closeMatch` row, and three MADIN trait assertions keyed directly to `NCBITaxon:1002340`. The reviewed YAML carries those same source attestations plus the GTDB taxonomy mapping, GTDB xref, GTDB-derived exact synonym, and NCBI exact synonym.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found no ATB, BacDive, GOLD, LPSN, or strain-info rows keyed to this identifier.

## Completeness

The record represents all direct local source rows keyed to `NCBITaxon:1002340`. It has no `strains`, `equivalent_identifiers`, `comments`, or product-level sections; none are required by the reviewed same-taxon evidence.

## Findings

- Major: a species-scale GTDB mapping is attached directly to the NCBI `Leisingera sp. ANG1` seed. `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Leisingera_sp000203975` to `NCBITaxon:1002340` with `skos:closeMatch` and `genome_count: 6`, and the generator turns that row into a taxonomy mapping, a GTDB xref, and an `EXACT_SYNONYM` of `Leisingera sp000203975`. Owner: the GTDB mapping import behind `data/raw/gtdb_mappings.tsv` and the generated `data/taxa` emission of GTDB close-match synonyms.

## Recommended Edits

- Review whether the `GTDB:s__Leisingera_sp000203975` close match and its derived `Leisingera sp000203975` exact synonym should remain on `NCBITaxon:1002340`, or whether only the NCBI synonym `Phaeobacter gallaeciensis ANG1` and directly keyed MADIN trait assertions should be kept on this NCBI placeholder.

## Follow-up Checks

- After curation, rerun `just validate data/taxa/bacteria/leisingera_sp_ang1.yaml` and `just validate-strict data/taxa/bacteria/leisingera_sp_ang1.yaml`.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- `just validate-history` was not run because this read-only review did not add a `history/` decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `leisingera_sp_ang1` review.
