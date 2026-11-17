# YAML Record Review: Apiotrichum domesticum

## Target

- File: `data/taxa/eukaryota/apiotrichum_domesticum.yaml`
- Identifier: `NCBITaxon:82514`
- Label: `Apiotrichum domesticum`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:105983` / `Apiotrichum`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Basidiomycota` -> `Agaricomycotina` -> `Tremellomycetes` -> `Trichosporonales` -> `Trichosporonaceae` -> `Apiotrichum`
- Existing review report: none found for `*apiotrichum_domesticum.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/apiotrichum_domesticum.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/apiotrichum_domesticum.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:82514`, labelled `Apiotrichum domesticum` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:82514` is a `SPECIES` child of `NCBITaxon:105983` / `Apiotrichum`.
- The generated NCBI synonym block matches the raw NCBI row: exact synonym `Trichosporon domesticum` and related synonyms `Apiotrichum domesticum (Sugita, A. Nishikawa & Shinoda) A.M. Yurkov & Boekhout, 2015` and `Trichosporon domesticum Sugita, A. Nishikawa & Shinoda, 1995`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Apiotrichum domesticum, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:82514`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A no-ignore, hidden-file search for the bounded identifier `NCBITaxon:82514` and exact label `Apiotrichum domesticum` found only the generated taxon/page/path rows, the raw NCBI/GOLD/scope/type-material rows, and page index rows for this record. No duplicate review report was present; ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:82514`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:82514` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0144228`, `Apiotrichum domesticum JCM 9580`, strain and culture collection ID `JCM 9580`.
- GOLD organism `Go0144228` has one project, `Gp0149825`, with BioProject `PRJDB3573` and BioSample `SAMD00028323`.
- GOLD project `Gp0149825` is linked to genome analysis `Ga0133589` with GenBank assembly accession `GCA_001599015.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 4 direct strain rows for `82514`, 0 deposit-only rows, and 0 missing exclusions; all four source IDs, `straininfo.strain:65900`, `straininfo.strain:179512`, `straininfo.strain:201075`, and `straininfo.strain:203470`, are excluded locally as `no_eligible_own_deposit_match`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `82514`.
- `data/raw/ncbi_type_material.tsv` has six type-material rows for `NCBITaxon:82514` under the synonym label `Trichosporon domesticum`: duplicate punctuation variants of culture from type material `CBS 8280` / `CBS:8280`, type material `JCM 9580` / `JCM:9580`, and type material `NCYC 2665` / `NCYC:2665`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks: BacDive has no exact NCBI match, and all exact StrainInfo matches are explicitly excluded.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/apiotrichum_domesticum.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonyms, type-material evidence, count-consistent one-organism GOLD source attestation, and StrainInfo exclusion behavior when regenerating the record.

## Follow-up Checks

- If the StrainInfo exclusion policy for `no_eligible_own_deposit_match` changes, re-evaluate the four excluded StrainInfo rows for `NCBITaxon:82514` and check whether any should contribute to `strain_count`.
- Rerun `just validate data/taxa/eukaryota/apiotrichum_domesticum.yaml` and `just validate-strict data/taxa/eukaryota/apiotrichum_domesticum.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Apiotrichum domesticum JCM 9580` is project-linked through `AP PROJECT GOLD IDS = Gp0149825`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
