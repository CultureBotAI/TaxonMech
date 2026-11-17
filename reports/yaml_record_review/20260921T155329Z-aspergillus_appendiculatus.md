# YAML Record Review: Aspergillus appendiculatus

## Target

- File: `data/taxa/eukaryota/aspergillus_appendiculatus.yaml`
- Identifier: `NCBITaxon:1140386`
- Label: `Aspergillus appendiculatus`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:2720874` / `Aspergillus subgen. Aspergillus`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `Eurotiomycetes` -> `Eurotiomycetidae` -> `Eurotiales` -> `Aspergillaceae` -> `Aspergillus` -> `Aspergillus subgen. Aspergillus`
- Existing review report: none found for `*aspergillus_appendiculatus.md` under the ignored `reports/yaml_record_review/` tree. A no-ignore, hidden-file search over `reports/yaml_record_review/` for `aspergillus_appendiculatus` also found no existing report body that mentioned this slug; ignored files were included.

## Validation

- `just validate data/taxa/eukaryota/aspergillus_appendiculatus.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/aspergillus_appendiculatus.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:1140386`, labelled `Aspergillus appendiculatus` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:1140386` is a `SPECIES` child of `NCBITaxon:2720874` / `Aspergillus subgen. Aspergillus`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonyms `Eurotium appendiculatum` and `Eurotium aridicola`, plus related synonyms `Aspergillus appendiculatus Blaser, 1975` and `Eurotium appendiculatum Blaser, 1975`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Aspergillus appendiculatus, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has one historical ID, `NCBITaxon:1140387`, merged into the current `NCBITaxon:1140386` identifier.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:1140386`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:1140386` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0446096`, `Aspergillus appendiculatus CBS 374.75`, with strain and culture collection ID `CBS 374.75`.
- GOLD organism `Go0446096` has three projects, `Gp0312193`, `Gp0487753`, and `Gp0509214`, with BioProjects `PRJNA585375`, `PRJNA710750`, and `PRJNA708578` and BioSamples `SAMN13170423`, `SAMN18247059`, and `SAMN18243022`.
- No native GOLD genome analysis rows were linked to `Go0446096` or to any of its projects.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 6 direct strain rows for `1140386`, all already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `1140386`.
- Quoted exact JSON-string lookups for the visible NCBI type-material and native GOLD collection numbers found 0 BacDive rows and one StrainInfo row, `straininfo.strain:63235`, which is already among the excluded exact StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has 10 rows for `NCBITaxon:1140386`, covering culture from holotype `CBS 374.75` and `PIL 588`, holotype `ZT 8286`, and type material `ETH 8286` and `IMI 278374`, with punctuation variants.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, NCBITaxon and GOLD source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, all exact StrainInfo rows are already excluded, and the exact NCBI/GOLD `CBS 374.75` token does not add an eligible local BacDive own deposit.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/aspergillus_appendiculatus.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym split, count-consistent aggregate/native GOLD source attestation, NCBI type-material inventory behavior, historical merge handling, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/aspergillus_appendiculatus.yaml` and `just validate-strict data/taxa/eukaryota/aspergillus_appendiculatus.yaml` after regenerating the taxon record.

## Additional Notes

- The six exact StrainInfo rows are independently real source observations for `Aspergillus appendiculatus`: they include the `CBS 374.75` / `IMI 278374` type-material row, three IHEM rows, `MUCL 54673`, and `CBS 101746` / `CGMCC 3.4673`. Their exclusion rows are consistent with the generated `strain_count: 0` because none has an eligible matched local BacDive own deposit.
- The NCBI type-material rows are present in the local source inventory, but this generated eukaryotic record has no `nomenclature` block because TaxonMech currently generates `nomenclature` from LPSN rather than from NCBI `typematerial.dmp`.
