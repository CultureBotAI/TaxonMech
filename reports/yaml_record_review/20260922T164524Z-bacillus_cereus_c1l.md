# YAML Record Review: Bacillus cereus C1L

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/bacillus_cereus_c1l.yaml
- Started UTC: 2026-09-22T16:45:24Z
- Finished UTC: 2026-09-22T16:45:24Z
- Verdict: needs curation

## Target

Reviewed `data/taxa/bacteria/bacillus_cereus_c1l.yaml`, the generated `TaxonRecord` for `NCBITaxon:1003239` / `Bacillus cereus C1L`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1003239`
- Label: `Bacillus cereus C1L`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1396` / `Bacillus cereus`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/bacillus_cereus_c1l.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/bacillus_cereus_c1l.yaml` | Passed. |
| `just validate-strict data/taxa/bacteria/bacillus_cereus_c1l.yaml data/taxa/bacteria/escarpia_spicata_endosymbiont_alvin_2837.yaml data/taxa/bacteria/escarpia_spicata_endosymbiont_alvin_2839.yaml data/taxa/bacteria/vestimentiferan_endosymbiont_shinkai_6500.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:1003239` to the strain label `Bacillus cereus C1L`, rank `STRAIN`, parent `NCBITaxon:1396`, exact synonyms `Bacillus cereus str. C1L` and `Bacillus cereus strain C1L`, source bundle `ncbitaxon|gtdb|madin_etal`, and snapshot date `2026-09-13`; the YAML carries those NCBI identity fields.
- The parent row maps `NCBITaxon:1396` to species `Bacillus cereus`, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Bacillati`, `Bacillota`, `Bacilli`, `Caryophanales`, `Bacillaceae`, `Bacillus`, and `Bacillus cereus group`.
- The GTDB mapping row for `NCBITaxon:1003239` exists in `data/raw/gtdb_mappings.tsv`, but it maps the strain to species-level `GTDB:s__Bacillus_A_cereus`, which is broader than this exact strain.

## Evidence

- The NCBI source attestation and five same-taxon MADIN trait attestations are supported exactly by `data/raw/ncbitaxon_taxa.tsv` and `data/raw/madin_taxa.tsv`.
- The GTDB source row is present, but its `genome_count: 2275` belongs to the `GTDB:s__Bacillus_A_cereus` species cluster and should not be treated as 2,275 genomes attesting this exact `C1L` strain.

## Completeness

- The record correctly leaves GOLD, causal-graph, and BacDive strain slots absent; no GOLD organism, causal graph, or same-taxon BacDive strain was attested in the reviewed raw rows.
- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo` plus `data/taxa/PATHS.tsv` found the exact NCBI, GTDB, MADIN, and PATHS rows and no GOLD, LPSN, BacDive, StrainInfo, medium, or strain-genome evidence that would require additional same-strain blocks.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| major | A GTDB species cluster is over-scoped onto the strain. `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Bacillus_A_cereus` to `NCBITaxon:1003239` with `skos:closeMatch` and `genome_count: 2275`, and the generated strain record turns that into a GTDB xref, a `Bacillus A cereus` exact synonym, and a GTDB source attestation with `2275 GENOME`. A species cluster is broader than the `C1L` strain, so this mapping should not be represented as strain-level close/equivalent evidence. | `data/raw/gtdb_mappings.tsv` generation and the taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`. |

## Recommended Edits

- Adjust GTDB mapping generation so species-level GTDB clusters are not emitted as `skos:closeMatch` rows for NCBI strain taxa, or adjust seeding so those broader species mappings do not create `EXACT_SYNONYM`, `xrefs`, or strain-level genome counts.
- Regenerate `data/taxa/bacteria/bacillus_cereus_c1l.yaml` from the corrected maintained mapping rows.

## Follow-up Checks

- Rerun `just validate data/taxa/bacteria/bacillus_cereus_c1l.yaml` and a strict validation over the regenerated file.
- Re-check `data/raw/gtdb_mappings.tsv` for `NCBITaxon:1003239` and verify that `GTDB:s__Bacillus_A_cereus` is absent from this strain or no longer projected as a close/equivalent synonym.

## Additional Notes

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-bacillus_cereus_c1l.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
