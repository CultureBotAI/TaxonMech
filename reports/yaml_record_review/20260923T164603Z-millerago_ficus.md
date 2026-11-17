# YAML Record Review: Millerago ficus

- Record: `data/taxa/eukaryota/millerago_ficus.yaml`
- Reviewed: `2026-09-23T16:46:03Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1176389`
- Label: `Millerago ficus`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:3379936` (`Millerago`)

## Validation

- `just validate data/taxa/eukaryota/millerago_ficus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microthecium_fimicola.yaml data/taxa/eukaryota/microthyrium_microscopicum.yaml data/taxa/eukaryota/middelhovenomyces_tepae.yaml data/taxa/eukaryota/millerago_ficus.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:261325` has the same identifier, label, species rank, `NCBITaxon:3379936` parent, genetic code `1`, exact synonym, three related synonyms, and `gold` attestation copied into the YAML.
- The YAML keeps `Candida ficus` as an exact synonym and preserves `Candida ficus`, `Candida sp. STN-8`, and the 2026 `Millerago ficus` authority string as related synonyms from NCBI.
- The YAML lineage contains the expected 13 entries from `root` through `Millerago`.

## Evidence

- `curation/seed_scope.tsv:58201` includes `NCBITaxon:1176389` with reason `attested rule: Millerago ficus, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:3896` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0705055` / `CBS 12638` / `Gp0831075`; no native GOLD analysis rows are linked to that project ID.
- A complete `rg --no-ignore --hidden` scan found seven NCBI type-material rows at `data/raw/ncbi_type_material.tsv:11573-11579`, covering `CICC 1980`, `CBS 12638`, and `STN 8` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact StrainInfo rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:1176389`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the seven `CICC 1980`, `CBS 12638`, and `STN 8` spellings remain grouped as source aliases.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1176389`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
