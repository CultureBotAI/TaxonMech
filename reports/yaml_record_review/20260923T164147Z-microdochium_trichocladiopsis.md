# YAML Record Review: Microdochium trichocladiopsis

- Record: `data/taxa/eukaryota/microdochium_trichocladiopsis.yaml`
- Reviewed: `2026-09-23T16:41:47Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1682393`
- Label: `Microdochium trichocladiopsis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:67608` (`Microdochium`)

## Validation

- `just validate data/taxa/eukaryota/microdochium_trichocladiopsis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microcyclosporella_mali.yaml data/taxa/eukaryota/microdochium_bolleyi.yaml data/taxa/eukaryota/microdochium_trichocladiopsis.yaml data/taxa/eukaryota/micromonas_sp.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:439096` has the same identifier, label, species rank, `NCBITaxon:67608` parent, genetic code `1`, related synonym, and `gold` attestation copied into the YAML.
- The `Microdochium trichocladiopsis Hern.-Restr. & Crous, 2015` authority string is carried as a related synonym from NCBI.
- The YAML lineage contains the expected 16 entries from `root` through `Microdochium`.

## Evidence

- `curation/seed_scope.tsv:61017` includes `NCBITaxon:1682393` with reason `attested rule: Microdochium trichocladiopsis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:14504` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0358406` / `MPI-CAGE-CH-0230`, including projects `Gp0197047` and `Gp0197048`; no native GOLD analysis rows are linked to those project IDs.
- A complete `rg --no-ignore --hidden` scan found two NCBI type-material rows at `data/raw/ncbi_type_material.tsv:51940-51941`, covering `CBS 623.77` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact StrainInfo rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:1682393`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the two `CBS 623.77` spellings remain grouped as source aliases.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1682393`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
