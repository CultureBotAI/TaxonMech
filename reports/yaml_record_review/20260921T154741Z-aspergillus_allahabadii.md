# YAML Record Review: Aspergillus allahabadii

## Target

- File: `data/taxa/eukaryota/aspergillus_allahabadii.yaml`
- Identifier: `NCBITaxon:1612426`
- Label: `Aspergillus allahabadii`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:2720871` / `Aspergillus subgen. Circumdati`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `Eurotiomycetes` -> `Eurotiomycetidae` -> `Eurotiales` -> `Aspergillaceae` -> `Aspergillus` -> `Aspergillus subgen. Circumdati`
- Existing review report: none found for `*aspergillus_allahabadii.md` under the ignored `reports/yaml_record_review/` tree. A no-ignore, hidden-file search over `reports/yaml_record_review/` for `aspergillus_allahabadii` also found no existing report body that mentioned this slug; ignored files were included.

## Validation

- `just validate data/taxa/eukaryota/aspergillus_allahabadii.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/aspergillus_allahabadii.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:1612426`, labelled `Aspergillus allahabadii` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:1612426` is a `SPECIES` child of `NCBITaxon:2720871` / `Aspergillus subgen. Circumdati`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms, and it preserves the related synonym `Aspergillus allahabadii B.S. Mehrotra & Agnihotri, 1962`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Aspergillus allahabadii, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:1612426`, so the generated current identifier is not represented as merged away in the local raw snapshot.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:1612426`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:1612426` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0108073`, `Aspergillus allahabadii CBS 164.63`, with strain and culture collection ID `CBS 164.63`.
- GOLD organism `Go0108073` has two projects, `Gp0108073` and `Gp0108074`, with BioProjects `PRJNA334020` and `PRJNA459594` and BioSamples `SAMN05446801` and `SAMN09074065`.
- No native GOLD genome analysis rows were linked to `Go0108073` or to either of its projects.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 3 direct strain rows for `1612426`, all already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `1612426`.
- Exact NCBI holotype and GOLD token lookups found 0 BacDive rows and 1 StrainInfo row, `straininfo.strain:74722`, which is already among the excluded exact StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has 14 culture-from-holotype rows for `NCBITaxon:1612426`, covering `ATCC 15055`, `CBS 164.63`, `IMI 139273`, `MUCL 13571`, `NRRL 4539`, `NRRL MOLD 4539`, and `WB 4539` with punctuation variants.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, genetic code, `strain_count`, NCBITaxon and GOLD source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, all exact StrainInfo rows are already excluded, and the GOLD/NCBI holotype token shared with `straininfo.strain:74722` still has no eligible matched local BacDive own deposit.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/aspergillus_allahabadii.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonym, count-consistent aggregate/native GOLD source attestation, NCBI type-material inventory behavior, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/aspergillus_allahabadii.yaml` and `just validate-strict data/taxa/eukaryota/aspergillus_allahabadii.yaml` after regenerating the taxon record.

## Additional Notes

- The three exact StrainInfo rows are independently real source observations for `Aspergillus allahabadii`: `straininfo.strain:74722` has the holotype deposits and aliases `MUCL 13571`, `ATCC 15055`, `IMI 139273`, `CBS 164.63`, `IHEM 5629`, `BCRC 32174`, `CCRC 32174`, `FRR 4849`, and `NRRL 4539`; `straininfo.strain:146172` has `IHEM 2978`; and `straininfo.strain:186916` has `IMI 362227` and `NRRL 4101`. Their exclusion rows are consistent with the generated `strain_count: 0` because none has an eligible matched local BacDive own deposit.
- The NCBI holotype rows are present in the local source inventory, but this generated eukaryotic record has no `nomenclature` block because TaxonMech currently generates `nomenclature` from LPSN rather than from NCBI `typematerial.dmp`.
