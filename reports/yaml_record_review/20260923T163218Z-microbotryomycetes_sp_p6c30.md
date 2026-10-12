# YAML Record Review: Microbotryomycetes sp. P6C30

- Record: `data/taxa/eukaryota/microbotryomycetes_sp_p6c30.yaml`
- Reviewed: `2026-09-23T16:32:18Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:3424171`
- Label: `Microbotryomycetes sp. P6C30`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:412475` (`unclassified Microbotryomycetes`)

## Validation

- `just validate data/taxa/eukaryota/microbotryomycetes_sp_p6c30.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microascus_trigonosporus_cbs_218_31.yaml data/taxa/eukaryota/microbotryomycetes_sp_p6c30.yaml data/taxa/eukaryota/microbotryum_lychnidis_dioicae.yaml data/taxa/eukaryota/microbotryum_lychnidis_dioicae_p1a1_lamole.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:631774` has the same identifier, label, species rank, `NCBITaxon:412475` parent, genetic code `1`, empty synonym fields, and `gold` attestation copied into the YAML.
- The YAML lineage contains the expected ten entries from `root` through `unclassified Microbotryomycetes`.

## Evidence

- `data/seed_scope.tsv:63628` includes `NCBITaxon:3424171` with reason `attested rule: Microbotryomycetes sp. P6C30, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:32822` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism evidence for `Go0568415` / `P6C30`, with transcriptome project `Gp0539714` and standard draft project `Gp0543360`; no native analysis rows join through those projects.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:3424171`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact StrainInfo rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:3424171`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If this provisional Microbotryomycetes organism is later assigned to a named species, revisit the unclassified parent and exact GOLD placement.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:3424171`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
