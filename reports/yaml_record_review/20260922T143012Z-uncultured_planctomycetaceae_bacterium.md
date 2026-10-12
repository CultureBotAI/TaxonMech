# YAML Record Review: uncultured Planctomycetaceae bacterium

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/uncultured_planctomycetaceae_bacterium.yaml`
- Started UTC: 2026-09-22T14:28:23Z
- Finished UTC: 2026-09-22T14:30:12Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/uncultured_planctomycetaceae_bacterium.yaml`
- Identifier: `NCBITaxon:100233`
- Slug: `uncultured_planctomycetaceae_bacterium`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:69409` (`environmental samples`)

## Validation

- `just validate data/taxa/bacteria/uncultured_planctomycetaceae_bacterium.yaml`: passed.
- `just validate-strict data/taxa/bacteria/bradyrhizobium_sp_mm3_1.yaml data/taxa/bacteria/bradyrhizobium_sp_mm4.yaml data/taxa/bacteria/bradyrhizobium_sp_mm1_2.yaml data/taxa/bacteria/uncultured_planctomycetaceae_bacterium.yaml`: passed.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:100233` / `uncultured Planctomycetaceae bacterium`.

- `identifier`, `label`, `rank`, and `parent_taxon: NCBITaxon:69409` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `PVC group`, `Planctomycetota`, `Planctomycetia`, `Planctomycetales`, `Planctomycetaceae`, then `environmental samples`.
- NCBI exact synonyms `uncultured Planctomycetaceae` and `unidentified Planctomycetaceae` are both represented.
- The GTDB mappings are intentionally broad pooled matches from many Planctomycetaceae-level MAG species onto this environmental NCBI placeholder.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI row and 321 GTDB broad-match mapping rows keyed to `NCBITaxon:100233`, and no ATB, BacDive, GOLD, LPSN, MADIN, or strain-info rows keyed to this identifier.

The reviewed YAML carries 321 `taxonomy_mappings`; `GTDB:s__UBA1268_sp016776925` is the primary GTDB source attestation with 19 genomes, and the source attestation notes the 320 further broad-match GTDB species represented in `taxonomy_mappings`.

## Completeness

The record includes the NCBI synonyms and all broad GTDB taxonomy mappings found in the pinned local evidence. It has no `strains`, `equivalent_identifiers`, `comments`, or product-level sections; none are required by the reviewed same-taxon evidence.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `uncultured_planctomycetaceae_bacterium` review.
