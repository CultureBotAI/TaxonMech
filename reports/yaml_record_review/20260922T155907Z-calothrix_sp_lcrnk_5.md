# YAML Record Review: Calothrix sp. LCRNK.5

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/calothrix_sp_lcrnk_5.yaml`
- Started UTC: 2026-09-22T15:58:09Z
- Finished UTC: 2026-09-22T15:59:07Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/calothrix_sp_lcrnk_5.yaml`
- Identifier: `NCBITaxon:1002831`
- Slug: `calothrix_sp_lcrnk_5`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2619626` (`unclassified Calothrix`)

## Validation

- `just validate data/taxa/bacteria/calothrix_sp_lcrnk_5.yaml`: passed.
- `just validate-strict data/taxa/bacteria/calothrix_sp_lcrnk_14.yaml data/taxa/bacteria/calothrix_sp_lcrnk_15.yaml data/taxa/bacteria/calothrix_sp_lcrnk_5.yaml data/taxa/bacteria/cyanothece_sp_lcrnk_21.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002831` / `Calothrix sp. LCRNK.5`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:2619626` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Bacillati`, `Cyanobacteriota/Melainabacteria group`, `Cyanobacteriota`, `Cyanophyceae`, `Nostocales`, `Calotrichaceae`, `Calothrix`, then `unclassified Calothrix`.
- The NCBI exact synonym `Nostoc sp. LCRNK.5` is present in `synonyms`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:1002831`; its label, rank, exact synonym, genetic code, and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected `curation/seed_scope.tsv` and NCBI rows keyed to `NCBITaxon:1002831`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, MediaDive, BactoTraits, or strain-info rows keyed to this identifier.

## Completeness

The record carries the expected NCBI `synonyms`. It has no `taxonomy_mappings`, `xrefs`, `strains`, `comments`, or product-level sections. None are required by the reviewed local evidence.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `calothrix_sp_lcrnk_5` review.
