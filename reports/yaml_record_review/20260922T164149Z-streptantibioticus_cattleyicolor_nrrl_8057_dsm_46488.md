# YAML Record Review: Streptantibioticus cattleyicolor NRRL 8057 = DSM 46488

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/streptantibioticus_cattleyicolor_nrrl_8057_dsm_46488.yaml
- Started UTC: 2026-09-22T16:41:49Z
- Finished UTC: 2026-09-22T16:41:49Z
- Verdict: needs curation

## Target

Reviewed `data/taxa/bacteria/streptantibioticus_cattleyicolor_nrrl_8057_dsm_46488.yaml`, the generated `TaxonRecord` for `NCBITaxon:1003195` / `Streptantibioticus cattleyicolor NRRL 8057 = DSM 46488`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1003195`
- Label: `Streptantibioticus cattleyicolor NRRL 8057 = DSM 46488`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:29303` / `Streptantibioticus cattleyicolor`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/streptantibioticus_cattleyicolor_nrrl_8057_dsm_46488.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/streptantibioticus_cattleyicolor_nrrl_8057_dsm_46488.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_tennessee_str_txsc_txsc08_19.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_tennessee_str_txsc_txsc08_21.yaml data/taxa/bacteria/streptantibioticus_cattleyicolor_nrrl_8057_dsm_46488.yaml data/taxa/bacteria/achromobacter_insuavis_axx_a.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:1003195` to the strain label `Streptantibioticus cattleyicolor NRRL 8057 = DSM 46488`, rank `STRAIN`, parent `NCBITaxon:29303`, four `Streptomyces cattleya` exact synonyms, source bundle `ncbitaxon|gtdb|gold|madin_etal`, and snapshot date `2026-09-13`; the YAML carries those NCBI identity fields.
- The parent row maps `NCBITaxon:29303` to species `Streptantibioticus cattleyicolor`, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Bacillati`, `Actinomycetota`, `Actinomycetes`, `Kitasatosporales`, `Streptomycetaceae`, and `Streptantibioticus`.
- The GTDB mapping row for `NCBITaxon:1003195` exists in `data/raw/gtdb_mappings.tsv`, but it maps the strain to species-level `GTDB:s__Streptantibioticus_cattleyicolor`, which is broader than this exact strain.

## Evidence

- The NCBI source attestation, two same-taxon GOLD organism attestations, and one same-taxon MADIN trait attestation are supported exactly by `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gold_organisms.tsv`, and `data/raw/madin_taxa.tsv`.
- The GTDB source row is present, but its `genome_count: 3` belongs to the `GTDB:s__Streptantibioticus_cattleyicolor` species cluster and should not be treated as three genomes attesting this exact `NRRL 8057 = DSM 46488` strain.

## Completeness

- The record correctly leaves causal-graph and direct BacDive strain slots absent; `data/raw/bacdive_strains.tsv` classifies `kgmicrobe.strain:bacdive_16011` under the parent species `NCBITaxon:29303`, not under this exact NCBI strain taxon.
- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo` plus `data/taxa/PATHS.tsv` found the exact NCBI, GTDB, GOLD, MADIN, PATHS, and strain-inventory rows and no LPSN, ATB, medium, or causal-graph evidence that would require additional same-strain blocks.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| major | A GTDB species cluster is over-scoped onto the strain. `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Streptantibioticus_cattleyicolor` to `NCBITaxon:1003195` with `skos:closeMatch` and `genome_count: 3`, and the generated strain record turns that into a GTDB xref, a `Streptantibioticus cattleyicolor` exact synonym, and a GTDB source attestation with `3 GENOME`. A species cluster is broader than the `NRRL 8057 = DSM 46488` strain, so this mapping should not be represented as strain-level close/equivalent evidence. | `data/raw/gtdb_mappings.tsv` generation and the taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`. |

## Recommended Edits

- Adjust GTDB mapping generation so species-level GTDB clusters are not emitted as `skos:closeMatch` rows for NCBI strain taxa, or adjust seeding so those broader species mappings do not create `EXACT_SYNONYM`, `xrefs`, or strain-level genome counts.
- Regenerate `data/taxa/bacteria/streptantibioticus_cattleyicolor_nrrl_8057_dsm_46488.yaml` from the corrected maintained mapping rows.

## Follow-up Checks

- Rerun `just validate data/taxa/bacteria/streptantibioticus_cattleyicolor_nrrl_8057_dsm_46488.yaml` and a strict validation over the regenerated file.
- Re-check `data/raw/gtdb_mappings.tsv` for `NCBITaxon:1003195` and verify that `GTDB:s__Streptantibioticus_cattleyicolor` is absent from this strain or no longer projected as a close/equivalent synonym.

## Additional Notes

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-streptantibioticus_cattleyicolor_nrrl_8057_dsm_46488.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- Exact same-NCBI rows for `NCBITaxon:1003195` also exist in `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, and `data/straininfo/assemblies.tsv`; those are retained in the strain inventories keyed to `kgmicrobe.strain:bacdive_16011`, while the canonical BacDive strain row is filed under the parent species.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
