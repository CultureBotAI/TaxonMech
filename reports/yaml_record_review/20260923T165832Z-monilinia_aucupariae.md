# YAML Record Review: Monilinia aucupariae

- Record: `data/taxa/eukaryota/monilinia_aucupariae.yaml`
- Reviewed: `2026-09-23T16:58:32Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:61194`
- Label: `Monilinia aucupariae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:38447` (`Monilinia`)

## Validation

- `just validate data/taxa/eukaryota/monilinia_aucupariae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/monilinia_aucupariae.yaml data/taxa/eukaryota/monilinia_fructicola.yaml data/taxa/eukaryota/monilinia_fructigena.yaml data/taxa/eukaryota/monilinia_laxa.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:7766` has the same identifier, label, species rank, `NCBITaxon:38447` parent, genetic code `1`, exact synonym, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Sclerotinia aucupariae` as an exact synonym and the `Monilinia aucupariae` and `Sclerotinia aucupariae` authority strings as related synonyms from NCBI.
- The YAML lineage contains the expected 15 entries from `root` through `Monilinia`.

## Evidence

- `curation/seed_scope.tsv:53027` includes `NCBITaxon:61194` with reason `attested rule: Monilinia aucupariae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:39851` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0384660` for `Monilinia aucupariae LMK 733`, one linked project row, `Gp0235774`, and one linked native analysis.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:61194`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has one exact direct row and two exact deposit-bearing rows for `NCBITaxon:61194`, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:61194`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:61194`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
