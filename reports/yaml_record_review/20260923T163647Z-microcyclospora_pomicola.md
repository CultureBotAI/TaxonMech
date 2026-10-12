# YAML Record Review: Microcyclospora pomicola

- Record: `data/taxa/eukaryota/microcyclospora_pomicola.yaml`
- Reviewed: `2026-09-23T16:36:47Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:766055`
- Label: `Microcyclospora pomicola`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:766053` (`Microcyclospora`)

## Validation

- `just validate data/taxa/eukaryota/microcyclospora_pomicola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microchloropsis_salina.yaml data/taxa/eukaryota/microconidiobolus_paulus.yaml data/taxa/eukaryota/microcyclospora_pomicola.yaml data/taxa/eukaryota/microcyclospora_tardicrescens.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:177917` has the same identifier, label, species rank, `NCBITaxon:766053` parent, genetic code `1`, empty synonym fields, and `gold` attestation copied into the YAML.
- The YAML lineage contains the expected 16 entries from `root` through `Microcyclospora`.

## Evidence

- `data/seed_scope.tsv:56688` includes `NCBITaxon:766055` with reason `attested rule: Microcyclospora pomicola, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:42555` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project/analysis evidence for `Go0449056` / `SP1-49Fa` / `Gp0313458`.
- A complete `rg --no-ignore --hidden` scan found two NCBI type-material rows at `data/raw/ncbi_type_material.tsv:263298-263299`, covering `CBS 126141` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact StrainInfo rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:766055`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the two `CBS 126141` spellings remain grouped as source aliases.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:766055`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
