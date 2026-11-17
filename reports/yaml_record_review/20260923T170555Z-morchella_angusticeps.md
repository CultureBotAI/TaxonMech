# YAML Record Review: Morchella angusticeps

- Record: `data/taxa/eukaryota/morchella_angusticeps.yaml`
- Reviewed: `2026-09-23T17:05:55Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:60347`
- Label: `Morchella angusticeps`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:1051054` (`Morchella sect. Distantes`)

## Validation

- `just validate data/taxa/eukaryota/morchella_angusticeps.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_anatolica.yaml data/taxa/eukaryota/morchella_angusticeps.yaml data/taxa/eukaryota/morchella_arbutiphila.yaml data/taxa/eukaryota/morchella_brunnea.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:7604` has the same identifier, label, species rank, `NCBITaxon:1051054` parent, genetic code `1`, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Morchella angusticeps Peck, 1879` and `Morchella sp. Mel-15` as related synonyms from NCBI.
- The YAML lineage contains the expected 14 entries from `root` through `Morchella sect. Distantes`.

## Evidence

- `curation/seed_scope.tsv:53021` includes `NCBITaxon:60347` with reason `attested rule: Morchella angusticeps, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:39785` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0513055` for `Morchella angusticeps NRRL 20909`, two linked project rows, and no linked native analyses.
- A complete `rg --no-ignore --hidden` scan found six NCBI type-material rows at `data/raw/ncbi_type_material.tsv:241100-241105`, covering `F 04090601` epitype aliases and `NYSF 268` holotype aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has eight exact direct rows and 11 exact deposit-bearing rows for `NCBITaxon:60347`, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found old IDs `NCBITaxon:746137` and `NCBITaxon:746157` merging into `NCBITaxon:60347`, while a complete exact scan found neither old ID retained in `data/raw/ncbitaxon_taxa.tsv`; no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:60347`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
