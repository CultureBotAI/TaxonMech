# YAML Record Review: Acetivibrionales bacterium

## Target

- File: `data/taxa/bacteria/acetivibrionales_bacterium.yaml`
- Identifier: `NCBITaxon:3121602`
- PATHS.tsv row: 423866
- Label: `Acetivibrionales bacterium`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:3121601` (`unclassified Acetivibrionales`)

## Validation

- `just validate data/taxa/bacteria/acetivibrionales_bacterium.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrionales_bacterium.yaml data/taxa/bacteria/acetoanaerobium_noterae.yaml data/taxa/bacteria/acetoanaerobium_pronyense.yaml data/taxa/bacteria/acetoanaerobium_sp.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species-level placeholder under the no-rank NCBI `unclassified Acetivibrionales` node.
- `data/raw/ncbitaxon_taxa.tsv` line 601603 pins `NCBITaxon:3121602` to label `Acetivibrionales bacterium`, rank `SPECIES`, parent `NCBITaxon:3121601`, genetic code 11, source set `ncbitaxon|gtdb`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the record under `unclassified Acetivibrionales`, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/gtdb_mappings.tsv` lines 262237-262245 support the nine `skos:broadMatch` GTDB species mappings, and `data/raw/gtdb_species.tsv` lines 53478, 53559-53560, 53564, 53577, 84651, 106448, 106455, and 149923 support their GTDB species records and genome counts.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrionales_bacterium`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 121163 keeps this taxon in scope as `attested rule: Acetivibrionales bacterium, 2 sources incl. NCBI`.
- A gitignore-independent `rg --no-ignore --hidden` scan of `data/raw`, `data/atb`, and `data/straininfo` found only the NCBI taxonomy row and the nine GTDB broad mappings for `NCBITaxon:3121602`.

## Completeness

- NCBITAXON and GTDB source attestations are represented with the expected assertion units.
- `taxonomy_mappings` carries every local broad GTDB species mapping: the 13-genome `GTDB:s__DTU013_sp002385815`, the 3-genome `GTDB:s__DTU059_sp012523705`, the two 2-genome `DTU059` species, and five 1-genome species.
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
