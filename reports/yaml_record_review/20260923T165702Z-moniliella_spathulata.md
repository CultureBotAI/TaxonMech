# YAML Record Review: Moniliella spathulata

- Record: `data/taxa/eukaryota/moniliella_spathulata.yaml`
- Reviewed: `2026-09-23T16:57:02Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:64620`
- Label: `Moniliella spathulata`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:64607` (`Moniliella`)

## Validation

- `just validate data/taxa/eukaryota/moniliella_spathulata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/moneuplotes_crassus.yaml data/taxa/eukaryota/moniliella_acetoabutans.yaml data/taxa/eukaryota/moniliella_spathulata.yaml data/taxa/eukaryota/moniliella_suaveolens.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:8199` has the same identifier, label, species rank, `NCBITaxon:64607` parent, genetic code `1`, exact synonym, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Trichosporonoides spathulata` as an exact synonym and the `Moniliella spathulata` and `Trichosporonoides spathulata` authority strings as related synonyms from NCBI.
- The YAML lineage contains the expected 12 entries from `root` through `Moniliella`.

## Evidence

- `curation/seed_scope.tsv:53102` includes `NCBITaxon:64620` with reason `attested rule: Moniliella spathulata, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:40354` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- A bounded exact scan of the native GOLD JSONL snapshot found no exact organism, project, or analysis rows for NCBI taxon `64620`.
- A complete `rg --no-ignore --hidden` scan found two NCBI type-material rows at `data/raw/ncbi_type_material.tsv:244580-244581`, covering `CBS 241.79` aliases under the `Trichosporonoides spathulata` type-material name.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has three exact direct rows and seven exact deposit-bearing rows for `NCBITaxon:64620`, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:64620`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- Reconcile the transformed GOLD aggregate count of 3 with the absence of exact native GOLD organism rows on the next GOLD refresh.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:64620`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
