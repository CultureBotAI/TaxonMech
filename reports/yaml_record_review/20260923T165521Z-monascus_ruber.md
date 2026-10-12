# YAML Record Review: Monascus ruber

- Record: `data/taxa/eukaryota/monascus_ruber.yaml`
- Reviewed: `2026-09-23T16:55:21Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:89489`
- Label: `Monascus ruber`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:5097` (`Monascus`)

## Validation

- `just validate data/taxa/eukaryota/monascus_ruber.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mollisiaceae_sp_dmi_dod_qoi.yaml data/taxa/eukaryota/monascus_aurantiacus.yaml data/taxa/eukaryota/monascus_purpureus.yaml data/taxa/eukaryota/monascus_ruber.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:14351` has the same identifier, label, species rank, `NCBITaxon:5097` parent, genetic code `1`, exact synonym, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Backusia terricola` as an exact synonym and the `Backusia terricola`, `Monascus ruber`, and `Monascus sp. ATCC 16433` authority strings as related synonyms from NCBI.
- The YAML lineage contains the expected 15 entries from `root` through `Monascus`.

## Evidence

- `curation/seed_scope.tsv:53478` includes `NCBITaxon:89489` with reason `attested rule: Monascus ruber, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:44061` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0384633` for `Monascus ruber CBS 127566`, one linked project row, `Gp0235744`, and one linked native analysis.
- A complete `rg --no-ignore --hidden` scan found six NCBI type-material rows at `data/raw/ncbi_type_material.tsv:271497-271502`, covering `Backusia terricola` and `Monascus ruber` designations.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has 91 exact direct rows and 170 exact deposit-bearing rows for `NCBITaxon:89489`, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found old ID `NCBITaxon:159235` merging into `NCBITaxon:89489`, while a complete exact scan found that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`; no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:89489`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
