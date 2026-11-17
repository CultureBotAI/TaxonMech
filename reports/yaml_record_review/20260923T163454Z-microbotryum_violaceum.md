# YAML Record Review: Microbotryum violaceum

- Record: `data/taxa/eukaryota/microbotryum_violaceum.yaml`
- Reviewed: `2026-09-23T16:34:54Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:5272`
- Label: `Microbotryum violaceum`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:34416` (`Microbotryum`)

## Validation

- `just validate data/taxa/eukaryota/microbotryum_violaceum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microbotryum_saponariae.yaml data/taxa/eukaryota/microbotryum_silenes_acaulis.yaml data/taxa/eukaryota/microbotryum_silenes_dioicae.yaml data/taxa/eukaryota/microbotryum_violaceum.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2325` has the same identifier, label, species rank, `NCBITaxon:34416` parent, genetic code `1`, exact synonyms, related synonyms, and `gold` attestation copied into the YAML.
- The `Uredo violacea` and `Ustilago violacea` exact synonyms and three authority-bearing related synonyms match the NCBI row.
- The YAML lineage contains the expected 12 entries from `root` through `Microbotryum`.

## Evidence

- `data/seed_scope.tsv:51958` includes `NCBITaxon:5272` with reason `attested rule: Microbotryum violaceum, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:37972` reports GOLD organism count `15`, matching the YAML GOLD `assertion_count`.
- A complete exact scan of the native GOLD snapshot contains 16 exact organism rows and 16 project rows, beginning with legacy blank-strain `Go0004148` and continuing through the `1296`, `1253`, `1249`, `1247`, `1118`, and `Mv_1441` strains; a complete `AP PROJECT GOLD IDS` scan found 15 native analysis rows.
- A complete `rg --no-ignore --hidden` scan found three NCBI neotype rows at `data/raw/ncbi_type_material.tsv:228428-228430`, all for `GLM 50283` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero generated rows under `data/raw/strain_*`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:5272`; two StrainInfo related-record rows also target `NCBITaxon:5272`, but no generated raw strain rows were present for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:56381` maps side-inventory old ID `NCBITaxon:289079` into `NCBITaxon:5272`; no retained old-ID row was present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the three `GLM 50283` neotype spellings remain grouped as source aliases.
- If StrainInfo-only or StrainInfo-related records become eligible for strain generation, revisit the exact StrainInfo hit set and the two ATCC 48849 related-record rows for this taxon.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted `NCBITaxon:289079` old ID.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:5272`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
- GOLD aggregate rows can differ from local native exact rows; for `NCBITaxon:5272`, the generated aggregate count is `15`, while the exact native GOLD files currently contain 16 matching organism rows and 15 matching analysis rows.
