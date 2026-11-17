# YAML Record Review: Metschnikowia laotica

- Record: `data/taxa/eukaryota/metschnikowia_laotica.yaml`
- Reviewed: `2026-09-23T16:09:33Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:2201245`
- Label: `Metschnikowia laotica`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_laotica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_laotica.yaml data/taxa/eukaryota/metschnikowia_lochheadii.yaml data/taxa/eukaryota/metschnikowia_lopburiensis_nom_inval.yaml data/taxa/eukaryota/metschnikowia_lunata.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:521300` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonyms, and `gold` attestation copied into the YAML.
- The related synonyms `Metschnikowia laotica Sipiczki, 2014` and `Metschnikowia sp. 11-524` match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:62475` includes `NCBITaxon:2201245` with reason `attested rule: Metschnikowia laotica, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:20901` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains an exact organism/project chain for `Go0705069` / `CBS 12961` and project `Gp0831090`.
- A complete `rg --no-ignore --hidden` scan found three NCBI type-material rows at `data/raw/ncbi_type_material.tsv:87722-87724`, covering `11-524` and `CBS 12961` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:8629` maps side-inventory old ID `NCBITaxon:1227370` into `NCBITaxon:2201245`; no retained old-ID rows were present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the three type-material spellings remain grouped as source aliases.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted old ID.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:2201245`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
