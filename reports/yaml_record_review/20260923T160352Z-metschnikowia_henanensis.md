# YAML Record Review: Metschnikowia henanensis

- Record: `data/taxa/eukaryota/metschnikowia_henanensis.yaml`
- Reviewed: `2026-09-23T16:03:52Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:2201244`
- Label: `Metschnikowia henanensis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_henanensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_hawaiiana.yaml data/taxa/eukaryota/metschnikowia_hawaiiensis.yaml data/taxa/eukaryota/metschnikowia_henanensis.yaml data/taxa/eukaryota/metschnikowia_hibisci.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:521299` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonyms, and `gold` attestation copied into the YAML.
- The two spelling variants of the `Metschnikowia henanensis` authority and the provisional `Metschnikowia sp. BY-97` related synonym match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:62474` includes `NCBITaxon:2201244` with reason `attested rule: Metschnikowia henanensis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:20900` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains an exact organism/project chain for `Go0705061` / `CBS 12677` and project `Gp0831081`.
- A complete `rg --no-ignore --hidden` scan found six NCBI type-material rows at `data/raw/ncbi_type_material.tsv:87716-87721`, covering `BY-97`, `CBS 12677`, and `CICC 1982` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:7815` maps side-inventory old ID `NCBITaxon:1208021` into `NCBITaxon:2201244`; no retained old-ID rows were present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the six type-material spellings remain grouped as source aliases.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted old ID.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:2201244`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
