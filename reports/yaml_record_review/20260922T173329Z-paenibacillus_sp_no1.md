# YAML Record Review: Paenibacillus sp. NO1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/paenibacillus_sp_no1.yaml
- Started UTC: 2026-09-22T17:33:29Z
- Finished UTC: 2026-09-22T17:33:29Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/paenibacillus_sp_no1.yaml`, the generated `TaxonRecord` for `NCBITaxon:1003833` / `Paenibacillus sp. NO1`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1003833`
- Label: `Paenibacillus sp. NO1`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:185978` / `unclassified Paenibacillus`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/paenibacillus_sp_no1.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/paenibacillus_sp_no1.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/stappia_sp_fg_4.yaml data/taxa/bacteria/paenibacillus_sp_no1.yaml data/taxa/bacteria/mycobacterium_sp_b10_07_09_0206.yaml data/taxa/bacteria/paenalicyclobacillus_cellulosilyticus.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:1003833` to species label `Paenibacillus sp. NO1`, parent `NCBITaxon:185978`, source bundle `ncbitaxon`, and snapshot date `2026-09-13`; the YAML carries those exact identity fields.
- The parent row maps `NCBITaxon:185978` to the `unclassified Paenibacillus` node, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Bacillati`, `Bacillota`, `Bacilli`, `Caryophanales`, `Paenibacillaceae`, and `Paenibacillus`.
- No GTDB mapping, synonym, or xref is projected for this NCBI-only species record, matching the reviewed source rows.

## Evidence

- The NCBI source attestation is supported exactly by the `NCBITaxon:1003833` row in `data/raw/ncbitaxon_taxa.tsv`.

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

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-paenibacillus_sp_no1.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
