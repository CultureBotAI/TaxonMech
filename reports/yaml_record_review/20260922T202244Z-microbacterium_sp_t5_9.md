# YAML Record Review: Microbacterium sp. T5-9
- Repository: TaxonMech
- Record: `data/taxa/bacteria/microbacterium_sp_t5_9.yaml`
- Started UTC: 2026-09-22T20:21:34Z
- Finished UTC: 2026-09-22T20:22:44Z
- Verdict: pass

## Target
- Reviewed `NCBITaxon:1004897` / `microbacterium_sp_t5_9`.
- The record is a `SPECIES`-rank `BACTERIA` record for `Microbacterium sp. T5-9`.
- Parentage is the seeded NCBI placement under `NCBITaxon:2609290` (`unclassified Microbacterium`), with lineage through `Actinomycetota`, `Actinomycetes`, `Micrococcales`, `Microbacteriaceae`, and `Microbacterium`.

## Validation
- `just validate data/taxa/bacteria/microbacterium_sp_t5_9.yaml` completed successfully with no LinkML issues.
- `just validate-strict data/taxa/bacteria/microbacterium_sp_t5_9.yaml data/taxa/bacteria/chryseobacterium_sp_t5_15.yaml data/taxa/bacteria/pseudomonas_sp_t2_1.yaml data/taxa/bacteria/serratia_sp_t2_62.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was not applicable because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `id: NCBITaxon:1004897`, `label: Microbacterium sp. T5-9`, `rank: SPECIES`, `domain: BACTERIA`, `parent: NCBITaxon:2609290`, and `genetic_code: 11` match the pinned row in `data/raw/ncbitaxon_taxa.tsv`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a directly seeded NCBI Taxon record.
- The placeholder name under `unclassified Microbacterium` mirrors the local NCBI snapshot; no formal species epithet is inferred.

## Evidence
- The exact same-taxon source rows for `NCBITaxon:1004897` and `microbacterium_sp_t5_9` were limited to `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv`.
- The gitignore-independent `rg --no-ignore --hidden` search across `data/raw`, `data/atb`, `data/straininfo`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv` found no GTDB, GOLD, MADIN, ATB, or StrainInfo rows for this taxon.
- The generated `source_attestations` entry is therefore correctly limited to one NCBITAXON attestation.

## Completeness
- `strain_count: 0` is consistent with the absence of same-taxon strain rows in the local pinned StrainInfo tables.
- The record contains the available identity, parent, lineage, and NCBI attestation evidence.
- The empty synonym, GTDB, ATB, strain, and assembly sections are expected for this NCBI-only seed.

## Findings
- No findings.

## Recommended Edits
- None.

## Follow-up Checks
- None required for this record.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name *-microbacterium_sp_t5_9.md` returned no prior ignored report for this stem.
- Live NCBI lookup was not used; the local pinned NCBI Taxon row dated `2026-09-13` was treated as the source of truth.
