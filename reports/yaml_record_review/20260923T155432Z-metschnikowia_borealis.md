# YAML Record Review: Metschnikowia borealis

- Record: `data/taxa/eukaryota/metschnikowia_borealis.yaml`
- Reviewed: `2026-09-23T15:54:32Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:73518`
- Label: `Metschnikowia borealis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_borealis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_borealis.yaml data/taxa/eukaryota/metschnikowia_bowlesiae.yaml data/taxa/eukaryota/metschnikowia_caudata.yaml data/taxa/eukaryota/metschnikowia_cerradonensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:10324` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, exact synonym, related synonyms, and `gold` attestation copied into the YAML.
- The exact synonym `Metschnikowia continentalis var. borealis` and both related authority names match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:53258` includes `NCBITaxon:73518` with reason `attested rule: Metschnikowia borealis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:42064` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains three exact organism/project rows for `SUB 99-207.1`, `UWOPS 96-101.1`, and `NRRL Y-27451`, with analyses for the first two projects.
- A complete `rg --no-ignore --hidden` scan found eight NCBI type-material rows at `data/raw/ncbi_type_material.tsv:260965-260972`, covering `NRRL Y-27451`, `CBS 8431`, and `UWO(PS) 96-104.2` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No NCBI merge row, retained old ID, or auxiliary BactoTraits, GTDB, LPSN, MADIN, or MediaDive row was found for `NCBITaxon:73518`.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the eight accession spellings remain grouped as source aliases and do not inflate `strain_count`.
- If future GOLD-to-strain joins start emitting non-BacDive organisms, check whether the three exact native GOLD rows should become concrete strain records or remain aggregate evidence only.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:73518`; the type-material rows were additionally confirmed with a complete ignored-file-inclusive `rg --no-ignore --hidden` pass.
