# YAML Record Review: Asinibacterium sp. OR43

## Target

- File: `data/taxa/bacteria/asinibacterium_sp_or43.yaml`
- Identifier: `NCBITaxon:1076522`
- Label: `Asinibacterium sp. OR43`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2632724` / `unclassified Asinibacterium`
- Lineage: `root` -> `cellular organisms` -> `Bacteria` -> `Pseudomonadati` -> `FCB group` -> `Bacteroidota/Chlorobiota group` -> `Bacteroidota` -> `Chitinophagia` -> `Chitinophagales` -> `Chitinophagaceae` -> `Asinibacterium` -> `unclassified Asinibacterium`
- Existing review report: none found for `*asinibacterium_sp_or43.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/bacteria/asinibacterium_sp_or43.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/bacteria/asinibacterium_sp_or43.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:1076522`, labelled `Asinibacterium sp. OR43` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:1076522` is a `SPECIES` child of `NCBITaxon:2632724` / `unclassified Asinibacterium`.
- The generated record correctly has no NCBI synonym block because the raw NCBI row has no exact or related NCBI synonyms in the snapshot.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Asinibacterium sp. OR43, 3 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:1076522`, so the generated current identifier is not represented as merged away in the local raw snapshot.
- A no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:1076522`, the exact label, and the slug found the generated taxon and path rows, the raw NCBI/GTDB/MADIN/scope rows, the legacy page path, and one prior review note that names this slug as a neighboring record. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:1076522`.
- `data/raw/gtdb_mappings.tsv` has one close match for `NCBITaxon:1076522`: `GTDB:s__Sediminibacterium_sp000515315` with genome count `2`.
- The generated `taxonomy_mappings`, GTDB exact synonym, xref, and `GTDB` source attestation are count-, predicate-, and ID-consistent with the raw GTDB row.
- `data/raw/madin_taxa.tsv` has one row for `NCBITaxon:1076522` with count `2`, matching the generated `MADIN` source attestation.
- `data/raw/gold_organisms.tsv` has no row for `NCBITaxon:1076522`, consistent with the absence of a generated `GOLD` source attestation.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0006532`, `Asinibacterium sp. OR43`, with strain `OR43` and no culture collection ID.
- GOLD organism `Go0006532` has one project, `Gp0006532`, with BioProject `PRJNA76969` and BioSample `SAMN02441571`.
- GOLD project `Gp0006532` is linked to genome analysis `Ga0025045` with GenBank assembly accession `GCA_000427525.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `1076522`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `1076522`.
- Exact quoted `OR43` token lookups found 0 BacDive rows and 0 StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:1076522`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, GTDB taxonomy mapping, GTDB synonym/xref, genetic code, `strain_count`, NCBITaxon, GTDB, and MADIN source attestations, and generation history.
- There are no strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive and StrainInfo have no exact NCBI match, and the native GOLD `OR43` token does not add an eligible local BacDive or StrainInfo strain.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/bacteria/asinibacterium_sp_or43.yaml`; it is generated and validates strictly.
- Preserve the no-rank `unclassified Asinibacterium` parent, the close GTDB mapping, the GTDB xref and synonym, the MADIN source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/bacteria/asinibacterium_sp_or43.yaml` and `just validate-strict data/taxa/bacteria/asinibacterium_sp_or43.yaml` after regenerating the taxon record.

## Additional Notes

- The local native GOLD snapshot has an inspectable same-taxon organism row for `1076522`, while `data/raw/gold_organisms.tsv` has no row. This source-snapshot mismatch is not itself a YAML defect when the aggregate file supports the absence of a generated `GOLD` source attestation.
- The native GOLD analysis for `Asinibacterium sp. OR43` is project-linked through `AP PROJECT GOLD IDS = Gp0006532`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
