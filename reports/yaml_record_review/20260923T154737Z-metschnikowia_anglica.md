# YAML Record Review: Metschnikowia anglica

- Record: `data/taxa/eukaryota/metschnikowia_anglica.yaml`
- Reviewed: `2026-09-23T15:47:37Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:2201240`
- Label: `Metschnikowia anglica`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_anglica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_anglica.yaml data/taxa/eukaryota/metschnikowia_arizonensis.yaml data/taxa/eukaryota/metschnikowia_australis.yaml data/taxa/eukaryota/metschnikowia_baotianmanensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:521298` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, and `gold` attestation copied into the YAML.
- The related synonym `Metschnikowia anglica Kurtzman, Robnett & Basehoar, 2018` matches the NCBI row; the row has no exact synonyms.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:62473` includes `NCBITaxon:2201240` with reason `attested rule: Metschnikowia anglica, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:20899` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains one exact organism/project pair for `Metschnikowia anglica CBS 15342`: `Go0705126` and `Gp0831149`; no linked native GOLD analysis row was found.
- A complete `rg --no-ignore --hidden` scan found 11 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:87705-87715`, covering `NRRL Y-7298` holotype aliases and `CBS 14173` / `CBS 15342` culture-from-holotype aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No NCBI merge row, retained old ID, or auxiliary BactoTraits, GTDB, LPSN, MADIN, or MediaDive row was found for `NCBITaxon:2201240`.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the `NRRL Y-7298`, `CBS 14173`, and `CBS 15342` spellings stay grouped as source aliases and do not inflate `strain_count`.
- If future GOLD-to-strain joins start emitting non-BacDive organisms, check whether `Go0705126` should become a concrete `CBS 15342` strain or remain aggregate evidence only.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:2201240`; the type-material rows were additionally confirmed with a complete ignored-file-inclusive `rg --no-ignore --hidden` pass.
