# YAML Record Review: Morchella brunnea

- Record: `data/taxa/eukaryota/morchella_brunnea.yaml`
- Reviewed: `2026-09-23T17:05:55Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1174671`
- Label: `Morchella brunnea`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:1051054` (`Morchella sect. Distantes`)

## Validation

- `just validate data/taxa/eukaryota/morchella_brunnea.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_anatolica.yaml data/taxa/eukaryota/morchella_angusticeps.yaml data/taxa/eukaryota/morchella_arbutiphila.yaml data/taxa/eukaryota/morchella_brunnea.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:260859` has the same identifier, label, species rank, `NCBITaxon:1051054` parent, genetic code `1`, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Morchella brunnea M. Kuo, 2012` and `Morchella sp. Mel-22` as related synonyms from NCBI.
- The YAML lineage contains the expected 14 entries from `root` through `Morchella sect. Distantes`.

## Evidence

- `curation/seed_scope.tsv:58192` includes `NCBITaxon:1174671` with reason `attested rule: Morchella brunnea, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:3861` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has two exact organism rows for `JGI 1270818` and `NRRL 20869`, three linked project rows, and no linked native analyses.
- A complete `rg --no-ignore --hidden` scan found two NCBI type-material rows at `data/raw/ncbi_type_material.tsv:11418-11419`, covering `OSC 138686` holotype aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has no exact direct or deposit rows for `NCBITaxon:1174671`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found old IDs `NCBITaxon:746145` and `NCBITaxon:746165` merging into `NCBITaxon:1174671`, while a complete exact scan found neither old ID retained in `data/raw/ncbitaxon_taxa.tsv`; no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1174671`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
