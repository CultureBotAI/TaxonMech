# YAML Record Review: Metschnikowia krissii

- Record: `data/taxa/eukaryota/metschnikowia_krissii.yaml`
- Reviewed: `2026-09-23T16:07:41Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:27324`
- Label: `Metschnikowia krissii`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_krissii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_krissii.yaml data/taxa/eukaryota/metschnikowia_kunwiensis.yaml data/taxa/eukaryota/metschnikowia_lachancei.yaml data/taxa/eukaryota/metschnikowia_lacustris.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2735` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, exact synonym, related synonyms, and `gold` attestation copied into the YAML.
- The exact synonym `Metschnikowiella krissii` and the two related Metschnikowia/Metschnikowiella authority strings match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:52152` includes `NCBITaxon:27324` with reason `attested rule: Metschnikowia krissii, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:25465` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains an exact organism/project chain for `Go0705573` / `NRRL Y-5389` and project `Gp0831617`.
- A complete `rg --no-ignore --hidden` scan found seven NCBI type-material rows at `data/raw/ncbi_type_material.tsv:115111-115117`, covering `NRRL Y-5389` and `CBS 4823` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:27324`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:27324`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the seven type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact StrainInfo hits for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:27324`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
