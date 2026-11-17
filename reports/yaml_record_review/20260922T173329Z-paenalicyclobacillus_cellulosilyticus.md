# YAML Record Review: Paenalicyclobacillus cellulosilyticus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/paenalicyclobacillus_cellulosilyticus.yaml
- Started UTC: 2026-09-22T17:33:29Z
- Finished UTC: 2026-09-22T17:33:29Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/paenalicyclobacillus_cellulosilyticus.yaml`, the generated `TaxonRecord` for `NCBITaxon:1003997` / `Paenalicyclobacillus cellulosilyticus`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1003997`
- Label: `Paenalicyclobacillus cellulosilyticus`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:3479148` / `Paenalicyclobacillus`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/paenalicyclobacillus_cellulosilyticus.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/paenalicyclobacillus_cellulosilyticus.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/stappia_sp_fg_4.yaml data/taxa/bacteria/paenibacillus_sp_no1.yaml data/taxa/bacteria/mycobacterium_sp_b10_07_09_0206.yaml data/taxa/bacteria/paenalicyclobacillus_cellulosilyticus.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:1003997` to species label `Paenalicyclobacillus cellulosilyticus`, parent `NCBITaxon:3479148`, source bundle `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold`, and snapshot date `2026-09-13`; the YAML carries those exact identity fields.
- The parent row maps `NCBITaxon:3479148` to genus `Paenalicyclobacillus`, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Bacillati`, `Bacillota`, `Bacilli`, `Caryophanales`, and `Alicyclobacillaceae`.
- The LPSN overlay preserves `lpsn:68884`, its type-strain designations, publications, sequence accession, and the local note that LPSN marks this name deprecated as a synonym of a later correct name.
- The single GTDB mapping is a two-genome `skos:closeMatch` to `GTDB:s__Alicyclobacillus_J_cellulosilyticus`; because it is a close match, the YAML correctly emits both an xref and the GTDB-derived exact synonym `Alicyclobacillus J cellulosilyticus`.

## Evidence

- The NCBI source attestation is supported exactly by the `NCBITaxon:1003997` row in `data/raw/ncbitaxon_taxa.tsv`.
- The LPSN nomenclature block is supported by `lpsn:68884` in `data/raw/lpsn_names.tsv`, and its related synonym `Alicyclobacillus cellulosilyticus` is supported by `lpsn:791953`.
- The GTDB, BacDive, MediaDive, GOLD, culture-collection, type-material, strain-assembly, strain-genome, strain-related, and StrainInfo rows keyed to `NCBITaxon:1003997` are all represented in the generated taxonomy mapping, source attestations, type-strain entry, or nested genome and related-record lists.
- The generated type-strain entry for `kgmicrobe.strain:bacdive_158167` carries the expected `DSM-107339`, `JCM-18487`, and `KCTC-33007` culture-collection identifiers, 10 assembly evidence rows, nine genome records, and 26 related records.

## Completeness

- The record correctly leaves MADIN, BactoTraits, ATB, and causal-graph slots absent.
- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo` plus `data/taxa/PATHS.tsv` found the expected NCBI, LPSN, GTDB, BacDive, MediaDive, GOLD, type-material, culture-collection, genome, StrainInfo, and PATHS rows; no MADIN, BactoTraits, AllTheBacteria, or causal-graph evidence was found for the exact identifier, label, or slug.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-paenalicyclobacillus_cellulosilyticus.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
