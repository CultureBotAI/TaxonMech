# YAML Record Review: Metschnikowia hawaiiensis

- Record: `data/taxa/eukaryota/metschnikowia_hawaiiensis.yaml`
- Reviewed: `2026-09-23T16:03:52Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:27323`
- Label: `Metschnikowia hawaiiensis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_hawaiiensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_hawaiiana.yaml data/taxa/eukaryota/metschnikowia_hawaiiensis.yaml data/taxa/eukaryota/metschnikowia_henanensis.yaml data/taxa/eukaryota/metschnikowia_hibisci.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2734` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonym, and `gold` attestation copied into the YAML.
- The related synonym `Metschnikowia hawaiiensis Lachance, Starmer & Phaff, 1990` matches the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:52151` includes `NCBITaxon:27323` with reason `attested rule: Metschnikowia hawaiiensis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:25464` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0455168` / `UWOPS 87-2203.2`, `Go0455169` / `UWOPS 91-745.2`, and `Go0705277` / `NRRL Y-17272`, with projects `Gp0323494`, `Gp0323495`, and `Gp0831312`.
- Native GOLD also contains analysis rows for the two UWOPS projects.
- A complete `rg --no-ignore --hidden` scan found 12 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:115099-115110`, covering `ATCC 76059`, `CBS 7432`, `IFO 10791`, `IGC 4220`, `NRRL Y-17272`, and `UWO(PS) 87-2167.2` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:27323`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:27323`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the 12 type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact StrainInfo hits for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:27323`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
