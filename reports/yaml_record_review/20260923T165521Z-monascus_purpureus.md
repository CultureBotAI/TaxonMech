# YAML Record Review: Monascus purpureus

- Record: `data/taxa/eukaryota/monascus_purpureus.yaml`
- Reviewed: `2026-09-23T16:55:21Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:5098`
- Label: `Monascus purpureus`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:5097` (`Monascus`)

## Validation

- `just validate data/taxa/eukaryota/monascus_purpureus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mollisiaceae_sp_dmi_dod_qoi.yaml data/taxa/eukaryota/monascus_aurantiacus.yaml data/taxa/eukaryota/monascus_purpureus.yaml data/taxa/eukaryota/monascus_ruber.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2230` has the same identifier, label, species rank, `NCBITaxon:5097` parent, genetic code `1`, exact synonyms, related synonym, and `gold` attestation copied into the YAML.
- The YAML preserves all five NCBI exact synonyms, `Monascus albidus`, `Monascus anka`, `Monascus araneosus`, `Monascus purpurea`, and `Monascus rubiginosus`, plus the `Monascus purpureus Went, 1895` authority string as a related synonym.
- The YAML lineage contains the expected 15 entries from `root` through `Monascus`.

## Evidence

- `curation/seed_scope.tsv:51936` includes `NCBITaxon:5098` with reason `attested rule: Monascus purpureus, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:37485` reports GOLD organism count `5`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has five exact organism rows for `HQ1`, `P7048X-2`, `PF1702S`, `TNC21`, and `YY-1`, five linked project rows, and four linked native analyses.
- A complete `rg --no-ignore --hidden` scan found 30 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:225809-225838`, covering `Monascus araneosus`, `Monascus purpureus`, and `Monascus rubiginosus` designations.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has 100 exact direct rows and 219 exact deposit-bearing rows for `NCBITaxon:5098`, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found old IDs `NCBITaxon:184207`, `NCBITaxon:296184`, `NCBITaxon:46690`, and `NCBITaxon:64613` merging into `NCBITaxon:5098`, while a complete exact scan found none of those IDs retained in `data/raw/ncbitaxon_taxa.tsv`; no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:5098`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
