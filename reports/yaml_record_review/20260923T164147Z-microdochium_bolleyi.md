# YAML Record Review: Microdochium bolleyi

- Record: `data/taxa/eukaryota/microdochium_bolleyi.yaml`
- Reviewed: `2026-09-23T16:41:47Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:196109`
- Label: `Microdochium bolleyi`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:67608` (`Microdochium`)

## Validation

- `just validate data/taxa/eukaryota/microdochium_bolleyi.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microcyclosporella_mali.yaml data/taxa/eukaryota/microdochium_bolleyi.yaml data/taxa/eukaryota/microdochium_trichocladiopsis.yaml data/taxa/eukaryota/micromonas_sp.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:38942` has the same identifier, label, species rank, `NCBITaxon:67608` parent, genetic code `1`, exact synonym, two related synonyms, and `gold` attestation copied into the YAML.
- The YAML keeps `Gloeosporium bolleyi` as an exact synonym and the two authority strings as related synonyms, matching the NCBI source row.
- The YAML lineage contains the expected 16 entries from `root` through `Microdochium`.

## Evidence

- `curation/seed_scope.tsv:54431` includes `NCBITaxon:196109` with reason `attested rule: Microdochium bolleyi, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:18028` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project/analysis evidence for `Go0111687` / `J235TASD1`, with two native GOLD projects and two native GOLD analysis rows linked through `Gp0113784`.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_type_material.tsv` rows for `NCBITaxon:196109`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has exact rows for `NCBITaxon:196109` directly and in deposits, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:196109`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If the generator starts materializing StrainInfo-only fungal records, re-check the 28 direct and 30 deposit-level native StrainInfo hits for `NCBITaxon:196109` against the expected local-strain policy.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:196109`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
