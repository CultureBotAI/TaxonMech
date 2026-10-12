# YAML Record Review: Acetivibrio sp.

## Target

- File: `data/taxa/bacteria/acetivibrio_sp.yaml`
- Identifier: `NCBITaxon:1872092`
- PATHS.tsv row: 296614
- Label: `Acetivibrio sp.`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:2641281` (`unclassified Acetivibrio`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_sp.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_mesophilus.yaml data/taxa/bacteria/acetivibrio_saccincola.yaml data/taxa/bacteria/acetivibrio_sp.yaml data/taxa/bacteria/acetivibrio_sp_6_13.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species placeholder below `unclassified Acetivibrio`.
- `data/raw/ncbitaxon_taxa.tsv` line 489176 pins `NCBITaxon:1872092` to label `Acetivibrio sp.`, rank `SPECIES`, parent `NCBITaxon:2641281`, genetic code 11, exact synonym `Hungateiclostridium sp.`, source set `ncbitaxon|gtdb`, and NCBI snapshot `2026-09-13`.
- `data/raw/ncbitaxon_taxa.tsv` line 539492 supports the immediate `unclassified Acetivibrio` parent, and the raw parent rows place that placeholder below `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/gtdb_mappings.tsv` lines 70930-70935 support the six `skos:broadMatch` mappings from pooled DIGJ01 and Hungateiclostridium GTDB species to `NCBITaxon:1872092`; `data/raw/gtdb_species.tsv` lines 52785-52787 and 74472, 74475-74476 support their genome counts.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_sp`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 80062 keeps this taxon in scope as `attested rule: Acetivibrio sp., 2 sources incl. NCBI`.
- The six GTDB broad-match rows carry genome counts 6, 5, 2, 1, 1, and 1, matching the YAML `taxonomy_mappings`.
- The YAML intentionally leaves `strain_count: 0` because this source-backed placeholder has NCBI/GTDB identity evidence but no directly projected local BacDive strain evidence.

## Completeness

- NCBITAXON and GTDB attestations are represented with the expected assertion units and counts.
- All six local GTDB species that pool onto `NCBITaxon:1872092` are present as `skos:broadMatch` mappings with the standard kg-microbe broad-match note.
- The exact NCBI synonym `Hungateiclostridium sp.` is present.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
