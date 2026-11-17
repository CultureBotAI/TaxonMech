# YAML Record Review: Rickettsiella armadillidii

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/rickettsiella_armadillidii.yaml`
- Started UTC: 2026-09-22T14:36:50Z
- Finished UTC: 2026-09-22T14:38:09Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/rickettsiella_armadillidii.yaml`
- Identifier: `NCBITaxon:1002363`
- Slug: `rickettsiella_armadillidii`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:59195` (`Rickettsiella`)

## Validation

- `just validate data/taxa/bacteria/rickettsiella_armadillidii.yaml`: passed.
- `just validate-strict data/taxa/bacteria/uncultured_actinomycete.yaml data/taxa/bacteria/rickettsiella_armadillidii.yaml data/taxa/bacteria/hafnia_alvei_atcc_51873.yaml data/taxa/bacteria/lacticaseibacillus_rhamnosus_atcc_21052.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002363` / `Rickettsiella armadillidii`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:59195` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Pseudomonadota`, `Gammaproteobacteria`, `Legionellales`, `Coxiellaceae`, then `Rickettsiella`.
- The four NCBI related synonyms are represented as `RELATED_SYNONYM`, including the three host-specific symbiont labels.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:1002363`; its label, rank, related synonyms, genetic code, and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI row keyed to `NCBITaxon:1002363`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, or strain-info rows keyed to this identifier. The same scan found three side-inventory old NCBI IDs, `NCBITaxon:424494`, `NCBITaxon:424495`, and `NCBITaxon:424496`, merged into this current ID; a follow-up exact search found no retained retired rows for those old IDs in `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, or `curation/seed_scope.tsv`.

## Completeness

The record includes the NCBI species identity and all four NCBI related synonyms. It has no `taxonomy_mappings`, `xrefs`, `strains`, `equivalent_identifiers`, `replaces`, `comments`, or product-level sections. None are required by the reviewed local evidence or the merged-ID side inventory.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `rickettsiella_armadillidii` review.
