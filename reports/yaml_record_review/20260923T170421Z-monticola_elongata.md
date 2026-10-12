# YAML Record Review: Monticola elongata

- Record: `data/taxa/eukaryota/monticola_elongata.yaml`
- Reviewed: `2026-09-23T17:04:21Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1508191`
- Label: `Monticola elongata`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:1508190` (`Monticola`)

## Validation

- `just validate data/taxa/eukaryota/monticola_elongata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/monosporozyma_unispora.yaml data/taxa/eukaryota/monosporozyma_yasuniensis.yaml data/taxa/eukaryota/monticola_elongata.yaml data/taxa/eukaryota/morchella_americana.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:387390` has the same identifier, label, species rank, `NCBITaxon:1508190` parent, genetic code `1`, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Dothideomycetes sp. CCFEE 5394`, `Monticola elongata Selbmann & Egidi, 2014`, and `Teratosphaeriaceae sp. CCFEE 5499` as related synonyms from NCBI.
- The YAML lineage contains the expected 16 entries from `root` through `Monticola`.

## Evidence

- `curation/seed_scope.tsv:60375` includes `NCBITaxon:1508191` with reason `attested rule: Monticola elongata, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:11869` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0583371` for `Monticola elongata CCFEE 5394`, two linked project rows, and no linked native analyses.
- A complete `rg --no-ignore --hidden` scan found four NCBI type-material rows at `data/raw/ncbi_type_material.tsv:37871-37874`, covering `CCFEE 5394` culture-from-holotype aliases and `CBS 136206` holotype aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has no exact direct or deposit rows for `NCBITaxon:1508191`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found old IDs `NCBITaxon:1507826` and `NCBITaxon:702007` merging into `NCBITaxon:1508191`, while a complete exact scan found neither old ID retained in `data/raw/ncbitaxon_taxa.tsv`; no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1508191`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
