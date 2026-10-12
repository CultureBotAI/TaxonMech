# YAML Record Review: Morchella arbutiphila

- Record: `data/taxa/eukaryota/morchella_arbutiphila.yaml`
- Reviewed: `2026-09-23T17:05:55Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1810715`
- Label: `Morchella arbutiphila`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:1051054` (`Morchella sect. Distantes`)

## Validation

- `just validate data/taxa/eukaryota/morchella_arbutiphila.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_anatolica.yaml data/taxa/eukaryota/morchella_angusticeps.yaml data/taxa/eukaryota/morchella_arbutiphila.yaml data/taxa/eukaryota/morchella_brunnea.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:473442` has the same identifier, label, species rank, `NCBITaxon:1051054` parent, genetic code `1`, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Morchella arbutiphila Loizides, Bellanger & P.-A. Moreau, 2016`, `Morchella sp. Mel-30`, and `Morchella sp. PAM-2016a` as related synonyms from NCBI.
- The YAML lineage contains the expected 14 entries from `root` through `Morchella sect. Distantes`.

## Evidence

- `curation/seed_scope.tsv:61301` includes `NCBITaxon:1810715` with reason `attested rule: Morchella arbutiphila, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:16001` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0535692` for `Morchella arbutiphila PhC 291`, two linked project rows, and no linked native analyses.
- A complete `rg --no-ignore --hidden` scan found five NCBI type-material rows at `data/raw/ncbi_type_material.tsv:61394-61398`, covering `LIP 0000366` holotype aliases and `10-IV-2015` type-material designations.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has no exact direct or deposit rows for `NCBITaxon:1810715`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found old ID `NCBITaxon:1009837` merging into `NCBITaxon:1810715`, while a complete exact scan found that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`; no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1810715`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
