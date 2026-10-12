# YAML Record Review: Microchloropsis salina

- Record: `data/taxa/eukaryota/microchloropsis_salina.yaml`
- Reviewed: `2026-09-23T16:36:47Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:2511165`
- Label: `Microchloropsis salina`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:2511164` (`Microchloropsis`)

## Validation

- `just validate data/taxa/eukaryota/microchloropsis_salina.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microchloropsis_salina.yaml data/taxa/eukaryota/microconidiobolus_paulus.yaml data/taxa/eukaryota/microcyclospora_pomicola.yaml data/taxa/eukaryota/microcyclospora_tardicrescens.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:528758` has the same identifier, label, species rank, `NCBITaxon:2511164` parent, genetic code `1`, exact synonyms, related synonyms, and `gold` attestation copied into the YAML.
- The Nannochloropsis exact synonyms, CCMP369 related synonym, and Microchloropsis/Nannochloropsis authority strings match the NCBI row.
- The YAML lineage contains the expected ten entries from `root` through `Microchloropsis`.

## Evidence

- `data/seed_scope.tsv:62746` includes `NCBITaxon:2511165` with reason `attested rule: Microchloropsis salina, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:22851` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism evidence for `Go0038537` / blank strain and `Go0574320` / `CCMP1776`, with three exact project rows and two native analysis rows.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:2511165`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:2511165`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this algal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:44424` and `NCBITaxon:5749` into `NCBITaxon:2511165`; no retained old-ID rows were present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, recheck this record for newly supplied CCMP369 or Nannochloropsis type rows.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact StrainInfo hit set for this taxon.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the two omitted old IDs.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:2511165`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
- GOLD aggregate rows can differ from local native exact rows; for `NCBITaxon:2511165`, the generated aggregate count is `3`, while the exact native GOLD files currently contain two matching organism rows and three matching project rows.
