# YAML Record Review: Moelleriella libera

- Record: `data/taxa/eukaryota/moelleriella_libera.yaml`
- Reviewed: `2026-09-23T16:53:08Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:324773`
- Label: `Moelleriella libera`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:511189` (`Moelleriella`)

## Validation

- `just validate data/taxa/eukaryota/moelleriella_libera.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/moelleriella_libera.yaml data/taxa/eukaryota/moesziomyces_antarcticus.yaml data/taxa/eukaryota/moesziomyces_aphidis.yaml data/taxa/eukaryota/mollisia_scopiformis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:66307` has the same identifier, label, species rank, `NCBITaxon:511189` parent, genetic code `1`, two exact synonyms, two related synonyms, and `gold` attestation copied into the YAML.
- The YAML keeps `Aschersonia aleyrodis` and `Hypocrella libera` as exact synonyms and preserves both `Hypocrella` and `Moelleriella` authority strings as related synonyms from NCBI.
- The YAML lineage contains the expected 16 entries from `root` through `Moelleriella`.

## Evidence

- `curation/seed_scope.tsv:55211` includes `NCBITaxon:324773` with reason `attested rule: Moelleriella libera, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:32132` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has no exact organism/project/analysis rows for numeric NCBI taxon `324773`; the committed GOLD attestation is therefore traceable only through the transformed GOLD aggregate inventory.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_type_material.tsv` rows for `NCBITaxon:324773`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has exact rows for `NCBITaxon:324773` directly and in deposits, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:38511` redirects `NCBITaxon:217359` into this taxon, but a complete `rg --no-ignore --hidden` scan found no retained old-ID row in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- On the next KG-Microbe GOLD refresh, re-check whether the transformed GOLD edge that produces the single aggregate row still exists for `NCBITaxon:324773`, since the local native GOLD JSONL mirror has no exact organism row for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:324773`; type-material and side-inventory old-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
