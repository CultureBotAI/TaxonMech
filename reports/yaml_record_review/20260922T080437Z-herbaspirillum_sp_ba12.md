# YAML Record Review: Herbaspirillum sp. BA12

## Target

- File: `data/taxa/bacteria/herbaspirillum_sp_ba12.yaml`
- Identifier: `NCBITaxon:100000`
- PATHS.tsv row: 3
- Label: `Herbaspirillum sp. BA12`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:2624150` (`unclassified Herbaspirillum`)

## Validation

- `just validate data/taxa/bacteria/herbaspirillum_sp_ba12.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/ancylobacter_aquaticus.yaml data/taxa/bacteria/herbaspirillum_sp_ba12.yaml data/taxa/bacteria/microbacterium_sp_6_11_vpa.yaml data/taxa/bacteria/mycobacterium_sp_1_1_ves.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species-level placeholder under the no-rank NCBI `unclassified Herbaspirillum` node.
- `data/raw/ncbitaxon_taxa.tsv` line 17104 pins `NCBITaxon:100000` to label `Herbaspirillum sp. BA12`, rank `SPECIES`, parent `NCBITaxon:2624150`, genetic code 11, exact synonym `Herbispirillum sp. BA12`, source set `ncbitaxon`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the record under `unclassified Herbaspirillum`, `Herbaspirillum`, Oxalobacteraceae, Burkholderiales, Betaproteobacteria, Pseudomonadota, Pseudomonadati, and Bacteria, matching the YAML lineage.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `herbaspirillum_sp_ba12`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 142933 keeps this taxon in scope as `attested rule: Herbaspirillum sp. BA12, 1 sources incl. NCBI`.
- A gitignore-independent `rg --no-ignore --hidden` scan of `data/raw`, `data/atb`, and `data/straininfo` found only the NCBI taxonomy row for `NCBITaxon:100000`.

## Completeness

- The sole NCBITAXON source attestation is represented with one `NAME` assertion and the pinned NCBI snapshot date.
- The NCBI exact synonym is preserved in `synonyms`.
- `strain_count: 0` is consistent with the lack of direct GTDB, BacDive, GOLD, AllTheBacteria, or StrainInfo rows for this NCBI taxon in the local source inventories.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
