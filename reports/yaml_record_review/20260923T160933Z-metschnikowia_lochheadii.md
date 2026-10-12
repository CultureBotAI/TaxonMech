# YAML Record Review: Metschnikowia lochheadii

- Record: `data/taxa/eukaryota/metschnikowia_lochheadii.yaml`
- Reviewed: `2026-09-23T16:09:33Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:135832`
- Label: `Metschnikowia lochheadii`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_lochheadii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_laotica.yaml data/taxa/eukaryota/metschnikowia_lochheadii.yaml data/taxa/eukaryota/metschnikowia_lopburiensis_nom_inval.yaml data/taxa/eukaryota/metschnikowia_lunata.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:27150` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonyms, and `gold` attestation copied into the YAML.
- The related synonyms `Metschnikowia lochheadii Lachance, 2001` and `Metschnikowia sp. CBS 8808` match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:53968` includes `NCBITaxon:135832` with reason `attested rule: Metschnikowia lochheadii, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:8709` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0455149` / `UWOPS 03-167a3`, `Go0455178` / `UWOPS 99-661.1`, and `Go0705430` / `NRRL Y-27457`, with projects `Gp0323475`, `Gp0323504`, and `Gp0831473`.
- Native GOLD also contains analysis rows for the two UWOPS projects.
- A complete `rg --no-ignore --hidden` scan found eight NCBI type-material rows at `data/raw/ncbi_type_material.tsv:25758-25765`, covering `CBS 8807`, `NRRL Y-27457`, and `UWO(PS) 00-133.2` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:135832`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:135832`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the eight type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact StrainInfo hits for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:135832`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
