# YAML Record Review: Mitosporidium daphniae

- Record: `data/taxa/eukaryota/mitosporidium_daphniae.yaml`
- Reviewed: `2026-09-23T16:51:19Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1485682`
- Label: `Mitosporidium daphniae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:1633384` (`Mitosporidium`)

## Validation

- `just validate data/taxa/eukaryota/mitosporidium_daphniae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/minutocellus_polymorphus.yaml data/taxa/eukaryota/mitosporidium_daphniae.yaml data/taxa/eukaryota/mixia_osmundae.yaml data/taxa/eukaryota/modicella_reniformis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:380164` has the same identifier, label, species rank, `NCBITaxon:1633384` parent, genetic code `1`, three related synonyms, and `gold` attestation copied into the YAML.
- The YAML keeps `Microsporidia sp. JFP-2104`, `Microsporidia sp. UGP3`, and the `Mitosporidium daphniae` authority string as related synonyms from NCBI.
- The YAML lineage contains the expected 9 entries from `root` through `Mitosporidium`.

## Evidence

- `curation/seed_scope.tsv:60259` includes `NCBITaxon:1485682` with reason `attested rule: Mitosporidium daphniae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:11511` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project/analysis evidence for `Go0107713` / `UGP3` / `Gp0107713`.
- A complete `rg --no-ignore --hidden` scan found two NCBI reference-material rows at `data/raw/ncbi_type_material.tsv:35524-35525`, covering `UGP3` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact StrainInfo rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this microsporidian in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:1485682`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that both `UGP3` spellings remain grouped as reference-material aliases.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1485682`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
