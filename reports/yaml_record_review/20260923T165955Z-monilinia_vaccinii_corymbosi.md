# YAML Record Review: Monilinia vaccinii-corymbosi

- Record: `data/taxa/eukaryota/monilinia_vaccinii_corymbosi.yaml`
- Reviewed: `2026-09-23T16:59:55Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:61207`
- Label: `Monilinia vaccinii-corymbosi`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:38447` (`Monilinia`)

## Validation

- `just validate data/taxa/eukaryota/monilinia_vaccinii_corymbosi.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/monilinia_vaccinii_corymbosi.yaml data/taxa/eukaryota/moniliophthora_perniciosa.yaml data/taxa/eukaryota/moniliophthora_roreri.yaml data/taxa/eukaryota/monocercomonoides_exilis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:7767` has the same identifier, label, species rank, `NCBITaxon:38447` parent, genetic code `1`, exact synonyms, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Monilia vaccinii-corymbosi` and `Sclerotinia vaccinii-corymbosi` as exact synonyms and their authority strings plus the `Monilinia vaccinii-corymbosi` authority string as related synonyms from NCBI.
- The YAML lineage contains the expected 15 entries from `root` through `Monilinia`.

## Evidence

- `curation/seed_scope.tsv:53028` includes `NCBITaxon:61207` with reason `attested rule: Monilinia vaccinii-corymbosi, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:39853` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0631617` for `Monilinia vaccinii-corymbosi RL-1`, one linked project row, `Gp0645148`, and one linked native analysis.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:61207`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has four exact direct rows and four exact deposit-bearing rows for `NCBITaxon:61207`, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:61207`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:61207`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
