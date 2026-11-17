# YAML Record Review: Metchnikovella incurvata

- Record: `data/taxa/eukaryota/metchnikovella_incurvata.yaml`
- Reviewed: `2026-09-23T15:44:12Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:2248764`
- Label: `Metchnikovella incurvata`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:2248763` (`Metchnikovella`)

## Validation

- `just validate data/taxa/eukaryota/metchnikovella_incurvata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metchnikovella_incurvata.yaml data/taxa/eukaryota/metschnikowia_aberdeeniae.yaml data/taxa/eukaryota/metschnikowia_agaves.yaml data/taxa/eukaryota/metschnikowia_amazonensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:522073` has the same identifier, label, species rank, `NCBITaxon:2248763` parent, genetic code `1`, and `gold` attestation copied into the YAML.
- The related synonym `Metchnikovella incurvata Caullery & Mesnil, 1914` matches the NCBI row; the row has no exact synonyms.
- The YAML lineage contains the expected 10 entries from `root` through `Metchnikovella`.

## Evidence

- `data/seed_scope.tsv:62498` includes `NCBITaxon:2248764` with reason `attested rule: Metchnikovella incurvata, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:21186` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains one exact organism/project/analysis chain for `Metchnikovella incurvata LNA5`: `Go0518221`, `Gp0442302`, and AP name `Metchnikovella incurvata LNA5`.
- The bounded scan found no NCBI type-material rows for this NCBI ID.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No NCBI merge row, retained old ID, or auxiliary BactoTraits, GTDB, LPSN, MADIN, or MediaDive row was found for `NCBITaxon:2248764`.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future GOLD-to-strain joins start emitting non-BacDive organisms, check whether `Go0518221` should become a concrete `LNA5` strain or remain aggregate evidence only.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:2248764`.
