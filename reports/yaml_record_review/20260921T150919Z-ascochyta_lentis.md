# YAML Record Review: Ascochyta lentis

## Target

- File: `data/taxa/eukaryota/ascochyta_lentis.yaml`
- Identifier: `NCBITaxon:205686`
- Label: `Ascochyta lentis`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:5453` / `Ascochyta`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `dothideomyceta` -> `Dothideomycetes` -> `Pleosporomycetidae` -> `Pleosporales` -> `Pleosporineae` -> `Didymellaceae` -> `Ascochyta`
- Existing review report: none found for `*ascochyta_lentis.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/ascochyta_lentis.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/ascochyta_lentis.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:205686`, labelled `Ascochyta lentis` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:205686` is a `SPECIES` child of `NCBITaxon:5453` / `Ascochyta`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonym `Didymella lentis` and related synonyms `Ascochyta lentis Vassiljevsky, 1938` and `Ascochyta lentis Vassiljevsky, 1940`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Ascochyta lentis, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps old identifier `NCBITaxon:547107` into `NCBITaxon:205686`; it has no row mapping `NCBITaxon:205686` to another target, so the generated current identifier is not represented as merged away in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:205686`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/merged-ID rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:205686`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:205686` with count `2`.
- Exact native GOLD inspection found the same two organism rows for the same taxon: `Go0631698` / `Ascochyta lentis Al4` and `Go0676614` / `Ascochyta lentis Kewell`.
- GOLD organism `Go0631698` has project `Gp0645273` with BioProject `PRJNA510691` and BioSample `SAMN10613129`; project `Gp0645273` is linked to genome analysis `Ga0553542` with GenBank assembly accession `GCA_004011705.1`.
- GOLD organism `Go0676614` has project `Gp0778413` with BioProject `PRJNA680004` and BioSample `SAMN16869256`; project `Gp0778413` is linked to genome analysis `Ga0662243` with GenBank assembly accession `GCA_016097375.2`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 6 direct strain rows for `205686`, all already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `205686`.
- `data/raw/ncbi_type_material.tsv` has no rows for `NCBITaxon:205686`.
- Exact `Kewell` and `Ascochyta lentis` token lookups found 0 BacDive rows and only the same excluded StrainInfo rows.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, all exact StrainInfo rows are already excluded, and the native GOLD rows expose only bare `Al4` and `Kewell` strain tokens with no eligible local BacDive or StrainInfo join.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/ascochyta_lentis.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym split, current NCBI identifier, count-consistent two-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/ascochyta_lentis.yaml` and `just validate-strict data/taxa/eukaryota/ascochyta_lentis.yaml` after regenerating the taxon record.

## Additional Notes

- Both native GOLD analyses for `Ascochyta lentis` are project-linked through `AP PROJECT GOLD IDS`; they do not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
