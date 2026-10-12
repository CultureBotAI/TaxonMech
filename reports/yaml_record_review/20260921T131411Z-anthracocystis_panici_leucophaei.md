# YAML Record Review: Anthracocystis panici-leucophaei

## Target

- File: `data/taxa/eukaryota/anthracocystis_panici_leucophaei.yaml`
- Identifier: `NCBITaxon:249478`
- Label: `Anthracocystis panici-leucophaei`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:1392992` / `Anthracocystis`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Basidiomycota` -> `Ustilaginomycotina` -> `Ustilaginomycetes` -> `Ustilaginales` -> `Ustilaginaceae` -> `Anthracocystis`
- Existing review report: none found for `*anthracocystis_panici_leucophaei.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/anthracocystis_panici_leucophaei.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/anthracocystis_panici_leucophaei.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:249478`, labelled `Anthracocystis panici-leucophaei` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:249478` is a `SPECIES` child of `NCBITaxon:1392992` / `Anthracocystis`.
- The generated NCBI synonym block matches the raw NCBI row: six exact synonyms from the raw synonym column and four authority-bearing related synonyms from the raw equivalent-name column.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Anthracocystis panici-leucophaei, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps old `NCBITaxon:307807` to the current identifier `NCBITaxon:249478`.
- A no-ignore, hidden-file search for the bounded identifier `NCBITaxon:249478` and exact label `Anthracocystis panici-leucophaei` found only the generated taxon/page/path rows, the raw NCBI/GOLD/scope/type-material/merged-ID rows, and the page index rows for this record. No duplicate review report was present; ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:249478`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:249478` with count `1`.
- Exact native GOLD inspection found one current organism row for the same taxon: `Go0591117`, `Anthracocystis panici-leucophaei SPL10`, strain `SPL10`.
- The native GOLD organism has project `Gp0605062` with BioProject `PRJNA648134` and BioSample `SAMN15629615`.
- The native GOLD project is linked to genome analysis `Ga0661563`, whose GenBank accessions all use assembly accession `GCA_014826065.1`.
- Exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `249478`; there were therefore 0 local StrainInfo exclusions to account for.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `249478`.
- `data/raw/ncbi_type_material.tsv` has one type-material row for `NCBITaxon:249478`: `holotype` `58832a (DAR)` under the synonym label `Lundquistia fascicularis`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks.
- The GOLD organism carries only the native strain name `SPL10` and no `ORGANISM CULTURE COLLECTION ID`, so there is no inspectable local culture-collection token that would be expected to join through the BacDive-derived strain inventory.
- The NCBI type-material row does not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/anthracocystis_panici_leucophaei.yaml`; it is generated and validates strictly.
- Preserve the current NCBI synonyms, old-ID merge context, and count-consistent GOLD source attestation when regenerating the record.

## Follow-up Checks

- If a future GOLD refresh adds a culture collection identifier for organism `Go0591117`, check whether the token joins against BacDive-derived local strain inventory and whether `strain_count` should become nonzero.
- Rerun `just validate data/taxa/eukaryota/anthracocystis_panici_leucophaei.yaml` and `just validate-strict data/taxa/eukaryota/anthracocystis_panici_leucophaei.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis is project-linked through `AP PROJECT GOLD IDS = Gp0605062`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
