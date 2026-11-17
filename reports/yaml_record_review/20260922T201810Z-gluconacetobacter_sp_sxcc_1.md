# YAML Record Review: Gluconacetobacter sp. SXCC-1
- Repository: TaxonMech
- Record: `data/taxa/bacteria/gluconacetobacter_sp_sxcc_1.yaml`
- Started UTC: 2026-09-22T20:17:03Z
- Finished UTC: 2026-09-22T20:18:10Z
- Verdict: pass

## Target
- Reviewed `NCBITaxon:1004836` / `gluconacetobacter_sp_sxcc_1`.
- The record is a `SPECIES`-rank `BACTERIA` record for `Gluconacetobacter sp. SXCC-1`.
- Parentage is the seeded NCBI placement under `NCBITaxon:2639119` (`unclassified Gluconacetobacter`), with lineage through `Pseudomonadota`, `Alphaproteobacteria`, `Acetobacterales`, `Acetobacteraceae`, and `Gluconacetobacter`.

## Validation
- `just validate data/taxa/bacteria/gluconacetobacter_sp_sxcc_1.yaml` completed successfully.
- `just validate-strict data/taxa/bacteria/spiroplasma_symbiont_of_antonina_crawii.yaml data/taxa/bacteria/beta_symbiont_of_antonina_crawii.yaml data/taxa/bacteria/gluconacetobacter_sp_sxcc_1.yaml data/taxa/bacteria/gamma_symbiont_of_antonina_crawii.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was not applicable because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `id: NCBITaxon:1004836`, `label: Gluconacetobacter sp. SXCC-1`, `rank: SPECIES`, `domain: BACTERIA`, `parent: NCBITaxon:2639119`, and `genetic_code: 11` match the pinned row in `data/raw/ncbitaxon_taxa.tsv`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a directly seeded NCBI Taxon record.
- The `Komagataeibacter rhaeticus` synonym and `GTDB:s__Komagataeibacter_rhaeticus` xref are supported by the same-taxon GTDB species mapping.

## Evidence
- Local same-taxon source rows for `NCBITaxon:1004836` include `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv`.
- `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Komagataeibacter_rhaeticus` to this NCBI species with `skos:closeMatch` and `genome_count: 15`.
- `data/raw/madin_taxa.tsv` contributes five trait assertions.
- The gitignore-independent `rg --no-ignore --hidden` search across `data/raw`, `data/atb`, `data/straininfo`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv` found no ATB, GOLD, or StrainInfo rows for this exact NCBI taxon.

## Completeness
- `strain_count: 0` is consistent with the absence of same-taxon strain rows in the local pinned StrainInfo tables.
- The record includes the expected NCBITAXON, GTDB, and MADIN source attestations from the pinned source rows.
- The empty ATB, strain, and assembly sections are expected for the local evidence present here.

## Findings
- No findings.

## Recommended Edits
- None.

## Follow-up Checks
- None required for this record.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name *-gluconacetobacter_sp_sxcc_1.md` returned no prior ignored report for this stem.
- Live NCBI and GTDB lookup were not used; local pinned source rows dated `2026-09-13` were treated as the source of truth.
