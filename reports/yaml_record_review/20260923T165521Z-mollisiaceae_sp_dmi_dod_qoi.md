# YAML Record Review: Mollisiaceae sp. DMI_Dod_QoI

- Record: `data/taxa/eukaryota/mollisiaceae_sp_dmi_dod_qoi.yaml`
- Reviewed: `2026-09-23T16:55:21Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:2728926`
- Label: `Mollisiaceae sp. DMI_Dod_QoI`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:2755576` (`unclassified Mollisiaceae`)

## Validation

- `just validate data/taxa/eukaryota/mollisiaceae_sp_dmi_dod_qoi.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mollisiaceae_sp_dmi_dod_qoi.yaml data/taxa/eukaryota/monascus_aurantiacus.yaml data/taxa/eukaryota/monascus_purpureus.yaml data/taxa/eukaryota/monascus_ruber.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:548030` has the same identifier, label, species rank, `NCBITaxon:2755576` parent, genetic code `1`, and `gold` attestation copied into the YAML.
- The record has no NCBI synonyms in either the YAML or source row.
- The YAML lineage contains the expected 15 entries from `root` through `unclassified Mollisiaceae`.

## Evidence

- `curation/seed_scope.tsv:63000` includes `NCBITaxon:2728926` with reason `attested rule: Mollisiaceae sp. DMI_Dod_QoI, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:25381` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0632092` for `Helotiales sp. DMI_Dod_QoI`, one linked project row, `Gp0645913`, and one linked native analysis.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:2728926`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has no exact direct or deposit rows for `NCBITaxon:2728926`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:2728926`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:2728926`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
