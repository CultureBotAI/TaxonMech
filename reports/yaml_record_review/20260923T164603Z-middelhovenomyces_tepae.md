# YAML Record Review: Middelhovenomyces tepae

- Record: `data/taxa/eukaryota/middelhovenomyces_tepae.yaml`
- Reviewed: `2026-09-23T16:46:03Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:45597`
- Label: `Middelhovenomyces tepae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:1540074` (`Middelhovenomyces`)

## Validation

- `just validate data/taxa/eukaryota/middelhovenomyces_tepae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microthecium_fimicola.yaml data/taxa/eukaryota/microthyrium_microscopicum.yaml data/taxa/eukaryota/middelhovenomyces_tepae.yaml data/taxa/eukaryota/millerago_ficus.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:5633` has the same identifier, label, species rank, `NCBITaxon:1540074` parent, genetic code `1`, exact synonym, two related synonyms, and `gold` attestation copied into the YAML.
- The YAML keeps `Candida tepae` as an exact synonym and preserves both authority strings as related synonyms from NCBI.
- The YAML lineage contains the expected 13 entries from `root` through `Middelhovenomyces`.

## Evidence

- `curation/seed_scope.tsv:52679` includes `NCBITaxon:45597` with reason `attested rule: Middelhovenomyces tepae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:36088` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project/analysis evidence for `Go0517053` / `NRRL Y-17670` / `Gp0441091`.
- A complete `rg --no-ignore --hidden` scan found 11 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:215660-215670`, covering `ATCC 22979`, `CBS 5115`, `IFO 10316`, `JCM 10265`, and `NRRL Y-17670` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has exact rows for `NCBITaxon:45597` directly and in deposits, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:45597`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the 11 `ATCC`, `CBS`, `IFO`, `JCM`, and `NRRL` spellings remain grouped as source aliases.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:45597`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
