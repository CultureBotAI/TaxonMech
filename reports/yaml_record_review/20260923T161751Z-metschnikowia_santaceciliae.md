# YAML Record Review: Metschnikowia santaceciliae

- Record: `data/taxa/eukaryota/metschnikowia_santaceciliae.yaml`
- Reviewed: `2026-09-23T16:17:51Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:197674`
- Label: `Metschnikowia santaceciliae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_santaceciliae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_reukaufii.yaml data/taxa/eukaryota/metschnikowia_rubicola.yaml data/taxa/eukaryota/metschnikowia_santaceciliae.yaml data/taxa/eukaryota/metschnikowia_shivogae.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:39279` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonym, and `gold` attestation copied into the YAML.
- The related synonym `Metschnikowia santaceciliae Lachance, J.M. Bowles & Starmer, 2003` matches the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:54442` includes `NCBITaxon:197674` with reason `attested rule: Metschnikowia santaceciliae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:18279` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project/analysis chains for `UWOPS 01-142b1` and `UWOPS 01-517a1`: `Go0455141` / `Gp0323467` and `Go0455143` / `Gp0323469`.
- A complete `rg --no-ignore --hidden` scan found seven NCBI type-material rows at `data/raw/ncbi_type_material.tsv:76055-76061`, covering `CBS 9148`, `MUCL 46202`, and `UWO(PS) 01-517a1` / `UWOPS 01-517a1` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:197674`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:197674`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the seven type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact StrainInfo hits for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:197674`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
