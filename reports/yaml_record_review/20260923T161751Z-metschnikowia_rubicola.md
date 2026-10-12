# YAML Record Review: Metschnikowia rubicola

- Record: `data/taxa/eukaryota/metschnikowia_rubicola.yaml`
- Reviewed: `2026-09-23T16:17:51Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:2201248`
- Label: `Metschnikowia rubicola`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_rubicola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_reukaufii.yaml data/taxa/eukaryota/metschnikowia_rubicola.yaml data/taxa/eukaryota/metschnikowia_santaceciliae.yaml data/taxa/eukaryota/metschnikowia_shivogae.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:521302` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonym, and `gold` attestation copied into the YAML.
- The related synonym `Metschnikowia rubicola Kurtzman, Robnett & Basehoar, 2018` matches the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:62477` includes `NCBITaxon:2201248` with reason `attested rule: Metschnikowia rubicola, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:20903` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains an exact organism/project chain for `Go0705127` / `CBS 15344` and project `Gp0831150`.
- A complete `rg --no-ignore --hidden` scan found nine NCBI type-material rows at `data/raw/ncbi_type_material.tsv:87734-87742`, covering `CBS 15344` and `NRRL Y-6064` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:2201248`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the nine type-material spellings remain grouped as source aliases.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:2201248`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
