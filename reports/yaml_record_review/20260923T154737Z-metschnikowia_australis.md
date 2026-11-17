# YAML Record Review: Metschnikowia australis

- Record: `data/taxa/eukaryota/metschnikowia_australis.yaml`
- Reviewed: `2026-09-23T15:47:37Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:27321`
- Label: `Metschnikowia australis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_australis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_anglica.yaml data/taxa/eukaryota/metschnikowia_arizonensis.yaml data/taxa/eukaryota/metschnikowia_australis.yaml data/taxa/eukaryota/metschnikowia_baotianmanensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2732` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, exact synonym, related synonyms, and `gold` attestation copied into the YAML.
- The exact synonym `Metschnikowia bicuspidata var. australis` and both related authority forms match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:52149` includes `NCBITaxon:27321` with reason `attested rule: Metschnikowia australis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:25459` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project pairs for `UFMG-CM-Y6158` and `NRRL Y-17414`; the former also has analysis project `Gp0236146`.
- A complete `rg --no-ignore --hidden` scan found 16 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:115047-115062`, covering `NRRL Y-17414` culture-from-holotype variants plus `ATCC 22298`, `CBS 5847`, `IFO 10783`, `IGC 4212`, and `NRRL Y-7013` type-material aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No NCBI merge row, retained old ID, or auxiliary BactoTraits, GTDB, LPSN, MADIN, or MediaDive row was found for `NCBITaxon:27321`.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the 16 aliases are grouped by source strain and do not inflate `strain_count`.
- If future GOLD-to-strain joins start emitting non-BacDive organisms, check whether the two exact native GOLD rows should become concrete strain records or remain aggregate evidence only.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:27321`; the type-material rows were additionally confirmed with a complete ignored-file-inclusive `rg --no-ignore --hidden` pass.
