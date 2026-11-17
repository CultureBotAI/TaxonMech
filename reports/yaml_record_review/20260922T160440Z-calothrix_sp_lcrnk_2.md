# YAML Record Review: Calothrix sp. LCRNK.2

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/calothrix_sp_lcrnk_2.yaml`
- Started UTC: 2026-09-22T16:03:42Z
- Finished UTC: 2026-09-22T16:04:40Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/calothrix_sp_lcrnk_2.yaml`
- Identifier: `NCBITaxon:1002843`
- Slug: `calothrix_sp_lcrnk_2`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2619626` (`unclassified Calothrix`)

## Validation

- `just validate data/taxa/bacteria/calothrix_sp_lcrnk_2.yaml`: passed.
- `just validate-strict data/taxa/bacteria/calothrix_sp_lcrnk_2.yaml data/taxa/bacteria/nostoc_sp_lcrnk_21.yaml data/taxa/bacteria/nostoc_sp_lcrnk_3.yaml data/taxa/bacteria/calothrix_sp_lcrnk_7.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002843` / `Calothrix sp. LCRNK.2`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, `parent_taxon: NCBITaxon:2619626`, and the exact synonym `Nostoc sp. LCRNK.2` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Bacillati`, `Cyanobacteriota/Melainabacteria group`, `Cyanobacteriota`, `Cyanophyceae`, `Nostocales`, `Calotrichaceae`, `Calothrix`, then `unclassified Calothrix`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:1002843`; its label, rank, genetic code, synonym, and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected `curation/seed_scope.tsv` and NCBI rows keyed to `NCBITaxon:1002843` / `Calothrix sp. LCRNK.2`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, MediaDive, BactoTraits, or strain-info rows keyed to this taxon.

## Completeness

The record has no `taxonomy_mappings`, `xrefs`, `strains`, `equivalent_identifiers`, `comments`, or product-level sections. None are required by the reviewed local evidence.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `calothrix_sp_lcrnk_2` review.
