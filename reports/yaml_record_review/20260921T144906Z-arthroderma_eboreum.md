# YAML Record Review: Arthroderma eboreum

## Target

- File: `data/taxa/eukaryota/arthroderma_eboreum.yaml`
- Identifier: `NCBITaxon:310283`
- Label: `Arthroderma eboreum`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:63399` / `Arthroderma`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `Eurotiomycetes` -> `Eurotiomycetidae` -> `Onygenales` -> `Arthrodermataceae` -> `Arthroderma`
- Existing review report: none found for `*arthroderma_eboreum.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/arthroderma_eboreum.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/arthroderma_eboreum.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:310283`, labelled `Arthroderma eboreum` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:310283` is a `SPECIES` child of `NCBITaxon:63399` / `Arthroderma`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonym `Trichophyton eboreum` and related synonyms `Arthroderma eboreum (Brasch & Y. Graser) Y. Graser & de Hoog, 2018` and `Trichophyton eboreum Brasch & Y. Graser, 2005`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Arthroderma eboreum, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:310283`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:310283`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/type-material rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:310283`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:310283` with count `3`.
- Exact native GOLD inspection found the same three organism rows for the same taxon: `Go0628282` / `Trichophyton eboreum DSM 16978`, `Go0628283` / `Trichophyton eboreum CBS 117155`, and `Go0628284` / `Trichophyton eboreum 367/04`.
- The local native GOLD snapshot has 0 project rows for those organism IDs and 0 analysis rows attached directly through `AP ORGANISM GOLD ID` or indirectly through `AP PROJECT GOLD IDS`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 1 direct strain row for `310283`, already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `310283`.
- `data/raw/ncbi_type_material.tsv` has four type-material rows for `NCBITaxon:310283`, covering `CBS 117155`, `CBS:117155`, `DSM 16978`, and `DSM:16978`.
- Exact `CBS 117155`, `DSM 16978`, and `367/04` token lookups found 0 BacDive rows and only the same excluded StrainInfo row, `straininfo.strain:281027`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, the one exact StrainInfo row is already excluded, and the native GOLD organism tokens do not add eligible local BacDive or StrainInfo strains.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/arthroderma_eboreum.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym split, type-material evidence, count-consistent three-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/arthroderma_eboreum.yaml` and `just validate-strict data/taxa/eukaryota/arthroderma_eboreum.yaml` after regenerating the taxon record.

## Additional Notes

- The three native GOLD organism rows currently have no project or analysis rows in the local native GOLD snapshot, so there are no GOLD genome accessions to reconcile for this record.
