# YAML Record Review: Oculatella subterranea 'SP1402/Zammit 2007/5'

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/oculatella_subterranea_sp1402_zammit_2007_5.yaml`
- Started UTC: 2026-09-22T16:15:57Z
- Finished UTC: 2026-09-22T16:17:21Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/oculatella_subterranea_sp1402_zammit_2007_5.yaml`
- Identifier: `NCBITaxon:1002916`
- Slug: `oculatella_subterranea_sp1402_zammit_2007_5`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1240887` (`Oculatella subterranea`)

## Validation

- `just validate data/taxa/bacteria/oculatella_subterranea_sp1402_zammit_2007_5.yaml`: passed.
- `just validate-strict data/taxa/bacteria/oculatella_subterranea_sp1402_zammit_2007_5.yaml data/taxa/bacteria/leptolyngbya_sp_sp1001_zammit_2007_6.yaml data/taxa/bacteria/thermoflexibacter_ruber.yaml data/taxa/eukaryota/lithodesmium_intricatum.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002916` / `Oculatella subterranea 'SP1402/Zammit 2007/5'`.

- `identifier`, `label`, `rank: STRAIN`, `genetic_code: 11`, `parent_taxon: NCBITaxon:1240887`, and the exact synonym `Leptolyngbya sp. 'SP1402/Zammit 2007/5'` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Bacillati`, `Cyanobacteriota/Melainabacteria group`, `Cyanobacteriota`, `Cyanophyceae`, `Oculatellales`, `Oculatellaceae`, `Oculatella`, then `Oculatella subterranea`.
- `grounding_status: EXACT` is correct for the NCBI strain seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:1002916`; its label, rank, genetic code, synonym, and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, and NCBI rows keyed to `NCBITaxon:1002916` / `Oculatella subterranea 'SP1402/Zammit 2007/5'`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, MediaDive, BactoTraits, strain-info, or NCBI merge-ledger rows keyed to this taxon.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `oculatella_subterranea_sp1402_zammit_2007_5` review.
