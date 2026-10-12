# YAML Record Review: Apiotrichum gamsii

## Target

- File: `data/taxa/eukaryota/apiotrichum_gamsii.yaml`
- Identifier: `NCBITaxon:1105092`
- Label: `Apiotrichum gamsii`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:105983` / `Apiotrichum`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Basidiomycota` -> `Agaricomycotina` -> `Tremellomycetes` -> `Trichosporonales` -> `Trichosporonaceae` -> `Apiotrichum`
- Existing review report: none found for `*apiotrichum_gamsii.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/apiotrichum_gamsii.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/apiotrichum_gamsii.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:1105092`, labelled `Apiotrichum gamsii` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:1105092` is a `SPECIES` child of `NCBITaxon:105983` / `Apiotrichum`.
- The generated NCBI synonym block matches the raw NCBI row: exact synonym `Trichosporon gamsii` and related synonyms `Apiotrichum gamsii (Middelhoven, Scorzetti, Sigler & Fell) A.M. Yurkov & Boekhout, 2015`, `Trichosporon gamsii Middelhoven, Scorzetti, Sigler & Fell, 2004`, `Trichosporon sp. CBS 8245`, and `Trichosporon sp. CBS8245`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Apiotrichum gamsii, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps old `NCBITaxon:113459` and `NCBITaxon:159131` to the current identifier `NCBITaxon:1105092`.
- A no-ignore, hidden-file search for the bounded identifier `NCBITaxon:1105092` and exact label `Apiotrichum gamsii` found only the generated taxon/page/path rows, the raw NCBI/GOLD/scope/type-material/merged-ID rows, and page index rows for this record. No duplicate review report was present; ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:1105092`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:1105092` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0138994`, `Apiotrichum gamsii JCM 9941`, strain and culture collection ID `JCM 9941`.
- GOLD organism `Go0138994` has one project, `Gp0144051`, with BioProject `PRJDB3703` and BioSample `SAMD00028424`.
- GOLD project `Gp0144051` is linked to genome analysis `Ga0129235` with GenBank assembly accession `GCA_001600315.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 1 direct strain row for `1105092`, 0 deposit-only rows, and 0 missing exclusions; `straininfo.strain:106997` is excluded locally as `no_eligible_own_deposit_match`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `1105092`.
- `data/raw/ncbi_type_material.tsv` has seven type-material rows for `NCBITaxon:1105092` under the synonym label `Trichosporon gamsii`, including duplicate punctuation variants for `CBS 8245` and `JCM 9941`, plus `BCRC:22274`, `CCRC 22274`, and `CCRC:22274`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks: BacDive has no exact NCBI match, and the exact StrainInfo match is explicitly excluded.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/apiotrichum_gamsii.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonyms, old-ID merge context, type-material evidence, count-consistent one-organism GOLD source attestation, and StrainInfo exclusion behavior when regenerating the record.

## Follow-up Checks

- If the StrainInfo exclusion policy for `no_eligible_own_deposit_match` changes, re-evaluate `straininfo.strain:106997` and check whether it should contribute to `strain_count`.
- Rerun `just validate data/taxa/eukaryota/apiotrichum_gamsii.yaml` and `just validate-strict data/taxa/eukaryota/apiotrichum_gamsii.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Apiotrichum gamsii JCM 9941` is project-linked through `AP PROJECT GOLD IDS = Gp0144051`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
