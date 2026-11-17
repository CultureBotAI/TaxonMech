# YAML Record Review: Promicromonospora sp. 10.25-Bb

## Target

- File: `data/taxa/bacteria/promicromonospora_sp_10_25_bb.yaml`
- Identifier: `NCBITaxon:1000005`
- PATHS.tsv row: 9
- Label: `Promicromonospora sp. 10.25-Bb`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:2647929` (`unclassified Promicromonospora`)

## Validation

- `just validate data/taxa/bacteria/promicromonospora_sp_10_25_bb.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/mycobacterium_sp_1_12_ves.yaml data/taxa/bacteria/nocardia_sp_3_2_vpr.yaml data/taxa/bacteria/polaromonas_sp_7_23_vpa.yaml data/taxa/bacteria/promicromonospora_sp_10_25_bb.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species-level placeholder under the no-rank NCBI `unclassified Promicromonospora` node.
- `data/raw/ncbitaxon_taxa.tsv` line 208806 pins `NCBITaxon:1000005` to label `Promicromonospora sp. 10.25-Bb`, rank `SPECIES`, parent `NCBITaxon:2647929`, genetic code 11, source set `ncbitaxon`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the record under `unclassified Promicromonospora`, `Promicromonospora`, Promicromonosporaceae, Micrococcales, Actinomycetes, Actinomycetota, Bacillati, and Bacteria, matching the YAML lineage.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `promicromonospora_sp_10_25_bb`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 309920 keeps this taxon in scope as `attested rule: Promicromonospora sp. 10.25-Bb, 1 sources incl. NCBI`.
- A gitignore-independent `rg --no-ignore --hidden` scan of `data/raw`, `data/atb`, and `data/straininfo` found only the NCBI taxonomy row for `NCBITaxon:1000005`.

## Completeness

- The sole NCBITAXON source attestation is represented with one `NAME` assertion and the pinned NCBI snapshot date.
- The record has no GTDB or LPSN cross-reference in the local source inventories, and the YAML correspondingly has no `taxonomy_mappings`, `nomenclature`, or `xrefs` block.
- `strain_count: 0` is consistent with the lack of direct BacDive, GOLD, AllTheBacteria, or StrainInfo rows for this NCBI taxon in the local source inventories.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
