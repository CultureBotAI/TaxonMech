# YAML Record Review: Metschnikowia hamakuensis

- Record: `data/taxa/eukaryota/metschnikowia_hamakuensis.yaml`
- Reviewed: `2026-09-23T16:01:17Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:301365`
- Label: `Metschnikowia hamakuensis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_hamakuensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_drosophilae.yaml data/taxa/eukaryota/metschnikowia_gelsemii.yaml data/taxa/eukaryota/metschnikowia_gruessii.yaml data/taxa/eukaryota/metschnikowia_hamakuensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:61444` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonym, and `gold` attestation copied into the YAML.
- The related synonym `Metschnikowia hamakuensis Lachance, 2005` matches the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:55073` includes `NCBITaxon:301365` with reason `attested rule: Metschnikowia hamakuensis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:30148` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0455155` / `UWOPS 04-199.1`, `Go0455157` / `UWOPS 04-207.1`, and `Go0705502` / `NRRL Y-27834`, with projects `Gp0323481`, `Gp0323483`, and `Gp0831545`.
- Native GOLD also contains analysis rows for the two UWOPS projects.
- A complete `rg --no-ignore --hidden` scan found seven NCBI type-material rows at `data/raw/ncbi_type_material.tsv:155112-155118`, covering `CBS 10056`, `NRRL Y-27834`, and `UWO-PS 04-207.1` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:301365`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the seven type-material spellings remain grouped as source aliases.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:301365`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
