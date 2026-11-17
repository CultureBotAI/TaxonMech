# YAML Record Review: uncultured ammonia-oxidizing bacterium DGGE-SC-TNF-E1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_dgge_sc_tnf_e1.yaml
- Started UTC: 2026-09-22T17:24:13Z
- Finished UTC: 2026-09-22T17:24:13Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_dgge_sc_tnf_e1.yaml`, the generated `TaxonRecord` for `NCBITaxon:100355` / `uncultured ammonia-oxidizing bacterium DGGE-SC-TNF-E1`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:100355`
- Label: `uncultured ammonia-oxidizing bacterium DGGE-SC-TNF-E1`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:47949` / `environmental samples`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_dgge_sc_tnf_e1.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_dgge_sc_tnf_e1.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_dgge_ag_ntnf_e1.yaml data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_dgge_sc_ntf_e1.yaml data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_dgge_sc_tnf_e1.yaml data/taxa/bacteria/uncultured_ammonia_oxidizing_bacterium_dgge_sc_tf_e1.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:100355` to species label `uncultured ammonia-oxidizing bacterium DGGE-SC-TNF-E1`, parent `NCBITaxon:47949`, source bundle `ncbitaxon`, and snapshot date `2026-09-13`; the YAML carries those exact identity fields.
- The parent row maps `NCBITaxon:47949` to the Nitrosomonadaceae `environmental samples` node, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Pseudomonadati`, `Pseudomonadota`, `Betaproteobacteria`, `Nitrosomonadales`, and `Nitrosomonadaceae`.
- No GTDB mapping, synonym, or xref is projected for this NCBI-only species record, matching the reviewed source rows.

## Evidence

- The NCBI source attestation is supported exactly by the `NCBITaxon:100355` row in `data/raw/ncbitaxon_taxa.tsv`.

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

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-uncultured_ammonia_oxidizing_bacterium_dgge_sc_tnf_e1.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
