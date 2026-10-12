# YAML Record Review: Acetispira formosa (nom. nud.)

## Target

- File: `data/taxa/bacteria/acetispira_formosa_nom_nud.yaml`
- Identifier: `NCBITaxon:2946587`
- PATHS.tsv row: 396516
- Label: `Acetispira formosa (nom. nud.)`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:3777614` (`Acetispira (nom. nud.)`)

## Validation

- `just validate data/taxa/bacteria/acetispira_formosa_nom_nud.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/aceticella_sp_75b_ac.yaml data/taxa/bacteria/acetilactobacillus_jinshanensis.yaml data/taxa/bacteria/acetilactobacillus_sp.yaml data/taxa/bacteria/acetispira_formosa_nom_nud.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` NCBI species-level bacterial taxon with NCBI's `nom. nud.` qualifier preserved in the label and lineage.
- `data/raw/ncbitaxon_taxa.tsv` line 575426 pins `NCBITaxon:2946587` to label `Acetispira formosa (nom. nud.)`, rank `SPECIES`, parent `NCBITaxon:3777614`, genetic code 11, exact synonym `Acetispira formosa`, four NCBI related synonyms, source set `ncbitaxon|gtdb`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place `NCBITaxon:3777614` (`Acetispira (nom. nud.)`) under `NCBITaxon:3796085` (`Acetispirales (nom. nud.)`), then under Deltaproteobacteria, the `delta/epsilon subdivisions` clade, and Bacteria, matching the YAML lineage.
- `data/raw/ncbi_merged_ids.tsv` line 74120 records retired `NCBITaxon:3777616` as merged into this taxon.

## Evidence

- An exact `find` probe under `reports/yaml_record_review` found no existing report for `acetispira_formosa_nom_nud`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 110656 keeps this taxon in scope as `attested rule: Acetispira formosa (nom. nud.), 2 sources incl. NCBI`.
- `data/raw/gtdb_species.tsv` line 5274 and `data/raw/gtdb_mappings.tsv` line 237261 support the `GTDB:s__Adiutrix_sp023525915` `skos:closeMatch` mapping to `NCBITaxon:2946587` with `genome_count: 1`.
- The GTDB source label `s__Adiutrix_sp023525915` is represented as xref `GTDB:s__Adiutrix_sp023525915` and as exact synonym `Adiutrix sp023525915`.
- The gitignore-independent bounded exact-ID/source-ID scan across `data/raw`, `data/atb`, and `data/straininfo` found no BacDive, LPSN, MediaDive, GOLD, ATB, or StrainInfo evidence for this NCBI taxon.

## Completeness

- The NCBITAXON and GTDB attestations are both represented, and the record carries the only GTDB mapping found for `NCBITaxon:2946587`.
- No same-taxon strain, nomenclature, medium, GOLD, or ATB rows were present in the scanned local inventories, so the empty `strains` and `nomenclature` surfaces are consistent with the source evidence.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
