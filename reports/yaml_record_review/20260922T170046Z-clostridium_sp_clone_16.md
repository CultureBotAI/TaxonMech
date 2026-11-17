# YAML Record Review: Clostridium sp. Clone-16

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/clostridium_sp_clone_16.yaml
- Started UTC: 2026-09-22T17:00:46Z
- Finished UTC: 2026-09-22T17:00:46Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/clostridium_sp_clone_16.yaml`, the generated `TaxonRecord` for `NCBITaxon:1003365` / `Clostridium sp. Clone-16`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1003365`
- Label: `Clostridium sp. Clone-16`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2614128` / `unclassified Clostridium`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/clostridium_sp_clone_16.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/clostridium_sp_clone_16.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/clostridium_sp_clone_16.yaml data/taxa/bacteria/clostridium_sp_clone_17.yaml data/taxa/bacteria/clostridium_sp_clone_24.yaml data/taxa/bacteria/clostridium_sp_clone_25.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:1003365` to species label `Clostridium sp. Clone-16`, parent `NCBITaxon:2614128`, source bundle `ncbitaxon`, and snapshot date `2026-09-13`; the YAML carries those exact identity fields.
- The parent row maps `NCBITaxon:2614128` to the `unclassified Clostridium` node, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Bacillati`, `Bacillota`, `Clostridia`, `Eubacteriales`, `Clostridiaceae`, and `Clostridium`.
- No GTDB mapping, synonym, or xref is projected for this NCBI-only species record, matching the reviewed source rows.

## Evidence

- The NCBI source attestation is supported exactly by the `NCBITaxon:1003365` row in `data/raw/ncbitaxon_taxa.tsv`.

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

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-clostridium_sp_clone_16.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
