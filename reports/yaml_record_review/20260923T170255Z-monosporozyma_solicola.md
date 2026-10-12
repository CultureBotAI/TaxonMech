# YAML Record Review: Monosporozyma solicola

- Record: `data/taxa/eukaryota/monosporozyma_solicola.yaml`
- Reviewed: `2026-09-23T17:02:55Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1089532`
- Label: `Monosporozyma solicola`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:3162981` (`Monosporozyma`)

## Validation

- `just validate data/taxa/eukaryota/monosporozyma_solicola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/monosporozyma_aquatica.yaml data/taxa/eukaryota/monosporozyma_servazzii.yaml data/taxa/eukaryota/monosporozyma_siamensis.yaml data/taxa/eukaryota/monosporozyma_solicola.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:234320` has the same identifier, label, species rank, `NCBITaxon:3162981` parent, genetic code `1`, exact synonym, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Kazachstania solicola` as an exact synonym and the `Kazachstania solicola`, `Kazachstania sp. CBS 6904`, and `Monosporozyma solicola` strings as related synonyms from NCBI.
- The YAML lineage contains the expected 13 entries from `root` through `Monosporozyma`.

## Evidence

- `curation/seed_scope.tsv:57577` includes `NCBITaxon:1089532` with reason `attested rule: Monosporozyma solicola, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:1645` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0517025` for `Kazachstania solicola NRRL Y-27207`, two linked project rows, and two linked native analyses.
- A complete `rg --no-ignore --hidden` scan found eight NCBI type-material rows at `data/raw/ncbi_type_material.tsv:5863-5870`, covering `CBS 6904`, `DBVPG 6357`, `IFO 10867`, and `NRRL Y-27207` aliases under the `Kazachstania solicola` type-material name.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has zero exact direct rows and two exact deposit rows for `NCBITaxon:1089532`, but neither is represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found old ID `NCBITaxon:271219` merging into `NCBITaxon:1089532`, while a complete exact scan found that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`; no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1089532`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
