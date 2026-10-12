# YAML Record Review: Aspergillus aculeatinus

## Target

- File: `data/taxa/eukaryota/aspergillus_aculeatinus.yaml`
- Identifier: `NCBITaxon:487661`
- Label: `Aspergillus aculeatinus`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:2720871` / `Aspergillus subgen. Circumdati`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `Eurotiomycetes` -> `Eurotiomycetidae` -> `Eurotiales` -> `Aspergillaceae` -> `Aspergillus` -> `Aspergillus subgen. Circumdati`
- Existing review report: none found for `*aspergillus_aculeatinus.md` under the ignored `reports/yaml_record_review/` tree. A no-ignore, hidden-file search over `reports/yaml_record_review/` for `aspergillus_aculeatinus` also found no existing report body that mentioned this slug; ignored files were included.

## Validation

- `just validate data/taxa/eukaryota/aspergillus_aculeatinus.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/aspergillus_aculeatinus.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:487661`, labelled `Aspergillus aculeatinus` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:487661` is a `SPECIES` child of `NCBITaxon:2720871` / `Aspergillus subgen. Circumdati`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms, and it preserves the related synonyms `Aspergillus aculeatinus Noonim, Frisvad, Varga & Samson 2008` and `Aspergillus sp. JV-2007e`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Aspergillus aculeatinus, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:487661`, so the generated current identifier is not represented as merged away in the local raw snapshot.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:487661`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:487661` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0047200`, `Aspergillus aculeatinus CBS 121060`, with strain and culture collection ID `CBS 121060`.
- GOLD organism `Go0047200` has two projects, `Gp0047200` and `Gp0047201`, with BioProjects `PRJNA235093` and `PRJNA250910` and BioSamples `SAMN05660730` and `SAMN03003123`.
- No native GOLD genome analysis rows were linked to `Go0047200` or to either of its projects.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 3 direct strain rows for `487661`, all already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `487661`.
- Exact `CBS 121060`, `CBS:121060`, `IBT 29077`, and `IBT:29077` token lookups found 0 BacDive rows and 0 StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has four rows for `NCBITaxon:487661`: `CBS 121060`, `CBS:121060`, `IBT 29077`, and `IBT:29077`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, NCBITaxon and GOLD source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, all exact StrainInfo rows are already excluded, and the NCBI/GOLD `CBS 121060` and NCBI-only `IBT 29077` type-material tokens do not add eligible local BacDive or StrainInfo strains.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/aspergillus_aculeatinus.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonyms, count-consistent aggregate/native GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/aspergillus_aculeatinus.yaml` and `just validate-strict data/taxa/eukaryota/aspergillus_aculeatinus.yaml` after regenerating the taxon record.

## Additional Notes

- The three exact StrainInfo rows are independently real source observations for `Aspergillus aculeatinus`: `straininfo.strain:15321`, `straininfo.strain:17172`, and `straininfo.strain:277006` have available `IHEM 27413`, `IHEM 26959`, and `IHEM 20714` deposits. Their exclusion rows are consistent with the generated `strain_count: 0` because none has an eligible matched local BacDive own deposit.
- The NCBI type-material rows are present in the local source inventory, but this generated eukaryotic record has no `nomenclature` block because TaxonMech currently generates `nomenclature` from LPSN rather than from NCBI `typematerial.dmp`.
