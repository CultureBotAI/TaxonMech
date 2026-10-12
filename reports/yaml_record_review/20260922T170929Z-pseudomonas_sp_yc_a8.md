# YAML Record Review: Pseudomonas sp. YC-A8

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pseudomonas_sp_yc_a8.yaml
- Started UTC: 2026-09-22T17:09:29Z
- Finished UTC: 2026-09-22T17:09:29Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/pseudomonas_sp_yc_a8.yaml`, the generated `TaxonRecord` for `NCBITaxon:1003389` / `Pseudomonas sp. YC-A8`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1003389`
- Label: `Pseudomonas sp. YC-A8`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:196821` / `unclassified Pseudomonas`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/pseudomonas_sp_yc_a8.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/pseudomonas_sp_yc_a8.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_kc_a8.yaml data/taxa/bacteria/pseudomonas_sp_yc_a18.yaml data/taxa/bacteria/pseudomonas_sp_yc_a8.yaml data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_mpn1_sc_ntnf_c2.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:1003389` to species label `Pseudomonas sp. YC-A8`, parent `NCBITaxon:196821`, source bundle `ncbitaxon`, and snapshot date `2026-09-13`; the YAML carries those exact identity fields.
- The parent row maps `NCBITaxon:196821` to the `unclassified Pseudomonas` node, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Pseudomonadati`, `Pseudomonadota`, `Gammaproteobacteria`, `Pseudomonadales`, `Pseudomonadaceae`, and `Pseudomonas`.
- No GTDB mapping, synonym, or xref is projected for this NCBI-only species record, matching the reviewed source rows.

## Evidence

- The NCBI source attestation is supported exactly by the `NCBITaxon:1003389` row in `data/raw/ncbitaxon_taxa.tsv`.

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

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-pseudomonas_sp_yc_a8.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
