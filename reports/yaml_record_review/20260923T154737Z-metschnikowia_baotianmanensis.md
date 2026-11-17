# YAML Record Review: Metschnikowia baotianmanensis

- Record: `data/taxa/eukaryota/metschnikowia_baotianmanensis.yaml`
- Reviewed: `2026-09-23T15:47:37Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:2860400`
- Label: `Metschnikowia baotianmanensis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_baotianmanensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_anglica.yaml data/taxa/eukaryota/metschnikowia_arizonensis.yaml data/taxa/eukaryota/metschnikowia_australis.yaml data/taxa/eukaryota/metschnikowia_baotianmanensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:565512` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, and `gold` attestation copied into the YAML.
- The two related synonyms, `Metschnikowia baotianmanensis F.L. Hui & L.N. Huang, 2019` and `Metschnikowia sp. NYNU 15613`, match the NCBI row; the row has no exact synonyms.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:63324` includes `NCBITaxon:2860400` with reason `attested rule: Metschnikowia baotianmanensis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:27785` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains one exact organism/project pair for `Metschnikowia baotianmanensis CBS 15869`: `Go0705134` and `Gp0831157`; no linked native GOLD analysis row was found.
- A complete `rg --no-ignore --hidden` scan found 10 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:133244-133253`, covering `CBS 15869`, `CICC 33085`, and `NYNU 15613` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:26927` maps side-inventory old ID `NCBITaxon:1775915` into `NCBITaxon:2860400`; no retained old-ID row was present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the `CBS 15869`, `CICC 33085`, and `NYNU 15613` aliases stay grouped by source strain.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted `NCBITaxon:1775915` old ID.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:2860400`; the type-material rows were additionally confirmed with a complete ignored-file-inclusive `rg --no-ignore --hidden` pass.
