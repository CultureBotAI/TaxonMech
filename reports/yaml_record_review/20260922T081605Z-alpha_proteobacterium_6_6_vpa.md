# YAML Record Review: alpha proteobacterium 6.6-VPa

## Target

- File: `data/taxa/bacteria/alpha_proteobacterium_6_6_vpa.yaml`
- Identifier: `NCBITaxon:1000027`
- PATHS.tsv row: 33
- Label: `alpha proteobacterium 6.6-VPa`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:33807` (`unclassified Alphaproteobacteria`)

## Validation

- `just validate data/taxa/bacteria/alpha_proteobacterium_6_6_vpa.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/intrasporangiaceae_bacterium_7_31_vpa.yaml data/taxa/bacteria/intrasporangiaceae_bacterium_7_4_vpa.yaml data/taxa/bacteria/micrococcineae_bacterium_9_2_bp.yaml data/taxa/bacteria/alpha_proteobacterium_6_6_vpa.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species-level placeholder under the no-rank NCBI `unclassified Alphaproteobacteria` node.
- `data/raw/ncbitaxon_taxa.tsv` line 208828 pins `NCBITaxon:1000027` to label `alpha proteobacterium 6.6-VPa`, rank `SPECIES`, parent `NCBITaxon:33807`, genetic code 11, source set `ncbitaxon`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the record under `unclassified Alphaproteobacteria`, Alphaproteobacteria, Pseudomonadota, Pseudomonadati, and Bacteria, matching the YAML lineage.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `alpha_proteobacterium_6_6_vpa`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 309942 keeps this taxon in scope as `attested rule: alpha proteobacterium 6.6-VPa, 1 sources incl. NCBI`.
- A gitignore-independent `rg --no-ignore --hidden` scan of `data/raw`, `data/atb`, and `data/straininfo` found only the NCBI taxonomy row for `NCBITaxon:1000027`.

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
