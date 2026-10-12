# YAML Record Review: Ascosphaera apis ARSEF 7405

## Target

- File: `data/taxa/eukaryota/ascosphaera_apis_arsef_7405.yaml`
- Identifier: `NCBITaxon:392613`
- Label: `Ascosphaera apis ARSEF 7405`
- Rank: `STRAIN`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:5105` / `Ascosphaera apis`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `Eurotiomycetes` -> `Eurotiomycetidae` -> `Onygenales` -> `Ascosphaeraceae` -> `Ascosphaera` -> `Ascosphaera apis`
- Existing review report: none found for `*ascosphaera_apis_arsef_7405.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/ascosphaera_apis_arsef_7405.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/ascosphaera_apis_arsef_7405.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI strain `NCBITaxon:392613`, labelled `Ascosphaera apis ARSEF 7405` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:392613` is a `STRAIN` child of `NCBITaxon:5105` / `Ascosphaera apis`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonym `Ascosphaera apis USDA-ARSEF 7405`, with no related synonyms in the snapshot.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Ascosphaera apis ARSEF 7405, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps old identifier `NCBITaxon:1081101` into `NCBITaxon:392613`; it has no row mapping `NCBITaxon:392613` to another target, so the generated current identifier is not represented as merged away in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:392613`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/merged-ID rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:392613`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:392613` with count `1`.
- Exact native GOLD inspection found two organism rows for the same taxon: `Go0002467`, `Ascosphaera apis USDA-ARSEF 7405`, with strain `USDA-ARSEF 7405`, and `Go0039311`, `Ascosphaera apis ARSEF 7405`, with no strain or culture collection ID.
- Native GOLD organism `Go0002467` has one project, `Gp0002467`, with BioProject `PRJNA17285` and BioSample `SAMN00253832`; organism `Go0039311` has one project, `Gp0039311`, with BioProject `PRJNA72725` and BioSample `SAMN04908326`.
- GOLD projects `Gp0002467` and `Gp0039311` are linked to genome analyses `Ga0039218` and `Ga0129553`; `Ga0039218` has GenBank ID `AARE00000000` and no assembly accession, and `Ga0129553` has GenBank assembly accession `GCA_001636715.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `392613`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `392613`.
- Exact `USDA-ARSEF 7405` and `ARSEF 7405` token lookups found 0 BacDive rows and 0 StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:392613`.

## Completeness

- The compact generated record has the expected identifier, label, strain rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of local `strains` is consistent with the source checks: BacDive and StrainInfo have no exact NCBI match, and the native GOLD ARSEF 7405 tokens do not add an eligible local BacDive or StrainInfo strain.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/ascosphaera_apis_arsef_7405.yaml`; it is generated and validates strictly.
- Preserve the NCBI strain rank, exact NCBI synonym, current NCBI identifier, count-consistent aggregate GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/ascosphaera_apis_arsef_7405.yaml` and `just validate-strict data/taxa/eukaryota/ascosphaera_apis_arsef_7405.yaml` after regenerating the taxon record.

## Additional Notes

- The aggregate GOLD source count of 1 comes from `data/raw/gold_organisms.tsv`; the local native `data/gold/organisms.jsonl.gz` snapshot has two inspectable same-taxon organism rows for `392613`. This source-count mismatch is not itself a YAML defect when the aggregate file supports the generated count.
- Both native GOLD genome analyses for this strain are project-linked through `AP PROJECT GOLD IDS`; neither uses `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
