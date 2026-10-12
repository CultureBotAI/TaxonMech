# YAML Record Review: Moniliella acetoabutans

- Record: `data/taxa/eukaryota/moniliella_acetoabutans.yaml`
- Reviewed: `2026-09-23T16:57:02Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1117156`
- Label: `Moniliella acetoabutans`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:64607` (`Moniliella`)

## Validation

- `just validate data/taxa/eukaryota/moniliella_acetoabutans.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/moneuplotes_crassus.yaml data/taxa/eukaryota/moniliella_acetoabutans.yaml data/taxa/eukaryota/moniliella_spathulata.yaml data/taxa/eukaryota/moniliella_suaveolens.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:241047` has the same identifier, label, species rank, `NCBITaxon:64607` parent, genetic code `1`, exact synonym, and `gold` attestation copied into the YAML.
- The YAML preserves `Moniliella acetoabutans Stolk & Dakin, 1966` as an exact synonym from NCBI.
- The YAML lineage contains the expected 12 entries from `root` through `Moniliella`.

## Evidence

- `curation/seed_scope.tsv:57707` includes `NCBITaxon:1117156` with reason `attested rule: Moniliella acetoabutans, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:2094` reports GOLD organism count `5`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has five exact organism rows for strains `ATCC 18455`, `CBS 169.66`, `CMI 159918`, `DSM 3551`, and `IMI 159918`; this local native snapshot has no linked project or analysis rows for those five organism IDs.
- A complete `rg --no-ignore --hidden` scan found 12 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:7077-7088`, covering the `CBS H-7346` holotype plus `ATCC 18455`, `CBS 169.66`, `DSM 3551`, `IMI 159918`, and `MUCL 7981` type-material aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has nine exact direct rows and 23 exact deposit-bearing rows for `NCBITaxon:1117156`, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found old ID `NCBITaxon:173229` merging into `NCBITaxon:1117156`, while a complete exact scan found that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`; no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- Reconcile the five exact native GOLD organism rows without linked project rows on the next GOLD refresh.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1117156`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
