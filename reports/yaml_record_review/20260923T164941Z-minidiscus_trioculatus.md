# YAML Record Review: Minidiscus trioculatus

- Record: `data/taxa/eukaryota/minidiscus_trioculatus.yaml`
- Reviewed: `2026-09-23T16:49:41Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:265540`
- Label: `Minidiscus trioculatus`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:265539` (`Minidiscus`)

## Validation

- `just validate data/taxa/eukaryota/minidiscus_trioculatus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/millerozyma_pseudofarinosa.yaml data/taxa/eukaryota/minidiscus_trioculatus.yaml data/taxa/eukaryota/minutisphaera_aspera.yaml data/taxa/eukaryota/minutisphaera_parafimbriatispora.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:54355` has the same identifier, label, species rank, `NCBITaxon:265539` parent, genetic code `1`, exact synonym, two related synonyms, and `gold` attestation copied into the YAML.
- The YAML keeps `Coscinodiscus trioculatus` as an exact synonym and preserves the `Coscinodiscus` and `Minidiscus` authority strings as related synonyms from NCBI.
- The YAML lineage contains the expected 12 entries from `root` through `Minidiscus`.

## Evidence

- `curation/seed_scope.tsv:54881` includes `NCBITaxon:265540` with reason `attested rule: Minidiscus trioculatus, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:24371` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has no exact organism/project/analysis rows for numeric NCBI taxon `265540`; the committed GOLD attestation is therefore traceable only through the transformed GOLD aggregate inventory.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_type_material.tsv` rows for `NCBITaxon:265540`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has exact rows for `NCBITaxon:265540` directly and in deposits, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this diatom in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:265540`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- On the next KG-Microbe GOLD refresh, re-check whether the transformed GOLD edge that produces the single aggregate row still exists for `NCBITaxon:265540`, since the local native GOLD JSONL mirror has no exact organism row for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:265540`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
