# YAML Record Review: Microbotryum silenes-dioicae

- Record: `data/taxa/eukaryota/microbotryum_silenes_dioicae.yaml`
- Reviewed: `2026-09-23T16:34:54Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:796604`
- Label: `Microbotryum silenes-dioicae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:34416` (`Microbotryum`)

## Validation

- `just validate data/taxa/eukaryota/microbotryum_silenes_dioicae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microbotryum_saponariae.yaml data/taxa/eukaryota/microbotryum_silenes_acaulis.yaml data/taxa/eukaryota/microbotryum_silenes_dioicae.yaml data/taxa/eukaryota/microbotryum_violaceum.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:179752` has the same identifier, label, species rank, `NCBITaxon:34416` parent, genetic code `1`, related synonym, and `gold` attestation copied into the YAML.
- The `Microbotryum silenes-dioicae` authority string matches the NCBI row.
- The YAML lineage contains the expected 12 entries from `root` through `Microbotryum`.

## Evidence

- `data/seed_scope.tsv:56714` includes `NCBITaxon:796604` with reason `attested rule: Microbotryum silenes-dioicae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:42819` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project/analysis evidence for `MsdSdi1` and `1303`.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:796604`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact StrainInfo rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:796604`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, recheck this record for any newly supplied Silene dioica type spellings.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:796604`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
