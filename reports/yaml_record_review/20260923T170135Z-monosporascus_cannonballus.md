# YAML Record Review: Monosporascus cannonballus

- Record: `data/taxa/eukaryota/monosporascus_cannonballus.yaml`
- Reviewed: `2026-09-23T17:01:35Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:155416`
- Label: `Monosporascus cannonballus`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:155415` (`Monosporascus`)

## Validation

- `just validate data/taxa/eukaryota/monosporascus_cannonballus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/monosiga_ovata.yaml data/taxa/eukaryota/monosporascus_cannonballus.yaml data/taxa/eukaryota/monosporascus_ibericus.yaml data/taxa/eukaryota/monosporozyma_aerobia.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:32223` has the same identifier, label, species rank, `NCBITaxon:155415` parent, genetic code `1`, related synonym, and `gold` attestation copied into the YAML.
- The YAML preserves `Monosporascus cannonballus Pollack & Uecker, 1974` as a related synonym from NCBI.
- The YAML lineage contains the expected 16 entries from `root` through `Monosporascus`.

## Evidence

- `curation/seed_scope.tsv:54111` includes `NCBITaxon:155416` with reason `attested rule: Monosporascus cannonballus, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:12441` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has two exact organism rows for `CBS 586.93` and `CBS 609.92`, two linked project rows, and two linked native analyses.
- A complete `rg --no-ignore --hidden` scan found four NCBI type-material rows at `data/raw/ncbi_type_material.tsv:42078-42081`, covering `ATCC 26931` and `CBS 609.92` culture-from-type-material aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has five exact direct rows and eight exact deposit-bearing rows for `NCBITaxon:155416`, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:155416`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:155416`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
