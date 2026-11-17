# YAML Record Review: Metschnikowia lunata

- Record: `data/taxa/eukaryota/metschnikowia_lunata.yaml`
- Reviewed: `2026-09-23T16:09:33Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:27325`
- Label: `Metschnikowia lunata`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_lunata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_laotica.yaml data/taxa/eukaryota/metschnikowia_lochheadii.yaml data/taxa/eukaryota/metschnikowia_lopburiensis_nom_inval.yaml data/taxa/eukaryota/metschnikowia_lunata.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2736` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonym, and `gold` attestation copied into the YAML.
- The related synonym `Metschnikowia lunata Golubev, 1977` matches the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:52153` includes `NCBITaxon:27325` with reason `attested rule: Metschnikowia lunata, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:25467` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains an exact organism/project chain for `Go0705622` / `NRRL Y-7131` and project `Gp0831668`.
- A complete `rg --no-ignore --hidden` scan found 16 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:115127-115142`, covering `ATCC 22033`, `CBS 5946`, `IFO 1605`, `IGC 4209`, `JCM 1798`, `NRRL Y-7131`, and `VKM Y-1651` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:27325`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:27325`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the 16 type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact StrainInfo hits for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:27325`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
