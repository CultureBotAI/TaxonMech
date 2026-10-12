# YAML Record Review: Chryseobacterium sp. T5-15
- Repository: TaxonMech
- Record: `data/taxa/bacteria/chryseobacterium_sp_t5_15.yaml`
- Started UTC: 2026-09-22T20:21:34Z
- Finished UTC: 2026-09-22T20:22:44Z
- Verdict: pass

## Target
- Reviewed `NCBITaxon:1004898` / `chryseobacterium_sp_t5_15`.
- The record is a `SPECIES`-rank `BACTERIA` record for `Chryseobacterium sp. T5-15`.
- Parentage is the seeded NCBI placement under `NCBITaxon:2593645` (`unclassified Chryseobacterium`), with lineage through `Bacteroidota`, `Flavobacteriia`, `Flavobacteriales`, `Weeksellaceae`, and `Chryseobacterium`.

## Validation
- `just validate data/taxa/bacteria/chryseobacterium_sp_t5_15.yaml` completed successfully.
- `just validate-strict data/taxa/bacteria/microbacterium_sp_t5_9.yaml data/taxa/bacteria/chryseobacterium_sp_t5_15.yaml data/taxa/bacteria/pseudomonas_sp_t2_1.yaml data/taxa/bacteria/serratia_sp_t2_62.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was not applicable because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `id: NCBITaxon:1004898`, `label: Chryseobacterium sp. T5-15`, `rank: SPECIES`, `domain: BACTERIA`, `parent: NCBITaxon:2593645`, and `genetic_code: 11` match the pinned row in `data/raw/ncbitaxon_taxa.tsv`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a directly seeded NCBI Taxon record.
- The placeholder name under `unclassified Chryseobacterium` mirrors the local NCBI snapshot; no formal species epithet is inferred.

## Evidence
- The exact same-taxon source rows for `NCBITaxon:1004898` and `chryseobacterium_sp_t5_15` were limited to `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv`.
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
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name *-chryseobacterium_sp_t5_15.md` returned no prior ignored report for this stem.
- Live NCBI lookup was not used; the local pinned NCBI Taxon row dated `2026-09-13` was treated as the source of truth.
