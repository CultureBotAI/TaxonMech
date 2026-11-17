# YAML Record Review: Monosporozyma yasuniensis

- Record: `data/taxa/eukaryota/monosporozyma_yasuniensis.yaml`
- Reviewed: `2026-09-23T17:04:21Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1468137`
- Label: `Monosporozyma yasuniensis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:3162981` (`Monosporozyma`)

## Validation

- `just validate data/taxa/eukaryota/monosporozyma_yasuniensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/monosporozyma_unispora.yaml data/taxa/eukaryota/monosporozyma_yasuniensis.yaml data/taxa/eukaryota/monticola_elongata.yaml data/taxa/eukaryota/morchella_americana.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:374951` has the same identifier, label, species rank, `NCBITaxon:3162981` parent, genetic code `1`, exact synonym, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Kazachstania yasuniensis` as an exact synonym and all six Kazachstania/Monosporozyma related synonyms from NCBI.
- The YAML lineage contains the expected 13 entries from `root` through `Monosporozyma`.

## Evidence

- `curation/seed_scope.tsv:60230` includes `NCBITaxon:1468137` with reason `attested rule: Monosporozyma yasuniensis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:11276` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0705087` for `Monosporozyma yasuniensis CBS 13946`, and one linked project row, `Gp0831108`; the local native snapshot has no linked analysis rows for this organism/project.
- A complete `rg --no-ignore --hidden` scan found six NCBI type-material rows at `data/raw/ncbi_type_material.tsv:33820-33825`, covering `CBS 13946`, `NCYC 4008`, and `CLQCA 20-132` aliases under the `Kazachstania yasuniensis` type-material name.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has no exact direct or deposit rows for `NCBITaxon:1468137`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found old IDs `NCBITaxon:1468138`, `NCBITaxon:1468139`, and `NCBITaxon:1571155` merging into `NCBITaxon:1468137`, while a complete exact scan found none of those IDs retained in `data/raw/ncbitaxon_taxa.tsv`; no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1468137`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
