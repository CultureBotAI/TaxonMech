# YAML Record Review: Salmonella enterica subsp. enterica serovar Agona str. SA-4

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_agona_str_sa_4.yaml
- Started UTC: 2026-09-22T16:39:40Z
- Finished UTC: 2026-09-22T16:39:40Z
- Verdict: needs curation

## Target

Reviewed `data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_agona_str_sa_4.yaml`, the generated `TaxonRecord` for `NCBITaxon:1003188` / `Salmonella enterica subsp. enterica serovar Agona str. SA-4`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1003188`
- Label: `Salmonella enterica subsp. enterica serovar Agona str. SA-4`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:58095` / `Salmonella enterica subsp. enterica serovar Agona`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_agona_str_sa_4.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_agona_str_sa_4.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_agona_str_sa_3.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_agona_str_sa_4.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_agona_str_sa_5.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_agona_str_sar_b1.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:1003188` to the strain label `Salmonella enterica subsp. enterica serovar Agona str. SA-4`, rank `STRAIN`, parent `NCBITaxon:58095`, exact synonym `Salmonella enterica subsp. enterica serovar Agona strain SA-4`, source bundle `ncbitaxon|gtdb|gold`, and snapshot date `2026-09-13`; the YAML carries those NCBI identity fields.
- The parent row maps `NCBITaxon:58095` to `Salmonella enterica subsp. enterica serovar Agona`, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Pseudomonadati`, `Pseudomonadota`, `Gammaproteobacteria`, `Enterobacterales`, `Enterobacteriaceae`, `Salmonella`, `Salmonella enterica`, and `Salmonella enterica subsp. enterica`.
- The GTDB mapping row for `NCBITaxon:1003188` exists in `data/raw/gtdb_mappings.tsv`, but it maps the strain to species-level `GTDB:s__Salmonella_enterica`, which is broader than this exact strain.

## Evidence

- The NCBI source attestation and the same-taxon GOLD organism row are supported exactly by `data/raw/ncbitaxon_taxa.tsv` and `data/raw/gold_organisms.tsv`.
- The GTDB source row is present, but its `genome_count: 21527` belongs to the entire `GTDB:s__Salmonella_enterica` species cluster and should not be treated as 21,527 genomes attesting this `SA-4` strain.

## Completeness

- The record correctly leaves causal-graph and BacDive strain slots absent; no causal graph or same-taxon BacDive strain was attested in the reviewed raw rows.
- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo` plus `data/taxa/PATHS.tsv` found the exact NCBI, GTDB, GOLD, and PATHS rows and no LPSN, BacDive, StrainInfo, trait, medium, or strain-genome evidence that would require additional same-strain blocks.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| major | A GTDB species cluster is over-scoped onto the strain. `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Salmonella_enterica` to `NCBITaxon:1003188` with `skos:closeMatch` and `genome_count: 21527`, and the generated strain record turns that into a GTDB xref, a `Salmonella enterica` exact synonym, and a GTDB source attestation with `21527 GENOME`. A species cluster is broader than the `SA-4` strain, so this mapping should not be represented as strain-level close/equivalent evidence. | `data/raw/gtdb_mappings.tsv` generation and the taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`. |

## Recommended Edits

- Adjust GTDB mapping generation so species-level GTDB clusters are not emitted as `skos:closeMatch` rows for NCBI strain taxa, or adjust seeding so those broader species mappings do not create `EXACT_SYNONYM`, `xrefs`, or strain-level genome counts.
- Regenerate `data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_agona_str_sa_4.yaml` from the corrected maintained mapping rows.

## Follow-up Checks

- Rerun `just validate data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_agona_str_sa_4.yaml` and a strict validation over the regenerated file.
- Re-check `data/raw/gtdb_mappings.tsv` for `NCBITaxon:1003188` and verify that `GTDB:s__Salmonella_enterica` is absent from this strain or no longer projected as a close/equivalent synonym.

## Additional Notes

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-salmonella_enterica_subsp_enterica_serovar_agona_str_sa_4.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
