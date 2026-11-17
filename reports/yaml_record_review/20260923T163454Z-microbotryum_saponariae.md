# YAML Record Review: Microbotryum saponariae

- Record: `data/taxa/eukaryota/microbotryum_saponariae.yaml`
- Reviewed: `2026-09-23T16:34:54Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:289078`
- Label: `Microbotryum saponariae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:34416` (`Microbotryum`)

## Validation

- `just validate data/taxa/eukaryota/microbotryum_saponariae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microbotryum_saponariae.yaml data/taxa/eukaryota/microbotryum_silenes_acaulis.yaml data/taxa/eukaryota/microbotryum_silenes_dioicae.yaml data/taxa/eukaryota/microbotryum_violaceum.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:58996` has the same identifier, label, species rank, `NCBITaxon:34416` parent, genetic code `1`, related synonym, and `gold` attestation copied into the YAML.
- The `Microbotryum saponariae` authority string matches the NCBI row.
- The YAML lineage contains the expected 12 entries from `root` through `Microbotryum`.

## Evidence

- `data/seed_scope.tsv:55011` includes `NCBITaxon:289078` with reason `attested rule: Microbotryum saponariae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:28168` reports GOLD organism count `4`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project/analysis evidence for `1269 A2`, `1268 A1`, `MsaSof1`, and `MsaSof2`.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:289078`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- One exact StrainInfo direct/deposit row exists for `NCBITaxon:289078`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay row is expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:289078`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, recheck this record for any newly supplied Saponariae holotype spellings.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact `DSM 27121` StrainInfo deposit for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:289078`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
