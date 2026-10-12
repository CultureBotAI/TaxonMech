# YAML Record Review: Onion yellows phytoplasma

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/onion_yellows_phytoplasma.yaml
- Started UTC: 2026-09-22T17:29:28Z
- Finished UTC: 2026-09-22T17:29:28Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/onion_yellows_phytoplasma.yaml`, the generated `TaxonRecord` for `NCBITaxon:100379` / `Onion yellows phytoplasma`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:100379`
- Label: `Onion yellows phytoplasma`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:3042590` / `16SrI (Aster yellows group)`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/onion_yellows_phytoplasma.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/onion_yellows_phytoplasma.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/prochlorococcus_marinus_subsp_pastoris_str_pcc_9511.yaml data/taxa/eukaryota/leptographium_procerum.yaml data/taxa/bacteria/uncultured_planctomycetales_bacterium.yaml data/taxa/bacteria/onion_yellows_phytoplasma.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:100379` to species label `Onion yellows phytoplasma`, parent `NCBITaxon:3042590`, source bundle `ncbitaxon|madin_etal`, and snapshot date `2026-09-13`; the YAML carries those exact identity fields.
- The parent row maps `NCBITaxon:3042590` to `16SrI (Aster yellows group)`, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Bacillati`, `Mycoplasmatota`, `Mollicutes`, `Acholeplasmatales`, `Acholeplasmataceae`, and `Candidatus Phytoplasma`.
- The single projected synonym, `Phytoplasma sp. onion yellows`, is the exact synonym present on the pinned NCBI row.

## Evidence

- The NCBI source attestation is supported exactly by the `NCBITaxon:100379` row in `data/raw/ncbitaxon_taxa.tsv`.
- The MADIN source attestation is supported exactly by the direct `NCBITaxon:100379` row in `data/raw/madin_taxa.tsv` with four trait assertions.
- The hidden-aware exact source scan also found two descendant NCBI strain rows that point to `NCBITaxon:100379` as their parent; those are child taxa, not same-record source assertions, and this parent record does not gather them into `strains`.

## Completeness

- The record correctly leaves GTDB, GOLD, causal-graph, BacDive strain, and strain-genome slots absent.
- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo` plus `data/taxa/PATHS.tsv` found the expected NCBI, MADIN, NCBI child, and PATHS rows; no direct GTDB, GOLD, LPSN, BacDive, StrainInfo, medium, or strain-genome evidence was found for the exact identifier, label, or slug.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-onion_yellows_phytoplasma.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
