# YAML Record Review: Armillaria obscura

## Target

- File: `data/taxa/eukaryota/armillaria_obscura.yaml`
- Identifier: `NCBITaxon:2074775`
- Label: `Armillaria obscura`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:47424` / `Armillaria`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Basidiomycota` -> `Agaricomycotina` -> `Agaricomycetes` -> `Agaricomycetidae` -> `Agaricales` -> `Marasmiineae` -> `Physalacriaceae` -> `Armillaria`
- Existing review report: none found for `*armillaria_obscura.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/armillaria_obscura.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/armillaria_obscura.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:2074775`, labelled `Armillaria obscura` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:2074775` is a `SPECIES` child of `NCBITaxon:47424` / `Armillaria`.
- The generated NCBI synonym block matches the raw NCBI row: it has one exact synonym, `Agaricus obscurus`, and two related synonyms, `Agaricus obscurus Schaeff., 1774` and `Armillaria obscura (Schaeff.) Herink, 1973`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Armillaria obscura, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:2074775`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:2074775`.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:2074775`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:2074775`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:2074775` with count `3`.
- Exact native GOLD inspection found three organism rows for the same taxon: `Go0618258`, `Armillaria obscura DSM 3734`; `Go0618259`, `Armillaria obscura 780811.1.2`; and `Go0618260`, `Armillaria obscura 132`.
- No native GOLD project or analysis rows link to any of the three exact organism rows.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 7 direct strain rows for `2074775`, all already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `2074775`.
- A `DSM 3734` / `780811.1.2` token lookup found 0 BacDive rows and one StrainInfo row for the neighboring species `Armillaria ostoyae`, not for `Armillaria obscura`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, the seven exact StrainInfo rows are all excluded because they have no eligible own deposit, and the specific native GOLD tokens checked do not add an eligible local strain.
- The absence of `nomenclature` is consistent with the local source inventory: `data/raw/ncbi_type_material.tsv` has no row for this identifier, and generated `nomenclature` entries currently come from LPSN only.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/armillaria_obscura.yaml`; it is generated and validates strictly.
- Preserve the NCBI exact and related synonyms, count-consistent three-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/armillaria_obscura.yaml` and `just validate-strict data/taxa/eukaryota/armillaria_obscura.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD snapshot has no project or analysis rows for its three exact `NCBITaxon:2074775` organisms.
