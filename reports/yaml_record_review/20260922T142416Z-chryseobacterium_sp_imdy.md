# YAML Record Review: Chryseobacterium sp. IMDY

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/chryseobacterium_sp_imdy.yaml`
- Started UTC: 2026-09-22T14:23:25Z
- Finished UTC: 2026-09-22T14:24:16Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/chryseobacterium_sp_imdy.yaml`
- Identifier: `NCBITaxon:1002238`
- Slug: `chryseobacterium_sp_imdy`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2593645` (`unclassified Chryseobacterium`)

## Validation

- `just validate data/taxa/bacteria/chryseobacterium_sp_imdy.yaml`: passed.
- `just validate-strict data/taxa/bacteria/pseudomonas_sp_aw4.yaml data/taxa/bacteria/leuconostoc_sp_imw2.yaml data/taxa/bacteria/chryseobacterium_sp_imdy.yaml data/taxa/bacteria/kocuria_sp_tm2.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002238` / `Chryseobacterium sp. IMDY`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:2593645` matches the pinned NCBI parent, `unclassified Chryseobacterium`.
- The lineage stays within Bacteria through `FCB group`, `Bacteroidota/Chlorobiota group`, `Bacteroidota`, `Flavobacteriia`, `Flavobacteriales`, `Weeksellaceae`, `Chryseobacterium`, then `unclassified Chryseobacterium`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:1002238`; its label and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI row keyed to `NCBITaxon:1002238`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, or strain-info rows keyed to this identifier.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `chryseobacterium_sp_imdy` review.
