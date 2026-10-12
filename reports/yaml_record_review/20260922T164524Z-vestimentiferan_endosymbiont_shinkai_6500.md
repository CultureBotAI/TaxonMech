# YAML Record Review: vestimentiferan endosymbiont 'Shinkai #6500'

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/vestimentiferan_endosymbiont_shinkai_6500.yaml
- Started UTC: 2026-09-22T16:45:24Z
- Finished UTC: 2026-09-22T16:45:24Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/vestimentiferan_endosymbiont_shinkai_6500.yaml`, the generated `TaxonRecord` for `NCBITaxon:100327` / `vestimentiferan endosymbiont 'Shinkai #6500'`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:100327`
- Label: `vestimentiferan endosymbiont 'Shinkai #6500'`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:32036` / `sulfur-oxidizing symbionts`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/vestimentiferan_endosymbiont_shinkai_6500.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/vestimentiferan_endosymbiont_shinkai_6500.yaml` | Passed. |
| `just validate-strict data/taxa/bacteria/bacillus_cereus_c1l.yaml data/taxa/bacteria/escarpia_spicata_endosymbiont_alvin_2837.yaml data/taxa/bacteria/escarpia_spicata_endosymbiont_alvin_2839.yaml data/taxa/bacteria/vestimentiferan_endosymbiont_shinkai_6500.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:100327` to species label `vestimentiferan endosymbiont 'Shinkai #6500'`, parent `NCBITaxon:32036`, source bundle `ncbitaxon`, and snapshot date `2026-09-13`; the YAML carries those exact identity fields.
- The parent row maps `NCBITaxon:32036` to the `sulfur-oxidizing symbionts` clade, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Pseudomonadati`, `Pseudomonadota`, `Gammaproteobacteria`, and `Gammaproteobacteria incertae sedis`.
- No GTDB mapping, external synonym, or xref is projected for this NCBI-only species record, matching the reviewed source rows.

## Evidence

- The NCBI source attestation is supported exactly by the `NCBITaxon:100327` row in `data/raw/ncbitaxon_taxa.tsv`.

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

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-vestimentiferan_endosymbiont_shinkai_6500.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
