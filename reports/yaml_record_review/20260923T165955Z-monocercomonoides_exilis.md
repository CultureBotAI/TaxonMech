# YAML Record Review: Monocercomonoides exilis

- Record: `data/taxa/eukaryota/monocercomonoides_exilis.yaml`
- Reviewed: `2026-09-23T16:59:55Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:2049356`
- Label: `Monocercomonoides exilis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:302781` (`Monocercomonoides`)

## Validation

- `just validate data/taxa/eukaryota/monocercomonoides_exilis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/monilinia_vaccinii_corymbosi.yaml data/taxa/eukaryota/moniliophthora_perniciosa.yaml data/taxa/eukaryota/moniliophthora_roreri.yaml data/taxa/eukaryota/monocercomonoides_exilis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:513837` has the same identifier, label, species rank, `NCBITaxon:302781` parent, genetic code `1`, exact synonym, related synonym, and `gold` attestation copied into the YAML.
- The YAML preserves `Monocercomonoides sp. PA203` as an exact synonym and `Monocercomonoides exilis Nie, 1950` as a related synonym from NCBI.
- The YAML lineage contains the expected eight entries from `root` through `Monocercomonoides`.

## Evidence

- `curation/seed_scope.tsv:62191` includes `NCBITaxon:2049356` with reason `attested rule: Monocercomonoides exilis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:19510` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0144318` for `Monocercomonoides exilis PA203`, one linked project row, `Gp0149919`, and one linked native analysis.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:2049356`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has no exact direct or deposit rows for `NCBITaxon:2049356`.
- No auxiliary rows were found in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found old ID `NCBITaxon:453998` merging into `NCBITaxon:2049356`, while a complete exact scan found that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`; no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:2049356`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
