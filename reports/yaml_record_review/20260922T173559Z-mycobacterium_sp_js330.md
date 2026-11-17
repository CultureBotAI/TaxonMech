# YAML Record Review: Mycobacterium sp. JS330

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/mycobacterium_sp_js330.yaml
- Started UTC: 2026-09-22T17:35:59Z
- Finished UTC: 2026-09-22T17:35:59Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/mycobacterium_sp_js330.yaml`, the generated `TaxonRecord` for `NCBITaxon:1004011` / `Mycobacterium sp. JS330`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1004011`
- Label: `Mycobacterium sp. JS330`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2642494` / `unclassified Mycobacterium`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/mycobacterium_sp_js330.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/mycobacterium_sp_js330.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/exiguobacterium_sp_wh10_8_2.yaml data/taxa/bacteria/chitinophaga_sancti.yaml data/taxa/bacteria/mycobacterium_sp_js330.yaml data/taxa/bacteria/arthrospira_innermongoliensis_bz_2011.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:1004011` to species label `Mycobacterium sp. JS330`, parent `NCBITaxon:2642494`, source bundle `ncbitaxon`, and snapshot date `2026-09-13`; the YAML carries those exact identity fields.
- The parent row maps `NCBITaxon:2642494` to the `unclassified Mycobacterium` node, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Bacillati`, `Actinomycetota`, `Actinomycetes`, `Mycobacteriales`, `Mycobacteriaceae`, and `Mycobacterium`.
- No GTDB mapping, synonym, or xref is projected for this NCBI-only species record, matching the reviewed source rows.

## Evidence

- The NCBI source attestation is supported exactly by the `NCBITaxon:1004011` row in `data/raw/ncbitaxon_taxa.tsv`.

## Completeness

- The record correctly leaves GTDB, GOLD, MADIN, causal-graph, BacDive strain, and synonym slots absent.
- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo` plus `data/taxa/PATHS.tsv` found only the exact NCBI and PATHS rows; no GTDB, GOLD, MADIN, LPSN, BacDive, StrainInfo, medium, or strain-genome evidence was found for the exact identifier, label, or slug.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-mycobacterium_sp_js330.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
