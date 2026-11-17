# YAML Record Review: Tolypothrix sp. LCRNK_3

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/tolypothrix_sp_lcrnk_3.yaml`
- Started UTC: 2026-09-22T16:11:10Z
- Finished UTC: 2026-09-22T16:12:08Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/tolypothrix_sp_lcrnk_3.yaml`
- Identifier: `NCBITaxon:1002863`
- Slug: `tolypothrix_sp_lcrnk_3`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2649714` (`unclassified Tolypothrix`)

## Validation

- `just validate data/taxa/bacteria/tolypothrix_sp_lcrnk_3.yaml`: passed.
- `just validate-strict data/taxa/bacteria/tolypothrix_sp_lcrnk_3.yaml data/taxa/bacteria/tolypothrix_sp_lcrnk_5.yaml data/taxa/bacteria/tolypothrix_sp_lcrnk_8.yaml data/taxa/bacteria/gaiella_occulta.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002863` / `Tolypothrix sp. LCRNK_3`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:2649714` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Bacillati`, `Cyanobacteriota/Melainabacteria group`, `Cyanobacteriota`, `Cyanophyceae`, `Nostocales`, `Tolypothrichaceae`, `Tolypothrix`, then `unclassified Tolypothrix`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:1002863`; its label, rank, genetic code, and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, and NCBI rows keyed to `NCBITaxon:1002863` / `Tolypothrix sp. LCRNK_3`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, MediaDive, BactoTraits, strain-info, or NCBI merge-ledger rows keyed to this taxon.

## Completeness

The record has no `taxonomy_mappings`, `synonyms`, `xrefs`, `strains`, `equivalent_identifiers`, `comments`, or product-level sections. None are required by the reviewed local evidence.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `tolypothrix_sp_lcrnk_3` review.
