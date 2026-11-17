# YAML Record Review: Metschnikowia hibisci

- Record: `data/taxa/eukaryota/metschnikowia_hibisci.yaml`
- Reviewed: `2026-09-23T16:03:52Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:73520`
- Label: `Metschnikowia hibisci`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_hibisci.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_hawaiiana.yaml data/taxa/eukaryota/metschnikowia_hawaiiensis.yaml data/taxa/eukaryota/metschnikowia_henanensis.yaml data/taxa/eukaryota/metschnikowia_hibisci.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:10325` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonym, and `gold` attestation copied into the YAML.
- The related synonym `Metschnikowia hibisci Lachance, C.A. Rosa, Starmer, Schlag-Edl., J.S.F. Barker & J.M. Bowles, 1998` matches the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:53259` includes `NCBITaxon:73520` with reason `attested rule: Metschnikowia hibisci, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:42065` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0455171` / `UWOPS 95-797.2`, `Go0455172` / `UWOPS 95-805.1`, and `Go0705428` / `NRRL Y-27453`, with projects `Gp0323497`, `Gp0323498`, and `Gp0831471`.
- Native GOLD also contains analysis rows for the two UWOPS projects.
- A complete `rg --no-ignore --hidden` scan found 11 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:260973-260983`, covering `CBS 8433`, `NRRL Y-27453`, and `UWO(PS)95-797.2` / `UWOPS 95-797.2` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:73520`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:73520`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the 11 type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact StrainInfo hits for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:73520`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
