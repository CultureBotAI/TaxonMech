# YAML Record Review: Metschnikowia aberdeeniae

- Record: `data/taxa/eukaryota/metschnikowia_aberdeeniae.yaml`
- Reviewed: `2026-09-23T15:44:12Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:353897`
- Label: `Metschnikowia aberdeeniae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_aberdeeniae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metchnikovella_incurvata.yaml data/taxa/eukaryota/metschnikowia_aberdeeniae.yaml data/taxa/eukaryota/metschnikowia_agaves.yaml data/taxa/eukaryota/metschnikowia_amazonensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:73103` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, and `gold` attestation copied into the YAML.
- The two related synonyms, `Metschnikowia aberdeeniae Lachance & Starmer, 2006` and `Metschnikowia sp. SUB 05-213.1`, match the NCBI row; the row has no exact synonyms.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:55327` includes `NCBITaxon:353897` with reason `attested rule: Metschnikowia aberdeeniae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:33049` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains three exact organisms and projects for `SUB 05-213.1`, `UWOPS 07-202.1`, and `NRRL Y-27921`, with analyses for the first two projects.
- A complete `rg --no-ignore --hidden` scan found nine NCBI type-material rows at `data/raw/ncbi_type_material.tsv:191790-191798`, covering `NRRL Y-27921`, `CBS 10289`, and `SUB 05-213.1` spelling variants.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No NCBI merge row, retained old ID, or auxiliary BactoTraits, GTDB, LPSN, MADIN, or MediaDive row was found for `NCBITaxon:353897`.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the five `NRRL Y-27921`, two `CBS 10289`, and two `SUB 05-213.1` spellings stay grouped by biological source.
- If future GOLD-to-strain joins start emitting non-BacDive organisms, check whether the three exact GOLD organisms should become concrete strain records or remain aggregate evidence only.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:353897`; the type-material rows were additionally confirmed with a complete ignored-file-inclusive `rg --no-ignore --hidden` pass.
