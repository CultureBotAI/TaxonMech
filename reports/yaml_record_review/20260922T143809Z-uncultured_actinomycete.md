# YAML Record Review: uncultured actinomycete

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/uncultured_actinomycete.yaml`
- Started UTC: 2026-09-22T14:36:50Z
- Finished UTC: 2026-09-22T14:38:09Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/uncultured_actinomycete.yaml`
- Identifier: `NCBITaxon:100235`
- Slug: `uncultured_actinomycete`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:56769` (`environmental samples`)

## Validation

- `just validate data/taxa/bacteria/uncultured_actinomycete.yaml`: passed.
- `just validate-strict data/taxa/bacteria/uncultured_actinomycete.yaml data/taxa/bacteria/rickettsiella_armadillidii.yaml data/taxa/bacteria/hafnia_alvei_atcc_51873.yaml data/taxa/bacteria/lacticaseibacillus_rhamnosus_atcc_21052.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:100235` / `uncultured actinomycete`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:56769` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Actinomycetota`, `Actinomycetes`, `Actinomycetales`, then `environmental samples`.
- The six NCBI exact synonyms, including `Unknown actinomycete`, `unclassified actinomycete`, and `unidentified Actinomycetes bacterium`, are represented.
- The two GTDB mappings are intentionally broad pooled matches from MAG species onto this environmental NCBI placeholder.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI row and two GTDB broad-match mapping rows keyed to `NCBITaxon:100235`, and no ATB, BacDive, GOLD, LPSN, MADIN, or strain-info rows keyed to this identifier.

The same scan found two side-inventory old NCBI IDs, `NCBITaxon:35767` and `NCBITaxon:56770`, merged into this current ID by `data/raw/ncbi_merged_ids.tsv`; a follow-up exact search found no retained retired rows for those old IDs in `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, or `curation/seed_scope.tsv`.

## Completeness

The record includes the NCBI synonyms and both broad GTDB taxonomy mappings found in the pinned local evidence. It has no `strains`, `equivalent_identifiers`, `replaces`, `comments`, or product-level sections; none are required by the reviewed same-taxon evidence or the merged-ID side inventory.

## Findings

No findings.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- `just validate-history` was not run because this read-only review did not add a `history/` decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `uncultured_actinomycete` review.
