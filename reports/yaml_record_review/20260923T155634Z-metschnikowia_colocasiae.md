# YAML Record Review: Metschnikowia colocasiae

- Record: `data/taxa/eukaryota/metschnikowia_colocasiae.yaml`
- Reviewed: `2026-09-23T15:56:34Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:473035`
- Label: `Metschnikowia colocasiae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_colocasiae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_chrysomelidarum.yaml data/taxa/eukaryota/metschnikowia_chrysoperlae.yaml data/taxa/eukaryota/metschnikowia_colocasiae.yaml data/taxa/eukaryota/metschnikowia_continentalis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:105631` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonyms, and `gold` attestation copied into the YAML.
- The three related synonyms in the YAML match the NCBI row; the row has no exact synonyms.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:55770` includes `NCBITaxon:473035` with reason `attested rule: Metschnikowia colocasiae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:36498` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains three exact organism/project rows for `UWOPS 03-134.2`, `UWOPS 03-202.1`, and `NRRL Y-27629`, with analyses for the two `UWOPS` projects.
- A complete `rg --no-ignore --hidden` scan found six NCBI type-material rows at `data/raw/ncbi_type_material.tsv:218681-218686`, covering `CBS 9739`, `NRRL Y-27629`, and `UWO(PS) 03-134.2` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:41170` maps side-inventory old ID `NCBITaxon:236301` into `NCBITaxon:473035`; no retained old-ID row was present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the six type-material spellings remain grouped as source aliases.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted `NCBITaxon:236301` old ID.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:473035`; the type-material rows were additionally confirmed with a complete ignored-file-inclusive `rg --no-ignore --hidden` pass.
