# YAML Record Review: Leptographium procerum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/leptographium_procerum.yaml
- Started UTC: 2026-09-22T17:29:28Z
- Finished UTC: 2026-09-22T17:29:28Z
- Verdict: pass

## Target

Reviewed `data/taxa/eukaryota/leptographium_procerum.yaml`, the generated `TaxonRecord` for `NCBITaxon:100367` / `Leptographium procerum`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:100367`
- Label: `Leptographium procerum`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:96312` / `Leptographium`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/eukaryota/leptographium_procerum.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/eukaryota/leptographium_procerum.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/prochlorococcus_marinus_subsp_pastoris_str_pcc_9511.yaml data/taxa/eukaryota/leptographium_procerum.yaml data/taxa/bacteria/uncultured_planctomycetales_bacterium.yaml data/taxa/bacteria/onion_yellows_phytoplasma.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:100367` to species label `Leptographium procerum`, parent `NCBITaxon:96312`, genetic code `1`, and snapshot date `2026-09-13`; the YAML carries those exact identity fields.
- The parent row maps `NCBITaxon:96312` to genus `Leptographium`, and the YAML lineage is root-first and reaches that parent through `Eukaryota`, `Opisthokonta`, `Fungi`, `Dikarya`, `Ascomycota`, `saccharomyceta`, `Pezizomycotina`, `leotiomyceta`, `sordariomyceta`, `Sordariomycetes`, `Sordariomycetidae`, `Ophiostomatales`, and `Ophiostomataceae`.
- The YAML preserves all five NCBI synonyms: the exact synonym `Verticicladiella procera` plus four related-name strings for the authorship or `WIN(M)` entries.

## Evidence

- The NCBI source attestation is supported exactly by the `NCBITaxon:100367` row in `data/raw/ncbitaxon_taxa.tsv`.
- The GOLD source attestation is supported exactly by the `NCBITaxon:100367` row in `data/raw/gold_organisms.tsv`.
- `data/raw/ncbi_merged_ids.tsv` contains two retired identifiers that merge into `NCBITaxon:100367`; those rows are auxiliary redirect evidence and do not create additional YAML slots.

## Completeness

- The record correctly leaves GTDB, MADIN, causal-graph, BacDive strain, and strain-genome slots absent.
- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo` plus `data/taxa/PATHS.tsv` found the expected NCBI, GOLD, NCBI-merged-ID, and PATHS rows; no GTDB, MADIN, LPSN, BacDive, StrainInfo, medium, or strain-genome evidence was found for the exact identifier, label, or slug.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-leptographium_procerum.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
