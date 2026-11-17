# YAML Record Review: Aspergillus alabamensis

## Target

- File: `data/taxa/eukaryota/aspergillus_alabamensis.yaml`
- Identifier: `NCBITaxon:657433`
- Label: `Aspergillus alabamensis`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:2720871` / `Aspergillus subgen. Circumdati`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `Eurotiomycetes` -> `Eurotiomycetidae` -> `Eurotiales` -> `Aspergillaceae` -> `Aspergillus` -> `Aspergillus subgen. Circumdati`
- Existing review report: none found for `*aspergillus_alabamensis.md` under the ignored `reports/yaml_record_review/` tree. A no-ignore, hidden-file search over `reports/yaml_record_review/` for `aspergillus_alabamensis` also found no existing report body that mentioned this slug; ignored files were included.

## Validation

- `just validate data/taxa/eukaryota/aspergillus_alabamensis.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/aspergillus_alabamensis.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:657433`, labelled `Aspergillus alabamensis` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:657433` is a `SPECIES` child of `NCBITaxon:2720871` / `Aspergillus subgen. Circumdati`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms, and it preserves the related synonym `Aspergillus alabamensis Balajee, Baddley, Frisvad & Samson, 2009`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Aspergillus alabamensis, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:657433`, so the generated current identifier is not represented as merged away in the local raw snapshot.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:657433`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:657433` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0108233`, `Aspergillus alabamensis IBT 12702`, with strain and culture collection ID `IBT 12702`.
- GOLD organism `Go0108233` has two projects, `Gp0108233` and `Gp0108234`, with BioProjects `PRJNA333930` and `PRJNA459669` and BioSamples `SAMN05446815` and `SAMN09074263`.
- No native GOLD genome analysis rows were linked to `Go0108233` or to either of its projects.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 9 direct strain rows for `657433`, all already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `657433`.
- Exact `IBT 12702`, `CBS 125693`, `CBS:125693`, `UAB 20`, `UAB20`, `UAB:20`, and `UAB<ESP>:20` token lookups found 0 BacDive rows and 0 StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has six rows for `NCBITaxon:657433`, covering culture from holotype `CBS 125693` / `CBS:125693` and culture from type material `UAB 20` / `UAB20` / `UAB:20` / `UAB<ESP>:20`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, genetic code, `strain_count`, NCBITaxon and GOLD source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, all exact StrainInfo rows are already excluded, and the GOLD `IBT 12702` and NCBI type-material tokens do not add eligible local BacDive or StrainInfo strains.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/aspergillus_alabamensis.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonym, count-consistent aggregate/native GOLD source attestation, NCBI type-material inventory behavior, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/aspergillus_alabamensis.yaml` and `just validate-strict data/taxa/eukaryota/aspergillus_alabamensis.yaml` after regenerating the taxon record.

## Additional Notes

- The nine exact StrainInfo rows are independently real source observations for `Aspergillus alabamensis`: they have available `IHEM 26013`, `IHEM 27007`, `IHEM 26967`, `IHEM 27415`, `IHEM 9697`, `IHEM 14067`, `IHEM 5051`, `IHEM 5063`, and `IHEM 18048` deposits. Their exclusion rows are consistent with the generated `strain_count: 0` because none has an eligible matched local BacDive own deposit.
- The NCBI type-material rows are present in the local source inventory, but this generated eukaryotic record has no `nomenclature` block because TaxonMech currently generates `nomenclature` from LPSN rather than from NCBI `typematerial.dmp`.
