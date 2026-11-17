# YAML Record Review: Armillaria borealis

## Target

- File: `data/taxa/eukaryota/armillaria_borealis.yaml`
- Identifier: `NCBITaxon:47425`
- Label: `Armillaria borealis`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:47424` / `Armillaria`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Basidiomycota` -> `Agaricomycotina` -> `Agaricomycetes` -> `Agaricomycetidae` -> `Agaricales` -> `Marasmiineae` -> `Physalacriaceae` -> `Armillaria`
- Existing review report: none found for `*armillaria_borealis.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/armillaria_borealis.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/armillaria_borealis.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:47425`, labelled `Armillaria borealis` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:47425` is a `SPECIES` child of `NCBITaxon:47424` / `Armillaria`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms and two related synonyms, `Armillaria borealis Marxm. & Korhonen, 1982` and `northern honey fungus`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Armillaria borealis, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:47425`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:47425`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/type-material rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:47425`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:47425` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0403317`, `Armillaria borealis FPL87.14`, strain `FPL87.14`, and no culture collection ID.
- GOLD organism `Go0403317` has two projects: `Gp0295055` with BioProject `PRJNA519844` and BioSample `SAMN10865534`, and `Gp0304610` with BioProject `PRJNA519861` and BioSample `SAMN10865533`.
- GOLD project `Gp0304610` is linked to genome analysis `Ga0264383`; the analysis has no GenBank assembly accession in the native snapshot.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 11 direct strain rows for `47425`, all already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `47425`.
- An exact `FPL87.14` token lookup found 0 BacDive rows and 0 StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has two type-material rows for `NCBITaxon:47425`, spelling the same collection as `CBS 155.83` and `CBS:155.83`.
- A `CBS 155.83` / `CBS:155.83` token lookup found one StrainInfo row, `straininfo.strain:154346`; it is one of the excluded exact-NCBI StrainInfo rows and does not imply a missing generated strain.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, the 11 exact StrainInfo rows are all excluded because they have no eligible own deposit, and neither the GOLD `FPL87.14` token nor the NCBI `CBS 155.83` type-material token adds an eligible local strain.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/armillaria_borealis.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonyms, type-material evidence, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/armillaria_borealis.yaml` and `just validate-strict data/taxa/eukaryota/armillaria_borealis.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Armillaria borealis FPL87.14` is project-linked through `AP PROJECT GOLD IDS = Gp0304610`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
