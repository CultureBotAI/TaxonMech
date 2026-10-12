# YAML Record Review: Articulospora tetracladia

## Target

- File: `data/taxa/eukaryota/articulospora_tetracladia.yaml`
- Identifier: `NCBITaxon:253309`
- Label: `Articulospora tetracladia`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:253308` / `Articulospora`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `sordariomyceta` -> `Leotiomycetes` -> `Helotiales` -> `Discinellaceae` -> `Articulospora`
- Existing review report: none found for `*articulospora_tetracladia.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/articulospora_tetracladia.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/articulospora_tetracladia.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:253309`, labelled `Articulospora tetracladia` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:253309` is a `SPECIES` child of `NCBITaxon:253308` / `Articulospora`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms and one related synonym, `Articulospora tetracladia Ingold, 1942`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Articulospora tetracladia, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:253309`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:253309`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:253309`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:253309` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0519043`, `Articulospora tetracladia NNIBRFG329`.
- GOLD organism `Go0519043` has one project, `Gp0443176`, with BioProject `PRJNA445174` and BioSample `SAMN08769848`.
- GOLD project `Gp0443176` is linked to genome analysis `Ga0656486` with GenBank assembly accession `GCA_003415645.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 14 direct strain rows for `253309`, all already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `253309`.
- `data/raw/ncbi_type_material.tsv` has no rows for `NCBITaxon:253309`.
- Exact `NNIBRFG329` token lookups found 0 BacDive rows and 0 StrainInfo rows.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, all exact StrainInfo rows are already excluded, and the native GOLD `NNIBRFG329` token does not add an eligible local BacDive or StrainInfo strain.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/articulospora_tetracladia.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonym, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/articulospora_tetracladia.yaml` and `just validate-strict data/taxa/eukaryota/articulospora_tetracladia.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Articulospora tetracladia NNIBRFG329` is project-linked through `AP PROJECT GOLD IDS = Gp0443176`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
