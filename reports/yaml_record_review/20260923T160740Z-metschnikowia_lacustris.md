# YAML Record Review: Metschnikowia lacustris

- Record: `data/taxa/eukaryota/metschnikowia_lacustris.yaml`
- Reviewed: `2026-09-23T16:07:41Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:2654411`
- Label: `Metschnikowia lacustris`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_lacustris.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_krissii.yaml data/taxa/eukaryota/metschnikowia_kunwiensis.yaml data/taxa/eukaryota/metschnikowia_lachancei.yaml data/taxa/eukaryota/metschnikowia_lacustris.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:540770` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonyms, and `gold` attestation copied into the YAML.
- The related synonyms `Metschnikowia lacustris Lachance, 2020` and `Metschnikowia sp. UWOPS 12.619.2` match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:62918` includes `NCBITaxon:2654411` with reason `attested rule: Metschnikowia lacustris, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:24342` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains an exact organism/project/analysis chain for `Go0683047` / `UWOPS 12.619.2` and project `Gp0785155`.
- A complete `rg --no-ignore --hidden` scan found four NCBI type-material rows at `data/raw/ncbi_type_material.tsv:107397-107400`, covering `UWOPS 12-619.2` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:70248` maps side-inventory old ID `NCBITaxon:3416516` into `NCBITaxon:2654411`; no retained old-ID rows were present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the four type-material spellings remain grouped as source aliases.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted old ID.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:2654411`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
