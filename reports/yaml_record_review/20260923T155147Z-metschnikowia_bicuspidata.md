# YAML Record Review: Metschnikowia bicuspidata

- Record: `data/taxa/eukaryota/metschnikowia_bicuspidata.yaml`
- Reviewed: `2026-09-23T15:51:47Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:27322`
- Label: `Metschnikowia bicuspidata`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_bicuspidata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_bicuspidata.yaml data/taxa/eukaryota/metschnikowia_bicuspidata_var_bicuspidata_nrrl_yb_4993.yaml data/taxa/eukaryota/metschnikowia_bicuspidata_var_californica.yaml data/taxa/eukaryota/metschnikowia_bicuspidata_var_chathamia.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2733` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, `Monospora bicuspidata` exact synonym, related synonyms, and `gold` attestation copied into the YAML.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.
- The direct-descendant exclusion note is appropriate because `Metschnikowia bicuspidata var. californica`, `var. chathamia`, and `var. bicuspidata NRRL YB-4993` are seeded as exact descendant records outside this direct species count.

## Evidence

- `data/seed_scope.tsv:52150` includes `NCBITaxon:27322` with reason `attested rule: Metschnikowia bicuspidata, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:25462` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- Exact native GOLD extraction found three local organisms, 10 linked projects, and two analysis rows filed under exact NCBI taxon `27322`; the projects cover `Go0005934`, `Go0072273`, and `Go0111683`.
- `data/raw/ncbi_type_material.tsv:115089-115092` has four `Monospora bicuspidata` culture-from-type-material rows covering `CBS 5575` and `NRRL YB-4993` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:56423` and `NCBITaxon:58629` into `NCBITaxon:27322`; no retained old-ID row was present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future descendant aggregation becomes desired, keep the `var. californica`, `var. chathamia`, and `NRRL YB-4993` child records separate from this direct species count to avoid double counting.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted `NCBITaxon:56423` and `NCBITaxon:58629` old IDs.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:27322`; native GOLD projects were additionally confirmed by a complete exact extraction from `data/gold/*.jsonl.gz`.
