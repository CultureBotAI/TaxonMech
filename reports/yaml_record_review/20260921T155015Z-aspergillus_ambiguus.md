# YAML Record Review: Aspergillus ambiguus

## Target

- File: `data/taxa/eukaryota/aspergillus_ambiguus.yaml`
- Identifier: `NCBITaxon:176160`
- Label: `Aspergillus ambiguus`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:2720871` / `Aspergillus subgen. Circumdati`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `Eurotiomycetes` -> `Eurotiomycetidae` -> `Eurotiales` -> `Aspergillaceae` -> `Aspergillus` -> `Aspergillus subgen. Circumdati`
- Existing review report: none found for `*aspergillus_ambiguus.md` under the ignored `reports/yaml_record_review/` tree. A no-ignore, hidden-file search over `reports/yaml_record_review/` for `aspergillus_ambiguus` also found no existing report body that mentioned this slug; ignored files were included.

## Validation

- `just validate data/taxa/eukaryota/aspergillus_ambiguus.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/aspergillus_ambiguus.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:176160`, labelled `Aspergillus ambiguus` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:176160` is a `SPECIES` child of `NCBITaxon:2720871` / `Aspergillus subgen. Circumdati`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms, and it preserves the related synonym `Aspergillus ambiguus Sappa, 1955`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Aspergillus ambiguus, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:176160`, so the generated current identifier is not represented as merged away in the local raw snapshot.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:176160`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:176160` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0108235`, `Aspergillus ambiguus CBS 117.58`, with strain and culture collection ID `CBS 117.58`.
- GOLD organism `Go0108235` has three projects, `Gp0108235`, `Gp0108236`, and `Gp0248661`, with BioProjects `PRJNA333931`, `PRJNA459670`, and `PRJNA457644` and BioSamples `SAMN05446763`, `SAMN09074257`, and `SAMN09066865`.
- No native GOLD genome analysis rows were linked to `Go0108235` or to any of its projects.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 2 direct strain rows for `176160`, both already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `176160`.
- Quoted exact JSON-string lookups for the visible NCBI type-material and native GOLD collection numbers found 0 BacDive rows and 1 StrainInfo row, `straininfo.strain:153700`, which is already among the excluded exact StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has 14 rows for `NCBITaxon:176160`, covering culture from lectotype `NRRL 4737`, culture from neotype `CBS 117.58`, and culture from type material `ATCC 16827`, `IMI 139274`, `QM 8155`, and `WB 4737`, with punctuation variants.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, genetic code, `strain_count`, NCBITaxon and GOLD source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, both exact StrainInfo rows are already excluded, and exact quoted collection-token lookups did not reveal an eligible local BacDive own deposit for the GOLD or NCBI type-material accessions.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/aspergillus_ambiguus.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonym, count-consistent aggregate/native GOLD source attestation, NCBI type-material inventory behavior, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/aspergillus_ambiguus.yaml` and `just validate-strict data/taxa/eukaryota/aspergillus_ambiguus.yaml` after regenerating the taxon record.

## Additional Notes

- The two exact StrainInfo rows are independently real source observations for `Aspergillus ambiguus`: `straininfo.strain:153700` has `CBS 117.58`, `ATCC 16827`, `IMI 139274`, `BCRC 33359`, `CCRC 33359`, and `NRRL 4737` deposits, while `straininfo.strain:273725` has `MUCL 13573`. Their exclusion rows are consistent with the generated `strain_count: 0` because neither has an eligible matched local BacDive own deposit.
- The NCBI type-material rows are present in the local source inventory, but this generated eukaryotic record has no `nomenclature` block because TaxonMech currently generates `nomenclature` from LPSN rather than from NCBI `typematerial.dmp`.
