# YAML Record Review: Aspergillus arenarioides

## Target

- File: `data/taxa/eukaryota/aspergillus_arenarioides.yaml`
- Identifier: `NCBITaxon:1507547`
- Label: `Aspergillus arenarioides`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:2720871` / `Aspergillus subgen. Circumdati`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `Eurotiomycetes` -> `Eurotiomycetidae` -> `Eurotiales` -> `Aspergillaceae` -> `Aspergillus` -> `Aspergillus subgen. Circumdati`
- Existing review report: none found for `*aspergillus_arenarioides.md` under the ignored `reports/yaml_record_review/` tree. A no-ignore, hidden-file search over `reports/yaml_record_review/` for `aspergillus_arenarioides` also found no existing report body that mentioned this slug; ignored files were included.

## Validation

- `just validate data/taxa/eukaryota/aspergillus_arenarioides.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/aspergillus_arenarioides.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:1507547`, labelled `Aspergillus arenarioides` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:1507547` is a `SPECIES` child of `NCBITaxon:2720871` / `Aspergillus subgen. Circumdati`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonym `Aspergillus spnov5arenarius`, plus related synonyms `Aspergillus arenarioides Visagie, Hirooka & Samson, 2014` and `Aspergillus sp. 5 CMV-2014`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Aspergillus arenarioides, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:1507547`, so the generated current identifier is not represented as merged away in the local raw snapshot.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:1507547`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:1507547` with count `1`.
- Exact native GOLD inspection found 0 organism rows, 0 project rows, and 0 analysis rows for `1507547` in the local `data/gold/*.jsonl.gz` snapshot.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 1 direct strain row for `1507547`, already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `1507547`.
- Quoted exact JSON-string lookups for the visible NCBI type-material collection numbers found 0 BacDive rows and 0 StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has six rows for `NCBITaxon:1507547`, covering culture from holotype `CBS 138200` and `DTO 268E3` plus holotype `CBS H-21812`, with punctuation variants.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, NCBITaxon and GOLD source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, the exact StrainInfo row is already excluded, and exact quoted collection-token lookups did not reveal an eligible local BacDive or StrainInfo row for the NCBI type-material accessions.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/aspergillus_arenarioides.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym split, aggregate GOLD source attestation, NCBI type-material inventory behavior, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/aspergillus_arenarioides.yaml` and `just validate-strict data/taxa/eukaryota/aspergillus_arenarioides.yaml` after regenerating the taxon record.

## Additional Notes

- The local native GOLD snapshot has no inspectable organism row for `NCBITaxon:1507547`; the generated record only attests the aggregate GOLD organism count already present in `data/raw/gold_organisms.tsv`.
- The exact StrainInfo row is an independently real source observation for `Aspergillus arenarioides`: `straininfo.strain:18803` has available `IHEM 27117`. Its exclusion row is consistent with the generated `strain_count: 0` because it has no eligible matched local BacDive own deposit.
- The NCBI type-material rows are present in the local source inventory, but this generated eukaryotic record has no `nomenclature` block because TaxonMech currently generates `nomenclature` from LPSN rather than from NCBI `typematerial.dmp`.
