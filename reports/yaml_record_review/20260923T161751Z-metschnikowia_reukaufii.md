# YAML Record Review: Metschnikowia reukaufii

- Record: `data/taxa/eukaryota/metschnikowia_reukaufii.yaml`
- Reviewed: `2026-09-23T16:17:51Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:27327`
- Label: `Metschnikowia reukaufii`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_reukaufii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_reukaufii.yaml data/taxa/eukaryota/metschnikowia_rubicola.yaml data/taxa/eukaryota/metschnikowia_santaceciliae.yaml data/taxa/eukaryota/metschnikowia_shivogae.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2738` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, exact synonyms, related synonyms, and `gold` attestation copied into the YAML.
- The three exact synonyms and four related synonyms for Anthomyces/Candida/Metschnikowia/Nectaromyces names match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:52155` includes `NCBITaxon:27327` with reason `attested rule: Metschnikowia reukaufii, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:25474` reports GOLD organism count `106`, matching the YAML GOLD `assertion_count`.
- A complete exact scan of the native GOLD snapshot contains 105 exact organism rows and 831 project rows for this taxon, with rows beginning at `Go0119167` / `MR1` and then transcriptome-heavy `CY*` and `MY*` strain series; a complete `AP PROJECT GOLD IDS` scan found one analysis row for project `Gp0443541`.
- A complete `rg --no-ignore --hidden` scan found 17 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:115246-115262`, covering `ATCC 18407`, `CBS 5834`, `DBVPG 6185`, `IFO 1679`, `IGC 4446`, `JCM 7534`, `NRRL Y-7112`, and `UCD 62-311` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:27327`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:27327`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the 17 type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the large exact StrainInfo hit set for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:27327`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
- GOLD aggregate rows can differ from local native exact rows; for `NCBITaxon:27327`, the generated aggregate count is `106`, while the exact native GOLD files currently contain 105 matching organism rows.
