# YAML Record Review: Metschnikowia bicuspidata var. bicuspidata NRRL YB-4993

- Record: `data/taxa/eukaryota/metschnikowia_bicuspidata_var_bicuspidata_nrrl_yb_4993.yaml`
- Reviewed: `2026-09-23T15:51:47Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:869754`
- Label: `Metschnikowia bicuspidata var. bicuspidata NRRL YB-4993`
- Rank/domain: `STRAIN` / `EUKARYOTA`
- Parent: `NCBITaxon:280587` (`Metschnikowia bicuspidata var. bicuspidata`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_bicuspidata_var_bicuspidata_nrrl_yb_4993.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_bicuspidata.yaml data/taxa/eukaryota/metschnikowia_bicuspidata_var_bicuspidata_nrrl_yb_4993.yaml data/taxa/eukaryota/metschnikowia_bicuspidata_var_californica.yaml data/taxa/eukaryota/metschnikowia_bicuspidata_var_chathamia.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:184163` has the same identifier, label, strain rank, `NCBITaxon:280587` parent, genetic code `12`, empty synonym fields, and `gold` attestation copied into the YAML.
- The YAML lineage contains the expected 15 entries from `root` through parent variety `Metschnikowia bicuspidata var. bicuspidata`.

## Evidence

- `data/seed_scope.tsv:56806` includes `NCBITaxon:869754` with reason `attested rule: Metschnikowia bicuspidata var. bicuspidata NRRL YB-4993, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:43581` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The bounded scan found no exact native GOLD organism/project/analysis rows for NCBI taxon `869754` in the local `data/gold/*.jsonl.gz` snapshots.
- The bounded scan found no NCBI type-material rows for this exact strain taxon.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No NCBI merge row, retained old ID, or auxiliary BactoTraits, GTDB, LPSN, MADIN, or MediaDive row was found for `NCBITaxon:869754`.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future GOLD-to-strain joins begin reconciling species-filed `NRRL YB-4993` rows, check whether the `Go0005934` organism currently filed under `NCBITaxon:27322` should be connected to this exact strain.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:869754`.
