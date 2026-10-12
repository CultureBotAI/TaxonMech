# YAML Record Review: Arthrinium puccinioides

## Target

- File: `data/taxa/eukaryota/arthrinium_puccinioides.yaml`
- Identifier: `NCBITaxon:335850`
- Label: `Arthrinium puccinioides`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:112177` / `Arthrinium`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `sordariomyceta` -> `Sordariomycetes` -> `Xylariomycetidae` -> `Amphisphaeriales` -> `Apiosporaceae` -> `Arthrinium`
- Existing review report: none found for `*arthrinium_puccinioides.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/arthrinium_puccinioides.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/arthrinium_puccinioides.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:335850`, labelled `Arthrinium puccinioides` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:335850` is a `SPECIES` child of `NCBITaxon:112177` / `Arthrinium`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms and one related synonym, `Arthrinium puccinioides Kunze & J.C. Schmidt, 1823`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Arthrinium puccinioides, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:335850`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:335850`.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:335850`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:335850`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:335850` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0681842`, `Arthrinium puccinioides CBS 549.89`, strain `CBS 549.89`, and culture collection ID `CBS:549.89`.
- GOLD organism `Go0681842` has one project, `Gp0783899`, with BioProject `PRJNA764836` and BioSample `SAMN21529904`.
- GOLD project `Gp0783899` is linked to genome analysis `Ga0663214` with GenBank assembly accession `GCA_022414665.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 2 direct strain rows for `335850`, both already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `335850`.
- A `CBS 549.89` token lookup found 0 BacDive rows and one StrainInfo row for `Volutella consors`, not for `Arthrinium puccinioides`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, the two exact StrainInfo rows are already excluded, and the native GOLD `CBS 549.89` token does not add an eligible local strain.
- The absence of `nomenclature` is consistent with the local source inventory: `data/raw/ncbi_type_material.tsv` has no row for this identifier, and generated `nomenclature` entries currently come from LPSN only.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/arthrinium_puccinioides.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonym, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/arthrinium_puccinioides.yaml` and `just validate-strict data/taxa/eukaryota/arthrinium_puccinioides.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Arthrinium puccinioides CBS 549.89` is project-linked through `AP PROJECT GOLD IDS = Gp0783899`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
