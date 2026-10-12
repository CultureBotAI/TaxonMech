# YAML Record Review: Metschnikowia agaves

- Record: `data/taxa/eukaryota/metschnikowia_agaves.yaml`
- Reviewed: `2026-09-23T15:44:12Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:56417`
- Label: `Metschnikowia agaves`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_agaves.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metchnikovella_incurvata.yaml data/taxa/eukaryota/metschnikowia_aberdeeniae.yaml data/taxa/eukaryota/metschnikowia_agaves.yaml data/taxa/eukaryota/metschnikowia_amazonensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:7091` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, and `gold` attestation copied into the YAML.
- The related synonym `Metschnikowia agaves Lachance, 1993` matches the NCBI row; the row has no exact synonyms.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:52960` includes `NCBITaxon:56417` with reason `attested rule: Metschnikowia agaves, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:38920` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains one exact organism/project pair for `Metschnikowia agaves NRRL Y-17915`: `Go0705364` and `Gp0831401`; no linked native GOLD analysis row was found.
- A complete `rg --no-ignore --hidden` scan found ten NCBI type-material rows at `data/raw/ncbi_type_material.tsv:235988-235997`, covering `ATCC 90148`, `CBS 7744`, `IFO 10860`, `NRRL Y-17915`, and `UWO(PS) 92-207.1` spelling variants.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No NCBI merge row, retained old ID, or auxiliary BactoTraits, GTDB, LPSN, MADIN, or MediaDive row was found for `NCBITaxon:56417`.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the ten accession spellings collapse to the expected source aliases and do not inflate `strain_count`.
- If future GOLD-to-strain joins start emitting non-BacDive organisms, check whether `Go0705364` should become a concrete `NRRL Y-17915` strain or remain aggregate evidence only.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:56417`; the type-material rows were additionally confirmed with a complete ignored-file-inclusive `rg --no-ignore --hidden` pass.
