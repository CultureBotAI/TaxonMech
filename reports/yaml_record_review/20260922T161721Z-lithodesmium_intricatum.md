# YAML Record Review: Lithodesmium intricatum

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/eukaryota/lithodesmium_intricatum.yaml`
- Started UTC: 2026-09-22T16:15:57Z
- Finished UTC: 2026-09-22T16:17:21Z
- Verdict: pass

## Target

- Record: `data/taxa/eukaryota/lithodesmium_intricatum.yaml`
- Identifier: `NCBITaxon:1003076`
- Slug: `lithodesmium_intricatum`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:59811` (`Lithodesmium`)

## Validation

- `just validate data/taxa/eukaryota/lithodesmium_intricatum.yaml`: passed.
- `just validate-strict data/taxa/bacteria/oculatella_subterranea_sp1402_zammit_2007_5.yaml data/taxa/bacteria/leptolyngbya_sp_sp1001_zammit_2007_6.yaml data/taxa/bacteria/thermoflexibacter_ruber.yaml data/taxa/eukaryota/lithodesmium_intricatum.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1003076` / `Lithodesmium intricatum`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 1`, `parent_taxon: NCBITaxon:59811`, and the `Ditylum intricatum` / `Triceratium intricatum` synonym set match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Eukaryota through `Sar`, `Stramenopiles`, `Ochrophyta`, `Bacillariophyta`, `Thalassiosirophyceae`, `Lithodesmiophycidae`, `Lithodesmiales`, `Lithodesmiaceae`, then `Lithodesmium`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The exact same-taxon source rows are the generated NCBI row for `NCBITaxon:1003076` and one GOLD organism-count row for the same identifier; the label, rank, genetic code, synonyms, and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, NCBI, and GOLD rows keyed to `NCBITaxon:1003076` / `Lithodesmium intricatum`, and no ATB, BacDive, GTDB, LPSN, MADIN, MediaDive, BactoTraits, strain-info, or NCBI merge-ledger rows keyed to this taxon.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `lithodesmium_intricatum` review.
