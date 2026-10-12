# YAML Record Review: Armillaria ostoyae

## Target

- File: `data/taxa/eukaryota/armillaria_ostoyae.yaml`
- Identifier: `NCBITaxon:47428`
- Label: `Armillaria ostoyae`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:47424` / `Armillaria`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Basidiomycota` -> `Agaricomycotina` -> `Agaricomycetes` -> `Agaricomycetidae` -> `Agaricales` -> `Marasmiineae` -> `Physalacriaceae` -> `Armillaria`
- Existing review report: none found for `*armillaria_ostoyae.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/armillaria_ostoyae.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/armillaria_ostoyae.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:47428`, labelled `Armillaria ostoyae` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:47428` is a `SPECIES` child of `NCBITaxon:47424` / `Armillaria`.
- The generated NCBI synonym block matches the raw NCBI row: it has one exact synonym, `Armillariella ostoyae`, and three related synonyms, `Armillaria ostoyae (Romagn.) Herink 1973`, `Armillaria sp. NABS1`, and `Armillariella ostoyae Romagn., 1970`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Armillaria ostoyae, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has two retired identifiers that now merge into `NCBITaxon:47428`: `NCBITaxon:139079` and `NCBITaxon:181916`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:47428`.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:47428`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/merged-ID rows, the legacy page path, and the preceding `armillaria_obscura` review's near-miss note. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:47428`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:47428` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0588271`, `Armillaria ostoyae C18/9`, strain `C18/9`, and no culture collection ID.
- GOLD organism `Go0588271` has one project, `Gp0602218`, with BioProject `PRJEB19205` and BioSample `SAMEA54519418`.
- GOLD project `Gp0602218` is linked to genome analysis `Ga0519653` with GenBank assembly accession `GCA_900157425.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 13 direct strain rows for `47428`, all already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `47428`.
- A `DSM 3734` / `NABS1` token lookup found one StrainInfo row, `straininfo.strain:112596`; it is one of the excluded exact-NCBI StrainInfo rows and does not imply a missing generated strain.
- An exact `C18/9` token lookup found 0 BacDive rows and 0 StrainInfo rows.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, the 13 exact StrainInfo rows are all excluded because they have no eligible own deposit, and the native GOLD `C18/9` token does not add an eligible local strain.
- The absence of `nomenclature` is consistent with the local source inventory: `data/raw/ncbi_type_material.tsv` has no row for this identifier, and generated `nomenclature` entries currently come from LPSN only.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/armillaria_ostoyae.yaml`; it is generated and validates strictly.
- Preserve the NCBI exact and related synonyms, retained merged-ID context, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/armillaria_ostoyae.yaml` and `just validate-strict data/taxa/eukaryota/armillaria_ostoyae.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Armillaria ostoyae C18/9` is project-linked through `AP PROJECT GOLD IDS = Gp0602218`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
