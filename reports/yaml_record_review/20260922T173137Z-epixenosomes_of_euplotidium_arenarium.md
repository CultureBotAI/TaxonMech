# YAML Record Review: Epixenosomes of Euplotidium arenarium

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/epixenosomes_of_euplotidium_arenarium.yaml
- Started UTC: 2026-09-22T17:31:37Z
- Finished UTC: 2026-09-22T17:31:37Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/epixenosomes_of_euplotidium_arenarium.yaml`, the generated `TaxonRecord` for `NCBITaxon:100380` / `Epixenosomes of Euplotidium arenarium`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:100380`
- Label: `Epixenosomes of Euplotidium arenarium`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:278955` / `unclassified Opitutaceae`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/epixenosomes_of_euplotidium_arenarium.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/epixenosomes_of_euplotidium_arenarium.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/epixenosomes_of_euplotidium_arenarium.yaml data/taxa/bacteria/bacillus_sp_fg_1.yaml data/taxa/bacteria/paracoccus_sp_fg_2.yaml data/taxa/bacteria/planomicrobium_sp_fg_3.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:100380` to species label `Epixenosomes of Euplotidium arenarium`, parent `NCBITaxon:278955`, source bundle `ncbitaxon`, and snapshot date `2026-09-13`; the YAML carries those exact identity fields.
- The parent row maps `NCBITaxon:278955` to the `unclassified Opitutaceae` node, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Pseudomonadati`, `PVC group`, `Verrucomicrobiota`, `Opitutia`, `Opitutales`, and `Opitutaceae`.
- No GTDB mapping, synonym, or xref is projected for this NCBI-only species record, matching the reviewed source rows.

## Evidence

- The NCBI source attestation is supported exactly by the `NCBITaxon:100380` row in `data/raw/ncbitaxon_taxa.tsv`.

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

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-epixenosomes_of_euplotidium_arenarium.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
