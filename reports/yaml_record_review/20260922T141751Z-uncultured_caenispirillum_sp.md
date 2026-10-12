# YAML Record Review: uncultured Caenispirillum sp.

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/uncultured_caenispirillum_sp.yaml`
- Started UTC: 2026-09-22T14:16:45Z
- Finished UTC: 2026-09-22T14:17:51Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/uncultured_caenispirillum_sp.yaml`
- Identifier: `NCBITaxon:1002208`
- Slug: `uncultured_caenispirillum_sp`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1002207` (`environmental samples`)

## Validation

- `just validate data/taxa/bacteria/uncultured_caenispirillum_sp.yaml`: passed.
- `just validate-strict data/taxa/bacteria/streptomyces_sp_erinlg_26.yaml data/taxa/bacteria/streptomyces_sp_erinlg_4.yaml data/taxa/bacteria/uncultured_caenispirillum_sp.yaml data/taxa/bacteria/uncultured_pelagicoccus_sp.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002208` / `uncultured Caenispirillum sp.`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:1002207` matches the pinned NCBI parent, `environmental samples`.
- The lineage stays within Bacteria through `Pseudomonadota`, `Alphaproteobacteria`, `Rhodospirillales`, `Novispirillaceae`, `Caenispirillum`, then `environmental samples`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:1002208`; its label and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI row keyed to `NCBITaxon:1002208`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, or strain-info rows keyed to this identifier.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `uncultured_caenispirillum_sp` review.
