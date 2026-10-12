# YAML Record Review: Ascoglobospora marina

## Target

- File: `data/taxa/eukaryota/ascoglobospora_marina.yaml`
- Identifier: `NCBITaxon:2970250`
- Label: `Ascoglobospora marina`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:3126311` / `Ascoglobospora`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `sordariomyceta` -> `Sordariomycetes` -> `Hypocreomycetidae` -> `Microascales` -> `Halosphaeriaceae` -> `Ascoglobospora`
- Existing review report: none found for `*ascoglobospora_marina.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/ascoglobospora_marina.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/ascoglobospora_marina.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:2970250`, labelled `Ascoglobospora marina` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:2970250` is a `SPECIES` child of `NCBITaxon:3126311` / `Ascoglobospora`.
- The generated NCBI synonym block matches the raw NCBI row: it has related synonyms `Ascoglobospora marina Abdel-Wahab, 2024` and `Halosphaeriaceae sp. MAAW-2022a`, with no exact synonyms in the snapshot.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Ascoglobospora marina, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:2970250`, so the generated current identifier is not represented as merged away in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:2970250`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/type-material rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:2970250`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:2970250` with count `1`.
- Exact native GOLD inspection found 0 organism rows for `2970250`, and therefore 0 project or analysis rows, in the local `data/gold/*.jsonl.gz` snapshot.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `2970250`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `2970250`.
- `data/raw/ncbi_type_material.tsv` has four rows for `NCBITaxon:2970250`, covering holotype `CBS H-23855`, `CBS-H-23855`, `CBS:H-23855`, and `CBSH-23855`.
- Exact CBS holotype-token lookups found 0 BacDive rows and 0 StrainInfo rows.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive and StrainInfo have no exact NCBI match, the type-material CBS tokens have no local BacDive or StrainInfo match, and there are no same-taxon organism rows in the local native GOLD snapshot from which to join a BacDive or StrainInfo strain.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/ascoglobospora_marina.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym split, type-material evidence, count-consistent aggregate GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/ascoglobospora_marina.yaml` and `just validate-strict data/taxa/eukaryota/ascoglobospora_marina.yaml` after regenerating the taxon record.

## Additional Notes

- The aggregate GOLD source count of 1 comes from `data/raw/gold_organisms.tsv`; the local native `data/gold/organisms.jsonl.gz` snapshot has no inspectable same-taxon row for `2970250`. This source-snapshot mismatch is not itself a YAML defect when the aggregate file supports the generated count.
