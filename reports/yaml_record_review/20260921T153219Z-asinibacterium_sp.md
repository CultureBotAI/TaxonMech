# YAML Record Review: Asinibacterium sp.

## Target

- File: `data/taxa/bacteria/asinibacterium_sp.yaml`
- Identifier: `NCBITaxon:1872645`
- Label: `Asinibacterium sp.`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2632724` / `unclassified Asinibacterium`
- Lineage: `root` -> `cellular organisms` -> `Bacteria` -> `Pseudomonadati` -> `FCB group` -> `Bacteroidota/Chlorobiota group` -> `Bacteroidota` -> `Chitinophagia` -> `Chitinophagales` -> `Chitinophagaceae` -> `Asinibacterium` -> `unclassified Asinibacterium`
- Existing review report: none found for `*asinibacterium_sp.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/bacteria/asinibacterium_sp.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/bacteria/asinibacterium_sp.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:1872645`, labelled `Asinibacterium sp.` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:1872645` is a `SPECIES` child of `NCBITaxon:2632724` / `unclassified Asinibacterium`.
- The generated record correctly has no NCBI synonym block because the raw NCBI row has no exact or related synonyms in the snapshot.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-13, with the generated reason `attested rule: Asinibacterium sp., 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:1872645`, so the generated current identifier is not represented as merged away in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:1872645`, the exact bare label context, and the exact bare slug found only the generated taxon and path rows plus the raw NCBI/GTDB/scope rows. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:1872645`.
- `data/raw/gtdb_mappings.tsv` has two broad matches for `NCBITaxon:1872645`: `GTDB:s__Sediminibacterium_sp041179065` with genome count `2`, and `GTDB:s__Sediminibacterium_sp041303215` with genome count `1`.
- The generated `taxonomy_mappings` block is count- and predicate-consistent with those two GTDB rows: both use `skos:broadMatch`, and the generated source labels and genome counts match the raw rows.
- The generated `GTDB` source attestation represents `GTDB:s__Sediminibacterium_sp041179065` with assertion count `2` and notes the one further pooled GTDB species, matching the two-row raw GTDB inventory.
- `data/raw/gold_organisms.tsv` has no row for `NCBITaxon:1872645`, consistent with the absence of a generated `GOLD` source attestation.
- Exact native GOLD inspection found 0 organism rows for `1872645`, and therefore 0 project or analysis rows, in the local `data/gold/*.jsonl.gz` snapshot.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `1872645`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `1872645`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:1872645`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, two GTDB taxonomy mappings, genetic code, `strain_count`, NCBITaxon and GTDB source attestations, and generation history.
- There are no strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive, StrainInfo, and both aggregate and native GOLD have no exact match for `1872645`.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/bacteria/asinibacterium_sp.yaml`; it is generated and validates strictly.
- Preserve the no-rank `unclassified Asinibacterium` parent, the two broad GTDB mappings, the pooled GTDB source attestation, empty NCBI synonym behavior, and empty BacDive/StrainInfo/GOLD behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/bacteria/asinibacterium_sp.yaml` and `just validate-strict data/taxa/bacteria/asinibacterium_sp.yaml` after regenerating the taxon record.

## Additional Notes

- The final no-ignore slug search used a bare-slug boundary to exclude neighboring generated records such as `asinibacterium_sp_or43`, `asinibacterium_sp_or53`, `asinibacterium_sp_zj6106`, and `uncultured_asinibacterium_sp`.
