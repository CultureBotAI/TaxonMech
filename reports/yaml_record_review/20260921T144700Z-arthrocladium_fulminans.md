# YAML Record Review: Arthrocladium fulminans

## Target

- File: `data/taxa/eukaryota/arthrocladium_fulminans.yaml`
- Identifier: `NCBITaxon:1758292`
- Label: `Arthrocladium fulminans`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:1758290` / `Arthrocladium`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `Eurotiomycetes` -> `Chaetothyriomycetidae` -> `Chaetothyriales` -> `Trichomeriaceae` -> `Arthrocladium`
- Existing review report: none found for `*arthrocladium_fulminans.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/arthrocladium_fulminans.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/arthrocladium_fulminans.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:1758292`, labelled `Arthrocladium fulminans` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:1758292` is a `SPECIES` child of `NCBITaxon:1758290` / `Arthrocladium`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms and one related synonym, `Arthrocladium fulminans Nascimento, Vicente & de Hoog, 2015`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Arthrocladium fulminans, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:1758292`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:1758292`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/type-material rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:1758292`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:1758292` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0517214`, `Arthrocladium fulminans CBS 136243`, strain and culture collection ID `CBS 136243`.
- GOLD organism `Go0517214` has one project, `Gp0441254`, with BioProject `PRJNA485507` and BioSample `SAMN09808970`.
- GOLD project `Gp0441254` is linked to genome analysis `Ga0656527` with GenBank assembly accession `GCA_003614865.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 1 direct strain row for `1758292`, already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `1758292`.
- `data/raw/ncbi_type_material.tsv` has two culture-from-holotype rows for `NCBITaxon:1758292`, spelling the same accession as `CBS 136243` and `CBS:136243`.
- Exact `CBS 136243` token lookups found 0 BacDive rows and 0 StrainInfo rows.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, the one exact StrainInfo row is already excluded, and neither the NCBI type-culture token nor the native GOLD `CBS 136243` token adds an eligible local strain.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/arthrocladium_fulminans.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonym, type-material evidence, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/arthrocladium_fulminans.yaml` and `just validate-strict data/taxa/eukaryota/arthrocladium_fulminans.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Arthrocladium fulminans CBS 136243` is project-linked through `AP PROJECT GOLD IDS = Gp0441254`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
