# YAML Record Review: Metschnikowia cerradonensis

- Record: `data/taxa/eukaryota/metschnikowia_cerradonensis.yaml`
- Reviewed: `2026-09-23T15:54:32Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:390697`
- Label: `Metschnikowia cerradonensis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_cerradonensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_borealis.yaml data/taxa/eukaryota/metschnikowia_bowlesiae.yaml data/taxa/eukaryota/metschnikowia_caudata.yaml data/taxa/eukaryota/metschnikowia_cerradonensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:82509` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, and `gold` attestation copied into the YAML.
- The three related synonyms in the YAML match the NCBI row, including both authority strings and `Metschnikowia sp. UFMG 03T67.1`; the row has no exact synonyms.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:55471` includes `NCBITaxon:390697` with reason `attested rule: Metschnikowia cerradonensis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:34086` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains three exact organism/project rows for `UFMG 03-T67.1`, `UFMG 03-T68.1`, and `NRRL Y-48067`, with analyses for the two `UFMG` projects.
- A complete `rg --no-ignore --hidden` scan found eight NCBI type-material rows at `data/raw/ncbi_type_material.tsv:201380-201387`, covering `CBS 10409`, `NRRL Y-48067`, and `UFMG 03-T67.1` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No NCBI merge row, retained old ID, or auxiliary BactoTraits, GTDB, LPSN, MADIN, or MediaDive row was found for `NCBITaxon:390697`.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the `CBS 10409`, `NRRL Y-48067`, and `UFMG 03-T67.1` forms are normalized as source aliases.
- If future GOLD-to-strain joins start emitting non-BacDive organisms, check whether the three exact native GOLD rows should become concrete strain records or remain aggregate evidence only.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:390697`; the type-material rows were additionally confirmed with a complete ignored-file-inclusive `rg --no-ignore --hidden` pass.
