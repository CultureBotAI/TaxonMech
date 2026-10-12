# YAML Record Review: Morchella diminutiva

- Record: `data/taxa/eukaryota/morchella_diminutiva.yaml`
- Reviewed: `2026-09-23T17:07:30Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1174667`
- Label: `Morchella diminutiva`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:1175439` (`Morchella sect. Morchella`)

## Validation

- `just validate data/taxa/eukaryota/morchella_diminutiva.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_conifericola.yaml data/taxa/eukaryota/morchella_deliciosa.yaml data/taxa/eukaryota/morchella_diminutiva.yaml data/taxa/eukaryota/morchella_disparilis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:260856` has the same identifier, label, species rank, `NCBITaxon:1175439` parent, genetic code `1`, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Morchella diminutiva M. Kuo, Dewsbury, Moncalvo & S.L. Stephenson 2012` and `Morchella sp. Mes-2` as related synonyms from NCBI.
- The YAML lineage contains the expected 14 entries from `root` through `Morchella sect. Morchella`.

## Evidence

- `curation/seed_scope.tsv:58189` includes `NCBITaxon:1174667` with reason `attested rule: Morchella diminutiva, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:3858` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0513056` for `Morchella diminutiva NRRL 26603`, two linked project rows, and no linked native analyses.
- A complete `rg --no-ignore --hidden` scan found four NCBI type-material rows at `data/raw/ncbi_type_material.tsv:11404-11407`, covering `F 05030404` holotype aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has no exact direct or deposit rows for `NCBITaxon:1174667`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found old IDs `NCBITaxon:746177` and `NCBITaxon:746192` merging into `NCBITaxon:1174667`, while a complete exact scan found neither old ID retained in `data/raw/ncbitaxon_taxa.tsv`; no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1174667`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
