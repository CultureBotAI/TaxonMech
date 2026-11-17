# YAML Record Review: uncultured Pelagicoccus sp.

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/uncultured_pelagicoccus_sp.yaml`
- Started UTC: 2026-09-22T14:16:45Z
- Finished UTC: 2026-09-22T14:17:51Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/uncultured_pelagicoccus_sp.yaml`
- Identifier: `NCBITaxon:1002210`
- Slug: `uncultured_pelagicoccus_sp`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1002209` (`environmental samples`)

## Validation

- `just validate data/taxa/bacteria/uncultured_pelagicoccus_sp.yaml`: passed.
- `just validate-strict data/taxa/bacteria/streptomyces_sp_erinlg_26.yaml data/taxa/bacteria/streptomyces_sp_erinlg_4.yaml data/taxa/bacteria/uncultured_caenispirillum_sp.yaml data/taxa/bacteria/uncultured_pelagicoccus_sp.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002210` / `uncultured Pelagicoccus sp.`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:1002209` matches the pinned NCBI parent, `environmental samples`.
- The lineage stays within Bacteria through `PVC group`, `Verrucomicrobiota`, `Opitutia`, `Puniceicoccales`, `Pelagicoccaceae`, `Pelagicoccus`, then `environmental samples`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The same NCBI species identifier is attested by both NCBI and GOLD in the local raw inventories: `data/raw/ncbitaxon_taxa.tsv` marks `NCBITaxon:1002210` as `ncbitaxon|gold`, and `data/raw/gold_organisms.tsv` has the matching count row for `NCBITaxon:1002210`.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI and GOLD rows keyed to `NCBITaxon:1002210`, and no ATB, BacDive, GTDB, LPSN, MADIN, or strain-info rows keyed to this identifier.

## Completeness

The record carries the two source attestations required by the reviewed local evidence and has no `taxonomy_mappings`, `synonyms`, `xrefs`, `strains`, `equivalent_identifiers`, `comments`, or product-level sections. None of those absent sections are required by the pinned same-taxon evidence.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `uncultured_pelagicoccus_sp` review.
