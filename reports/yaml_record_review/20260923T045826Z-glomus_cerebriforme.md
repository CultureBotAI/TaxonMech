# YAML Record Review: Glomus cerebriforme

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/glomus_cerebriforme.yaml
- Started UTC: 2026-09-23T04:58:26Z
- Finished UTC: 2026-09-23T04:58:26Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:658196` |
| Label | `Glomus cerebriforme` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:4875` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/glomus_cerebriforme.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/glomus_cerebriforme.yaml data/taxa/eukaryota/glonium_stellatum.yaml data/taxa/eukaryota/glucitozyma_multigemmis.yaml data/taxa/eukaryota/glutinoglossum_americanum.yaml` | Passed; the strict batch scanned 4 files with 0 error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with three organism assertions, three exact current native GOLD organisms with three linked native GOLD projects and two linked native analyses, two exact NCBI type-material rows, no exact StrainInfo rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:658196`, `label: Glomus cerebriforme`, `rank: SPECIES`, `parent_taxon: NCBITaxon:4875`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:152211`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Glomus`; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:40613`, which records three retained direct organisms for `NCBITaxon:658196`; this agrees with `source_attestations[1].assertion_count: 3` and its organism assertion unit. The current native GOLD catalogs contain exact organisms `Go0112003`, `Go0517195`, and `Go0589056`, with three linked native projects and two linked native analyses.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:658196`. The sole synonym, `Glomus cerebriforme McGee, 1986`, is present in `data/raw/ncbitaxon_taxa.tsv:152211` as a related synonym and is preserved with `synonym_type: RELATED_SYNONYM`.

The retained GOLD aggregate supplies three organism assertions. The current native GOLD catalogs have exact organism and project rows for `DAOM227022`, `JS1`, and `DAOM 227022`, with native analyses linked to the `JS1` and spaced `DAOM 227022` projects.

NCBI type-material rows list `ADW 16899` and `ADW:16899` as holotype material under `NCBITaxon:658196`.

No side `data/raw/ncbi_merged_ids.tsv` row, exact StrainInfo row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, one generated NCBI related synonym, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/glomus_cerebriforme.yaml` plus `just validate-strict data/taxa/eukaryota/glomus_cerebriforme.yaml`.

## Additional Notes

No prior exact ignored review report existed for `glomus_cerebriforme` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID, organism GOLD ID, or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
