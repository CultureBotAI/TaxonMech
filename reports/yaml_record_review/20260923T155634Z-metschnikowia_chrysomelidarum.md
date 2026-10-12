# YAML Record Review: Metschnikowia chrysomelidarum

- Record: `data/taxa/eukaryota/metschnikowia_chrysomelidarum.yaml`
- Reviewed: `2026-09-23T15:56:34Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:271316`
- Label: `Metschnikowia chrysomelidarum`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_chrysomelidarum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_chrysomelidarum.yaml data/taxa/eukaryota/metschnikowia_chrysoperlae.yaml data/taxa/eukaryota/metschnikowia_colocasiae.yaml data/taxa/eukaryota/metschnikowia_continentalis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:56031` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, exact synonym, related synonyms, and `gold` attestation copied into the YAML.
- The exact synonym `Candida chrysomelidarum` and the three related synonyms match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:54922` includes `NCBITaxon:271316` with reason `attested rule: Metschnikowia chrysomelidarum, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:25132` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains one exact organism/project pair for `Metschnikowia chrysomelidarum NRRL Y-27749`: `Go0705492` and `Gp0831535`; no linked native GOLD analysis row was found.
- A complete `rg --no-ignore --hidden` scan found eight NCBI type-material rows at `data/raw/ncbi_type_material.tsv:112595-112602`, covering `CBS 9904`, `ATCC MYA-4344`, and `NRRL Y-27749` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No NCBI merge row, retained old ID, or auxiliary BactoTraits, GTDB, LPSN, MADIN, or MediaDive row was found for `NCBITaxon:271316`.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the eight type-material spellings remain grouped as source aliases.
- If future GOLD-to-strain joins start emitting non-BacDive organisms, check whether `Go0705492` should become a concrete `NRRL Y-27749` strain or remain aggregate evidence only.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:271316`; the type-material rows were additionally confirmed with a complete ignored-file-inclusive `rg --no-ignore --hidden` pass.
