# YAML Record Review: Metarhizium pingshaense

- Record: `data/taxa/eukaryota/metarhizium_pingshaense.yaml`
- Reviewed: `2026-09-23T15:40:44Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1278899`
- Label: `Metarhizium pingshaense`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:5529` (`Metarhizium`)

## Validation

- `just validate data/taxa/eukaryota/metarhizium_pingshaense.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metarhizium_pingshaense.yaml data/taxa/eukaryota/metarhizium_rileyi.yaml data/taxa/eukaryota/metarhizium_robertsii.yaml data/taxa/eukaryota/metarhizium_robertsii_arsef_23.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:298625` has the same identifier, label, species rank, `NCBITaxon:5529` parent, genetic code `1`, and `gold` attestation copied into the YAML.
- The exact synonym `Metarhizium pingshaense Q.T. Chen & H.L. Guo, 1986` matches the NCBI row; the row has no related synonyms.
- The YAML lineage contains the expected 16 entries from `root` through `Metarhizium`.

## Evidence

- `data/seed_scope.tsv:58868` includes `NCBITaxon:1278899` with reason `attested rule: Metarhizium pingshaense, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:6493` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- `data/raw/ncbi_type_material.tsv:18733-18734` has the two exact NCBI culture-from-type-material designations for `CBS 257.90` / `CBS:257.90`.
- The bounded scan found no exact native GOLD organism/project/analysis rows for this NCBI ID in the local `data/gold/*.jsonl.gz` snapshots.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:71268` maps side-inventory old ID `NCBITaxon:348618` into `NCBITaxon:1278899`; no retained old-ID row was present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the two `CBS 257.90` forms are treated as source aliases rather than independent strains.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted `NCBITaxon:348618` old ID.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1278899`.
