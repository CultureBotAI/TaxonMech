# YAML Record Review: Providencia sp. SY-14

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/providencia_sp_sy_14.yaml
- Started UTC: 2026-09-22T16:48:20Z
- Finished UTC: 2026-09-22T16:48:20Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/providencia_sp_sy_14.yaml`, the generated `TaxonRecord` for `NCBITaxon:1003338` / `Providencia sp. SY-14`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1003338`
- Label: `Providencia sp. SY-14`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2633465` / `unclassified Providencia`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/providencia_sp_sy_14.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/providencia_sp_sy_14.yaml` | Passed. |
| `just validate-strict data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_mpn20_ag_ft_c1.yaml data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_mpn20_ag_ft_c2.yaml data/taxa/bacteria/providencia_sp_sy_14.yaml data/taxa/bacteria/providencia_sp_sy_23.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:1003338` to species label `Providencia sp. SY-14`, parent `NCBITaxon:2633465`, source bundle `ncbitaxon`, and snapshot date `2026-09-13`; the YAML carries those exact identity fields.
- The parent row maps `NCBITaxon:2633465` to the `unclassified Providencia` node, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Pseudomonadati`, `Pseudomonadota`, `Gammaproteobacteria`, `Enterobacterales`, `Morganellaceae`, and `Providencia`.
- No GTDB mapping, synonym, or xref is projected for this NCBI-only species record, matching the reviewed source rows.

## Evidence

- The NCBI source attestation is supported exactly by the `NCBITaxon:1003338` row in `data/raw/ncbitaxon_taxa.tsv`.

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

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-providencia_sp_sy_14.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
