# YAML Record Review: Nocardia sp. COA

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/nocardia_sp_coa.yaml`
- Started UTC: 2026-09-22T14:07:24Z
- Finished UTC: 2026-09-22T14:08:13Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/nocardia_sp_coa.yaml`
- Identifier: `NCBITaxon:1002114`
- Slug: `nocardia_sp_coa`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2637762` (`unclassified Nocardia`)

## Validation

- `just validate data/taxa/bacteria/nocardia_sp_coa.yaml`: passed.
- `just validate-strict data/taxa/bacteria/corynebacterium_sp_cob2.yaml data/taxa/bacteria/enterobacter_sp_cob5.yaml data/taxa/bacteria/micromonospora_sp_coa3.yaml data/taxa/bacteria/nocardia_sp_coa.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002114` / `Nocardia sp. COA`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:2637762` matches the pinned NCBI parent, `unclassified Nocardia`.
- The lineage stays within Bacteria through `Bacillati`, `Actinomycetota`, `Actinomycetes`, `Mycobacteriales`, `Nocardiaceae`, `Nocardia`, then `unclassified Nocardia`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:1002114`; its label and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI row keyed to `NCBITaxon:1002114`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, or strain-info rows keyed to this identifier.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `nocardia_sp_coa` review.
