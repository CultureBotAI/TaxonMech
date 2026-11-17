# YAML Record Review: Acetoanaerobium sp.

## Target

- File: `data/taxa/bacteria/acetoanaerobium_sp.yaml`
- Identifier: `NCBITaxon:1872093`
- PATHS.tsv row: 296615
- Label: `Acetoanaerobium sp.`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:2628769` (`unclassified Acetoanaerobium`)

## Validation

- `just validate data/taxa/bacteria/acetoanaerobium_sp.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrionales_bacterium.yaml data/taxa/bacteria/acetoanaerobium_noterae.yaml data/taxa/bacteria/acetoanaerobium_pronyense.yaml data/taxa/bacteria/acetoanaerobium_sp.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species-level placeholder under the no-rank NCBI `unclassified Acetoanaerobium` node.
- `data/raw/ncbitaxon_taxa.tsv` line 489177 pins `NCBITaxon:1872093` to label `Acetoanaerobium sp.`, rank `SPECIES`, parent `NCBITaxon:2628769`, genetic code 11, source set `ncbitaxon|gtdb`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the record under `unclassified Acetoanaerobium`, `Acetoanaerobium`, Filifactoraceae, Peptostreptococcales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/gtdb_species.tsv` lines 3283 and 3285 and `data/raw/gtdb_mappings.tsv` lines 70936-70937 support the two `skos:broadMatch` GTDB species mappings.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetoanaerobium_sp`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 80063 keeps this taxon in scope as `attested rule: Acetoanaerobium sp., 2 sources incl. NCBI`.
- A gitignore-independent `rg --no-ignore --hidden` scan of `data/raw`, `data/atb`, and `data/straininfo` found only the NCBI taxonomy row and the two GTDB broad mappings for `NCBITaxon:1872093`.

## Completeness

- NCBITAXON and GTDB source attestations are represented with the expected assertion units.
- `taxonomy_mappings` carries both local broad mappings: the 12-genome `GTDB:s__Acetoanaerobium_noterae` species and the 1-genome `GTDB:s__Acetoanaerobium_sp041831635` placeholder species.
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
