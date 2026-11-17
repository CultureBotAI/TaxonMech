# YAML Record Review: Metarhizium hybridum

- Record: `data/taxa/eukaryota/metarhizium_hybridum.yaml`
- Reviewed: `2026-09-23T15:37:10Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:3151832`
- Label: `Metarhizium hybridum`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:5529` (`Metarhizium`)

## Validation

- `just validate data/taxa/eukaryota/metarhizium_hybridum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metarhizium_guizhouense.yaml data/taxa/eukaryota/metarhizium_humberi.yaml data/taxa/eukaryota/metarhizium_hybridum.yaml data/taxa/eukaryota/metarhizium_majus.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:607173` has the same identifier, label, species rank, `NCBITaxon:5529` parent, genetic code `1`, and `gold` attestation copied into the YAML.
- The three related synonyms, `Metarhizium anisopliae ARSEF 549`, `Metarhizium hybridum Kobmoo, Mongkols. & Khons., 2024`, and `Metarhizium sp. NK-2024a`, match the NCBI row; the row has no exact synonyms.
- The YAML lineage contains the expected 16 entries from `root` through `Metarhizium`.

## Evidence

- `data/seed_scope.tsv:63583` includes `NCBITaxon:3151832` with reason `attested rule: Metarhizium hybridum, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:31778` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- `data/raw/ncbi_type_material.tsv:173048-173055` has the eight expected ARSEF 549 culture-from-holotype and BBH 50656 holotype spellings.
- The bounded scan found no exact native GOLD organism/project/analysis rows for this NCBI ID in the local `data/gold/*.jsonl.gz` snapshots.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:10524` maps side-inventory old ID `NCBITaxon:1276135` into `NCBITaxon:3151832`; no retained old-ID row was present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the four ARSEF 549 and four BBH 50656 spellings are collapsed or represented as aliases for two source designations.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted `NCBITaxon:1276135` old ID.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:3151832`.
