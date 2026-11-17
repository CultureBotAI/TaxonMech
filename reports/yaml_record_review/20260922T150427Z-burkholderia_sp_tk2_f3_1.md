# YAML Record Review: Burkholderia sp. TK2-F3-1

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/burkholderia_sp_tk2_f3_1.yaml`
- Started UTC: 2026-09-22T15:03:41Z
- Finished UTC: 2026-09-22T15:04:27Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/burkholderia_sp_tk2_f3_1.yaml`
- Identifier: `NCBITaxon:1002570`
- Slug: `burkholderia_sp_tk2_f3_1`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2613784` (`unclassified Burkholderia`)

## Validation

- `just validate data/taxa/bacteria/burkholderia_sp_tk2_f3_1.yaml`: passed.
- `just validate-strict data/taxa/bacteria/burkholderia_sp_tk2_f2_8.yaml data/taxa/bacteria/burkholderia_sp_tk2_f2_9.yaml data/taxa/bacteria/burkholderia_sp_tk2_f2_14.yaml data/taxa/bacteria/burkholderia_sp_tk2_f3_1.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002570` / `Burkholderia sp. TK2-F3-1`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:2613784` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Pseudomonadati`, `Pseudomonadota`, `Betaproteobacteria`, `Burkholderiales`, `Burkholderiaceae`, `Burkholderia`, then `unclassified Burkholderia`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:1002570`; its label, rank, genetic code, and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI row keyed to `NCBITaxon:1002570`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, MediaDive, BactoTraits, or strain-info rows keyed to this identifier.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `burkholderia_sp_tk2_f3_1` review.
