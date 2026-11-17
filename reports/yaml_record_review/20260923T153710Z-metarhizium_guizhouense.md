# YAML Record Review: Metarhizium guizhouense

- Record: `data/taxa/eukaryota/metarhizium_guizhouense.yaml`
- Reviewed: `2026-09-23T15:37:10Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:169041`
- Label: `Metarhizium guizhouense`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:5529` (`Metarhizium`)

## Validation

- `just validate data/taxa/eukaryota/metarhizium_guizhouense.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metarhizium_guizhouense.yaml data/taxa/eukaryota/metarhizium_humberi.yaml data/taxa/eukaryota/metarhizium_hybridum.yaml data/taxa/eukaryota/metarhizium_majus.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:34537` has the same identifier, label, species rank, `NCBITaxon:5529` parent, genetic code `1`, and `gold` attestation copied into the YAML.
- The three exact synonyms, `Cordyceps taii`, `Metacordyceps taii`, and `Metarhizium taii`, and the related authority synonym `Metarhizium guizhouense Q.T. Chen & H.L. Guo, 1986` match the NCBI row.
- The YAML lineage contains the expected 16 entries from `root` through `Metarhizium`.

## Evidence

- `data/seed_scope.tsv:54246` includes `NCBITaxon:169041` with reason `attested rule: Metarhizium guizhouense, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:14592` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- `data/raw/ncbi_type_material.tsv:52583-52584` has the two exact NCBI type-material designations for `CBS 258.90` / `CBS:258.90`.
- The bounded scan found no exact native GOLD organism/project/analysis rows for this NCBI ID in the local `data/gold/*.jsonl.gz` snapshots.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:71269` maps side-inventory old ID `NCBITaxon:348619` into `NCBITaxon:169041`; no retained old-ID row was present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the two `CBS 258.90` forms are either normalized together or intentionally preserved as source aliases.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted `NCBITaxon:348619` old ID.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:169041`.
