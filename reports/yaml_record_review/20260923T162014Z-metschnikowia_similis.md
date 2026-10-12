# YAML Record Review: Metschnikowia similis

- Record: `data/taxa/eukaryota/metschnikowia_similis.yaml`
- Reviewed: `2026-09-23T16:20:14Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:473037`
- Label: `Metschnikowia similis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_similis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_similis.yaml data/taxa/eukaryota/metschnikowia_sp_00_154_1.yaml data/taxa/eukaryota/metschnikowia_sp_01_655c1.yaml data/taxa/eukaryota/metschnikowia_sp_03_147_1.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:105632` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonyms, and `gold` attestation copied into the YAML.
- The `Metschnikowia similis` authority strings and `Metschnikowia sp. UWO(PS)01-138a3` related synonym match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:55771` includes `NCBITaxon:473037` with reason `attested rule: Metschnikowia similis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:36499` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0455145` / `UWOPS 03-133.4`, `Go0455148` / `UWOPS 03-158.2`, and `Go0705465` / `NRRL Y-27627`, with projects `Gp0323471`, `Gp0323474`, and `Gp0831508`.
- Native GOLD also contains analysis rows for the two UWOPS projects at `data/gold/analyses.jsonl.gz` lines 439122 and 439137.
- A complete `rg --no-ignore --hidden` scan found six NCBI type-material rows at `data/raw/ncbi_type_material.tsv:218687-218692`, covering `CBS 9737`, `NRRL Y-27627`, and `UWO(PS) 03-192.2` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:473037` at source line 132197, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:41171` maps side-inventory old ID `NCBITaxon:236303` into `NCBITaxon:473037`; no retained old-ID row was present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the six type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact `CBS 9062` StrainInfo deposit for this taxon.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted `NCBITaxon:236303` old ID.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:473037`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
