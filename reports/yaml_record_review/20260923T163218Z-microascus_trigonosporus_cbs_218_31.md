# YAML Record Review: Microascus trigonosporus CBS 218.31

- Record: `data/taxa/eukaryota/microascus_trigonosporus_cbs_218_31.yaml`
- Reviewed: `2026-09-23T16:32:18Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1314796`
- Label: `Microascus trigonosporus CBS 218.31`
- Rank/domain: `STRAIN` / `EUKARYOTA`
- Parent: `NCBITaxon:36921` (`Microascus trigonosporus`)

## Validation

- `just validate data/taxa/eukaryota/microascus_trigonosporus_cbs_218_31.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microascus_trigonosporus_cbs_218_31.yaml data/taxa/eukaryota/microbotryomycetes_sp_p6c30.yaml data/taxa/eukaryota/microbotryum_lychnidis_dioicae.yaml data/taxa/eukaryota/microbotryum_lychnidis_dioicae_p1a1_lamole.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:312646` has the same identifier, label, strain rank, `NCBITaxon:36921` parent, genetic code `1`, empty synonym fields, and `gold` attestation copied into the YAML.
- The strain lineage contains the expected 17 entries from `root` through `Microascus trigonosporus`.

## Evidence

- `data/seed_scope.tsv:59386` includes `NCBITaxon:1314796` with reason `attested rule: Microascus trigonosporus CBS 218.31, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:7697` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism evidence for `Go0033165` / `Microascus trigonosporus var. trigonosporus`, with no native project or analysis rows joining to that organism.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:1314796`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact StrainInfo rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal strain in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:1314796`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future GOLD refreshes add projects under exact organism `Go0033165`, verify that they continue to attach to the strain record rather than the parent species.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1314796`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
