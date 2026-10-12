# YAML Record Review: Flavobacterium sp. G23-27

## Target

- File: `data/taxa/bacteria/flavobacterium_sp_g23_27.yaml`
- Identifier: `NCBITaxon:1000033`
- PATHS.tsv row: 40
- Label: `Flavobacterium sp. G23-27`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:196869` (`unclassified Flavobacterium`)

## Validation

- `just validate data/taxa/bacteria/flavobacterium_sp_g23_27.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/agrobacterium_sp_g21_09.yaml data/taxa/bacteria/enterobacter_sp_p19_19.yaml data/taxa/bacteria/flavobacterium_sp_g23_27.yaml data/taxa/bacteria/erwinia_sp_koakin.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species-level placeholder under the no-rank NCBI `unclassified Flavobacterium` node.
- `data/raw/ncbitaxon_taxa.tsv` line 208834 pins `NCBITaxon:1000033` to label `Flavobacterium sp. G23-27`, rank `SPECIES`, parent `NCBITaxon:196869`, genetic code 11, source set `ncbitaxon`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the record under `unclassified Flavobacterium`, `Flavobacterium`, Flavobacteriaceae, Flavobacteriales, Flavobacteriia, Bacteroidota, the Bacteroidota/Chlorobiota group, the FCB group, Pseudomonadati, and Bacteria, matching the YAML lineage.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `flavobacterium_sp_g23_27`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 309948 keeps this taxon in scope as `attested rule: Flavobacterium sp. G23-27, 1 sources incl. NCBI`.
- A gitignore-independent `rg --no-ignore --hidden` scan of `data/raw`, `data/atb`, and `data/straininfo` found only the NCBI taxonomy row for `NCBITaxon:1000033`.

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
