# YAML Record Review: Metschnikowia continentalis

- Record: `data/taxa/eukaryota/metschnikowia_continentalis.yaml`
- Reviewed: `2026-09-23T15:56:34Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:73517`
- Label: `Metschnikowia continentalis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_continentalis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_chrysomelidarum.yaml data/taxa/eukaryota/metschnikowia_chrysoperlae.yaml data/taxa/eukaryota/metschnikowia_colocasiae.yaml data/taxa/eukaryota/metschnikowia_continentalis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:10323` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonym, and `gold` attestation copied into the YAML.
- The related synonym `Metschnikowia continentalis Lachance, C.A. Rosa, Starmer, Schlag-Edl., J.S.F. Barker & J.M. Bowles, 1998` matches the NCBI row; the row has no exact synonyms.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:53257` includes `NCBITaxon:73517` with reason `attested rule: Metschnikowia continentalis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:42063` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains three exact organism/project rows for `UWOPS 95-402.1`, `UWOPS 96-173`, and `NRRL Y-27449`, with analyses for the two `UWOPS` projects.
- A complete `rg --no-ignore --hidden` scan found 16 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:260949-260964`, covering `CBS 8429`, `NRRL Y-27449`, `UFMG 96-173`, and `UWO(PS) 95-797.2` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No NCBI merge row, retained old ID, or auxiliary BactoTraits, GTDB, LPSN, MADIN, or MediaDive row was found for `NCBITaxon:73517`.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the 16 type-material spellings remain grouped as source aliases.
- If future GOLD-to-strain joins start emitting non-BacDive organisms, check whether the three exact native GOLD rows should become concrete strain records or remain aggregate evidence only.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:73517`; the type-material rows were additionally confirmed with a complete ignored-file-inclusive `rg --no-ignore --hidden` pass.
