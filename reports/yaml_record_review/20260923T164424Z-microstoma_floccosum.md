# YAML Record Review: Microstoma floccosum

- Record: `data/taxa/eukaryota/microstoma_floccosum.yaml`
- Reviewed: `2026-09-23T16:44:24Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:61491`
- Label: `Microstoma floccosum`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:47221` (`Microstoma`)

## Validation

- `just validate data/taxa/eukaryota/microstoma_floccosum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microscypha_sp.yaml data/taxa/eukaryota/microsporum_canis.yaml data/taxa/eukaryota/microstoma_floccosum.yaml data/taxa/eukaryota/microstroma_glucosiphilum.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:7793` has the same identifier, label, species rank, `NCBITaxon:47221` parent, genetic code `1`, exact synonym, two related synonyms, and `gold` attestation copied into the YAML.
- The YAML keeps `Sarcoscypha floccosa` as an exact synonym and both authority strings as related synonyms, matching the NCBI source row.
- The YAML lineage contains the expected 13 entries from `root` through `Microstoma`.

## Evidence

- `curation/seed_scope.tsv:53040` includes `NCBITaxon:61491` with reason `attested rule: Microstoma floccosum, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:39878` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has no exact organism/project/analysis rows for numeric NCBI taxon `61491`; the committed GOLD attestation is therefore traceable only through the transformed GOLD aggregate inventory.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_type_material.tsv` rows for `NCBITaxon:61491`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has one exact direct row and one exact deposit row for `NCBITaxon:61491`, but no corresponding local strain inventory row is generated.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:61491`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- On the next KG-Microbe GOLD refresh, re-check whether the transformed GOLD edge that produces the single aggregate row still exists for `NCBITaxon:61491`, since the local native GOLD JSONL mirror has no exact organism row for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:61491`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
