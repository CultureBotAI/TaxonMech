# YAML Record Review: Microconidiobolus paulus

- Record: `data/taxa/eukaryota/microconidiobolus_paulus.yaml`
- Reviewed: `2026-09-23T16:36:47Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1342296`
- Label: `Microconidiobolus paulus`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:2878382` (`Microconidiobolus`)

## Validation

- `just validate data/taxa/eukaryota/microconidiobolus_paulus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microchloropsis_salina.yaml data/taxa/eukaryota/microconidiobolus_paulus.yaml data/taxa/eukaryota/microcyclospora_pomicola.yaml data/taxa/eukaryota/microcyclospora_tardicrescens.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:322565` has the same identifier, label, species rank, `NCBITaxon:2878382` parent, genetic code `1`, exact synonyms, related synonyms, and `gold` attestation copied into the YAML.
- The `Conidiobolus paulus` and `Conidiobolus undulatus` exact synonyms and authority strings match the NCBI row.
- The YAML lineage contains the expected 12 entries from `root` through `Microconidiobolus`.

## Evidence

- `data/seed_scope.tsv:59571` includes `NCBITaxon:1342296` with reason `attested rule: Microconidiobolus paulus, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:8344` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0527568` / `ARSEF 450` and `Gp0455903`; no native analysis rows join through that project.
- A complete `rg --no-ignore --hidden` scan found six NCBI type-material rows at `data/raw/ncbi_type_material.tsv:24213-24218`, covering `ARSEF 450`, `ATCC 12942`, and `CBS 140.57` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:1342296`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:13741` maps side-inventory old ID `NCBITaxon:1368621` into `NCBITaxon:1342296`; no retained old-ID row was present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the six Conidiobolus type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact StrainInfo hit set for this taxon.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted `NCBITaxon:1368621` old ID.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1342296`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
