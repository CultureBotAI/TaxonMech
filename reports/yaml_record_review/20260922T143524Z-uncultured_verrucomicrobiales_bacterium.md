# YAML Record Review: uncultured Verrucomicrobiales bacterium

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/uncultured_verrucomicrobiales_bacterium.yaml`
- Started UTC: 2026-09-22T14:31:12Z
- Finished UTC: 2026-09-22T14:35:24Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/uncultured_verrucomicrobiales_bacterium.yaml`
- Identifier: `NCBITaxon:100234`
- Slug: `uncultured_verrucomicrobiales_bacterium`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:48468` (`environmental samples`)

## Validation

- `just validate data/taxa/bacteria/uncultured_verrucomicrobiales_bacterium.yaml`: passed.
- `just validate-strict data/taxa/bacteria/bordetella_petrii_104.yaml data/taxa/bacteria/psychrobacter_sp_1501_2011.yaml data/taxa/bacteria/uncultured_verrucomicrobiales_bacterium.yaml data/taxa/bacteria/leisingera_sp_ang1.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:100234` / `uncultured Verrucomicrobiales bacterium`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:48468` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `PVC group`, `Verrucomicrobiota`, `Verrucomicrobiia`, `Verrucomicrobiales`, then `environmental samples`.
- NCBI exact synonyms `uncultured Verrucomicrobiales` and `unidentified Verrucomicrobiales` are both represented.
- The GTDB mappings are intentionally broad pooled matches from many Verrucomicrobiales-level MAG species onto this environmental NCBI placeholder.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI row and 125 GTDB broad-match mapping rows keyed to `NCBITaxon:100234`, and no ATB, BacDive, GOLD, LPSN, MADIN, or strain-info rows keyed to this identifier.

The reviewed YAML carries 125 `taxonomy_mappings`; `GTDB:s__UBA7971_sp002686885` is the primary GTDB source attestation with 65 genomes, and the source attestation notes the 124 further broad-match GTDB species represented in `taxonomy_mappings`.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `uncultured_verrucomicrobiales_bacterium` review.
