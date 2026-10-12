# YAML Record Review: beta-symbiont of Antonina crawii
- Repository: TaxonMech
- Record: `data/taxa/bacteria/beta_symbiont_of_antonina_crawii.yaml`
- Started UTC: 2026-09-22T20:17:03Z
- Finished UTC: 2026-09-22T20:18:10Z
- Verdict: pass

## Target
- Reviewed `NCBITaxon:100483` / `beta_symbiont_of_antonina_crawii`.
- The record is a `SPECIES`-rank `BACTERIA` record for `beta-symbiont of Antonina crawii`.
- Parentage is the seeded NCBI placement under `NCBITaxon:33809` (`unclassified Betaproteobacteria`), with lineage through `Pseudomonadota` and `Betaproteobacteria`.

## Validation
- `just validate data/taxa/bacteria/beta_symbiont_of_antonina_crawii.yaml` completed successfully.
- `just validate-strict data/taxa/bacteria/spiroplasma_symbiont_of_antonina_crawii.yaml data/taxa/bacteria/beta_symbiont_of_antonina_crawii.yaml data/taxa/bacteria/gluconacetobacter_sp_sxcc_1.yaml data/taxa/bacteria/gamma_symbiont_of_antonina_crawii.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was not applicable because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `id: NCBITaxon:100483`, `label: beta-symbiont of Antonina crawii`, `rank: SPECIES`, `domain: BACTERIA`, `parent: NCBITaxon:33809`, and `genetic_code: 11` match the pinned row in `data/raw/ncbitaxon_taxa.tsv`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a directly seeded NCBI Taxon record.
- The placeholder symbiont label is preserved exactly and no lower-rank or formal binomial identity is inferred.

## Evidence
- The exact same-taxon source rows for `NCBITaxon:100483` and `beta_symbiont_of_antonina_crawii` were limited to `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv`.
- The gitignore-independent `rg --no-ignore --hidden` search across `data/raw`, `data/atb`, `data/straininfo`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv` found no GTDB, GOLD, MADIN, ATB, or StrainInfo rows for this taxon.
- The generated `source_attestations` entry is therefore correctly limited to one NCBITAXON attestation.

## Completeness
- `strain_count: 0` is consistent with the absence of same-taxon strain rows in the local pinned StrainInfo tables.
- The record contains the available identity, parent, lineage, genetic-code, and NCBI attestation evidence.
- The empty synonym, GTDB, ATB, strain, and assembly sections are expected for this NCBI-only seed.

## Findings
- No findings.

## Recommended Edits
- None.

## Follow-up Checks
- None required for this record.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name *-beta_symbiont_of_antonina_crawii.md` returned no prior ignored report for this stem.
- Live NCBI lookup was not used; the local pinned NCBI Taxon row dated `2026-09-13` was treated as the source of truth.
