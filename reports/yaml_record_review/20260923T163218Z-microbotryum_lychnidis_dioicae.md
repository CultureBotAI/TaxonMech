# YAML Record Review: Microbotryum lychnidis-dioicae

- Record: `data/taxa/eukaryota/microbotryum_lychnidis_dioicae.yaml`
- Reviewed: `2026-09-23T16:32:18Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:288795`
- Label: `Microbotryum lychnidis-dioicae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:34416` (`Microbotryum`)

## Validation

- `just validate data/taxa/eukaryota/microbotryum_lychnidis_dioicae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microascus_trigonosporus_cbs_218_31.yaml data/taxa/eukaryota/microbotryomycetes_sp_p6c30.yaml data/taxa/eukaryota/microbotryum_lychnidis_dioicae.yaml data/taxa/eukaryota/microbotryum_lychnidis_dioicae_p1a1_lamole.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:58950` has the same identifier, label, species rank, `NCBITaxon:34416` parent, genetic code `1`, exact synonym, related synonym, and `gold` attestation copied into the YAML.
- The `Uredo antherarum d lychnidis-dioicae` exact synonym and 1815 authority string match the NCBI row.
- The YAML lineage contains the expected 12 entries from `root` through `Microbotryum`.

## Evidence

- `data/seed_scope.tsv:55010` includes `NCBITaxon:288795` with reason `attested rule: Microbotryum lychnidis-dioicae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:28139` reports GOLD organism count `20`, matching the YAML GOLD `assertion_count`.
- A complete exact scan of the native GOLD snapshot contains 20 exact organism rows, 20 project rows, and 20 analysis rows for direct `MvSl-*` strains under this species.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:288795`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- One exact StrainInfo direct/deposit row exists for `NCBITaxon:288795`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay row is expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:288795`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If direct filed-under-species GOLD rows are ever split to descendant strain records, revisit the 20 `MvSl-*` native GOLD organism rows.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact StrainInfo hit for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:288795`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
