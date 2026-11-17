# YAML Record Review: Moneuplotes crassus

- Record: `data/taxa/eukaryota/moneuplotes_crassus.yaml`
- Reviewed: `2026-09-23T16:57:02Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:5936`
- Label: `Moneuplotes crassus`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:152459` (`Moneuplotes`)

## Validation

- `just validate data/taxa/eukaryota/moneuplotes_crassus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/moneuplotes_crassus.yaml data/taxa/eukaryota/moniliella_acetoabutans.yaml data/taxa/eukaryota/moniliella_spathulata.yaml data/taxa/eukaryota/moniliella_suaveolens.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2622` has the same identifier, label, species rank, `NCBITaxon:152459` parent, ciliate genetic code `10`, exact synonym, related synonym, and `gold` attestation copied into the YAML.
- The YAML preserves `Euplotes crassus` as an exact synonym and `Moneuplotes crassus Dujardin, 1841` as a related synonym from NCBI.
- The YAML lineage contains the expected 12 entries from `root` through `Moneuplotes`.

## Evidence

- `curation/seed_scope.tsv:52112` includes `NCBITaxon:5936` with reason `attested rule: Moneuplotes crassus, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:39651` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0368749` for `Moneuplotes crassus CT5`, one linked project row, `Gp0236156`, and one linked native analysis.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:5936`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has no exact direct or deposit rows for `NCBITaxon:5936`.
- No auxiliary rows were found in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:5936`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:5936`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
