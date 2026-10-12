# YAML Record Review: Moniliophthora roreri

- Record: `data/taxa/eukaryota/moniliophthora_roreri.yaml`
- Reviewed: `2026-09-23T16:59:55Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:221103`
- Label: `Moniliophthora roreri`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:221102` (`Moniliophthora`)

## Validation

- `just validate data/taxa/eukaryota/moniliophthora_roreri.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/monilinia_vaccinii_corymbosi.yaml data/taxa/eukaryota/moniliophthora_perniciosa.yaml data/taxa/eukaryota/moniliophthora_roreri.yaml data/taxa/eukaryota/monocercomonoides_exilis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:43508` has the same identifier, label, species rank, `NCBITaxon:221102` parent, genetic code `1`, exact synonyms, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Crinipellis roreri` and `Monilia roreri` as exact synonyms and keeps their authority strings, the `Moniliophthora roreri` authority string, and `frosty pod rot of cocoa` as related synonyms from NCBI.
- The YAML lineage contains the expected 14 entries from `root` through `Moniliophthora`.

## Evidence

- `curation/seed_scope.tsv:54588` includes `NCBITaxon:221103` with reason `attested rule: Moniliophthora roreri, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:20983` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0119753` for `Moniliophthora roreri CBS 138632`, one linked project row, `Gp0126774`, and one linked native analysis.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:221103`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has 11 exact direct rows and 12 exact deposit-bearing rows for `NCBITaxon:221103`, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:221103`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:221103`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
