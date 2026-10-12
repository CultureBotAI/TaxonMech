# YAML Record Review: Arthrospira innermongoliensis BZ-2011

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/arthrospira_innermongoliensis_bz_2011.yaml
- Started UTC: 2026-09-22T17:35:59Z
- Finished UTC: 2026-09-22T17:35:59Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/arthrospira_innermongoliensis_bz_2011.yaml`, the generated `TaxonRecord` for `NCBITaxon:1004083` / `Arthrospira innermongoliensis BZ-2011`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1004083`
- Label: `Arthrospira innermongoliensis BZ-2011`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:942937` / `Arthrospira innermongoliensis`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/arthrospira_innermongoliensis_bz_2011.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/arthrospira_innermongoliensis_bz_2011.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/exiguobacterium_sp_wh10_8_2.yaml data/taxa/bacteria/chitinophaga_sancti.yaml data/taxa/bacteria/mycobacterium_sp_js330.yaml data/taxa/bacteria/arthrospira_innermongoliensis_bz_2011.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:1004083` to strain label `Arthrospira innermongoliensis BZ-2011`, parent `NCBITaxon:942937`, source bundle `ncbitaxon`, and snapshot date `2026-09-13`; the YAML carries those exact identity fields.
- The parent row maps `NCBITaxon:942937` to species `Arthrospira innermongoliensis`, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Bacillati`, `Cyanobacteriota/Melainabacteria group`, `Cyanobacteriota`, `Cyanophyceae`, `Oscillatoriophycideae`, `Oscillatoriales`, `Microcoleaceae`, and `Arthrospira`.
- The single projected synonym, `Spirulina innermongoliensis BZ-2011`, is the exact synonym present on the pinned NCBI row.

## Evidence

- The NCBI source attestation is supported exactly by the `NCBITaxon:1004083` row in `data/raw/ncbitaxon_taxa.tsv`.

## Completeness

- The record correctly leaves GTDB, GOLD, MADIN, causal-graph, BacDive strain, and non-NCBI synonym slots absent.
- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo` plus `data/taxa/PATHS.tsv` found only the exact NCBI and PATHS rows; no GTDB, GOLD, MADIN, LPSN, BacDive, StrainInfo, medium, or strain-genome evidence was found for the exact identifier, label, or slug.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-arthrospira_innermongoliensis_bz_2011.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
