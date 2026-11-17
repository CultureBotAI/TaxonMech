# YAML Record Review: Armillaria nabsnona

## Target

- File: `data/taxa/eukaryota/armillaria_nabsnona.yaml`
- Identifier: `NCBITaxon:64368`
- Label: `Armillaria nabsnona`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:47424` / `Armillaria`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Basidiomycota` -> `Agaricomycotina` -> `Agaricomycetes` -> `Agaricomycetidae` -> `Agaricales` -> `Marasmiineae` -> `Physalacriaceae` -> `Armillaria`
- Existing review report: none found for `*armillaria_nabsnona.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/armillaria_nabsnona.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/armillaria_nabsnona.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:64368`, labelled `Armillaria nabsnona` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:64368` is a `SPECIES` child of `NCBITaxon:47424` / `Armillaria`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms and one related synonym, `Armillaria nabsnona T. J. Volk & Burds., 1996`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Armillaria nabsnona, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:64368`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:64368`.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:64368`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:64368`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:64368` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0403318`, `Armillaria nabsnona CMW6904`, strain `CMW6904`, and no culture collection ID.
- GOLD organism `Go0403318` has two projects: `Gp0295056` with BioProject `PRJNA500235` and BioSample `SAMN10362910`, and `Gp0304609` with BioProject `PRJNA500837` and BioSample `SAMN10362911`.
- GOLD project `Gp0304609` is linked to genome analysis `Ga0264384`; the analysis has no GenBank assembly accession in the native snapshot.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct or deposit-only strain rows for `64368`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `64368`.
- An exact `CMW6904` token lookup found 0 BacDive rows and 0 StrainInfo rows.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive and StrainInfo have no exact NCBI matches, and the native GOLD `CMW6904` token does not add an eligible local strain.
- The absence of `nomenclature` is consistent with the local source inventory: `data/raw/ncbi_type_material.tsv` has no row for this identifier, and generated `nomenclature` entries currently come from LPSN only.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/armillaria_nabsnona.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonym, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/armillaria_nabsnona.yaml` and `just validate-strict data/taxa/eukaryota/armillaria_nabsnona.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Armillaria nabsnona CMW6904` is project-linked through `AP PROJECT GOLD IDS = Gp0304609`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
