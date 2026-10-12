# YAML Record Review: Acerihabitans sp.

## Target

- File: `data/taxa/bacteria/acerihabitans_sp.yaml`
- Identifier: `NCBITaxon:2811394`
- PATHS.tsv row: 378614
- Label: `Acerihabitans sp.`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:2811393` (`unclassified Acerihabitans`)

## Validation

- `just validate data/taxa/bacteria/acerihabitans_sp.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acer_platanoides_aster_yellows_phytoplasma.yaml data/taxa/bacteria/acerihabitans_arboris.yaml data/taxa/bacteria/acerihabitans_sp.yaml data/taxa/bacteria/acerihabitans_sp_bd602.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` NCBI species-level bacterial taxon.
- `data/raw/ncbitaxon_taxa.tsv` line 558480 pins `NCBITaxon:2811394` to label `Acerihabitans sp.`, rank `SPECIES`, parent `NCBITaxon:2811393`, genetic code 11, source set `ncbitaxon|gtdb`, and NCBI snapshot `2026-09-13`.
- The raw `NCBITaxon:2811393` row is `unclassified Acerihabitans` under genus `Acerihabitans`, matching the YAML `parent_taxon` and terminal no-rank lineage node.
- Higher NCBI rows for Pectobacteriaceae, Enterobacterales, Gammaproteobacteria, Pseudomonadota, Pseudomonadati, and Bacteria support the remainder of the lineage.

## Evidence

- An exact `find` probe under `reports/yaml_record_review` found no existing report for `acerihabitans_sp`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 104422 keeps this taxon in scope as `attested rule: Acerihabitans sp., 2 sources incl. NCBI`.
- `data/raw/gtdb_species.tsv` line 2988 and `data/raw/gtdb_mappings.tsv` line 220194 support the single `GTDB:s__Acerihabitans_sp036398755` `skos:closeMatch` mapping to `NCBITaxon:2811394` with `genome_count: 1`.
- The GTDB source label `s__Acerihabitans_sp036398755` is represented as xref `GTDB:s__Acerihabitans_sp036398755` and as exact synonym `Acerihabitans sp036398755`.
- The gitignore-independent exact-ID/source-ID scan across `data/raw`, `data/atb`, and `data/straininfo` found no BacDive, LPSN, MediaDive, GOLD, ATB, or StrainInfo evidence for this NCBI taxon.

## Completeness

- The NCBITAXON and GTDB attestations are both represented, and the record carries the only GTDB mapping found for `NCBITaxon:2811394`.
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
