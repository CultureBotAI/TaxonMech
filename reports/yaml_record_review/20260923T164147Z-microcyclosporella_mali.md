# YAML Record Review: Microcyclosporella mali

- Record: `data/taxa/eukaryota/microcyclosporella_mali.yaml`
- Reviewed: `2026-09-23T16:41:47Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:766057`
- Label: `Microcyclosporella mali`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:766052` (`Microcyclosporella`)

## Validation

- `just validate data/taxa/eukaryota/microcyclosporella_mali.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microcyclosporella_mali.yaml data/taxa/eukaryota/microdochium_bolleyi.yaml data/taxa/eukaryota/microdochium_trichocladiopsis.yaml data/taxa/eukaryota/micromonas_sp.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:177919` has the same identifier, label, species rank, `NCBITaxon:766052` parent, genetic code `1`, related synonym, and `gold` attestation copied into the YAML.
- The `Microcyclosporella mali J. Frank, Schroers & Crous, 2010` authority string is carried as a related synonym from NCBI.
- The YAML lineage contains the expected 16 entries from `root` through `Microcyclosporella`.

## Evidence

- `curation/seed_scope.tsv:56690` includes `NCBITaxon:766057` with reason `attested rule: Microcyclosporella mali, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:42557` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project/analysis evidence for `Go0449057` / `UMD1a` / `Gp0313459`.
- A complete `rg --no-ignore --hidden` scan found four NCBI type-material rows at `data/raw/ncbi_type_material.tsv:263302-263305`, covering `CBS 126136` and `CPC 16184` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact StrainInfo rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:766057`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the four `CBS 126136` and `CPC 16184` spellings remain grouped as source aliases.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:766057`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
