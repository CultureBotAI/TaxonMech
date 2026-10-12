# YAML Record Review: Armillaria mellea

## Target

- File: `data/taxa/eukaryota/armillaria_mellea.yaml`
- Identifier: `NCBITaxon:47429`
- Label: `Armillaria mellea`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:47424` / `Armillaria`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Basidiomycota` -> `Agaricomycotina` -> `Agaricomycetes` -> `Agaricomycetidae` -> `Agaricales` -> `Marasmiineae` -> `Physalacriaceae` -> `Armillaria`
- Existing review report: none found for `*armillaria_mellea.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/armillaria_mellea.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/armillaria_mellea.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:47429`, labelled `Armillaria mellea` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:47429` is a `SPECIES` child of `NCBITaxon:47424` / `Armillaria`.
- The generated NCBI synonym block matches the raw NCBI row: it has 7 exact synonyms and 6 related synonyms, including the strain-like related synonym `Armillaria sp. 'mellea-OH01'`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Armillaria mellea, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has two retired identifiers that now merge into `NCBITaxon:47429`: `NCBITaxon:3108592` and `NCBITaxon:621134`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:47429`.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:47429`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/merged-ID rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:47429`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:47429` with count `3`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0411498`, `Armillaria mellea ELDO17`, strain `ELDO17`, and no culture collection ID.
- GOLD organism `Go0411498` has two projects: `Gp0305071` with BioProject `PRJNA571622` and BioSample `SAMN12812551`, and `Gp0347914` with BioProject `PRJNA568830` and BioSample `SAMN12796359`.
- No native GOLD analysis rows link to organism `Go0411498` or to either project through `AP PROJECT GOLD IDS`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 115 direct strain rows for `47429` and 2 deposit-only rows; all 117 candidates are already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `47429`.
- Exact `mellea-OH01` and `ELDO17` token lookups found 0 BacDive rows and 0 StrainInfo rows.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, all 117 exact or deposit-only StrainInfo candidates are excluded because they have no eligible own deposit, and neither the NCBI `mellea-OH01` token nor the native GOLD `ELDO17` token adds an eligible local strain.
- The absence of `nomenclature` is consistent with the local source inventory: `data/raw/ncbi_type_material.tsv` has no row for this identifier, and generated `nomenclature` entries currently come from LPSN only.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/armillaria_mellea.yaml`; it is generated and validates strictly.
- Preserve the NCBI exact and related synonyms, retained merged-ID context, count-consistent aggregate GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/armillaria_mellea.yaml` and `just validate-strict data/taxa/eukaryota/armillaria_mellea.yaml` after regenerating the taxon record.

## Additional Notes

- The generated GOLD assertion count is backed by `data/raw/gold_organisms.tsv`, which is an aggregate transformed KG-Microbe GOLD count. The local native GOLD snapshot currently has one inspectable organism for `NCBITaxon:47429`, two projects, and no matching analysis rows.
