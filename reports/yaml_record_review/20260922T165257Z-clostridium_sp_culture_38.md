# YAML Record Review: Clostridium sp. Culture-38

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/clostridium_sp_culture_38.yaml
- Started UTC: 2026-09-22T16:52:57Z
- Finished UTC: 2026-09-22T16:52:57Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/clostridium_sp_culture_38.yaml`, the generated `TaxonRecord` for `NCBITaxon:1003348` / `Clostridium sp. Culture-38`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1003348`
- Label: `Clostridium sp. Culture-38`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2614128` / `unclassified Clostridium`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/clostridium_sp_culture_38.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/clostridium_sp_culture_38.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/clostridium_sp_culture_27.yaml data/taxa/bacteria/clostridium_sp_culture_38.yaml data/taxa/bacteria/clostridium_sp_culture_41.yaml data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_mpn20_ag_ft_e1.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:1003348` to species label `Clostridium sp. Culture-38`, parent `NCBITaxon:2614128`, source bundle `ncbitaxon`, and snapshot date `2026-09-13`; the YAML carries those exact identity fields.
- The parent row maps `NCBITaxon:2614128` to the `unclassified Clostridium` node, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Bacillati`, `Bacillota`, `Clostridia`, `Eubacteriales`, `Clostridiaceae`, and `Clostridium`.
- No GTDB mapping, synonym, or xref is projected for this NCBI-only species record, matching the reviewed source rows.

## Evidence

- The NCBI source attestation is supported exactly by the `NCBITaxon:1003348` row in `data/raw/ncbitaxon_taxa.tsv`.

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

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-clostridium_sp_culture_38.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
