# YAML Record Review: Ash witches'-broom phytoplasma

## Target

- File: `data/taxa/bacteria/ash_witches_broom_phytoplasma.yaml`
- Identifier: `NCBITaxon:273034`
- Label: `Ash witches'-broom phytoplasma`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:3042590` / `16SrI (Aster yellows group)`
- Lineage: `root` -> `cellular organisms` -> `Bacteria` -> `Bacillati` -> `Mycoplasmatota` -> `Mollicutes` -> `Acholeplasmatales` -> `Acholeplasmataceae` -> `Candidatus Phytoplasma` -> `16SrI (Aster yellows group)`
- Existing review report: none found for `*ash_witches_broom_phytoplasma.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/bacteria/ash_witches_broom_phytoplasma.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/bacteria/ash_witches_broom_phytoplasma.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:273034`, labelled `Ash witches'-broom phytoplasma` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:273034` is a `SPECIES` child of the 16SrI species group `NCBITaxon:3042590` / `16SrI (Aster yellows group)`.
- The generated record correctly has no NCBI synonym block because the raw NCBI row has no exact or related synonyms in the snapshot.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-13, with the generated reason `attested rule: Ash witches'-broom phytoplasma, 1 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:273034`, so the generated current identifier is not represented as merged away in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:273034`, the exact label, and the exact slug found only the generated taxon and path rows plus the raw NCBI and scope rows. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:273034`.
- `data/raw/gold_organisms.tsv` has no row for `NCBITaxon:273034`, consistent with the absence of a generated `GOLD` source attestation.
- Exact native GOLD inspection found 0 organism rows for `273034`, and therefore 0 project or analysis rows, in the local `data/gold/*.jsonl.gz` snapshot.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `273034`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `273034`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:273034`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, genetic code, `strain_count`, one NCBITaxon source attestation, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive, StrainInfo, and both aggregate and native GOLD have no exact match for `273034`.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/bacteria/ash_witches_broom_phytoplasma.yaml`; it is generated and validates strictly.
- Preserve the species-group parent, NCBI-only source attestation, empty synonym behavior, and empty BacDive/StrainInfo/GOLD behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/bacteria/ash_witches_broom_phytoplasma.yaml` and `just validate-strict data/taxa/bacteria/ash_witches_broom_phytoplasma.yaml` after regenerating the taxon record.

## Additional Notes

- The bounded no-ignore slug search deliberately excluded the longer `angustata_ash_witches_broom_phytoplasma` slug; that path is a different NCBI taxon and did not affect the target record.
