# YAML Record Review: Metschnikowia kamakouana

- Record: `data/taxa/eukaryota/metschnikowia_kamakouana.yaml`
- Reviewed: `2026-09-23T16:05:52Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:301367`
- Label: `Metschnikowia kamakouana`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_kamakouana.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_kamakouana.yaml data/taxa/eukaryota/metschnikowia_kipukae.yaml data/taxa/eukaryota/metschnikowia_kofuensis_nom_inval.yaml data/taxa/eukaryota/metschnikowia_koreensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:61445` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonym, and `gold` attestation copied into the YAML.
- The related synonym `Metschnikowia kamakouana Lachance, 2005` matches the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:55074` includes `NCBITaxon:301367` with reason `attested rule: Metschnikowia kamakouana, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:30149` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project/analysis chains for `UWOPS 04-112.5` and `UWOPS 04-206.1`: `Go0455153` / `Gp0323479` and `Go0455156` / `Gp0323482`.
- A complete `rg --no-ignore --hidden` scan found ten NCBI type-material rows at `data/raw/ncbi_type_material.tsv:155119-155128`, covering `CBS 10058`, `NRRL Y-27836`, and `UWO(PS) 04-112.5` / `UWOPS 04-112.5` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:301367`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:301367`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the ten type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact StrainInfo hits for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:301367`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
