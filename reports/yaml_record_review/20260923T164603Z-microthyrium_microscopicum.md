# YAML Record Review: Microthyrium microscopicum

- Record: `data/taxa/eukaryota/microthyrium_microscopicum.yaml`
- Reviewed: `2026-09-23T16:46:03Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:703497`
- Label: `Microthyrium microscopicum`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:1037661` (`Microthyrium`)

## Validation

- `just validate data/taxa/eukaryota/microthyrium_microscopicum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microthecium_fimicola.yaml data/taxa/eukaryota/microthyrium_microscopicum.yaml data/taxa/eukaryota/middelhovenomyces_tepae.yaml data/taxa/eukaryota/millerago_ficus.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:165044` has the same identifier, label, species rank, `NCBITaxon:1037661` parent, genetic code `1`, two related synonyms, and `gold` attestation copied into the YAML.
- The two `Microthyrium microscopicum` authority strings are carried as related synonyms from NCBI.
- The YAML lineage contains the expected 16 entries from `root` through `Microthyrium`.

## Evidence

- `curation/seed_scope.tsv:56494` includes `NCBITaxon:703497` with reason `attested rule: Microthyrium microscopicum, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:41688` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0033175` / `CBS 115976`, including projects `Gp0033175` and `Gp0033176`; no native GOLD analysis rows are linked to those project IDs.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_type_material.tsv` rows for `NCBITaxon:703497`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact StrainInfo rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:703497`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- Re-check GOLD project-to-analysis coverage if future native GOLD updates add analyses for `Gp0033175` or `Gp0033176`.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:703497`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
