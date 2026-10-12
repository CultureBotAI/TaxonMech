# YAML Record Review: Metschnikowia bicuspidata var. chathamia

- Record: `data/taxa/eukaryota/metschnikowia_bicuspidata_var_chathamia.yaml`
- Reviewed: `2026-09-23T15:51:47Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:278771`
- Label: `Metschnikowia bicuspidata var. chathamia`
- Rank/domain: `VARIETAS` / `EUKARYOTA`
- Parent: `NCBITaxon:27322` (`Metschnikowia bicuspidata`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_bicuspidata_var_chathamia.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_bicuspidata.yaml data/taxa/eukaryota/metschnikowia_bicuspidata_var_bicuspidata_nrrl_yb_4993.yaml data/taxa/eukaryota/metschnikowia_bicuspidata_var_californica.yaml data/taxa/eukaryota/metschnikowia_bicuspidata_var_chathamia.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:56731` has the same identifier, label, variety rank, `NCBITaxon:27322` parent, genetic code `12`, and `gold` attestation copied into the YAML.
- The related synonym `Metschnikowia bicuspidata var. chathamia Fell & J.I. Pitt, 1969` matches the NCBI row; the row has no exact synonyms.
- The YAML lineage contains the expected 14 entries from `root` through parent species `Metschnikowia bicuspidata`.

## Evidence

- `data/seed_scope.tsv:54941` includes `NCBITaxon:278771` with reason `attested rule: Metschnikowia bicuspidata var. chathamia, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:26567` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains one exact organism/project pair for `Metschnikowia bicuspidata var. chathamia NRRL Y-17917`: `Go0705366` and `Gp0831403`; no linked native GOLD analysis row was found.
- A complete `rg --no-ignore --hidden` scan found 11 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:121956-121966`, covering `ATCC 22300`, `CBS 5980`, `IGC 4972`, `NRRL Y-17917`, and `UCD 67-2` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:38929` maps side-inventory old ID `NCBITaxon:2201243` into `NCBITaxon:278771`; no retained old-ID row was present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the 11 accession spellings remain grouped as source aliases and do not inflate `strain_count`.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted `NCBITaxon:2201243` old ID.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:278771`; the type-material rows were additionally confirmed with a complete ignored-file-inclusive `rg --no-ignore --hidden` pass.
