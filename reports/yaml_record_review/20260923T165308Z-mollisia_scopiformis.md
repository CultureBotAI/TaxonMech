# YAML Record Review: Mollisia scopiformis

- Record: `data/taxa/eukaryota/mollisia_scopiformis.yaml`
- Reviewed: `2026-09-23T16:53:08Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:149040`
- Label: `Mollisia scopiformis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:86026` (`Mollisia`)

## Validation

- `just validate data/taxa/eukaryota/mollisia_scopiformis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/moelleriella_libera.yaml data/taxa/eukaryota/moesziomyces_antarcticus.yaml data/taxa/eukaryota/moesziomyces_aphidis.yaml data/taxa/eukaryota/mollisia_scopiformis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:30561` has the same identifier, label, species rank, `NCBITaxon:86026` parent, genetic code `1`, exact synonym, two related synonyms, and `gold` attestation copied into the YAML.
- The YAML keeps `Phialocephala scopiformis` as an exact synonym and preserves the `Mollisia` and `Phialocephala` authority strings as related synonyms from NCBI.
- The YAML lineage contains the expected 15 entries from `root` through `Mollisia`.

## Evidence

- `curation/seed_scope.tsv:54060` includes `NCBITaxon:149040` with reason `attested rule: Mollisia scopiformis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:11559` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot currently has exact organism rows for `CBS 120377` and `DAOMC 229536`, with ten linked project rows and two native GOLD analyses.
- A complete `rg --no-ignore --hidden` scan found two NCBI type-material rows at `data/raw/ncbi_type_material.tsv:35856-35857`, covering `CBS 468.94` aliases under the `Phialocephala scopiformis` type-material name.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has one exact direct row and three exact deposit rows for `NCBITaxon:149040`, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:149040`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- Reconcile the transformed GOLD aggregate count of 3 with the two exact native GOLD organism rows on the next GOLD refresh.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:149040`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
