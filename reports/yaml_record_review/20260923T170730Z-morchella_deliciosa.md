# YAML Record Review: Morchella deliciosa

- Record: `data/taxa/eukaryota/morchella_deliciosa.yaml`
- Reviewed: `2026-09-23T17:07:30Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1579548`
- Label: `Morchella deliciosa`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:1051054` (`Morchella sect. Distantes`)

## Validation

- `just validate data/taxa/eukaryota/morchella_deliciosa.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_conifericola.yaml data/taxa/eukaryota/morchella_deliciosa.yaml data/taxa/eukaryota/morchella_diminutiva.yaml data/taxa/eukaryota/morchella_disparilis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:407149` has the same identifier, label, species rank, `NCBITaxon:1051054` parent, genetic code `1`, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Morchella deliciosa Fr., 1822` and `Morchella sp. Mel-26` as related synonyms from NCBI.
- The YAML lineage contains the expected 14 entries from `root` through `Morchella sect. Distantes`.

## Evidence

- `curation/seed_scope.tsv:60508` includes `NCBITaxon:1579548` with reason `attested rule: Morchella deliciosa, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:12738` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0535689` for `Morchella deliciosa PhC 191`, two linked project rows, and no linked native analyses.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:1579548`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has three exact direct rows and seven exact deposit-bearing rows for `NCBITaxon:1579548`, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found old ID `NCBITaxon:1009834` merging into `NCBITaxon:1579548`, while a complete exact scan found that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`; no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1579548`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
