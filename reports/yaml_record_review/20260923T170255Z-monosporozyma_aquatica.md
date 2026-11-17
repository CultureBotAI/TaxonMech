# YAML Record Review: Monosporozyma aquatica

- Record: `data/taxa/eukaryota/monosporozyma_aquatica.yaml`
- Reviewed: `2026-09-23T17:02:55Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:311204`
- Label: `Monosporozyma aquatica`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:3162981` (`Monosporozyma`)

## Validation

- `just validate data/taxa/eukaryota/monosporozyma_aquatica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/monosporozyma_aquatica.yaml data/taxa/eukaryota/monosporozyma_servazzii.yaml data/taxa/eukaryota/monosporozyma_siamensis.yaml data/taxa/eukaryota/monosporozyma_solicola.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:63716` has the same identifier, label, species rank, `NCBITaxon:3162981` parent, genetic code `1`, exact synonym, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Kazachstania aquatica` as an exact synonym and the `Kazachstania aquatica` and `Monosporozyma aquatica` authority strings as related synonyms from NCBI.
- The YAML lineage contains the expected 13 entries from `root` through `Monosporozyma`.

## Evidence

- `curation/seed_scope.tsv:55132` includes `NCBITaxon:311204` with reason `attested rule: Monosporozyma aquatica, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:31408` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0705518` for `Monosporozyma aquatica NRRL Y-27993`, and one linked project row, `Gp0831561`; the local native snapshot has no linked analysis rows for this organism/project.
- A complete `rg --no-ignore --hidden` scan found 11 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:168167-168177`, covering `AS 2.0706`, `CBS 10102`, `CGMCC 2.0706`, and `NRRL Y-27993` aliases under the `Kazachstania aquatica` type-material name.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has one exact direct row and three exact deposit rows for `NCBITaxon:311204`, but it is not represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:311204`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:311204`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
