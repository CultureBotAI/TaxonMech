# YAML Record Review: Microbacterium sp. 6.11-VPa

## Target

- File: `data/taxa/bacteria/microbacterium_sp_6_11_vpa.yaml`
- Identifier: `NCBITaxon:1000000`
- PATHS.tsv row: 4
- Label: `Microbacterium sp. 6.11-VPa`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:2609290` (`unclassified Microbacterium`)

## Validation

- `just validate data/taxa/bacteria/microbacterium_sp_6_11_vpa.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/ancylobacter_aquaticus.yaml data/taxa/bacteria/herbaspirillum_sp_ba12.yaml data/taxa/bacteria/microbacterium_sp_6_11_vpa.yaml data/taxa/bacteria/mycobacterium_sp_1_1_ves.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species-level placeholder under the no-rank NCBI `unclassified Microbacterium` node.
- `data/raw/ncbitaxon_taxa.tsv` line 208801 pins `NCBITaxon:1000000` to label `Microbacterium sp. 6.11-VPa`, rank `SPECIES`, parent `NCBITaxon:2609290`, genetic code 11, source set `ncbitaxon`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the record under `unclassified Microbacterium`, `Microbacterium`, Microbacteriaceae, Micrococcales, Actinomycetes, Actinomycetota, Bacillati, and Bacteria, matching the YAML lineage.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `microbacterium_sp_6_11_vpa`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 309915 keeps this taxon in scope as `attested rule: Microbacterium sp. 6.11-VPa, 1 sources incl. NCBI`.
- A gitignore-independent `rg --no-ignore --hidden` scan of `data/raw`, `data/atb`, and `data/straininfo` found only the NCBI taxonomy row for `NCBITaxon:1000000`.

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
