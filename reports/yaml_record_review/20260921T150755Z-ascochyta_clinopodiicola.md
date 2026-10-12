# YAML Record Review: Ascochyta clinopodiicola

## Target

- File: `data/taxa/eukaryota/ascochyta_clinopodiicola.yaml`
- Identifier: `NCBITaxon:2249482`
- Label: `Ascochyta clinopodiicola`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:5453` / `Ascochyta`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `dothideomyceta` -> `Dothideomycetes` -> `Pleosporomycetidae` -> `Pleosporales` -> `Pleosporineae` -> `Didymellaceae` -> `Ascochyta`
- Existing review report: none found for `*ascochyta_clinopodiicola.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/ascochyta_clinopodiicola.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/ascochyta_clinopodiicola.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:2249482`, labelled `Ascochyta clinopodiicola` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:2249482` is a `SPECIES` child of `NCBITaxon:5453` / `Ascochyta`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms and one related synonym, `Ascochyta clinopodiicola D. Pem, Camporesi & K.D. Hyde, 2018`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Ascochyta clinopodiicola, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:2249482`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:2249482`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/type-material rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:2249482`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:2249482` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0678683`, `Ascochyta clinopodiicola IMI 359910`.
- GOLD organism `Go0678683` has one project, `Gp0780643`, with BioProject `PRJNA786750` and BioSample `SAMN30184420`.
- GOLD project `Gp0780643` is linked to genome analysis `Ga0622600` with GenBank assembly accession `GCA_027946445.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 1 direct strain row for `2249482`, already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `2249482`.
- `data/raw/ncbi_type_material.tsv` has five rows for `NCBITaxon:2249482`, covering culture-from-holotype `MFLUCC 18-0344` / `MFLUCC:18-0344`, holotype `MFLU 17-1034` / `MFLU:17-1034`, and type material `ICMP:21964`.
- Exact `IMI 359910`, `MFLUCC 18-0344`, `MFLU 17-1034`, and `ICMP:21964` token lookups found 0 BacDive rows and 0 StrainInfo rows.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, the one exact StrainInfo row is already excluded, and the native GOLD `IMI 359910` token does not add an eligible local BacDive or StrainInfo strain.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/ascochyta_clinopodiicola.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonym, type-material evidence, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/ascochyta_clinopodiicola.yaml` and `just validate-strict data/taxa/eukaryota/ascochyta_clinopodiicola.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Ascochyta clinopodiicola IMI 359910` is project-linked through `AP PROJECT GOLD IDS = Gp0780643`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
