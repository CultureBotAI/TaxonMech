# YAML Record Review: Chitinophaga sancti

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/chitinophaga_sancti.yaml
- Started UTC: 2026-09-22T17:35:59Z
- Finished UTC: 2026-09-22T17:35:59Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/chitinophaga_sancti.yaml`, the generated `TaxonRecord` for `NCBITaxon:1004` / `Chitinophaga sancti`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1004`
- Label: `Chitinophaga sancti`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:79328` / `Chitinophaga`
- Maintained owner: source rows under `data/raw/`, `data/atb/`, and `data/straininfo/`; do not patch `data/taxa/bacteria/chitinophaga_sancti.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/chitinophaga_sancti.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/exiguobacterium_sp_wh10_8_2.yaml data/taxa/bacteria/chitinophaga_sancti.yaml data/taxa/bacteria/mycobacterium_sp_js330.yaml data/taxa/bacteria/arthrospira_innermongoliensis_bz_2011.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:1004` to species label `Chitinophaga sancti`, parent `NCBITaxon:79328`, source bundle `ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal`, and snapshot date `2026-09-13`; the YAML carries those exact identity fields.
- The parent row maps `NCBITaxon:79328` to genus `Chitinophaga`, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Pseudomonadati`, `FCB group`, `Bacteroidota/Chlorobiota group`, `Bacteroidota`, `Chitinophagia`, `Chitinophagales`, and `Chitinophagaceae`.
- The LPSN overlay preserves the correct-name `lpsn:785446` record, its type-strain designations, publications, sequence accession, and the related synonym `Flexibacter sancti` from `lpsn:785447`.
- The GTDB mapping set correctly contains two `skos:broadMatch` rows. `GTDB:s__Chitinophaga_sancti` is linked by LPSN and therefore emits an xref, while `GTDB:s__Chitinophaga_sancti_B` remains a pooled broad match without an xref.

## Evidence

- The NCBI source attestation is supported exactly by the `NCBITaxon:1004` row in `data/raw/ncbitaxon_taxa.tsv`.
- The LPSN, GTDB, BacDive, GOLD, MADIN, NCBI type-material, culture-collection, strain-assembly, strain-genome, strain-related, AllTheBacteria, and StrainInfo source rows keyed to `NCBITaxon:1004` are represented in the generated nomenclature, taxonomy mappings, source attestations, three strain entries, and nested genome or related-record lists.
- The BacDive type strain is filed under descendant `NCBITaxon:1121282` / `Chitinophaga sancti DSM 784`; the generated parent species correctly gathers it with `classified_as: NCBITaxon:1121282`.
- The generated strain overlay carries three BacDive strains, 23 assembly evidence rows, 16 genome records, 88 related records, and the expected StrainInfo deposit links plus ATB assembly evidence.

## Completeness

- The record correctly leaves MediaDive, BactoTraits, and causal-graph slots absent at the parent `NCBITaxon:1004` record.
- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo` plus `data/taxa/PATHS.tsv` found the expected NCBI, LPSN, GTDB, BacDive, GOLD, MADIN, type-material, culture-collection, ATB, genome, StrainInfo, and PATHS rows. The same hidden-aware review included the descendant `NCBITaxon:1121282` BacDive row that feeds the type-strain entry.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-chitinophaga_sancti.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
