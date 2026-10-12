# YAML Record Review: Apiotrichum gracile

## Target

- File: `data/taxa/eukaryota/apiotrichum_gracile.yaml`
- Identifier: `NCBITaxon:82516`
- Label: `Apiotrichum gracile`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:105983` / `Apiotrichum`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Basidiomycota` -> `Agaricomycotina` -> `Tremellomycetes` -> `Trichosporonales` -> `Trichosporonaceae` -> `Apiotrichum`
- Existing review report: none found for `*apiotrichum_gracile.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/apiotrichum_gracile.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/apiotrichum_gracile.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:82516`, labelled `Apiotrichum gracile` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:82516` is a `SPECIES` child of `NCBITaxon:105983` / `Apiotrichum`.
- The generated NCBI synonym block matches the raw NCBI row: exact synonyms `Geotrichum gracile`, `Oidium gracile`, `Oospora gracilis`, and `Trichosporon gracile`, plus related synonyms `Apiotrichum gracile (Weigmann & A. Wolff) A.M. Yurkov & Boekhout, 2015`, `Oidium gracile Weigmann & A. Wolff, 1909`, and `Trichosporon gracile (Weigmann & A. Wolff) E. Guho & M.T. Sm., 1992`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Apiotrichum gracile, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:82516`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A no-ignore, hidden-file search for the bounded identifier `NCBITaxon:82516` and exact label `Apiotrichum gracile` found only the generated taxon/page/path rows, the raw NCBI/GOLD/scope/type-material rows, and page index rows for this record. No duplicate review report was present; ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:82516`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:82516` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0138935`, `Apiotrichum gracile JCM 10018`, strain and culture collection ID `JCM 10018`.
- GOLD organism `Go0138935` has one project, `Gp0143992`, with BioProject `PRJDB3704` and BioSample `SAMD00028425`.
- GOLD project `Gp0143992` is linked to genome analysis `Ga0129225` with GenBank assembly accession `GCA_001600335.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 11 direct strain rows for `82516`, 0 deposit-only rows, and 0 missing exclusions; all 11 direct IDs are excluded locally as `no_eligible_own_deposit_match`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `82516`.
- `data/raw/ncbi_type_material.tsv` has two type-material rows for `NCBITaxon:82516`: duplicate punctuation variants of culture from type material `CBS 8189` / `CBS:8189` under the synonym label `Oidium gracile`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks: BacDive has no exact NCBI match, and all exact StrainInfo matches are explicitly excluded.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/apiotrichum_gracile.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonyms, type-material evidence, count-consistent one-organism GOLD source attestation, and StrainInfo exclusion behavior when regenerating the record.

## Follow-up Checks

- If the StrainInfo exclusion policy for `no_eligible_own_deposit_match` changes, re-evaluate the 11 excluded StrainInfo rows for `NCBITaxon:82516` and check whether any should contribute to `strain_count`.
- Rerun `just validate data/taxa/eukaryota/apiotrichum_gracile.yaml` and `just validate-strict data/taxa/eukaryota/apiotrichum_gracile.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Apiotrichum gracile JCM 10018` is project-linked through `AP PROJECT GOLD IDS = Gp0143992`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
