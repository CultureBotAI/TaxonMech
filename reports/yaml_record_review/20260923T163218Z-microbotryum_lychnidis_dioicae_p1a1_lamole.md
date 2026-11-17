# YAML Record Review: Microbotryum lychnidis-dioicae p1A1 Lamole

- Record: `data/taxa/eukaryota/microbotryum_lychnidis_dioicae_p1a1_lamole.yaml`
- Reviewed: `2026-09-23T16:32:18Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:683840`
- Label: `Microbotryum lychnidis-dioicae p1A1 Lamole`
- Rank/domain: `STRAIN` / `EUKARYOTA`
- Parent: `NCBITaxon:288795` (`Microbotryum lychnidis-dioicae`)

## Validation

- `just validate data/taxa/eukaryota/microbotryum_lychnidis_dioicae_p1a1_lamole.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microascus_trigonosporus_cbs_218_31.yaml data/taxa/eukaryota/microbotryomycetes_sp_p6c30.yaml data/taxa/eukaryota/microbotryum_lychnidis_dioicae.yaml data/taxa/eukaryota/microbotryum_lychnidis_dioicae_p1a1_lamole.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:160637` has the same identifier, label, strain rank, `NCBITaxon:288795` parent, genetic code `1`, exact synonym, and `gold` attestation copied into the YAML.
- The `Microbotryum lychnidis-dioicae MvSl-1064` exact synonym matches the NCBI row.
- The strain lineage contains the expected 13 entries from `root` through `Microbotryum lychnidis-dioicae`.

## Evidence

- `data/seed_scope.tsv:56387` includes `NCBITaxon:683840` with reason `attested rule: Microbotryum lychnidis-dioicae p1A1 Lamole, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:41298` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project/analysis evidence for `Go0005981` / `Gp0005981`, `Go0137915` / `Gp0142947`, and `Go0373152` / `Gp0219952`.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:683840`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact StrainInfo rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal strain in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:683840`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future GOLD aggregates converge with local native GOLD, check whether the strain should retain two or three GOLD organism assertions.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:683840`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
- GOLD aggregate rows can differ from local native exact rows; for `NCBITaxon:683840`, the generated aggregate count is `2`, while the exact native GOLD files currently contain three matching organism rows.
