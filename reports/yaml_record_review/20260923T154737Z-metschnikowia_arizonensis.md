# YAML Record Review: Metschnikowia arizonensis

- Record: `data/taxa/eukaryota/metschnikowia_arizonensis.yaml`
- Reviewed: `2026-09-23T15:47:37Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:150206`
- Label: `Metschnikowia arizonensis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_arizonensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_anglica.yaml data/taxa/eukaryota/metschnikowia_arizonensis.yaml data/taxa/eukaryota/metschnikowia_australis.yaml data/taxa/eukaryota/metschnikowia_baotianmanensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:30978` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, and `gold` attestation copied into the YAML.
- The two related synonyms, `Metschnikowia arizonensis Lachance & J.M. Bowles, 2002` and `Metschnikowia cf. hawaiiensis UWO(PS)99-103.1.1`, match the NCBI row; the row has no exact synonyms.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:54063` includes `NCBITaxon:150206` with reason `attested rule: Metschnikowia arizonensis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:11766` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project/analysis chains for `UWOPS 99-103.3.1` and `UWOPS 99-103.4`: `Go0455175` / `Gp0323501` and `Go0455176` / `Gp0323502`.
- `data/raw/ncbi_type_material.tsv:37255-37258` has four culture-from-holotype aliases for `CBS 9064` and `UWO(PS) 99-103.3.1`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No NCBI merge row, retained old ID, or auxiliary BactoTraits, GTDB, LPSN, MADIN, or MediaDive row was found for `NCBITaxon:150206`.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future GOLD-to-strain joins start emitting non-BacDive organisms, check whether the two exact native GOLD rows should become concrete `UWOPS 99-103.*` strains or remain aggregate evidence only.
- If future generation begins materializing NCBI type-material accessions, verify that the `CBS 9064` and `UWO(PS) 99-103.3.1` aliases stay grouped by biological source.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:150206`.
