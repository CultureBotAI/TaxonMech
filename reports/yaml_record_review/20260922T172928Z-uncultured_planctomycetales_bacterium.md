# YAML Record Review: uncultured Planctomycetales bacterium

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/uncultured_planctomycetales_bacterium.yaml
- Started UTC: 2026-09-22T17:29:28Z
- Finished UTC: 2026-09-22T17:29:28Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/uncultured_planctomycetales_bacterium.yaml`, the generated `TaxonRecord` for `NCBITaxon:100371` / `uncultured Planctomycetales bacterium`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:100371`
- Label: `uncultured Planctomycetales bacterium`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:40903` / `environmental samples`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/uncultured_planctomycetales_bacterium.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/uncultured_planctomycetales_bacterium.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/prochlorococcus_marinus_subsp_pastoris_str_pcc_9511.yaml data/taxa/eukaryota/leptographium_procerum.yaml data/taxa/bacteria/uncultured_planctomycetales_bacterium.yaml data/taxa/bacteria/onion_yellows_phytoplasma.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:100371` to species label `uncultured Planctomycetales bacterium`, parent `NCBITaxon:40903`, source bundle `ncbitaxon|gtdb`, and snapshot date `2026-09-13`; the YAML carries those exact identity fields.
- The parent row maps `NCBITaxon:40903` to the Planctomycetales `environmental samples` node, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Pseudomonadati`, `PVC group`, `Planctomycetota`, `Planctomycetia`, and `Planctomycetales`.
- The YAML preserves the two NCBI exact synonyms, `uncultured Planctomycetales` and `unidentified Planctomycetales`.

## Evidence

- The NCBI source attestation is supported exactly by the `NCBITaxon:100371` row in `data/raw/ncbitaxon_taxa.tsv`.
- `data/raw/gtdb_mappings.tsv` contains 216 exact `NCBITaxon:100371` mappings; every projected YAML mapping is a pooled `skos:broadMatch`, and no GTDB xref or GTDB-derived exact synonym is emitted for those broad matches.
- The single GTDB source attestation points to the leading `GTDB:s__QWQI01_sp003670885` pooled species with `genome_count: 21`, while its notes correctly summarize the other 215 GTDB species represented in `taxonomy_mappings`.

## Completeness

- The record correctly leaves GOLD, MADIN, causal-graph, BacDive strain, and strain-genome slots absent.
- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo` plus `data/taxa/PATHS.tsv` found the expected NCBI, GTDB mapping, and PATHS rows; no GOLD, MADIN, LPSN, BacDive, StrainInfo, medium, or strain-genome evidence was found for the exact identifier, label, or slug.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-uncultured_planctomycetales_bacterium.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
