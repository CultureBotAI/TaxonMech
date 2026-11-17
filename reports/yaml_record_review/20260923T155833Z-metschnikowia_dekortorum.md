# YAML Record Review: Metschnikowia dekortorum

- Record: `data/taxa/eukaryota/metschnikowia_dekortorum.yaml`
- Reviewed: `2026-09-23T15:58:33Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:174643`
- Label: `Metschnikowia dekortorum`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_dekortorum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_corniflorae.yaml data/taxa/eukaryota/metschnikowia_cubensis.yaml data/taxa/eukaryota/metschnikowia_dekortorum.yaml data/taxa/eukaryota/metschnikowia_drakensbergensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:35423` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonym, and `gold` attestation copied into the YAML.
- The related synonym `Metschnikowia dekortorum Lachance & J.M. Bowles, 2002` matches the NCBI row; the row has no exact synonyms.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:54281` includes `NCBITaxon:174643` with reason `attested rule: Metschnikowia dekortorum, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:15182` reports GOLD organism count `4`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains four exact organism/project rows for `UWOPS 01-142b3`, `UWOPS 03-172.2`, `UWOPS 01-522a5`, and `NRRL Y-27430`, with analyses for the three `UWOPS` projects.
- A complete `rg --no-ignore --hidden` scan found nine NCBI type-material rows at `data/raw/ncbi_type_material.tsv:56549-56557`, covering `CBS 9063`, `NRRL Y-27430`, and `UWO(PS) 01-142b3` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No NCBI merge row, retained old ID, or auxiliary BactoTraits, GTDB, LPSN, MADIN, or MediaDive row was found for `NCBITaxon:174643`.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the nine type-material spellings remain grouped as source aliases.
- If future GOLD-to-strain joins start emitting non-BacDive organisms, check whether the four exact native GOLD rows should become concrete strain records or remain aggregate evidence only.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:174643`; the type-material rows were additionally confirmed with a complete ignored-file-inclusive `rg --no-ignore --hidden` pass.
