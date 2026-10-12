# YAML Record Review: Monosporozyma unispora

- Record: `data/taxa/eukaryota/monosporozyma_unispora.yaml`
- Reviewed: `2026-09-23T17:04:21Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:27294`
- Label: `Monosporozyma unispora`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:3162981` (`Monosporozyma`)

## Validation

- `just validate data/taxa/eukaryota/monosporozyma_unispora.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/monosporozyma_unispora.yaml data/taxa/eukaryota/monosporozyma_yasuniensis.yaml data/taxa/eukaryota/monticola_elongata.yaml data/taxa/eukaryota/morchella_americana.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2710` has the same identifier, label, species rank, `NCBITaxon:3162981` parent, genetic code `1`, exact synonyms, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Kazachstania unispora`, `Saccharomyces unispora`, and `Saccharomyces unisporus` as exact synonyms and the three authority strings as related synonyms from NCBI.
- The YAML lineage contains the expected 13 entries from `root` through `Monosporozyma`.

## Evidence

- `curation/seed_scope.tsv:52134` includes `NCBITaxon:27294` with reason `attested rule: Monosporozyma unispora, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:25397` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has two exact organism rows for `NRRL Y-1556` and `SB-162`, two linked project rows, and two linked native analyses.
- A complete `rg --no-ignore --hidden` scan found 20 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:114531-114550`, covering `Saccharomyces unisporus` type-material aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has 33 exact direct rows and 89 exact deposit-bearing rows for `NCBITaxon:27294`, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found old ID `NCBITaxon:1337060` merging into `NCBITaxon:27294`, while a complete exact scan found that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`; no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:27294`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
