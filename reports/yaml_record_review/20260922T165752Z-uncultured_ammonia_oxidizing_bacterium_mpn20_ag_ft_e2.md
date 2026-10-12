# YAML Record Review: uncultured ammonia-oxidizing bacterium MPN20-AG-FT-E2

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_mpn20_ag_ft_e2.yaml
- Started UTC: 2026-09-22T16:57:52Z
- Finished UTC: 2026-09-22T16:57:52Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_mpn20_ag_ft_e2.yaml`, the generated `TaxonRecord` for `NCBITaxon:100336` / `uncultured ammonia-oxidizing bacterium MPN20-AG-FT-E2`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:100336`
- Label: `uncultured ammonia-oxidizing bacterium MPN20-AG-FT-E2`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:47949` / `environmental samples`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_mpn20_ag_ft_e2.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_mpn20_ag_ft_e2.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/clostridium_sp_culture_jar_19.yaml data/taxa/bacteria/clostridium_sp_culture_jar_44.yaml data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_mpn20_ag_ft_e2.yaml data/taxa/bacteria/clostridium_sp_culture_jar_56.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:100336` to species label `uncultured ammonia-oxidizing bacterium MPN20-AG-FT-E2`, parent `NCBITaxon:47949`, source bundle `ncbitaxon`, and snapshot date `2026-09-13`; the YAML carries those exact identity fields.
- The parent row maps `NCBITaxon:47949` to the `environmental samples` node, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Pseudomonadati`, `Pseudomonadota`, `Betaproteobacteria`, `Nitrosomonadales`, and `Nitrosomonadaceae`.
- No GTDB mapping, synonym, or xref is projected for this NCBI-only species record, matching the reviewed source rows.

## Evidence

- The NCBI source attestation is supported exactly by the `NCBITaxon:100336` row in `data/raw/ncbitaxon_taxa.tsv`.

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

- The source audit used tab-bounded identifier matching so the shorter `NCBITaxon:100336` did not match longer identifiers such as `NCBITaxon:1003360`.
- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-uncultured_ammonia_oxidizing_bacterium_mpn20_ag_ft_e2.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
