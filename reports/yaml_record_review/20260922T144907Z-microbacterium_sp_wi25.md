# YAML Record Review: Microbacterium sp. WI25

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/microbacterium_sp_wi25.yaml`
- Started UTC: 2026-09-22T14:48:11Z
- Finished UTC: 2026-09-22T14:49:07Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/microbacterium_sp_wi25.yaml`
- Identifier: `NCBITaxon:1002535`
- Slug: `microbacterium_sp_wi25`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2609290` (`unclassified Microbacterium`)

## Validation

- `just validate data/taxa/bacteria/microbacterium_sp_wi25.yaml`: passed.
- `just validate-strict data/taxa/bacteria/streptomyces_sp_ca22.yaml data/taxa/bacteria/nonomuraea_sp_ca17.yaml data/taxa/bacteria/vibrio_sp_wi22.yaml data/taxa/bacteria/microbacterium_sp_wi25.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002535` / `Microbacterium sp. WI25`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:2609290` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Actinomycetota`, `Actinomycetes`, `Micrococcales`, `Microbacteriaceae`, `Microbacterium`, then `unclassified Microbacterium`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:1002535`; its label, rank, genetic code, and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI row keyed to `NCBITaxon:1002535`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, MediaDive, BactoTraits, or strain-info rows keyed to this identifier.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `microbacterium_sp_wi25` review.
