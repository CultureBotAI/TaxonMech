# YAML Record Review: Metarhizium rileyi

- Record: `data/taxa/eukaryota/metarhizium_rileyi.yaml`
- Reviewed: `2026-09-23T15:40:44Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1649241`
- Label: `Metarhizium rileyi`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:5529` (`Metarhizium`)

## Validation

- `just validate data/taxa/eukaryota/metarhizium_rileyi.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metarhizium_pingshaense.yaml data/taxa/eukaryota/metarhizium_rileyi.yaml data/taxa/eukaryota/metarhizium_robertsii.yaml data/taxa/eukaryota/metarhizium_robertsii_arsef_23.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:431017` has the same identifier, label, species rank, `NCBITaxon:5529` parent, genetic code `1`, and `gold` attestation copied into the YAML.
- The four exact synonyms and six related synonyms in the YAML match the NCBI row, including the `Beauveria`, `Botrytis`, `Nomuraea`, and `Spicaria` name forms.
- The YAML lineage contains the expected 16 entries from `root` through `Metarhizium`.

## Evidence

- `data/seed_scope.tsv:60956` includes `NCBITaxon:1649241` with reason `attested rule: Metarhizium rileyi, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:14161` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains one exact organism/project/analysis chain for `Metarhizium rileyi Cep018-CH2`: `Go0632157`, `Gp0645980`, and AP name `Metarhizium rileyi Cep018-CH2`.
- The bounded scan found no NCBI type-material rows for this NCBI ID.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:1081105` and `NCBITaxon:43344` into `NCBITaxon:1649241`; no retained old-ID row was present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future GOLD-to-strain joins start emitting non-BacDive organisms, check whether `Go0632157` should become a concrete `Cep018-CH2` strain or remain aggregate evidence only.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted `NCBITaxon:1081105` and `NCBITaxon:43344` old IDs.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1649241`.
