# YAML Record Review: Microbotryum silenes-acaulis

- Record: `data/taxa/eukaryota/microbotryum_silenes_acaulis.yaml`
- Reviewed: `2026-09-23T16:34:54Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:370302`
- Label: `Microbotryum silenes-acaulis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:34416` (`Microbotryum`)

## Validation

- `just validate data/taxa/eukaryota/microbotryum_silenes_acaulis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microbotryum_saponariae.yaml data/taxa/eukaryota/microbotryum_silenes_acaulis.yaml data/taxa/eukaryota/microbotryum_silenes_dioicae.yaml data/taxa/eukaryota/microbotryum_violaceum.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:77694` has the same identifier, label, species rank, `NCBITaxon:34416` parent, genetic code `1`, related synonyms, and `gold` attestation copied into the YAML.
- The `Microbotryum silenes-acaulis` authority string and `Microbotryum sp. MML-2006a` related synonym match the NCBI row.
- The YAML lineage contains the expected 12 entries from `root` through `Microbotryum`.

## Evidence

- `data/seed_scope.tsv:55383` includes `NCBITaxon:370302` with reason `attested rule: Microbotryum silenes-acaulis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:33566` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains two exact organism rows for strain `1248`, two project rows, and two analysis rows linked through `Gp0779021` and `Gp0779022`.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:370302`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact StrainInfo rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:370302`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, recheck this record for any newly supplied Silene acaulis type spellings.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:370302`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
