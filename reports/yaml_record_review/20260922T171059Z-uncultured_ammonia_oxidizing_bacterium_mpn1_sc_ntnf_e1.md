# YAML Record Review: uncultured ammonia-oxidizing bacterium MPN1-SC-NTNF-E1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_mpn1_sc_ntnf_e1.yaml
- Started UTC: 2026-09-22T17:10:59Z
- Finished UTC: 2026-09-22T17:10:59Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_mpn1_sc_ntnf_e1.yaml`, the generated `TaxonRecord` for `NCBITaxon:100340` / `uncultured ammonia-oxidizing bacterium MPN1-SC-NTNF-E1`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:100340`
- Label: `uncultured ammonia-oxidizing bacterium MPN1-SC-NTNF-E1`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:47949` / `environmental samples`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_mpn1_sc_ntnf_e1.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_mpn1_sc_ntnf_e1.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_mpn1_sc_ntnf_e1.yaml data/taxa/bacteria/actinoalloteichus_sp_sh18_2011.yaml data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_mpn1_sc_ntnf_e2.yaml data/taxa/bacteria/nocardiopsis_sp_an10_2011.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:100340` to species label `uncultured ammonia-oxidizing bacterium MPN1-SC-NTNF-E1`, parent `NCBITaxon:47949`, source bundle `ncbitaxon`, and snapshot date `2026-09-13`; the YAML carries those exact identity fields.
- The parent row maps `NCBITaxon:47949` to the `environmental samples` node, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Pseudomonadati`, `Pseudomonadota`, `Betaproteobacteria`, `Nitrosomonadales`, and `Nitrosomonadaceae`.
- No GTDB mapping, synonym, or xref is projected for this NCBI-only species record, matching the reviewed source rows.

## Evidence

- The NCBI source attestation is supported exactly by the `NCBITaxon:100340` row in `data/raw/ncbitaxon_taxa.tsv`.

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

- The source audit used tab-bounded identifier matching so the shorter `NCBITaxon:100340` did not match longer identifiers such as `NCBITaxon:1003409`.
- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-uncultured_ammonia_oxidizing_bacterium_mpn1_sc_ntnf_e1.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
