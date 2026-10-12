# YAML Record Review: Escherichia coli PCN097

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/escherichia_coli_pcn097.yaml`
- Started UTC: 2026-09-22T14:02:18Z
- Finished UTC: 2026-09-22T14:04:00Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/escherichia_coli_pcn097.yaml`
- Identifier: `NCBITaxon:1001992`
- Slug: `escherichia_coli_pcn097`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:562` (`Escherichia coli`)

## Validation

- `just validate data/taxa/bacteria/escherichia_coli_pcn097.yaml`: passed.
- `just validate-strict data/taxa/bacteria/escherichia_coli_pcn042.yaml data/taxa/bacteria/escherichia_coli_pcn079.yaml data/taxa/bacteria/escherichia_coli_pcn097.yaml data/taxa/archaea/nitrosarchaeum_koreense_my1.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1001992` / `Escherichia coli PCN097`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:562` matches the pinned NCBI parent, `Escherichia coli`.
- The lineage stays within Bacteria through `Pseudomonadota`, `Gammaproteobacteria`, `Enterobacterales`, `Enterobacteriaceae`, `Escherichia`, then `Escherichia coli`.
- `grounding_status: EXACT` is correct for the NCBI strain seed itself.

## Evidence

The NCBI and MADIN attestations are keyed directly to `NCBITaxon:1001992`; their labels and assertion counts match the reviewed raw rows.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI and MADIN rows keyed to `NCBITaxon:1001992`, and no ATB, BacDive, GOLD, GTDB, LPSN, or strain-info rows keyed to this identifier.

## Completeness

The NCBI-derived `Escherichia coli str. PCN097` and `Escherichia coli strain PCN097` synonyms preserve the strain identifier and are consistent with the reviewed strain.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `escherichia_coli_pcn097` review.
