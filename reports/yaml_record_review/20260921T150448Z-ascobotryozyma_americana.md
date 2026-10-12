# YAML Record Review: Ascobotryozyma americana

## Target

- File: `data/taxa/eukaryota/ascobotryozyma_americana.yaml`
- Identifier: `NCBITaxon:219603`
- Label: `Ascobotryozyma americana`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:2835221` / `Ascobotryozyma`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Saccharomycotina` -> `Trigonopsidomycetes` -> `Trigonopsidales` -> `Trigonopsidaceae` -> `Ascobotryozyma`
- Existing review report: none found for `*ascobotryozyma_americana.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/ascobotryozyma_americana.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/ascobotryozyma_americana.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:219603`, labelled `Ascobotryozyma americana` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:219603` is a `SPECIES` child of `NCBITaxon:2835221` / `Ascobotryozyma`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonym `Botryozyma americana J. Kerrigan, M.T. Sm. & J.D. Rogers, 2001` and related synonym `Ascobotryozyma americana J. Kerrigan, M.T. Sm. & J.D. Rogers, 2001`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Ascobotryozyma americana, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:219603`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:219603`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/type-material rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:219603`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:219603` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0705146`, `Ascobotryozyma americana CBS 8560`, with strain and culture collection ID `CBS 8560`.
- GOLD organism `Go0705146` has one project, `Gp0831169`, with BioProject `PRJNA736342` and BioSample `SAMN20341230`; the local native GOLD snapshot has no analysis rows attached directly through `AP ORGANISM GOLD ID` or indirectly through `AP PROJECT GOLD IDS`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 1 direct strain row for `219603` and 1 deposit-only row, both already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `219603`.
- `data/raw/ncbi_type_material.tsv` has four rows for `NCBITaxon:219603`, covering holotype `WSP 70152` / `WSP:70152` and culture-from-isotype `CBS 8560` / `CBS:8560`.
- Exact `CBS 8560` and `WSP 70152` token lookups found 0 BacDive rows and only the same excluded StrainInfo row, `straininfo.strain:179356`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, all exact and deposit-only StrainInfo rows are already excluded, and the native GOLD `CBS 8560` token does not add an eligible local BacDive or StrainInfo strain.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/ascobotryozyma_americana.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym split, type-material evidence, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/ascobotryozyma_americana.yaml` and `just validate-strict data/taxa/eukaryota/ascobotryozyma_americana.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD project for `Ascobotryozyma americana CBS 8560` currently has no matching analysis row in `data/gold/analyses.jsonl.gz`, so there are no GOLD genome accessions to reconcile for this record.
