# YAML Record Review: Metschnikowia caudata

- Record: `data/taxa/eukaryota/metschnikowia_caudata.yaml`
- Reviewed: `2026-09-23T15:54:32Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1506549`
- Label: `Metschnikowia caudata`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_caudata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_borealis.yaml data/taxa/eukaryota/metschnikowia_bowlesiae.yaml data/taxa/eukaryota/metschnikowia_caudata.yaml data/taxa/eukaryota/metschnikowia_cerradonensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:386909` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, and `gold` attestation copied into the YAML.
- The three related synonyms in the YAML match the NCBI row, including the two authority forms and `Metschnikowia sp. 5-6 CdV-2014`; the row has no exact synonyms.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:60361` includes `NCBITaxon:1506549` with reason `attested rule: Metschnikowia caudata, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:11837` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains three exact organism/project rows for `EBD-CdVSA57-2`, `EBD-CdVSA08-1`, and `NRRL Y-63722`, with analyses for the two `EBD-*` projects.
- A complete `rg --no-ignore --hidden` scan found six NCBI type-material rows at `data/raw/ncbi_type_material.tsv:37673-37678`, covering `CBS 13651`, `NRRL Y-63722`, and `EBD-CdVSA08-1` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No NCBI merge row, retained old ID, or auxiliary BactoTraits, GTDB, LPSN, MADIN, or MediaDive row was found for `NCBITaxon:1506549`.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the `CBS 13651`, `NRRL Y-63722`, and `EBD-CdVSA08-1` forms are normalized as source aliases.
- If future GOLD-to-strain joins start emitting non-BacDive organisms, check whether the three exact native GOLD rows should become concrete strain records or remain aggregate evidence only.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1506549`; the type-material rows were additionally confirmed with a complete ignored-file-inclusive `rg --no-ignore --hidden` pass.
