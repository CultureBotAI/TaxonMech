# YAML Record Review: Metschnikowia drakensbergensis

- Record: `data/taxa/eukaryota/metschnikowia_drakensbergensis.yaml`
- Reviewed: `2026-09-23T15:58:33Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1506548`
- Label: `Metschnikowia drakensbergensis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_drakensbergensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_corniflorae.yaml data/taxa/eukaryota/metschnikowia_cubensis.yaml data/taxa/eukaryota/metschnikowia_dekortorum.yaml data/taxa/eukaryota/metschnikowia_drakensbergensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:386908` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, exact synonym, related synonyms, and `gold` attestation copied into the YAML.
- The exact synonym `Candida sp. EBDM8Y1` and the nine related Candida/Metschnikowia provisional names match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:60360` includes `NCBITaxon:1506548` with reason `attested rule: Metschnikowia drakensbergensis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:11836` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project/analysis chains for `EBD-CdVSA09-2T` and `EBD-CdVSA10-2A`: `Go0455126` / `Gp0323452` and `Go0455127` / `Gp0323453`.
- A complete `rg --no-ignore --hidden` scan found six NCBI type-material rows at `data/raw/ncbi_type_material.tsv:37667-37672`, covering `CBS 13649`, `NRRL Y-63721`, and `EBD-CdVSA09-2` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:5446-5449` maps side-inventory old IDs `NCBITaxon:1150645`, `NCBITaxon:1150646`, `NCBITaxon:1150647`, and `NCBITaxon:1150648` into `NCBITaxon:1506548`; no retained old-ID rows were present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the six type-material spellings remain grouped as source aliases.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the four omitted old IDs.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1506548`; the type-material rows were additionally confirmed with a complete ignored-file-inclusive `rg --no-ignore --hidden` pass.
