# YAML Record Review: Metschnikowia kunwiensis

- Record: `data/taxa/eukaryota/metschnikowia_kunwiensis.yaml`
- Reviewed: `2026-09-23T16:07:41Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:279289`
- Label: `Metschnikowia kunwiensis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_kunwiensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_krissii.yaml data/taxa/eukaryota/metschnikowia_kunwiensis.yaml data/taxa/eukaryota/metschnikowia_lachancei.yaml data/taxa/eukaryota/metschnikowia_lacustris.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:56805` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, exact synonym, related synonym, and `gold` attestation copied into the YAML.
- The exact synonym `Candida kunwiensis` and the related synonym `Metschnikowia kunwiensis Brysch-Herzberg, 2004` match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:54947` includes `NCBITaxon:279289` with reason `attested rule: Metschnikowia kunwiensis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:26639` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains an exact organism/project chain for `Go0705550` / `NRRL Y-48698` and project `Gp0831593`.
- A complete `rg --no-ignore --hidden` scan found 11 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:122378-122388`, covering `CBS 9676`, `MH275`, and `NRRL Y-48698` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:279289`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:279289`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the 11 type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact StrainInfo hits for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:279289`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
