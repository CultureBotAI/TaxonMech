# YAML Record Review: Curtobacterium sp. IKATA003
- Repository: TaxonMech
- Record: `data/taxa/bacteria/curtobacterium_sp_ikata003.yaml`
- Started UTC: 2026-09-22T20:19:11Z
- Finished UTC: 2026-09-22T20:20:30Z
- Verdict: pass

## Target
- Reviewed `NCBITaxon:1004894` / `curtobacterium_sp_ikata003`.
- The record is a `SPECIES`-rank `BACTERIA` record for `Curtobacterium sp. IKATA003`.
- Parentage is the seeded NCBI placement under `NCBITaxon:257496` (`unclassified Curtobacterium`), with lineage through `Actinomycetota`, `Actinomycetes`, `Micrococcales`, `Microbacteriaceae`, and `Curtobacterium`.

## Validation
- `just validate data/taxa/bacteria/curtobacterium_sp_ikata003.yaml` completed successfully.
- `just validate-strict data/taxa/bacteria/acidithiobacillus_cuprithermicus.yaml data/taxa/bacteria/curtobacterium_sp_ikata001.yaml data/taxa/bacteria/curtobacterium_sp_ikata003.yaml data/taxa/bacteria/mucilaginibacter_sp_ikata004.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was not applicable because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `id: NCBITaxon:1004894`, `label: Curtobacterium sp. IKATA003`, `rank: SPECIES`, `domain: BACTERIA`, `parent: NCBITaxon:257496`, and `genetic_code: 11` match the pinned row in `data/raw/ncbitaxon_taxa.tsv`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a directly seeded NCBI Taxon record.
- The placeholder name under `unclassified Curtobacterium` mirrors the local NCBI snapshot; no formal species epithet is inferred.

## Evidence
- The exact same-taxon source rows for `NCBITaxon:1004894` and `curtobacterium_sp_ikata003` were limited to `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv`.
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
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name *-curtobacterium_sp_ikata003.md` returned no prior ignored report for this stem.
- Live NCBI lookup was not used; the local pinned NCBI Taxon row dated `2026-09-13` was treated as the source of truth.
