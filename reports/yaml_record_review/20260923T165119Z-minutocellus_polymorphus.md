# YAML Record Review: Minutocellus polymorphus

- Record: `data/taxa/eukaryota/minutocellus_polymorphus.yaml`
- Reviewed: `2026-09-23T16:51:19Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:265543`
- Label: `Minutocellus polymorphus`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:265542` (`Minutocellus`)

## Validation

- `just validate data/taxa/eukaryota/minutocellus_polymorphus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/minutocellus_polymorphus.yaml data/taxa/eukaryota/mitosporidium_daphniae.yaml data/taxa/eukaryota/mixia_osmundae.yaml data/taxa/eukaryota/modicella_reniformis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:54357` has the same identifier, label, species rank, `NCBITaxon:265542` parent, genetic code `1`, two exact synonyms, two related synonyms, and `gold` attestation copied into the YAML.
- The YAML keeps `Bellerochea polymorpha` and `Minutocellulus polymorphus` as exact synonyms and preserves the `Bellerochea` and `Minutocellus` authority strings as related synonyms from NCBI.
- The YAML lineage contains the expected 12 entries from `root` through `Minutocellus`.

## Evidence

- `curation/seed_scope.tsv:54882` includes `NCBITaxon:265543` with reason `attested rule: Minutocellus polymorphus, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:24372` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism rows for `CCMP 3303`, `NH13`, and `RCC 2270`; no native GOLD project or analysis rows are linked to those organism IDs.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_type_material.tsv` rows for `NCBITaxon:265543`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has exact rows for `NCBITaxon:265543` directly and in deposits, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this diatom in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:265543`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- Re-check GOLD project coverage if future native GOLD updates add projects for `Go0368746`, `Go0368747`, or `Go0368748`.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:265543`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
