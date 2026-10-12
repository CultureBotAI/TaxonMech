# YAML Record Review: Metschnikowia amazonensis

- Record: `data/taxa/eukaryota/metschnikowia_amazonensis.yaml`
- Reviewed: `2026-09-23T15:44:12Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:2576851`
- Label: `Metschnikowia amazonensis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_amazonensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metchnikovella_incurvata.yaml data/taxa/eukaryota/metschnikowia_aberdeeniae.yaml data/taxa/eukaryota/metschnikowia_agaves.yaml data/taxa/eukaryota/metschnikowia_amazonensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:532544` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, and `gold` attestation copied into the YAML.
- The two related synonyms, `Metschnikowia amazonensis Santos et al., 2019` and `Metschnikowia sp. DKL-2019a`, match the NCBI row; the row has no exact synonyms.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:62852` includes `NCBITaxon:2576851` with reason `attested rule: Metschnikowia amazonensis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:23550` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project/analysis chains for `UFMG-CM-6309` and `UFMG-CM-6307`: `Go0676991` / `Gp0778798` and `Go0676992` / `Gp0778799`.
- `data/raw/ncbi_type_material.tsv:102569-102572` has the four NCBI holotype spellings for `UFMG-CM-6309`, `UFMG-CM-Y6309`, `UFMG:CM-Y6309`, and `UFMG<BRA>:CM-Y6309`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No NCBI merge row, retained old ID, or auxiliary BactoTraits, GTDB, LPSN, MADIN, or MediaDive row was found for `NCBITaxon:2576851`.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future GOLD-to-strain joins start emitting non-BacDive organisms, check whether the two exact native GOLD rows should become concrete `UFMG-CM-*` strains or remain aggregate evidence only.
- If future generation begins materializing NCBI type-material accessions, verify that the four `UFMG-CM-6309` variants are normalized as one holotype concept.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:2576851`.
