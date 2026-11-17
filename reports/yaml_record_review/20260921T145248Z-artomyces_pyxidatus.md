# YAML Record Review: Artomyces pyxidatus

## Target

- File: `data/taxa/eukaryota/artomyces_pyxidatus.yaml`
- Identifier: `NCBITaxon:48021`
- Label: `Artomyces pyxidatus`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:182276` / `Artomyces`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Basidiomycota` -> `Agaricomycotina` -> `Agaricomycetes` -> `Agaricomycetes incertae sedis` -> `Russulales` -> `Auriscalpiaceae` -> `Artomyces`
- Existing review report: none found for `*artomyces_pyxidatus.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/artomyces_pyxidatus.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/artomyces_pyxidatus.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:48021`, labelled `Artomyces pyxidatus` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:48021` is a `SPECIES` child of `NCBITaxon:182276` / `Artomyces`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonyms `Artomyces pyxidata`, `Clavaria pyxidata`, and `Clavicorona pyxidata`, plus related synonyms `Artomyces pyxidatus (Pers.) Julich, 1982` and `Clavaria pyxidata Pers., 1794`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Artomyces pyxidatus, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps old identifier `NCBITaxon:1738081` into `NCBITaxon:48021`; it has no row mapping `NCBITaxon:48021` to another target, so the generated current identifier is not represented as merged away in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:48021`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/merged-ID rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:48021`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:48021` with count `2`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0072265`, `Artomyces pyxidatus HHB10654`. The aggregate GOLD count of 2 in `data/raw/gold_organisms.tsv` is therefore not fully replayable from the committed native GOLD organism snapshot, but the generated YAML follows the maintained aggregate raw inventory.
- GOLD organism `Go0072265` has two projects, `Gp0072265` with BioProject `PRJNA239090` and BioSample `SAMN02745582`, and `Gp0072266` with BioProject `PRJNA251065` and BioSample `SAMN03003469`.
- GOLD project `Gp0072265` is linked to genome analysis `Ga0226782`, which has IMG taxon ID `2761201804` and an empty `AP_GENBANK` list.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 9 direct strain rows for `48021`, all already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `48021`.
- `data/raw/ncbi_type_material.tsv` has no rows for `NCBITaxon:48021`.
- Exact `HHB10654` token lookups found 0 BacDive rows and 0 StrainInfo rows.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, all exact StrainInfo rows are already excluded, and the native GOLD `HHB10654` token does not add an eligible local BacDive or StrainInfo strain.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/artomyces_pyxidatus.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym split, count-consistent two-organism aggregate GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/artomyces_pyxidatus.yaml` and `just validate-strict data/taxa/eukaryota/artomyces_pyxidatus.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD row visible for `NCBITaxon:48021` is one organism behind a maintained aggregate count of 2. This is an upstream snapshot/accounting distinction between `data/raw/gold_organisms.tsv` and `data/gold/organisms.jsonl.gz`, not a defect in the generated YAML.
- The native GOLD analysis for `Artomyces pyxidatus HHB10654` is project-linked through `AP PROJECT GOLD IDS = Gp0072265`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
