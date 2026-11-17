# YAML Record Review: Aceticella sp. 75b-Ac

## Target

- File: `data/taxa/bacteria/aceticella_sp_75b_ac.yaml`
- Identifier: `NCBITaxon:3692757`
- PATHS.tsv row: 476612
- Label: `Aceticella sp. 75b-Ac`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:3051500` (`unclassified Aceticella`)

## Validation

- `just validate data/taxa/bacteria/aceticella_sp_75b_ac.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/aceticella_sp_75b_ac.yaml data/taxa/bacteria/acetilactobacillus_jinshanensis.yaml data/taxa/bacteria/acetilactobacillus_sp.yaml data/taxa/bacteria/acetispira_formosa_nom_nud.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` NCBI species-level bacterial taxon.
- `data/raw/ncbitaxon_taxa.tsv` line 641906 pins `NCBITaxon:3692757` to label `Aceticella sp. 75b-Ac`, rank `SPECIES`, parent `NCBITaxon:3051500`, genetic code 11, source set `ncbitaxon`, and NCBI snapshot `2026-09-13`.
- The raw `NCBITaxon:3051500` row is `unclassified Aceticella` under genus `Aceticella`, matching the YAML `parent_taxon` and terminal no-rank lineage node.
- Higher NCBI rows for Thermoanaerobacteraceae, Thermoanaerobacterales, Clostridia, Bacillota, Bacillati, and Bacteria support the remainder of the lineage.

## Evidence

- An exact `find` probe under `reports/yaml_record_review` found no existing report for `aceticella_sp_75b_ac`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 617736 keeps this taxon in scope as `attested rule: Aceticella sp. 75b-Ac, 1 sources incl. NCBI`.
- A gitignore-independent, bounded exact-ID scan across `data/raw`, `data/atb`, and `data/straininfo` found no same-taxon auxiliary source rows beyond the NCBI row, matching the YAML's single NCBITAXON `source_attestations` entry and absence of `taxonomy_mappings`, `nomenclature`, and `strains`.
- The YAML `genetic_code: 11` and `strain_count: 0` are consistent with the pinned raw NCBI row and the absence of matching strain inventories.

## Completeness

- The available local evidence for this leaf consists of the seeded NCBI name row and its NCBI lineage; all of those facts are represented in the YAML.
- No GTDB, LPSN, BacDive, MediaDive, GOLD, ATB, or StrainInfo evidence was present for `NCBITaxon:3692757` in the exact same-taxon local scans, so the record does not appear to be omitting structured auxiliary assertions.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
