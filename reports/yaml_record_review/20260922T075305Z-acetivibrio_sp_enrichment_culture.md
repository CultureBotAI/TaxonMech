# YAML Record Review: Acetivibrio sp. enrichment culture

## Target

- File: `data/taxa/bacteria/acetivibrio_sp_enrichment_culture.yaml`
- Identifier: `NCBITaxon:1574478`
- PATHS.tsv row: 210440
- Label: `Acetivibrio sp. enrichment culture`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:293325` (`environmental samples`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_sp_enrichment_culture.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_sp_c_56.yaml data/taxa/bacteria/acetivibrio_sp_enrichment_culture.yaml data/taxa/bacteria/acetivibrio_sp_enrichment_culture_clone_wsc_27.yaml data/taxa/bacteria/acetivibrio_sp_enrichment_culture_clone_wsc_3.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species placeholder below `Acetivibrio` environmental samples.
- `data/raw/ncbitaxon_taxa.tsv` line 405703 pins `NCBITaxon:1574478` to label `Acetivibrio sp. enrichment culture`, rank `SPECIES`, parent `NCBITaxon:293325`, genetic code 11, source set `ncbitaxon`, and NCBI snapshot `2026-09-13`.
- `data/raw/ncbitaxon_taxa.tsv` line 59874 supports the immediate `environmental samples` parent, and the raw parent rows place that placeholder below `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_sp_enrichment_culture`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 474239 keeps this taxon in scope as `attested rule: Acetivibrio sp. enrichment culture, 1 sources incl. NCBI`.
- A gitignore-independent exact scan for `NCBITaxon:1574478` under `data/raw`, `data/atb`, and `data/straininfo` found only the pinned NCBI taxonomy row for auxiliary source evidence, consistent with the compact NCBITAXON-only YAML record.

## Completeness

- The sole NCBITAXON attestation is represented with one `NAME` assertion and snapshot note `2026-09-13`.
- `strain_count: 0` is consistent with the absence of same-taxon BacDive, GOLD, GTDB, AllTheBacteria, and StrainInfo rows in the gitignore-independent source scan.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
