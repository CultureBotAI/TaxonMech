# YAML Record Review: Aspergillus angustatus

## Target

- File: `data/taxa/eukaryota/aspergillus_angustatus.yaml`
- Identifier: `NCBITaxon:2783700`
- Label: `Aspergillus angustatus`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:2720870` / `Aspergillus subgen. Nidulantes`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `Eurotiomycetes` -> `Eurotiomycetidae` -> `Eurotiales` -> `Aspergillaceae` -> `Aspergillus` -> `Aspergillus subgen. Nidulantes`
- Existing review report: none found for `*aspergillus_angustatus.md` under the ignored `reports/yaml_record_review/` tree. A no-ignore, hidden-file search over `reports/yaml_record_review/` for `aspergillus_angustatus` also found no existing report body that mentioned this slug; ignored files were included.

## Validation

- `just validate data/taxa/eukaryota/aspergillus_angustatus.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/aspergillus_angustatus.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:2783700`, labelled `Aspergillus angustatus` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:2783700` is a `SPECIES` child of `NCBITaxon:2720870` / `Aspergillus subgen. Nidulantes`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms, and it preserves the related synonyms `Aspergillus angustatus A.J. Chen, Frisvad & Samson, 2016` and `Aspergillus sp. 4 AJC-2016`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Aspergillus angustatus, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has one historical ID, `NCBITaxon:1810889`, merged into the current `NCBITaxon:2783700` identifier.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:2783700`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:2783700` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0446095`, `Aspergillus angustatus CBS 273.65`, with strain and culture collection ID `CBS 273.65`.
- GOLD organism `Go0446095` has three projects, `Gp0312192`, `Gp0487768`, and `Gp0509219`, with BioProjects `PRJNA713157`, `PRJNA710756`, and `PRJNA708581` and BioSamples `SAMN18261350`, `SAMN18247800`, and `SAMN18243423`.
- No native GOLD genome analysis rows were linked to `Go0446095` or to any of its projects.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `2783700`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `2783700`.
- Quoted exact JSON-string lookups for the visible NCBI type-material and native GOLD collection numbers found 0 BacDive rows and one taxonless StrainInfo `CBS 273.65` row, already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`.
- `data/raw/ncbi_type_material.tsv` has four rows for `NCBITaxon:2783700`, covering culture from holotype `CBS 273.65` / `CBS:273.65` and holotype `CBS H-22487` / `CBS:H-22487`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, NCBITaxon and GOLD source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive and StrainInfo have no exact NCBI match, and the only exact collection-token StrainInfo row has neither a strain-level nor deposit-level NCBI taxon.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/aspergillus_angustatus.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonyms, count-consistent aggregate/native GOLD source attestation, NCBI type-material inventory behavior, historical merge handling, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/aspergillus_angustatus.yaml` and `just validate-strict data/taxa/eukaryota/aspergillus_angustatus.yaml` after regenerating the taxon record.

## Additional Notes

- The exact `CBS 273.65` token appears in `straininfo.strain:162483`, whose StrainInfo record has no strain-level taxon and no deposit-level taxon. Its existing `no_eligible_own_deposit_match` exclusion is consistent with the generated `strain_count: 0`.
- The NCBI type-material rows are present in the local source inventory, but this generated eukaryotic record has no `nomenclature` block because TaxonMech currently generates `nomenclature` from LPSN rather than from NCBI `typematerial.dmp`.
