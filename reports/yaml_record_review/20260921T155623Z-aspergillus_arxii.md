# YAML Record Review: Aspergillus arxii

## Target

- File: `data/taxa/eukaryota/aspergillus_arxii.yaml`
- Identifier: `NCBITaxon:1131534`
- Label: `Aspergillus arxii`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:2720873` / `Aspergillus subgen. Cremei`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `Eurotiomycetes` -> `Eurotiomycetidae` -> `Eurotiales` -> `Aspergillaceae` -> `Aspergillus` -> `Aspergillus subgen. Cremei`
- Existing review report: none found for `*aspergillus_arxii.md` under the ignored `reports/yaml_record_review/` tree. A no-ignore, hidden-file search over `reports/yaml_record_review/` for `aspergillus_arxii` also found no existing report body that mentioned this slug; ignored files were included.

## Validation

- `just validate data/taxa/eukaryota/aspergillus_arxii.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/aspergillus_arxii.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:1131534`, labelled `Aspergillus arxii` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:1131534` is a `SPECIES` child of `NCBITaxon:2720873` / `Aspergillus subgen. Cremei`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonym `Cristaspora arxii`, plus related synonyms `Aspergillus arxii (Fort & Guarro) Houbraken, Visagie & Samson, 2014` and `Cristaspora arxii Fort & Guarro 1984`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Aspergillus arxii, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:1131534`, so the generated current identifier is not represented as merged away in the local raw snapshot.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:1131534`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:1131534` with count `1`.
- Exact native GOLD inspection found 0 organism rows, 0 project rows, and 0 analysis rows for `1131534` in the local `data/gold/*.jsonl.gz` snapshot.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 2 direct strain rows for `1131534`, both already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `1131534`.
- Quoted exact JSON-string lookups for the visible NCBI type-material collection numbers found 0 BacDive rows and two StrainInfo rows, both already excluded.
- `data/raw/ncbi_type_material.tsv` has six rows for `NCBITaxon:1131534`, covering `Cristaspora arxii` type material `ATCC 52744`, `CBS 525.83`, and `FMR 416`, with punctuation variants.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, NCBITaxon and GOLD source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, both exact StrainInfo rows are already excluded, and exact quoted collection-token lookups did not reveal an eligible local BacDive own deposit for the NCBI type-material accessions.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/aspergillus_arxii.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym split, aggregate GOLD source attestation, NCBI type-material inventory behavior for `Cristaspora arxii`, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/aspergillus_arxii.yaml` and `just validate-strict data/taxa/eukaryota/aspergillus_arxii.yaml` after regenerating the taxon record.

## Additional Notes

- The local native GOLD snapshot has no inspectable organism row for `NCBITaxon:1131534`; the generated record only attests the aggregate GOLD organism count already present in `data/raw/gold_organisms.tsv`.
- The two exact StrainInfo rows are independently real source observations for `Aspergillus arxii`: `straininfo.strain:171582` has `CBS 525.83`, `ATCC 52744`, and `UAMH 6051`, while `straininfo.strain:186969` has `IMI 281205`. Their exclusion rows are consistent with the generated `strain_count: 0` because neither has an eligible matched local BacDive own deposit.
- The NCBI type-material rows are present in the local source inventory, but this generated eukaryotic record has no `nomenclature` block because TaxonMech currently generates `nomenclature` from LPSN rather than from NCBI `typematerial.dmp`.
