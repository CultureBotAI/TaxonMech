# YAML Record Review: Monilinia laxa

- Record: `data/taxa/eukaryota/monilinia_laxa.yaml`
- Reviewed: `2026-09-23T16:58:32Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:61186`
- Label: `Monilinia laxa`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:38447` (`Monilinia`)

## Validation

- `just validate data/taxa/eukaryota/monilinia_laxa.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/monilinia_aucupariae.yaml data/taxa/eukaryota/monilinia_fructicola.yaml data/taxa/eukaryota/monilinia_fructigena.yaml data/taxa/eukaryota/monilinia_laxa.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:7765` has the same identifier, label, species rank, `NCBITaxon:38447` parent, genetic code `1`, exact synonyms, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Monilia laxa`, `Oidium laxum`, and `Sclerotinia laxa` as exact synonyms and their authority strings plus the `Monilinia laxa` authority string as related synonyms from NCBI.
- The YAML lineage contains the expected 15 entries from `root` through `Monilinia`.

## Evidence

- `curation/seed_scope.tsv:53026` includes `NCBITaxon:61186` with reason `attested rule: Monilinia laxa, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:39850` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has two exact organism rows for `8L` and `Mlax316`, two linked project rows, and two linked native analyses.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:61186`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has 48 exact direct rows and 52 exact deposit-bearing rows for `NCBITaxon:61186`, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:61186`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:61186`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
