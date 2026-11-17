# YAML Record Review: Prochlorococcus marinus subsp. pastoris str. PCC 9511

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/prochlorococcus_marinus_subsp_pastoris_str_pcc_9511.yaml
- Started UTC: 2026-09-22T17:29:28Z
- Finished UTC: 2026-09-22T17:29:28Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/prochlorococcus_marinus_subsp_pastoris_str_pcc_9511.yaml`, the generated `TaxonRecord` for `NCBITaxon:100363` / `Prochlorococcus marinus subsp. pastoris str. PCC 9511`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:100363`
- Label: `Prochlorococcus marinus subsp. pastoris str. PCC 9511`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:142479` / `Prochlorococcus marinus subsp. pastoris`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/prochlorococcus_marinus_subsp_pastoris_str_pcc_9511.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/prochlorococcus_marinus_subsp_pastoris_str_pcc_9511.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/prochlorococcus_marinus_subsp_pastoris_str_pcc_9511.yaml data/taxa/eukaryota/leptographium_procerum.yaml data/taxa/bacteria/uncultured_planctomycetales_bacterium.yaml data/taxa/bacteria/onion_yellows_phytoplasma.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:100363` to strain label `Prochlorococcus marinus subsp. pastoris str. PCC 9511`, parent `NCBITaxon:142479`, genetic code `11`, and snapshot date `2026-09-13`; the YAML carries those exact identity fields.
- The parent row maps `NCBITaxon:142479` to `Prochlorococcus marinus subsp. pastoris`, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Bacillati`, `Cyanobacteriota/Melainabacteria group`, `Cyanobacteriota`, `Cyanophyceae`, `Synechococcales`, `Prochlorococcaceae`, `Prochlorococcus`, and `Prochlorococcus marinus`.
- The single projected synonym, `Prochlorococcus sp. PCC 9511`, is the exact synonym present on the pinned NCBI row.

## Evidence

- The NCBI source attestation is supported exactly by the `NCBITaxon:100363` row in `data/raw/ncbitaxon_taxa.tsv`.

## Completeness

- The record correctly leaves GTDB, GOLD, MADIN, causal-graph, BacDive strain, and strain-genome slots absent.
- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo` plus `data/taxa/PATHS.tsv` found only the direct NCBI and PATHS rows for this strain; no direct GTDB, GOLD, MADIN, LPSN, BacDive, StrainInfo, medium, or strain-genome evidence was found for the exact identifier, label, or slug.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-prochlorococcus_marinus_subsp_pastoris_str_pcc_9511.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
