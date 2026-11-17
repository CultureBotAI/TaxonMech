# YAML Record Review: Monascus aurantiacus

- Record: `data/taxa/eukaryota/monascus_aurantiacus.yaml`
- Reviewed: `2026-09-23T16:55:21Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:225353`
- Label: `Monascus aurantiacus`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:5097` (`Monascus`)

## Validation

- `just validate data/taxa/eukaryota/monascus_aurantiacus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mollisiaceae_sp_dmi_dod_qoi.yaml data/taxa/eukaryota/monascus_aurantiacus.yaml data/taxa/eukaryota/monascus_purpureus.yaml data/taxa/eukaryota/monascus_ruber.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:44204` has the same identifier, label, species rank, `NCBITaxon:5097` parent, genetic code `1`, related synonym, and `gold` attestation copied into the YAML.
- The YAML preserves `Monascus aurantiacus Zhong Q. Li, 1982` as an NCBI related synonym.
- The YAML lineage contains the expected 15 entries from `root` through `Monascus`.

## Evidence

- `curation/seed_scope.tsv:54619` includes `NCBITaxon:225353` with reason `attested rule: Monascus aurantiacus, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:21243` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0039936` for `Monascus aurantiacus AS3.4384`, and one linked project row, `Gp0039936`; the local native snapshot has no linked analysis rows for this organism/project.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:225353`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has one exact direct row and one exact deposit row for `NCBITaxon:225353`, but neither is represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:225353`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:225353`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
