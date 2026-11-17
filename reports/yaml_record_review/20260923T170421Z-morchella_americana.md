# YAML Record Review: Morchella americana

- Record: `data/taxa/eukaryota/morchella_americana.yaml`
- Reviewed: `2026-09-23T17:04:21Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1582323`
- Label: `Morchella americana`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:1175439` (`Morchella sect. Morchella`)

## Validation

- `just validate data/taxa/eukaryota/morchella_americana.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/monosporozyma_unispora.yaml data/taxa/eukaryota/monosporozyma_yasuniensis.yaml data/taxa/eukaryota/monticola_elongata.yaml data/taxa/eukaryota/morchella_americana.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:408391` has the same identifier, label, species rank, `NCBITaxon:1175439` parent, genetic code `1`, exact synonym, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Morchella esculentoides` as an exact synonym and the `Morchella americana`, `Morchella esculentoides`, and `Morchella sp. Mes-4` strings as related synonyms from NCBI.
- The YAML lineage contains the expected 14 entries from `root` through `Morchella sect. Morchella`.

## Evidence

- `curation/seed_scope.tsv:60527` includes `NCBITaxon:1582323` with reason `attested rule: Morchella americana, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:12779` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0535694` for `Morchella americana PhC 192`, two linked project rows, and no linked native analyses.
- A complete `rg --no-ignore --hidden` scan found six NCBI type-material rows at `data/raw/ncbi_type_material.tsv:44269-44274`, covering `LIP 0900091` and `PhC51` holotype aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has no exact direct or deposit rows for `NCBITaxon:1582323`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found old IDs `NCBITaxon:1175440`, `NCBITaxon:746179`, and `NCBITaxon:746194` merging into `NCBITaxon:1582323`, while a complete exact scan found none of those IDs retained in `data/raw/ncbitaxon_taxa.tsv`; no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1582323`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
