# YAML Record Review: Metschnikowia gelsemii

- Record: `data/taxa/eukaryota/metschnikowia_gelsemii.yaml`
- Reviewed: `2026-09-23T16:01:17Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:407270`
- Label: `Metschnikowia gelsemii`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_gelsemii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_drosophilae.yaml data/taxa/eukaryota/metschnikowia_gelsemii.yaml data/taxa/eukaryota/metschnikowia_gruessii.yaml data/taxa/eukaryota/metschnikowia_hamakuensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:88041` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, exact synonyms, related synonyms, and `gold` attestation copied into the YAML.
- The exact synonyms `Candida gelsemii` and `Metschnikowia gelsemii (M.A. Lachance) C.P. Kurtzman, C.J. Robnett & E. Basehoar, 2018` match the NCBI row.
- The five related Candida/Metschnikowia synonyms match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:55537` includes `NCBITaxon:407270` with reason `attested rule: Metschnikowia gelsemii, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:34652` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains an exact organism/project chain for `Go0705528` / `Gp0831571`.
- A complete `rg --no-ignore --hidden` scan found six NCBI type-material rows at `data/raw/ncbi_type_material.tsv:205144-205149`, covering `NRRL Y-48212` and `UWO(PS)06-24.1` / `UWOPS 06-24.1` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:76202` and `data/raw/ncbi_merged_ids.tsv:76222` map side-inventory old IDs `NCBITaxon:407269` and `NCBITaxon:408168` into `NCBITaxon:407270`; no retained old-ID rows were present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the six type-material spellings remain grouped as source aliases.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the two omitted old IDs.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:407270`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
