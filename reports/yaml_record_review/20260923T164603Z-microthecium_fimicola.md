# YAML Record Review: Microthecium fimicola

- Record: `data/taxa/eukaryota/microthecium_fimicola.yaml`
- Reviewed: `2026-09-23T16:46:03Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1661791`
- Label: `Microthecium fimicola`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:1646516` (`Microthecium`)

## Validation

- `just validate data/taxa/eukaryota/microthecium_fimicola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microthecium_fimicola.yaml data/taxa/eukaryota/microthyrium_microscopicum.yaml data/taxa/eukaryota/middelhovenomyces_tepae.yaml data/taxa/eukaryota/millerago_ficus.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:433957` has the same identifier, label, species rank, `NCBITaxon:1646516` parent, genetic code `1`, two exact synonyms, six related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves the `Melanospora` names as exact and related synonyms, and keeps the `Sphaerodes` names plus `Microthecium sp. YM-2015c` as related synonyms from NCBI.
- The YAML lineage contains the expected 16 entries from `root` through `Microthecium`.

## Evidence

- `curation/seed_scope.tsv:60998` includes `NCBITaxon:1661791` with reason `attested rule: Microthecium fimicola, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:14311` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has no exact organism/project/analysis rows for numeric NCBI taxon `1661791`; the committed GOLD attestation is therefore traceable only through the transformed GOLD aggregate inventory.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_type_material.tsv` rows for `NCBITaxon:1661791`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has one exact direct row and one exact deposit row for `NCBITaxon:1661791`, but no corresponding local strain inventory row is generated.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:18991` redirects `NCBITaxon:152777` into this taxon, but a complete `rg --no-ignore --hidden` scan found no retained old-ID row in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- On the next KG-Microbe GOLD refresh, re-check whether the transformed GOLD edge that produces the single aggregate row still exists for `NCBITaxon:1661791`, since the local native GOLD JSONL mirror has no exact organism row for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1661791`; type-material and side-inventory old-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
