# YAML Record Review: Anabaena sp. LCRNK_4

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/anabaena_sp_lcrnk_4.yaml`
- Started UTC: 2026-09-22T15:54:09Z
- Finished UTC: 2026-09-22T15:55:04Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/anabaena_sp_lcrnk_4.yaml`
- Identifier: `NCBITaxon:1002824`
- Slug: `anabaena_sp_lcrnk_4`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2619674` (`unclassified Anabaena`)

## Validation

- `just validate data/taxa/bacteria/anabaena_sp_lcrnk_4.yaml`: passed.
- `just validate-strict data/taxa/bacteria/anabaena_sp_lcrnk_23.yaml data/taxa/bacteria/anabaena_sp_lcrnk_27.yaml data/taxa/bacteria/anabaena_sp_lcrnk_28.yaml data/taxa/bacteria/anabaena_sp_lcrnk_4.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002824` / `Anabaena sp. LCRNK_4`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:2619674` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Bacillati`, `Cyanobacteriota/Melainabacteria group`, `Cyanobacteriota`, `Cyanophyceae`, `Nostocales`, `Nostocaceae`, `Anabaena`, then `unclassified Anabaena`.
- The NCBI exact synonym `Anabaena sp. LCRNK.4` is present in `synonyms`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The exact same-taxon source rows are the NCBI row for `NCBITaxon:1002824` and the NCBI merged-ID row from old `NCBITaxon:1002819` to `NCBITaxon:1002824`.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected `curation/seed_scope.tsv`, NCBI, and NCBI merged-ID rows, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, MediaDive, BactoTraits, or strain-info rows keyed to `NCBITaxon:1002824`.

## Completeness

The record carries the expected NCBI `synonyms`. The raw NCBI merged-ID row for old `NCBITaxon:1002819` is ledger evidence only here: `NCBITaxon:1002819` is not in `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/straininfo`, or `data/atb`, and the YAML `replaces` field is seeded from retired NCBI taxon rows that carry `retired_into`.

There are no `taxonomy_mappings`, `xrefs`, `strains`, `comments`, or product-level sections. None are required by the reviewed local evidence.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `anabaena_sp_lcrnk_4` review.
