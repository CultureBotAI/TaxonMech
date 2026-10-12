# YAML Record Review: Asinibacterium sp. ZJ6106

## Target

- File: `data/taxa/bacteria/asinibacterium_sp_zj6106.yaml`
- Identifier: `NCBITaxon:1612199`
- Label: `Asinibacterium sp. ZJ6106`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2632724` / `unclassified Asinibacterium`
- Lineage: `root` -> `cellular organisms` -> `Bacteria` -> `Pseudomonadati` -> `FCB group` -> `Bacteroidota/Chlorobiota group` -> `Bacteroidota` -> `Chitinophagia` -> `Chitinophagales` -> `Chitinophagaceae` -> `Asinibacterium` -> `unclassified Asinibacterium`
- Existing review report: none found for `*asinibacterium_sp_zj6106.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/bacteria/asinibacterium_sp_zj6106.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/bacteria/asinibacterium_sp_zj6106.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:1612199`, labelled `Asinibacterium sp. ZJ6106` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:1612199` is a `SPECIES` child of `NCBITaxon:2632724` / `unclassified Asinibacterium`.
- The generated record correctly has no NCBI synonym block because the raw NCBI row has no exact or related NCBI synonyms in the snapshot.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-13, with the generated reason `attested rule: Asinibacterium sp. ZJ6106, 1 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:1612199`, so the generated current identifier is not represented as merged away in the local raw snapshot.
- A no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:1612199`, the exact label, and the slug found the generated taxon and path rows, the raw NCBI/scope rows, and one prior review note that names this slug as a neighboring record. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:1612199`.
- `data/raw/gtdb_mappings.tsv` has no row for `NCBITaxon:1612199`, consistent with the absence of generated `GTDB` taxonomy mappings, xrefs, synonyms, and source attestations.
- `data/raw/madin_taxa.tsv` has no row for `NCBITaxon:1612199`, consistent with the absence of a generated `MADIN` source attestation.
- `data/raw/gold_organisms.tsv` has no row for `NCBITaxon:1612199`, consistent with the absence of a generated `GOLD` source attestation.
- Exact native GOLD inspection found 0 organism rows for `1612199`, and therefore 0 project or analysis rows, in the local `data/gold/*.jsonl.gz` snapshot.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `1612199`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `1612199`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:1612199`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, genetic code, `strain_count`, NCBITaxon source attestation, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive, StrainInfo, and both aggregate and native GOLD have no exact match for `1612199`.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/bacteria/asinibacterium_sp_zj6106.yaml`; it is generated and validates strictly.
- Preserve the no-rank `unclassified Asinibacterium` parent, NCBITaxon-only source attestation, empty NCBI synonym behavior, and empty GTDB/MADIN/BacDive/StrainInfo/GOLD behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/bacteria/asinibacterium_sp_zj6106.yaml` and `just validate-strict data/taxa/bacteria/asinibacterium_sp_zj6106.yaml` after regenerating the taxon record.

## Additional Notes

- None.
