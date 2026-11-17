# YAML Record Review: Candidatus Pelagibacter sp. IMCC9063

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/candidatus_pelagibacter_sp_imcc9063.yaml`
- Started UTC: 2026-09-22T15:40:11Z
- Finished UTC: 2026-09-22T15:43:34Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/candidatus_pelagibacter_sp_imcc9063.yaml`
- Identifier: `NCBITaxon:1002672`
- Slug: `candidatus_pelagibacter_sp_imcc9063`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2647897` (`unclassified Candidatus Pelagibacter`)

## Validation

- `just validate data/taxa/bacteria/candidatus_pelagibacter_sp_imcc9063.yaml`: passed.
- `just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_amblyomma_americanum.yaml data/taxa/bacteria/candidatus_pelagibacter_sp_imcc9063.yaml data/taxa/bacteria/bacillus_sp_prb_1.yaml data/taxa/bacteria/roseovarius_sp_iob_12.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002672` / `Candidatus Pelagibacter sp. IMCC9063`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:2647897` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Pseudomonadati`, `Pseudomonadota`, `Alphaproteobacteria`, `Candidatus Pelagibacterales`, `Candidatus Pelagibacteraceae`, `Candidatus Pelagibacter`, then `unclassified Candidatus Pelagibacter`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The exact same-taxon source rows are the NCBI row for `NCBITaxon:1002672`, the GTDB `skos:closeMatch` row for `GTDB:s__IMCC9063_sp000195085`, and the MADIN row with 3 trait assertions.

- The NCBI row supplies `Pelagibacter sp. IMCC9063` and `marine bacterium IMCC9063` as exact synonyms; both are present in `synonyms` with `source: NCBITaxon`.
- The GTDB mapping supplies `GTDB:s__IMCC9063_sp000195085`, label `s__IMCC9063_sp000195085`, parent `GTDB:g__IMCC9063`, `mapping_predicate: skos:closeMatch`, and `genome_count: 2`; the reviewed YAML carries the corresponding `taxonomy_mappings` entry, GTDB exact synonym, GTDB xref, and GTDB source attestation.
- The MADIN row is keyed to `NCBITaxon:1002672` with assertion count 3, matching the MADIN `source_attestations` entry.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected `curation/seed_scope.tsv`, NCBI, GTDB, MADIN, and NCBI merged-ID rows. It found no ATB, BacDive, GOLD, LPSN, MediaDive, BactoTraits, or strain-info rows keyed to `NCBITaxon:1002672`; the additional `GTDB:s__IMCC9063_sp000195085` `skos:broadMatch` row belongs to `NCBITaxon:2026775`, and the generated `pelagibacteraceae_bacterium` record carries that pooling signal.

## Completeness

The record carries the expected GTDB `taxonomy_mappings`, NCBI and GTDB `synonyms`, GTDB `xrefs`, and NCBI, GTDB, and MADIN `source_attestations`. The raw NCBI merged-ID row for old `NCBITaxon:980517` is ledger evidence only here: `NCBITaxon:980517` is not in `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/straininfo`, or `data/atb`, and the YAML `replaces` field is seeded from retired NCBI taxon rows that carry `retired_into`.

There are no `strains`, `comments`, or product-level sections. None are required by the reviewed local evidence.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `candidatus_pelagibacter_sp_imcc9063` review.
