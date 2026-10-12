# YAML Record Review: Pigmentiphaga sp. D-2

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/pigmentiphaga_sp_d_2.yaml`
- Started UTC: 2026-09-22T14:09:03Z
- Finished UTC: 2026-09-22T14:10:03Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/pigmentiphaga_sp_d_2.yaml`
- Identifier: `NCBITaxon:1002116`
- Slug: `pigmentiphaga_sp_d_2`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2626614` (`unclassified Pigmentiphaga`)

## Validation

- `just validate data/taxa/bacteria/pigmentiphaga_sp_d_2.yaml`: passed.
- `just validate-strict data/taxa/bacteria/streptomyces_sp_702_2011.yaml data/taxa/bacteria/pigmentiphaga_sp_d_2.yaml data/taxa/bacteria/lactobacillus_sp_mnfs_3.yaml data/taxa/bacteria/bacterium_mnfs_9.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002116` / `Pigmentiphaga sp. D-2`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:2626614` matches the pinned NCBI parent, `unclassified Pigmentiphaga`.
- The lineage stays within Bacteria through `Pseudomonadota`, `Betaproteobacteria`, `Burkholderiales`, `Alcaligenaceae`, `Pigmentiphaga`, then `unclassified Pigmentiphaga`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The NCBI and GTDB attestations are keyed directly to `NCBITaxon:1002116`; their labels and assertion counts match the reviewed raw rows. The GTDB evidence is the species-level `GTDB:s__Pigmentiphaga_daeguensis` close match with `genome_count: 7`.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI and GTDB rows keyed to `NCBITaxon:1002116`, and no ATB, BacDive, GOLD, LPSN, MADIN, or strain-info rows keyed to this identifier.

## Completeness

The GTDB-derived `Pigmentiphaga daeguensis` exact synonym and xref are present and preserve the only non-NCBI mapping for this species-rank record.

The record has no `strains`, `equivalent_identifiers`, `comments`, or product-level sections. None are required by the reviewed local evidence.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `pigmentiphaga_sp_d_2` review.
