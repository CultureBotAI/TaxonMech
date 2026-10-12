# YAML Record Review: Metschnikowia gruessii

- Record: `data/taxa/eukaryota/metschnikowia_gruessii.yaml`
- Reviewed: `2026-09-23T16:01:17Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:45517`
- Label: `Metschnikowia gruessii`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_gruessii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_drosophilae.yaml data/taxa/eukaryota/metschnikowia_gelsemii.yaml data/taxa/eukaryota/metschnikowia_gruessii.yaml data/taxa/eukaryota/metschnikowia_hamakuensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:5585` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonym, and `gold` attestation copied into the YAML.
- The related synonym `Metschnikowia gruessii Gim.-Jurado, 1992` matches the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:52631` includes `NCBITaxon:45517` with reason `attested rule: Metschnikowia gruessii, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:36029` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0527706` / `VY0332` and `Go0705351` / `NRRL Y-17809`, with projects `Gp0456068`, `Gp0456074`, and `Gp0831388`.
- A complete `rg --no-ignore --hidden` scan found 11 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:214705-214715`, covering `CBS 7657`, `IFO 10788`, `IGC 4382`, and `NRRL Y-17809` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:45517`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the 11 type-material spellings remain grouped as source aliases.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:45517`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
