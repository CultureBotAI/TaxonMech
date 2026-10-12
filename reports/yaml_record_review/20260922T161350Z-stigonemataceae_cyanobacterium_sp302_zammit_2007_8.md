# YAML Record Review: Stigonemataceae cyanobacterium 'SP302/Zammit 2007/8'

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/stigonemataceae_cyanobacterium_sp302_zammit_2007_8.yaml`
- Started UTC: 2026-09-22T16:12:46Z
- Finished UTC: 2026-09-22T16:13:50Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/stigonemataceae_cyanobacterium_sp302_zammit_2007_8.yaml`
- Identifier: `NCBITaxon:1002910`
- Slug: `stigonemataceae_cyanobacterium_sp302_zammit_2007_8`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:299579` (`unclassified Stigonemataceae`)

## Validation

- `just validate data/taxa/bacteria/stigonemataceae_cyanobacterium_sp302_zammit_2007_8.yaml`: passed.
- `just validate-strict data/taxa/bacteria/cupriavidus_sp_swf65033.yaml data/taxa/bacteria/stigonemataceae_cyanobacterium_sa1301_zammit_2007_7.yaml data/taxa/bacteria/stigonemataceae_cyanobacterium_sp302_zammit_2007_8.yaml data/taxa/bacteria/oscillatoriales_cyanobacterium_2ad401_zammit_2007_9.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002910` / `Stigonemataceae cyanobacterium 'SP302/Zammit 2007/8'`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, `parent_taxon: NCBITaxon:299579`, and the exact synonym `Stigonematales cyanobacterium 'SP302/Zammit 2007/8'` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Bacillati`, `Cyanobacteriota/Melainabacteria group`, `Cyanobacteriota`, `Cyanophyceae`, `Nostocales`, `Stigonemataceae`, then `unclassified Stigonemataceae`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:1002910`; its label, rank, genetic code, synonym, and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, and NCBI rows keyed to `NCBITaxon:1002910` / `Stigonemataceae cyanobacterium 'SP302/Zammit 2007/8'`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, MediaDive, BactoTraits, strain-info, or NCBI merge-ledger rows keyed to this taxon.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `stigonemataceae_cyanobacterium_sp302_zammit_2007_8` review.
