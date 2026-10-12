# YAML Record Review: uncultured Cohaesibacter sp.

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/uncultured_cohaesibacter_sp.yaml`
- Started UTC: 2026-09-22T14:54:18Z
- Finished UTC: 2026-09-22T14:55:31Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/uncultured_cohaesibacter_sp.yaml`
- Identifier: `NCBITaxon:1002546`
- Slug: `uncultured_cohaesibacter_sp`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1002545` (`environmental samples`)

## Validation

- `just validate data/taxa/bacteria/uncultured_cohaesibacter_sp.yaml`: passed.
- `just validate-strict data/taxa/bacteria/uncultured_cohaesibacter_sp.yaml data/taxa/bacteria/uncultured_methylarcula_sp.yaml data/taxa/bacteria/burkholderia_sp_tk1_f1_3.yaml data/taxa/bacteria/burkholderia_sp_tk1_f1_5.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002546` / `uncultured Cohaesibacter sp.`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:1002545` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Pseudomonadota`, `Alphaproteobacteria`, `Hyphomicrobiales`, `Cohaesibacteraceae`, `Cohaesibacter`, then environmental samples.
- The eleven GTDB `skos:broadMatch` rows in `taxonomy_mappings` all map to `NCBITaxon:1002546` with the same `g__Cohaesibacter` parent and with genome counts matching `data/raw/gtdb_species.tsv`.
- The GTDB source attestation summarizes the largest four-genome mapping, `GTDB:s__Cohaesibacter_sp963667045`, and notes the ten further pooled GTDB species represented in `taxonomy_mappings`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The local same-record evidence includes the NCBI row plus eleven GTDB `skos:broadMatch` rows for one-to-four-genome `Cohaesibacter` species clusters; those GTDB rows are all represented in the reviewed YAML without creating GTDB-derived exact synonyms or xrefs for broad matches.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found no ATB, BacDive, GOLD, LPSN, MADIN, MediaDive, BactoTraits, or strain-info rows keyed to `NCBITaxon:1002546`. Exact GTDB identifier searches found the corresponding eleven rows in both `data/raw/gtdb_mappings.tsv` and `data/raw/gtdb_species.tsv`.

## Completeness

The record represents the direct NCBI and GTDB rows found in the pinned local evidence. It has no `synonyms`, `xrefs`, `strains`, `equivalent_identifiers`, `comments`, or product-level sections. None are required by the reviewed same-taxon evidence.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `uncultured_cohaesibacter_sp` review.
