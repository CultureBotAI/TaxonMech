# YAML Record Review: Monilinia fructicola

- Record: `data/taxa/eukaryota/monilinia_fructicola.yaml`
- Reviewed: `2026-09-23T16:58:32Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:38448`
- Label: `Monilinia fructicola`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:38447` (`Monilinia`)

## Validation

- `just validate data/taxa/eukaryota/monilinia_fructicola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/monilinia_aucupariae.yaml data/taxa/eukaryota/monilinia_fructicola.yaml data/taxa/eukaryota/monilinia_fructigena.yaml data/taxa/eukaryota/monilinia_laxa.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:4378` has the same identifier, label, species rank, `NCBITaxon:38447` parent, genetic code `1`, exact synonyms, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Ciboria fructicola` and `Monilia fructicola` as exact synonyms and the `Ciboria`, `Monilia`, and `Monilinia` authority strings as related synonyms from NCBI.
- The YAML lineage contains the expected 15 entries from `root` through `Monilinia`.

## Evidence

- `curation/seed_scope.tsv:52390` includes `NCBITaxon:38448` with reason `attested rule: Monilinia fructicola, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:33978` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has three exact organism rows for `CPMC6`, `LMK 125`, and `Mfrc123`, three linked project rows, and three linked native analyses.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:38448`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has 53 exact direct rows and 57 exact deposit-bearing rows for `NCBITaxon:38448`, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:38448`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:38448`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
