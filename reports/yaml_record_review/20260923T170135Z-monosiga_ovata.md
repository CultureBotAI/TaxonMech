# YAML Record Review: Monosiga ovata

- Record: `data/taxa/eukaryota/monosiga_ovata.yaml`
- Reviewed: `2026-09-23T17:01:35Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:81526`
- Label: `Monosiga ovata`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:81525` (`Monosiga`)

## Validation

- `just validate data/taxa/eukaryota/monosiga_ovata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/monosiga_ovata.yaml data/taxa/eukaryota/monosporascus_cannonballus.yaml data/taxa/eukaryota/monosporascus_ibericus.yaml data/taxa/eukaryota/monosporozyma_aerobia.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:12270` has the same identifier, label, species rank, `NCBITaxon:81525` parent, genetic code `1`, related synonym, and `gold` attestation copied into the YAML.
- The YAML preserves `Monosiga ovata Kent` as a related synonym from NCBI.
- The YAML lineage contains the expected eight entries from `root` through `Monosiga`.

## Evidence

- `curation/seed_scope.tsv:53368` includes `NCBITaxon:81526` with reason `attested rule: Monosiga ovata, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:42949` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has two exact organism rows, `Go0002871` for `Monosiga ovata` and `Go0008018` for `Monosiga ovata 2A4`, plus two linked project rows and no linked native analyses.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:81526`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has one exact direct row and one exact deposit row for `NCBITaxon:81526`, but it is not represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:81526`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- Reconcile the transformed GOLD aggregate count of 1 with the two exact native GOLD organism rows on the next GOLD refresh.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:81526`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
