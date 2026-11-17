# YAML Record Review: Metschnikowia cubensis

- Record: `data/taxa/eukaryota/metschnikowia_cubensis.yaml`
- Reviewed: `2026-09-23T15:58:33Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1323754`
- Label: `Metschnikowia cubensis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_cubensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_corniflorae.yaml data/taxa/eukaryota/metschnikowia_cubensis.yaml data/taxa/eukaryota/metschnikowia_dekortorum.yaml data/taxa/eukaryota/metschnikowia_drakensbergensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:315400` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonyms, and `gold` attestation copied into the YAML.
- The two authority-form related synonyms and `Metschnikowia sp. MUCL45753` match the NCBI row; the row has no exact synonyms.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:59460` includes `NCBITaxon:1323754` with reason `attested rule: Metschnikowia cubensis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:7867` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project/analysis chains for `MUCL 45751` and `MUCL 45753`: `Go0455129` / `Gp0323455` and `Go0455130` / `Gp0323456`.
- A complete `rg --no-ignore --hidden` scan found nine NCBI type-material rows at `data/raw/ncbi_type_material.tsv:22409-22417`, covering `CBS 10832`, `CRGF 279`, `MUCL 45753`, and `NRRL Y-48696` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:80368` maps side-inventory old ID `NCBITaxon:473036` into `NCBITaxon:1323754`; no retained old-ID row was present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the nine type-material spellings remain grouped as source aliases.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted `NCBITaxon:473036` old ID.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1323754`; the type-material rows were additionally confirmed with a complete ignored-file-inclusive `rg --no-ignore --hidden` pass.
