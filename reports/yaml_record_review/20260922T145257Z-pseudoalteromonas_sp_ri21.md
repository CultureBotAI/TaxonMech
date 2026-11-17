# YAML Record Review: Pseudoalteromonas sp. RI21

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/pseudoalteromonas_sp_ri21.yaml`
- Started UTC: 2026-09-22T14:51:51Z
- Finished UTC: 2026-09-22T14:52:57Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/pseudoalteromonas_sp_ri21.yaml`
- Identifier: `NCBITaxon:1002542`
- Slug: `pseudoalteromonas_sp_ri21`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:194690` (`unclassified Pseudoalteromonas`)

## Validation

- `just validate data/taxa/bacteria/pseudoalteromonas_sp_ri21.yaml`: passed.
- `just validate-strict data/taxa/bacteria/roseovarius_sp_ri7.yaml data/taxa/bacteria/ruegeria_sp_ri20.yaml data/taxa/bacteria/pseudoalteromonas_sp_ri21.yaml data/taxa/bacteria/uncultured_mesoflavibacter_sp.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002542` / `Pseudoalteromonas sp. RI21`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:194690` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Pseudomonadati`, `Pseudomonadota`, `Gammaproteobacteria`, `Alteromonadales`, `Pseudoalteromonadaceae`, `Pseudoalteromonas`, then `unclassified Pseudoalteromonas`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:1002542`; its label, rank, genetic code, and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI row keyed to `NCBITaxon:1002542`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, MediaDive, BactoTraits, or strain-info rows keyed to this identifier.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `pseudoalteromonas_sp_ri21` review.
