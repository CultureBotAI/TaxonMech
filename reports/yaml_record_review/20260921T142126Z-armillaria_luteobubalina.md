# YAML Record Review: Armillaria luteobubalina

## Target

- File: `data/taxa/eukaryota/armillaria_luteobubalina.yaml`
- Identifier: `NCBITaxon:153913`
- Label: `Armillaria luteobubalina`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:47424` / `Armillaria`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Basidiomycota` -> `Agaricomycotina` -> `Agaricomycetes` -> `Agaricomycetidae` -> `Agaricales` -> `Marasmiineae` -> `Physalacriaceae` -> `Armillaria`
- Existing review report: none found for `*armillaria_luteobubalina.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/armillaria_luteobubalina.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/armillaria_luteobubalina.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:153913`, labelled `Armillaria luteobubalina` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:153913` is a `SPECIES` child of `NCBITaxon:47424` / `Armillaria`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms and three related synonyms, `Armillaria luteobubalina Watling & Kile, 1978`, `Armillaria sp. CMW 5446`, and `Armillaria sp. CMW 8876`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Armillaria luteobubalina, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has two retired identifiers that now merge into `NCBITaxon:153913`: `NCBITaxon:179652` and `NCBITaxon:179655`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:153913`.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:153913`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/merged-ID rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:153913`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:153913` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0370581`, `Armillaria luteobubalina HWK02`, strain `HWK02`, and no culture collection ID.
- GOLD organism `Go0370581` has two projects: `Gp0216543` with BioProject `PRJNA500536` and BioSample `SAMN10363187`, and `Gp0306525` with BioProject `PRJNA455055` and BioSample `SAMN09063644`.
- GOLD project `Gp0216543` is linked to genome analysis `Ga0221606`; the analysis has no GenBank assembly accession in the native snapshot.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 1 direct strain row for `153913`, already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `153913`.
- Exact `CMW 5446` / `CMW 8876` and `HWK02` token lookups found 0 BacDive rows and 0 StrainInfo rows.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, the one exact StrainInfo row is excluded because it has no eligible own deposit, and neither the NCBI `CMW` synonym tokens nor the native GOLD `HWK02` token adds an eligible local strain.
- The absence of `nomenclature` is consistent with the local source inventory: `data/raw/ncbi_type_material.tsv` has no row for this identifier, and generated `nomenclature` entries currently come from LPSN only.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/armillaria_luteobubalina.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonyms, retained merged-ID context, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/armillaria_luteobubalina.yaml` and `just validate-strict data/taxa/eukaryota/armillaria_luteobubalina.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Armillaria luteobubalina HWK02` is project-linked through `AP PROJECT GOLD IDS = Gp0216543`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
