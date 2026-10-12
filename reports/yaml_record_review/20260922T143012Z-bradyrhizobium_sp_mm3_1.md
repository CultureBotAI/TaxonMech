# YAML Record Review: Bradyrhizobium sp. Mm3-1

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/bradyrhizobium_sp_mm3_1.yaml`
- Started UTC: 2026-09-22T14:28:23Z
- Finished UTC: 2026-09-22T14:30:12Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/bradyrhizobium_sp_mm3_1.yaml`
- Identifier: `NCBITaxon:100228`
- Slug: `bradyrhizobium_sp_mm3_1`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2631580` (`unclassified Bradyrhizobium`)

## Validation

- `just validate data/taxa/bacteria/bradyrhizobium_sp_mm3_1.yaml`: passed.
- `just validate-strict data/taxa/bacteria/bradyrhizobium_sp_mm3_1.yaml data/taxa/bacteria/bradyrhizobium_sp_mm4.yaml data/taxa/bacteria/bradyrhizobium_sp_mm1_2.yaml data/taxa/bacteria/uncultured_planctomycetaceae_bacterium.yaml`: passed.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:100228` / `Bradyrhizobium sp. Mm3-1`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:2631580` matches the pinned NCBI parent, `unclassified Bradyrhizobium`.
- The lineage stays within Bacteria through `Pseudomonadota`, `Alphaproteobacteria`, `Hyphomicrobiales`, `Nitrobacteraceae`, `Bradyrhizobium`, then `unclassified Bradyrhizobium`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:100228`; its label and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI row keyed to `NCBITaxon:100228`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, or strain-info rows keyed to this identifier.

## Completeness

The record has no `taxonomy_mappings`, `synonyms`, `xrefs`, `strains`, `equivalent_identifiers`, `comments`, or product-level sections. None are required by the reviewed local evidence.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `bradyrhizobium_sp_mm3_1` review.
