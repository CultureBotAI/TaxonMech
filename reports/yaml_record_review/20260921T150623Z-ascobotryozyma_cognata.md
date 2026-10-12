# YAML Record Review: Ascobotryozyma cognata

## Target

- File: `data/taxa/eukaryota/ascobotryozyma_cognata.yaml`
- Identifier: `NCBITaxon:219604`
- Label: `Ascobotryozyma cognata`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:2835221` / `Ascobotryozyma`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Saccharomycotina` -> `Trigonopsidomycetes` -> `Trigonopsidales` -> `Trigonopsidaceae` -> `Ascobotryozyma`
- Existing review report: none found for `*ascobotryozyma_cognata.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/ascobotryozyma_cognata.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/ascobotryozyma_cognata.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:219604`, labelled `Ascobotryozyma cognata` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:219604` is a `SPECIES` child of `NCBITaxon:2835221` / `Ascobotryozyma`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonym `Botryozyma cognata` and related synonyms `Ascobotryozyma cognata J. Kerrigan, M.T. Sm. & J.D. Rogers, 2003` and `Botryozyma cognata J. Kerrigan, M.T. Sm. & J.D. Rogers ex Lachance & Kurtzman, 2013`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Ascobotryozyma cognata, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:219604`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:219604`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/type-material rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:219604`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:219604` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0705155`, `Ascobotryozyma cognata CBS 8753`, with strain and culture collection ID `CBS 8753`.
- GOLD organism `Go0705155` has one project, `Gp0831178`, with BioProject `PRJNA736342` and BioSample `SAMN20341234`; the local native GOLD snapshot has no analysis rows attached directly through `AP ORGANISM GOLD ID` or indirectly through `AP PROJECT GOLD IDS`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `219604`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `219604`.
- `data/raw/ncbi_type_material.tsv` has two holotype rows for `NCBITaxon:219604`, spelling the same specimen as `WSP 70305` and `WSP:70305`.
- Exact `CBS 8753` and `WSP 70305` token lookups found 0 BacDive rows and one StrainInfo near miss, `straininfo.strain:179681`, classified only to genus-level `NCBITaxon:44069` / `Botryozyma` and carrying no genome sequences.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive and StrainInfo have no exact NCBI match, the native GOLD `CBS 8753` token does not add an eligible local BacDive or exact StrainInfo strain, and the single `CBS 8753` StrainInfo near miss is genus-level only.
- The NCBI holotype rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/ascobotryozyma_cognata.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym split, holotype evidence, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/ascobotryozyma_cognata.yaml` and `just validate-strict data/taxa/eukaryota/ascobotryozyma_cognata.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD project for `Ascobotryozyma cognata CBS 8753` currently has no matching analysis row in `data/gold/analyses.jsonl.gz`, so there are no GOLD genome accessions to reconcile for this record.
