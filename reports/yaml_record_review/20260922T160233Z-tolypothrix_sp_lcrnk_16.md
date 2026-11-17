# YAML Record Review: Tolypothrix sp. LCRNK.16

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/tolypothrix_sp_lcrnk_16.yaml`
- Started UTC: 2026-09-22T16:01:40Z
- Finished UTC: 2026-09-22T16:02:33Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/tolypothrix_sp_lcrnk_16.yaml`
- Identifier: `NCBITaxon:1002841`
- Slug: `tolypothrix_sp_lcrnk_16`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2649714` (`unclassified Tolypothrix`)

## Validation

- `just validate data/taxa/bacteria/tolypothrix_sp_lcrnk_16.yaml`: passed.
- `just validate-strict data/taxa/bacteria/nostoc_sp_lcrnk_13.yaml data/taxa/bacteria/nostoc_sp_lcrnk_14.yaml data/taxa/bacteria/tolypothrix_sp_lcrnk_16.yaml data/taxa/bacteria/nostoc_sp_lcrnk_19.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002841` / `Tolypothrix sp. LCRNK.16`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:2649714` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Bacillati`, `Cyanobacteriota/Melainabacteria group`, `Cyanobacteriota`, `Cyanophyceae`, `Nostocales`, `Tolypothrichaceae`, `Tolypothrix`, then `unclassified Tolypothrix`.
- The NCBI exact synonym `Nostoc sp. LCRNK.16` is present in `synonyms`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:1002841`; its label, rank, exact synonym, genetic code, and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected `curation/seed_scope.tsv` and NCBI rows keyed to `NCBITaxon:1002841`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, MediaDive, BactoTraits, or strain-info rows keyed to this identifier.

## Completeness

The record carries the expected NCBI `synonyms`. It has no `taxonomy_mappings`, `xrefs`, `strains`, `comments`, or product-level sections. None are required by the reviewed local evidence.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `tolypothrix_sp_lcrnk_16` review.
