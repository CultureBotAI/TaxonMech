# YAML Record Review: uncultured eukaryote

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/eukaryota/uncultured_eukaryote.yaml`
- Started UTC: 2026-09-22T15:48:04Z
- Finished UTC: 2026-09-22T15:49:06Z
- Verdict: pass

## Target

- Record: `data/taxa/eukaryota/uncultured_eukaryote.yaml`
- Identifier: `NCBITaxon:100272`
- Slug: `uncultured_eukaryote`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:61964` (`environmental samples`)

## Validation

- `just validate data/taxa/eukaryota/uncultured_eukaryote.yaml`: passed.
- `just validate-strict data/taxa/eukaryota/uncultured_eukaryote.yaml data/taxa/bacteria/novosphingobium_sp_hme6881.yaml data/taxa/bacteria/pectinatus_sottacetonis.yaml data/taxa/bacteria/helicobacter_bizzozeronii_ciii_1.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:100272` / `uncultured eukaryote`.

- `identifier`, `label`, `rank: SPECIES`, `taxon_domain: EUKARYOTA`, `genetic_code: 1`, and `parent_taxon: NCBITaxon:61964` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Eukaryota through `environmental samples`.
- The three NCBI exact synonyms in `data/raw/ncbitaxon_taxa.tsv` are present in `synonyms`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The exact same-taxon source rows are the NCBI row for `NCBITaxon:100272`, the GOLD organism row with 23 organisms, and the NCBI merged-ID row from old `NCBITaxon:52016` to `NCBITaxon:100272`.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected `curation/seed_scope.tsv`, NCBI, GOLD, and NCBI merged-ID rows, and no ATB, BacDive, GTDB, LPSN, MADIN, MediaDive, BactoTraits, or strain-info rows keyed to `NCBITaxon:100272`.

## Completeness

The record carries the expected NCBI `synonyms` and GOLD source attestation. The raw NCBI merged-ID row for old `NCBITaxon:52016` is ledger evidence only here: `NCBITaxon:52016` is not in `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/straininfo`, or `data/atb`, and the YAML `replaces` field is seeded from retired NCBI taxon rows that carry `retired_into`.

There are no `taxonomy_mappings`, `xrefs`, `strains`, `comments`, or product-level sections. None are required by the reviewed local evidence.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `uncultured_eukaryote` review.
