# YAML Record Review: Solibacillus silvestris StLB046

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/solibacillus_silvestris_stlb046.yaml`
- Started UTC: 2026-09-22T15:50:32Z
- Finished UTC: 2026-09-22T15:51:36Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/solibacillus_silvestris_stlb046.yaml`
- Identifier: `NCBITaxon:1002809`
- Slug: `solibacillus_silvestris_stlb046`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:76853` (`Solibacillus silvestris`)

## Validation

- `just validate data/taxa/bacteria/solibacillus_silvestris_stlb046.yaml`: passed.
- `just validate-strict data/taxa/bacteria/helicobacter_bizzozeronii_ccug_35545.yaml data/taxa/bacteria/helicobacter_salomonis_o6a.yaml data/taxa/bacteria/solibacillus_silvestris_stlb046.yaml data/taxa/bacteria/bacillus_sp_8b2.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002809` / `Solibacillus silvestris StLB046`.

- `identifier`, `label`, `rank: STRAIN`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:76853` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Bacillati`, `Bacillota`, `Bacilli`, `Caryophanales`, `Caryophanaceae`, `Solibacillus`, then `Solibacillus silvestris`.
- The two NCBI exact synonyms in `data/raw/ncbitaxon_taxa.tsv` are present in `synonyms`.
- `grounding_status: EXACT` is correct for the NCBI strain seed itself.

## Evidence

The exact same-taxon source rows are the NCBI row for `NCBITaxon:1002809`, the GTDB `skos:closeMatch` row for `GTDB:s__Solibacillus_silvestris`, and the MADIN row with 1 trait assertion.

- The GTDB row maps `GTDB:s__Solibacillus_silvestris` to this taxon with `skos:closeMatch` and 16 genomes, matching the YAML `taxonomy_mappings`, GTDB exact synonym, GTDB xref, and GTDB source attestation.
- The MADIN row is keyed to `NCBITaxon:1002809` with assertion count 1, matching the MADIN `source_attestations` entry.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected `curation/seed_scope.tsv`, NCBI, GTDB, and MADIN rows, and no ATB, BacDive, GOLD, LPSN, MediaDive, BactoTraits, or strain-info rows keyed to `NCBITaxon:1002809`.

## Completeness

The record carries the expected GTDB `taxonomy_mappings`, NCBI and GTDB `synonyms`, GTDB `xrefs`, and NCBI, GTDB, and MADIN `source_attestations`. There are no `strains`, `comments`, or product-level sections. None are required by the reviewed same-taxon local evidence.

## Findings

No findings in this generated YAML relative to the pinned local source rows.

## Recommended Edits

- None.

## Follow-up Checks

- Review whether the upstream `GTDB:s__Solibacillus_silvestris` `skos:closeMatch` rows should point at strain-level NCBI taxa. The same GTDB species also maps by close match to several other NCBI strain-level taxa and by broad match to the parent species `NCBITaxon:76853` in `data/raw/gtdb_mappings.tsv`.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- `just validate-history` was not run because this read-only review did not add a `history/` decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `solibacillus_silvestris_stlb046` review.
