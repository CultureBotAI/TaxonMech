# YAML Record Review: Bordetella petrii 104

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/bordetella_petrii_104.yaml`
- Started UTC: 2026-09-22T14:31:12Z
- Finished UTC: 2026-09-22T14:35:24Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/bordetella_petrii_104.yaml`
- Identifier: `NCBITaxon:1002338`
- Slug: `bordetella_petrii_104`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:94624` (`Bordetella petrii`)

## Validation

- `just validate data/taxa/bacteria/bordetella_petrii_104.yaml`: passed.
- `just validate-strict data/taxa/bacteria/bordetella_petrii_104.yaml data/taxa/bacteria/psychrobacter_sp_1501_2011.yaml data/taxa/bacteria/uncultured_verrucomicrobiales_bacterium.yaml data/taxa/bacteria/leisingera_sp_ang1.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002338` / `Bordetella petrii 104`.

- `identifier`, `label`, `rank: STRAIN`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:94624` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Pseudomonadota`, `Betaproteobacteria`, `Burkholderiales`, `Alcaligenaceae`, `Bordetella`, then `Bordetella petrii`.
- NCBI exact synonyms `Bordetella petrii str. 104` and `Bordetella petrii strain 104` are both represented.
- `grounding_status: EXACT` is correct for the NCBI strain seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:1002338`; its label, rank, synonyms, genetic code, and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI row keyed to `NCBITaxon:1002338`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, or strain-info rows keyed to this identifier.

## Completeness

The record includes the NCBI strain identity and both NCBI exact synonyms. It has no `taxonomy_mappings`, `xrefs`, `strains`, `equivalent_identifiers`, `comments`, or product-level sections. None are required by the reviewed same-taxon evidence.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `bordetella_petrii_104` review.
