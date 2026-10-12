# YAML Record Review: acesulfame-degrading bacterial consortium

## Target

- File: `data/taxa/bacteria/acesulfame_degrading_bacterial_consortium.yaml`
- Identifier: `NCBITaxon:2862871`
- PATHS.tsv row: 386244
- Label: `acesulfame-degrading bacterial consortium`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:49928` (`unclassified Bacteria`)

## Validation

- `just validate data/taxa/bacteria/acesulfame_degrading_bacterial_consortium.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acerihabitans_sp_kwt1480.yaml data/taxa/bacteria/acerihabitans_sp_kwt182.yaml data/taxa/bacteria/acerihabitans_sp_tg2.yaml data/taxa/bacteria/acesulfame_degrading_bacterial_consortium.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` NCBI species-level bacterial taxon.
- `data/raw/ncbitaxon_taxa.tsv` line 565689 pins `NCBITaxon:2862871` to label `acesulfame-degrading bacterial consortium`, rank `SPECIES`, parent `NCBITaxon:49928`, genetic code 11, source set `ncbitaxon`, and NCBI snapshot `2026-09-13`.
- `data/raw/ncbitaxon_taxa.tsv` line 6303 pins `NCBITaxon:49928` to `unclassified Bacteria` directly under `Bacteria`, matching the short YAML lineage.

## Evidence

- An exact `find` probe under `reports/yaml_record_review` found no existing report for `acesulfame_degrading_bacterial_consortium`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 578705 keeps this taxon in scope as `attested rule: acesulfame-degrading bacterial consortium, 1 sources incl. NCBI`.
- A gitignore-independent exact-ID scan across `data/raw`, `data/atb`, and `data/straininfo` found no same-taxon auxiliary source rows beyond the NCBI row, matching the YAML's single NCBITAXON `source_attestations` entry and absence of `taxonomy_mappings`, `nomenclature`, and `strains`.
- The YAML `genetic_code: 11` and `strain_count: 0` are consistent with the pinned raw NCBI row and the absence of matching strain inventories.

## Completeness

- The available local evidence for this consortium consists of the seeded NCBI name row and its NCBI lineage; all of those facts are represented in the YAML.
- No GTDB, LPSN, BacDive, MediaDive, GOLD, ATB, or StrainInfo evidence was present for `NCBITaxon:2862871` in the exact same-taxon local scans, so the record does not appear to be omitting structured auxiliary assertions.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
