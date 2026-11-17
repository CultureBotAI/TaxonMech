# YAML Record Review: Armillaria altimontana

## Target

- File: `data/taxa/eukaryota/armillaria_altimontana.yaml`
- Identifier: `NCBITaxon:1156164`
- Label: `Armillaria altimontana`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:47424` / `Armillaria`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Basidiomycota` -> `Agaricomycotina` -> `Agaricomycetes` -> `Agaricomycetidae` -> `Agaricales` -> `Marasmiineae` -> `Physalacriaceae` -> `Armillaria`
- Existing review report: none found for `*armillaria_altimontana.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/armillaria_altimontana.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/armillaria_altimontana.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:1156164`, labelled `Armillaria altimontana` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:1156164` is a `SPECIES` child of `NCBITaxon:47424` / `Armillaria`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms and two related synonyms, `Armillaria altimontana Brazee, B. Ortiz, Banik & D. L. Lindner, 2012` and `Armillaria sp. NJB-2012`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Armillaria altimontana, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:1156164`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:1156164`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/type-material rows, and no duplicate review report. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:1156164`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:1156164` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0677499`, `Armillaria altimontana 837-10`, strain `837-10`, and no culture collection ID.
- GOLD organism `Go0677499` has one project, `Gp0779317`, with BioProject `PRJNA766083` and BioSample `SAMN21618491`.
- GOLD project `Gp0779317` is linked to genome analysis `Ga0663262` with GenBank assembly accession `GCA_022818075.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct or deposit-only strain rows for `1156164`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `1156164`.
- A boundary-aware `837-10` / `CFMR POR100` token lookup found 0 BacDive rows and 0 StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has one type-material row for `NCBITaxon:1156164`: `CFMR POR100`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks: neither source has an exact NCBI match, and neither the GOLD `837-10` token nor the NCBI `CFMR POR100` token joins to either local strain source.
- The NCBI type-material row does not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/armillaria_altimontana.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonyms, type-material evidence, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/armillaria_altimontana.yaml` and `just validate-strict data/taxa/eukaryota/armillaria_altimontana.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Armillaria altimontana 837-10` is project-linked through `AP PROJECT GOLD IDS = Gp0779317`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
