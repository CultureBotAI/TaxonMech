# YAML Record Review: Morchella conifericola

- Record: `data/taxa/eukaryota/morchella_conifericola.yaml`
- Reviewed: `2026-09-23T17:07:30Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:2548439`
- Label: `Morchella conifericola`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:1051054` (`Morchella sect. Distantes`)

## Validation

- `just validate data/taxa/eukaryota/morchella_conifericola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_conifericola.yaml data/taxa/eukaryota/morchella_deliciosa.yaml data/taxa/eukaryota/morchella_diminutiva.yaml data/taxa/eukaryota/morchella_disparilis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:530104` has the same identifier, label, species rank, `NCBITaxon:1051054` parent, genetic code `1`, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Morchella conifericola Taskin, Buyukalaca & H.H. Dogan, 2016` and `Morchella sp. Mel-32` as related synonyms from NCBI.
- The YAML lineage contains the expected 14 entries from `root` through `Morchella sect. Distantes`.

## Evidence

- `curation/seed_scope.tsv:62776` includes `NCBITaxon:2548439` with reason `attested rule: Morchella conifericola, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:23184` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0513050` for `Morchella conifericola NRRL 54605`, two linked project rows, and no linked native analyses.
- A complete `rg --no-ignore --hidden` scan found three NCBI type-material rows at `data/raw/ncbi_type_material.tsv:100788-100790`, covering `ANK Taskin 110` and `Taskin 477` holotype aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has no exact direct or deposit rows for `NCBITaxon:2548439`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found old ID `NCBITaxon:1105048` merging into `NCBITaxon:2548439`, while a complete exact scan found that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`; no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:2548439`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
