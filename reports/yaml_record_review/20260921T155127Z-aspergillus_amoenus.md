# YAML Record Review: Aspergillus amoenus

## Target

- File: `data/taxa/eukaryota/aspergillus_amoenus.yaml`
- Identifier: `NCBITaxon:1220191`
- Label: `Aspergillus amoenus`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:5052` / `Aspergillus`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `Eurotiomycetes` -> `Eurotiomycetidae` -> `Eurotiales` -> `Aspergillaceae` -> `Aspergillus`
- Existing review report: none found for `*aspergillus_amoenus.md` under the ignored `reports/yaml_record_review/` tree. A no-ignore, hidden-file search over `reports/yaml_record_review/` for `aspergillus_amoenus` also found no existing report body that mentioned this slug; ignored files were included.

## Validation

- `just validate data/taxa/eukaryota/aspergillus_amoenus.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/aspergillus_amoenus.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:1220191`, labelled `Aspergillus amoenus` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:1220191` is a `SPECIES` child of `NCBITaxon:5052` / `Aspergillus`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms, and it preserves the related synonym `Aspergillus amoenus M. Roberg, 1931`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Aspergillus amoenus, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:1220191`, so the generated current identifier is not represented as merged away in the local raw snapshot.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:1220191`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:1220191` with count `3`.
- Exact native GOLD inspection found two organism rows for the same taxon: `Go0109131`, `Aspergillus amoenus CBS 111.32`, and `Go0657700`, `Aspergillus amoenus S2904`.
- Native GOLD has three project rows: standard-draft and transcriptome projects for `CBS 111.32`, with BioProjects `PRJNA333824` and `PRJNA459673`, and project `Gp0701968` for `S2904`, with BioProject `PRJNA833221`.
- Project `Gp0701968` links to native GOLD genome analysis `Ga0663629`, `Aspergillus amoenus S2904`, through `AP PROJECT GOLD IDS`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 2 direct strain rows and 1 deposit-only row for `1220191`; all 3 rows are already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `1220191`.
- Quoted exact JSON-string lookups for the visible NCBI type-material and native GOLD collection numbers found 0 BacDive rows.
- `data/raw/ncbi_type_material.tsv` has 10 rows for `NCBITaxon:1220191`, covering culture from holotype `NRRL 4838` and type material `CBS 111.32`, `IMI 211400`, and `NRRL 236`, with punctuation variants.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, genetic code, `strain_count`, NCBITaxon and GOLD source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, all exact StrainInfo direct/deposit rows are already excluded, and exact quoted collection-token lookups did not reveal an eligible local BacDive own deposit for the GOLD or NCBI type-material accessions.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/aspergillus_amoenus.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonym, aggregate GOLD source attestation, NCBI type-material inventory behavior, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/aspergillus_amoenus.yaml` and `just validate-strict data/taxa/eukaryota/aspergillus_amoenus.yaml` after regenerating the taxon record.

## Additional Notes

- The aggregate GOLD count in `data/raw/gold_organisms.tsv` is 3 while this local native GOLD snapshot exposes 2 exact organism rows. The generated record only attests the transformed aggregate count, so this native-snapshot mismatch is useful provenance rather than a YAML defect.
- The two direct StrainInfo rows are independently real source observations for `Aspergillus amoenus`: `straininfo.strain:220102` has `ICMP 1045`, and `straininfo.strain:230366` has `ICMP 1047`. The deposit-only row, `straininfo.strain:75692`, is labelled `Aspergillus versicolor` but has `ICMP 7592` and `DSM 1943` deposits under `NCBITaxon:1220191`. All three exclusion rows are consistent with the generated `strain_count: 0` because none has an eligible matched local BacDive own deposit.
- The NCBI type-material rows are present in the local source inventory, but this generated eukaryotic record has no `nomenclature` block because TaxonMech currently generates `nomenclature` from LPSN rather than from NCBI `typematerial.dmp`.
