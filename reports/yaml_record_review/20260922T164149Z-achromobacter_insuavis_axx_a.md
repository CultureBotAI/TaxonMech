# YAML Record Review: Achromobacter insuavis AXX-A

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_insuavis_axx_a.yaml
- Started UTC: 2026-09-22T16:41:49Z
- Finished UTC: 2026-09-22T16:41:49Z
- Verdict: needs curation

## Target

Reviewed `data/taxa/bacteria/achromobacter_insuavis_axx_a.yaml`, the generated `TaxonRecord` for `NCBITaxon:1003200` / `Achromobacter insuavis AXX-A`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1003200`
- Label: `Achromobacter insuavis AXX-A`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1287735` / `Achromobacter insuavis`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/achromobacter_insuavis_axx_a.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_insuavis_axx_a.yaml` | Passed. |
| `just validate-strict data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_tennessee_str_txsc_txsc08_19.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_tennessee_str_txsc_txsc08_21.yaml data/taxa/bacteria/streptantibioticus_cattleyicolor_nrrl_8057_dsm_46488.yaml data/taxa/bacteria/achromobacter_insuavis_axx_a.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:1003200` to the strain label `Achromobacter insuavis AXX-A`, rank `STRAIN`, parent `NCBITaxon:1287735`, NCBI exact synonyms `Achromobacter insuavis str. AXX-A` and `Achromobacter insuavis strain AXX-A`, source bundle `ncbitaxon|gtdb|gold|madin_etal`, and snapshot date `2026-09-13`; the YAML carries those NCBI identity fields.
- The parent row maps `NCBITaxon:1287735` to species `Achromobacter insuavis`, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Pseudomonadati`, `Pseudomonadota`, `Betaproteobacteria`, `Burkholderiales`, `Alcaligenaceae`, and `Achromobacter`.
- The GTDB mapping row for `NCBITaxon:1003200` exists in `data/raw/gtdb_mappings.tsv`, but it maps the strain to `GTDB:s__Achromobacter_insuavis_A`, a GTDB species cluster with 10 genomes, which is broader than this exact strain.

## Evidence

- The NCBI source attestation, one same-taxon GOLD organism attestation, and four same-taxon MADIN trait attestations are supported exactly by `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gold_organisms.tsv`, and `data/raw/madin_taxa.tsv`.
- The GTDB source row is present, but its `genome_count: 10` belongs to the `GTDB:s__Achromobacter_insuavis_A` species cluster and should not be treated as 10 genomes attesting this exact `AXX-A` strain.

## Completeness

- The record correctly leaves causal-graph and BacDive strain slots absent; no causal graph or same-taxon BacDive strain was attested in the reviewed raw rows.
- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo` plus `data/taxa/PATHS.tsv` found the exact NCBI, GTDB, GOLD, MADIN, and PATHS rows and no LPSN, BacDive, StrainInfo, medium, or strain-genome evidence that would require additional same-strain blocks.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| major | A GTDB species cluster is over-scoped onto the strain. `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Achromobacter_insuavis_A` to `NCBITaxon:1003200` with `skos:closeMatch` and `genome_count: 10`, and the generated strain record turns that into a GTDB xref, an `Achromobacter insuavis A` exact synonym, and a GTDB source attestation with `10 GENOME`. A GTDB species cluster is broader than the `AXX-A` strain, so this mapping should not be represented as strain-level close/equivalent evidence. | `data/raw/gtdb_mappings.tsv` generation and the taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`. |

## Recommended Edits

- Adjust GTDB mapping generation so GTDB species clusters are not emitted as `skos:closeMatch` rows for NCBI strain taxa, or adjust seeding so those broader species mappings do not create `EXACT_SYNONYM`, `xrefs`, or strain-level genome counts.
- Regenerate `data/taxa/bacteria/achromobacter_insuavis_axx_a.yaml` from the corrected maintained mapping rows.

## Follow-up Checks

- Rerun `just validate data/taxa/bacteria/achromobacter_insuavis_axx_a.yaml` and a strict validation over the regenerated file.
- Re-check `data/raw/gtdb_mappings.tsv` for `NCBITaxon:1003200` and verify that `GTDB:s__Achromobacter_insuavis_A` is absent from this strain or no longer projected as a close/equivalent synonym.

## Additional Notes

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-achromobacter_insuavis_axx_a.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
