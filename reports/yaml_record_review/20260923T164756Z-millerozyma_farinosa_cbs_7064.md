# YAML Record Review: Millerozyma farinosa CBS 7064

- Record: `data/taxa/eukaryota/millerozyma_farinosa_cbs_7064.yaml`
- Reviewed: `2026-09-23T16:47:56Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:559304`
- Label: `Millerozyma farinosa CBS 7064`
- Rank/domain: `STRAIN` / `EUKARYOTA`
- Parent: `NCBITaxon:4920` (`Millerozyma farinosa`)

## Validation

- `just validate data/taxa/eukaryota/millerozyma_farinosa_cbs_7064.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/millerago_galiae.yaml data/taxa/eukaryota/millerozyma_acaciae.yaml data/taxa/eukaryota/millerozyma_farinosa.yaml data/taxa/eukaryota/millerozyma_farinosa_cbs_7064.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:131314` has the same identifier, label, strain rank, `NCBITaxon:4920` parent, yeast genetic code `12`, exact synonym, and `gold` attestation copied into the YAML.
- The YAML keeps `Pichia farinosa CBS 7064` as an exact synonym from NCBI.
- The YAML lineage contains the expected 14 entries from `root` through `Millerozyma farinosa`.

## Evidence

- `curation/seed_scope.tsv:56031` includes `NCBITaxon:559304` with reason `attested rule: Millerozyma farinosa CBS 7064, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:38795` reports GOLD organism count `7`, matching the YAML GOLD `assertion_count`.
- A complete native GOLD organism scan found eight exact rows for numeric taxon `559304`, including `Go0038456` for `CBS 7064` and `Go0614144` through `Go0614150` for `NRRL Y-7553`, `NCYC 815`, `NBRC 1163`, `IFO 1163`, `DSM 3316`, `CBS 185`, and `691`.
- Those eight native organism rows link to three project rows and one analysis row for this taxon.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_type_material.tsv` rows for `NCBITaxon:559304`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact StrainInfo rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal strain in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:559304`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- Reconcile the transformed GOLD aggregate count of 7 with the eight exact native GOLD organism rows for `NCBITaxon:559304` on the next GOLD refresh.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:559304`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
