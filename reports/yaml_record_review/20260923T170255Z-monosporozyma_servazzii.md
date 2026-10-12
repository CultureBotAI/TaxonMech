# YAML Record Review: Monosporozyma servazzii

- Record: `data/taxa/eukaryota/monosporozyma_servazzii.yaml`
- Reviewed: `2026-09-23T17:02:55Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:27293`
- Label: `Monosporozyma servazzii`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:3162981` (`Monosporozyma`)

## Validation

- `just validate data/taxa/eukaryota/monosporozyma_servazzii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/monosporozyma_aquatica.yaml data/taxa/eukaryota/monosporozyma_servazzii.yaml data/taxa/eukaryota/monosporozyma_siamensis.yaml data/taxa/eukaryota/monosporozyma_solicola.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2709` has the same identifier, label, species rank, `NCBITaxon:3162981` parent, genetic code `1`, exact synonyms, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Kazachstania servazzi`, `Kazachstania servazzii`, and `Saccharomyces servazzii` as exact synonyms and the `Monosporozyma servazzii` and `Saccharomyces servazzii` authority strings as related synonyms from NCBI.
- The YAML lineage contains the expected 13 entries from `root` through `Monosporozyma`.

## Evidence

- `curation/seed_scope.tsv:52133` includes `NCBITaxon:27293` with reason `attested rule: Monosporozyma servazzii, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:25396` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has three exact organism rows for `CBS 4311`, `NRRL Y-12661`, and `SRCM102023`, three linked project rows, and one linked native analysis.
- A complete `rg --no-ignore --hidden` scan found 18 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:114513-114530`, covering `Saccharomyces servazzii` culture-from-lectotype and type-material aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has 31 exact direct rows and 59 exact deposit-bearing rows for `NCBITaxon:27293`, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:27293`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:27293`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
