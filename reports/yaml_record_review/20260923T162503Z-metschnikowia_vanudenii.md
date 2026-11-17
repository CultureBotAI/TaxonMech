# YAML Record Review: Metschnikowia vanudenii

- Record: `data/taxa/eukaryota/metschnikowia_vanudenii.yaml`
- Reviewed: `2026-09-23T16:25:03Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:299329`
- Label: `Metschnikowia vanudenii`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_vanudenii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_torresii.yaml data/taxa/eukaryota/metschnikowia_vanudenii.yaml data/taxa/eukaryota/metschnikowia_viticola.yaml data/taxa/eukaryota/metschnikowia_zobellii.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:60948` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonym, and `gold` attestation copied into the YAML.
- The `Metschnikowia vanudenii` authority string matches the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:55064` includes `NCBITaxon:299329` with reason `attested rule: Metschnikowia vanudenii, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:29996` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0705254` / `NRRL Y-17036` and `Gp0831289`; no native analysis rows join through that project.
- A complete `rg --no-ignore --hidden` scan found 11 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:153566-153576`, covering `CBS 9134`, `IGC 4650`, `NRRL Y-17036`, and `PYCC 4650` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact StrainInfo rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:299329`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the 11 type-material spellings remain grouped as source aliases.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:299329`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
