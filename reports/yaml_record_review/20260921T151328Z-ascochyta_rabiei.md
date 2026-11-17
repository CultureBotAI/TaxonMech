# YAML Record Review: Ascochyta rabiei

## Target

- File: `data/taxa/eukaryota/ascochyta_rabiei.yaml`
- Identifier: `NCBITaxon:5454`
- Label: `Ascochyta rabiei`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:5453` / `Ascochyta`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `dothideomyceta` -> `Dothideomycetes` -> `Pleosporomycetidae` -> `Pleosporales` -> `Pleosporineae` -> `Didymellaceae` -> `Ascochyta`
- Existing review report: none found for `*ascochyta_rabiei.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/ascochyta_rabiei.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/ascochyta_rabiei.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:5454`, labelled `Ascochyta rabiei` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:5454` is a `SPECIES` child of `NCBITaxon:5453` / `Ascochyta`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonyms `Didymella rabiei`, `Mycosphaerella rabiei`, `Phoma rabiei`, and `Zythia rabiei`, plus related synonyms `Ascochyta rabiei (Pass.) Labr., 1931`, `Didymella rabiei Kovatsch. ex Arx, 1962`, `Mycosphaerella rabiei Kovatsch. ex Gruyter, 2002`, `Phoma rabiei (Pass.) Khune ex Gruyter, 2002`, and `Zythia rabiei Pass., 1867`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Ascochyta rabiei, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps old identifier `NCBITaxon:547106` into `NCBITaxon:5454`; it has no row mapping `NCBITaxon:5454` to another target, so the generated current identifier is not represented as merged away in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:5454`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/merged-ID/type-material rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:5454`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:5454` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0145234`, `Ascochyta rabiei ArDII`, with strain `ArDII` and culture collection ID `ITCC 4638`.
- GOLD organism `Go0145234` has one project, `Gp0150874`, with BioProject `PRJNA272665` and BioSample `SAMN03284776`.
- GOLD project `Gp0150874` is linked to genome analysis `Ga0133582` with GenBank assembly accession `GCA_001630375.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 10 direct strain rows for `5454`, all already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `5454`.
- `data/raw/ncbi_type_material.tsv` has two rows for `NCBITaxon:5454`, covering culture-from-holotype `CBS 237.37` and `CBS:237.37`.
- Exact `ITCC 4638`, `ITCC:4638`, and `ArDII` token lookups found 0 BacDive rows and 0 StrainInfo rows.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, all exact StrainInfo rows are already excluded, and the native GOLD `ArDII` / `ITCC 4638` tokens do not add an eligible local BacDive or StrainInfo strain.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/ascochyta_rabiei.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym split, type-material evidence, current NCBI identifier, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/ascochyta_rabiei.yaml` and `just validate-strict data/taxa/eukaryota/ascochyta_rabiei.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Ascochyta rabiei ArDII` is project-linked through `AP PROJECT GOLD IDS = Gp0150874`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
