# YAML Record Review: Oculatella subterranea 'AD501/Zammit 2007/1'

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/oculatella_subterranea_ad501_zammit_2007_1.yaml`
- Started UTC: 2026-09-22T16:14:28Z
- Finished UTC: 2026-09-22T16:15:19Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/oculatella_subterranea_ad501_zammit_2007_1.yaml`
- Identifier: `NCBITaxon:1002912`
- Slug: `oculatella_subterranea_ad501_zammit_2007_1`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1240887` (`Oculatella subterranea`)

## Validation

- `just validate data/taxa/bacteria/oculatella_subterranea_ad501_zammit_2007_1.yaml`: passed.
- `just validate-strict data/taxa/bacteria/oculatella_subterranea_ad501_zammit_2007_1.yaml data/taxa/bacteria/oculatella_subterranea_sp301_zammit_2007_2.yaml data/taxa/bacteria/oculatella_subterranea_sp1401_1_zammit_2007_3.yaml data/taxa/bacteria/oculatella_subterranea_sp1401_2_zammit_2007_4.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002912` / `Oculatella subterranea 'AD501/Zammit 2007/1'`.

- `identifier`, `label`, `rank: STRAIN`, `genetic_code: 11`, `parent_taxon: NCBITaxon:1240887`, and the exact synonym `Leptolyngbya sp. 'AD501/Zammit 2007/1'` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Bacillati`, `Cyanobacteriota/Melainabacteria group`, `Cyanobacteriota`, `Cyanophyceae`, `Oculatellales`, `Oculatellaceae`, `Oculatella`, then `Oculatella subterranea`.
- `grounding_status: EXACT` is correct for the NCBI strain seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:1002912`; its label, rank, genetic code, synonym, and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, and NCBI rows keyed to `NCBITaxon:1002912` / `Oculatella subterranea 'AD501/Zammit 2007/1'`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, MediaDive, BactoTraits, strain-info, or NCBI merge-ledger rows keyed to this taxon.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `oculatella_subterranea_ad501_zammit_2007_1` review.
