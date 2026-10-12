# YAML Record Review: Helicobacter salomonis O6A

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/helicobacter_salomonis_o6a.yaml`
- Started UTC: 2026-09-22T15:50:32Z
- Finished UTC: 2026-09-22T15:51:36Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/helicobacter_salomonis_o6a.yaml`
- Identifier: `NCBITaxon:1002807`
- Slug: `helicobacter_salomonis_o6a`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:56878` (`Helicobacter salomonis`)

## Validation

- `just validate data/taxa/bacteria/helicobacter_salomonis_o6a.yaml`: passed.
- `just validate-strict data/taxa/bacteria/helicobacter_bizzozeronii_ccug_35545.yaml data/taxa/bacteria/helicobacter_salomonis_o6a.yaml data/taxa/bacteria/solibacillus_silvestris_stlb046.yaml data/taxa/bacteria/bacillus_sp_8b2.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002807` / `Helicobacter salomonis O6A`.

- `identifier`, `label`, `rank: STRAIN`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:56878` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Pseudomonadati`, `Campylobacterota`, `Epsilonproteobacteria`, `Campylobacterales`, `Helicobacteraceae`, `Helicobacter`, then `Helicobacter salomonis`.
- The two NCBI exact synonyms in `data/raw/ncbitaxon_taxa.tsv` are present in `synonyms`.
- `grounding_status: EXACT` is correct for the NCBI strain seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:1002807`; its label, rank, exact synonyms, genetic code, and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected `curation/seed_scope.tsv` and NCBI rows keyed to `NCBITaxon:1002807`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, MediaDive, BactoTraits, or strain-info rows keyed to this identifier.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `helicobacter_salomonis_o6a` review.
