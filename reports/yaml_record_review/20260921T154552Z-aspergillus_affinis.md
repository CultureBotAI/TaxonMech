# YAML Record Review: Aspergillus affinis

## Target

- File: `data/taxa/eukaryota/aspergillus_affinis.yaml`
- Identifier: `NCBITaxon:1070780`
- Label: `Aspergillus affinis`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:2720871` / `Aspergillus subgen. Circumdati`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `Eurotiomycetes` -> `Eurotiomycetidae` -> `Eurotiales` -> `Aspergillaceae` -> `Aspergillus` -> `Aspergillus subgen. Circumdati`
- Existing review report: none found for `*aspergillus_affinis.md` under the ignored `reports/yaml_record_review/` tree. A no-ignore, hidden-file search over `reports/yaml_record_review/` for `aspergillus_affinis` also found no existing report body that mentioned this slug; ignored files were included.

## Validation

- `just validate data/taxa/eukaryota/aspergillus_affinis.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/aspergillus_affinis.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:1070780`, labelled `Aspergillus affinis` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:1070780` is a `SPECIES` child of `NCBITaxon:2720871` / `Aspergillus subgen. Circumdati`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms, and it preserves the related synonyms `Aspergillus affinis Davolos, Persiani, Pietrangeli & Maggi 2011` and `Aspergillus sp. SR1`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Aspergillus affinis, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has one historical ID, `NCBITaxon:979891`, merged into the current `NCBITaxon:1070780` identifier.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:1070780`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:1070780` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0108201`, `Aspergillus affinis CBS 129190`, with strain and culture collection ID `CBS 129190`.
- GOLD organism `Go0108201` has three projects: standard-draft `Gp0108201` with BioProject `PRJNA333914` and BioSample `SAMN05446754`, plus two transcriptome projects, `Gp0248667` and `Gp0248668`, with BioProjects `PRJNA571996` and `PRJNA571997` and BioSamples `SAMN12812249` and `SAMN12812346`.
- Project `Gp0108201` links to native GOLD genome analysis `Ga0220850`, `Aspergillus affinis CBS 129190 Standard Draft`, through `AP PROJECT GOLD IDS`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 1 direct strain row for `1070780`, already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `1070780`.
- Exact `CBS 129190`, `ATCC MYA-4773`, `ATCC:MYA-4773`, and `ATCC:MYA:4773` token lookups found 0 BacDive rows and 0 StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has three holotype rows for `NCBITaxon:1070780`: `ATCC MYA-4773`, `ATCC:MYA-4773`, and `ATCC:MYA:4773`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, NCBITaxon and GOLD source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, the exact StrainInfo row is already excluded, and the GOLD `CBS 129190` and NCBI holotype `ATCC MYA-4773` tokens do not add eligible local BacDive or StrainInfo strains.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/aspergillus_affinis.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonyms, count-consistent aggregate/native GOLD source attestation, native GOLD project-analysis linkage, historical merge handling, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/aspergillus_affinis.yaml` and `just validate-strict data/taxa/eukaryota/aspergillus_affinis.yaml` after regenerating the taxon record.

## Additional Notes

- The exact StrainInfo row is an independently real source observation for `Aspergillus affinis`: `straininfo.strain:20772` has available `IHEM 26033` deposited under the same taxon. Its exclusion row is consistent with the generated `strain_count: 0` because it has no eligible matched local BacDive own deposit.
- The NCBI holotype rows are present in the local source inventory, but this generated eukaryotic record has no `nomenclature` block because TaxonMech currently generates `nomenclature` from LPSN rather than from NCBI `typematerial.dmp`.
