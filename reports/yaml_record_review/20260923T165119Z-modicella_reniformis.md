# YAML Record Review: Modicella reniformis

- Record: `data/taxa/eukaryota/modicella_reniformis.yaml`
- Reviewed: `2026-09-23T16:51:19Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1440133`
- Label: `Modicella reniformis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:1440132` (`Modicella`)

## Validation

- `just validate data/taxa/eukaryota/modicella_reniformis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/minutocellus_polymorphus.yaml data/taxa/eukaryota/mitosporidium_daphniae.yaml data/taxa/eukaryota/mixia_osmundae.yaml data/taxa/eukaryota/modicella_reniformis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:361325` has the same identifier, label, species rank, `NCBITaxon:1440132` parent, genetic code `1`, exact synonym, two related synonyms, and `gold` attestation copied into the YAML.
- The YAML keeps `Endogone reniformis` as an exact synonym and preserves the `Endogone` and `Modicella` authority strings as related synonyms from NCBI.
- The YAML lineage contains the expected 12 entries from `root` through `Modicella`.

## Evidence

- `curation/seed_scope.tsv:60141` includes `NCBITaxon:1440133` with reason `attested rule: Modicella reniformis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:10499` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0145909` / `F-58915` and `Go0145910` / `MES-2147`; no native GOLD analysis rows are linked to those project IDs.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_type_material.tsv` rows for `NCBITaxon:1440133`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact StrainInfo rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:1440133`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- Re-check GOLD project-to-analysis coverage if future native GOLD updates add analyses for `Gp0154270` or `Gp0154271`.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1440133`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
