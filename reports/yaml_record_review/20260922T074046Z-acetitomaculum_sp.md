# YAML Record Review: Acetitomaculum sp.

## Target

- File: `data/taxa/bacteria/acetitomaculum_sp.yaml`
- Identifier: `NCBITaxon:1872091`
- PATHS.tsv row: 296613
- Label: `Acetitomaculum sp.`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:2676916` (`unclassified Acetitomaculum`)

## Validation

- `just validate data/taxa/bacteria/acetitomaculum_sp.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetitomaculum_ruminis.yaml data/taxa/bacteria/acetitomaculum_ruminis_dsm_5522.yaml data/taxa/bacteria/acetitomaculum_sp.yaml data/taxa/bacteria/acetivibrio_aldrichii.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species-level NCBI placeholder under `unclassified Acetitomaculum`.
- `data/raw/ncbitaxon_taxa.tsv` line 489175 pins `NCBITaxon:1872091` to label `Acetitomaculum sp.`, rank `SPECIES`, parent `NCBITaxon:2676916`, genetic code 11, source set `ncbitaxon`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place `NCBITaxon:1872091` under `NCBITaxon:2676916` (`unclassified Acetitomaculum`), then `Acetitomaculum`, Lachnospiraceae, Lachnospirales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.

## Evidence

- An exact `find` probe under `reports/yaml_record_review` found no existing report for `acetitomaculum_sp`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 546145 keeps this taxon in scope as `attested rule: Acetitomaculum sp., 1 sources incl. NCBI`.
- The gitignore-independent bounded exact-ID/source scan across `data/raw`, `data/atb`, and `data/straininfo` found no LPSN, GTDB, BacDive, MediaDive, GOLD, MADIN, BactoTraits, StrainInfo, or ATB evidence for `NCBITaxon:1872091`.

## Completeness

- The NCBITAXON attestation is represented with the expected `assertion_count: 1` and NCBI snapshot note.
- Because the scanned local inventories expose no source rows for this exact NCBI taxon beyond `data/raw/ncbitaxon_taxa.tsv`, the empty nomenclature, synonym, xref, strain, taxonomy-mapping, and related-record surfaces are consistent with the available evidence.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
