# YAML Record Review: Nitrospirillum viridazoti Y2

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/nitrospirillum_viridazoti_y2.yaml
- Started UTC: 2026-09-22T16:43:29Z
- Finished UTC: 2026-09-22T16:43:29Z
- Verdict: needs curation

## Target

Reviewed `data/taxa/bacteria/nitrospirillum_viridazoti_y2.yaml`, the generated `TaxonRecord` for `NCBITaxon:1003237` / `Nitrospirillum viridazoti Y2`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1003237`
- Label: `Nitrospirillum viridazoti Y2`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:3144925` / `Nitrospirillum viridazoti`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/nitrospirillum_viridazoti_y2.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/nitrospirillum_viridazoti_y2.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/rickettsia_typhi_str_th1527.yaml data/taxa/bacteria/rickettsia_typhi_str_b9991cwpp.yaml data/taxa/bacteria/nitrospirillum_viridazoti_y2.yaml data/taxa/bacteria/chlamydia_abortus_llg.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:1003237` to the strain label `Nitrospirillum viridazoti Y2`, rank `STRAIN`, parent `NCBITaxon:3144925`, exact synonyms `Azospirillum amazonense Y2`, `Nitrospirillum amazonense Y2`, and `Nitrospirillum viridazoti ATCC 35120`, source bundle `ncbitaxon|gtdb|gold|madin_etal`, and snapshot date `2026-09-13`; the YAML carries those NCBI identity fields.
- The parent row maps `NCBITaxon:3144925` to species `Nitrospirillum viridazoti`, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Pseudomonadati`, `Pseudomonadota`, `Alphaproteobacteria`, `Rhodospirillales`, `Azospirillaceae`, and `Nitrospirillum`.
- The GTDB mapping row for `NCBITaxon:1003237` exists in `data/raw/gtdb_mappings.tsv`, but it maps the strain to species-level `GTDB:s__Nitrospirillum_viridazoti`, which is broader than this exact strain.

## Evidence

- The NCBI source attestation, one same-taxon GOLD organism attestation, and three same-taxon MADIN trait attestations are supported exactly by `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gold_organisms.tsv`, and `data/raw/madin_taxa.tsv`.
- The GTDB source row is present, but its `genome_count: 4` belongs to the `GTDB:s__Nitrospirillum_viridazoti` species cluster and should not be treated as four genomes attesting this exact `Y2` strain.

## Completeness

- The record correctly leaves causal-graph and direct BacDive strain slots absent; `data/raw/bacdive_strains.tsv` classifies `kgmicrobe.strain:bacdive_13970` under the parent species `NCBITaxon:3144925` and the legacy parent `NCBITaxon:28077`, not under this exact NCBI strain taxon.
- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo` plus `data/taxa/PATHS.tsv` found the exact NCBI, GTDB, GOLD, MADIN, PATHS, and strain-inventory rows and no LPSN, ATB, medium, or causal-graph evidence that would require additional same-strain blocks.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| major | A GTDB species cluster is over-scoped onto the strain. `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Nitrospirillum_viridazoti` to `NCBITaxon:1003237` with `skos:closeMatch` and `genome_count: 4`, and the generated strain record turns that into a GTDB xref, a `Nitrospirillum viridazoti` exact synonym, and a GTDB source attestation with `4 GENOME`. A species cluster is broader than the `Y2` strain, so this mapping should not be represented as strain-level close/equivalent evidence. | `data/raw/gtdb_mappings.tsv` generation and the taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`. |

## Recommended Edits

- Adjust GTDB mapping generation so species-level GTDB clusters are not emitted as `skos:closeMatch` rows for NCBI strain taxa, or adjust seeding so those broader species mappings do not create `EXACT_SYNONYM`, `xrefs`, or strain-level genome counts.
- Regenerate `data/taxa/bacteria/nitrospirillum_viridazoti_y2.yaml` from the corrected maintained mapping rows.

## Follow-up Checks

- Rerun `just validate data/taxa/bacteria/nitrospirillum_viridazoti_y2.yaml` and a strict validation over the regenerated file.
- Re-check `data/raw/gtdb_mappings.tsv` for `NCBITaxon:1003237` and verify that `GTDB:s__Nitrospirillum_viridazoti` is absent from this strain or no longer projected as a close/equivalent synonym.

## Additional Notes

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-nitrospirillum_viridazoti_y2.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- Exact same-NCBI rows for `NCBITaxon:1003237` also exist in `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; those are retained in the strain inventories keyed to `kgmicrobe.strain:bacdive_13970`, while the canonical BacDive strain row is filed under species-level taxa.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
