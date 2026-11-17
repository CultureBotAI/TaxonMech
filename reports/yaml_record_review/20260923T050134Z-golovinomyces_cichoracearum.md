# YAML Record Review: Golovinomyces cichoracearum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/golovinomyces_cichoracearum.yaml
- Started UTC: 2026-09-23T05:01:34Z
- Finished UTC: 2026-09-23T05:01:34Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:62708` |
| Label | `Golovinomyces cichoracearum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:184027` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/golovinomyces_cichoracearum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/gnomoniopsis_castaneae.yaml data/taxa/eukaryota/gnomoniopsis_smithogilvyi.yaml data/taxa/eukaryota/goffeauzyma_gilvescens.yaml data/taxa/eukaryota/golovinomyces_cichoracearum.yaml` | Passed; the strict batch exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with four organism assertions, four exact current native GOLD organisms with seven linked native GOLD projects and four linked native analyses, no exact NCBI type-material rows, no exact StrainInfo rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:62708`, `label: Golovinomyces cichoracearum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:184027`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:7922`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Golovinomyces`; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:40003`, which records four retained direct organisms for `NCBITaxon:62708`; this agrees with `source_attestations[1].assertion_count: 4` and its organism assertion unit. The current native GOLD catalogs also contain exact organisms `Go0111646`, `Go0631366`, `Go0631367`, and `Go0631368`, with seven linked native projects and four linked native analyses.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:62708`. `Erysiphe cichoracearum` and `Golovinomyces cichoracearum (DC.) Heluta, 1988` are present in `data/raw/ncbitaxon_taxa.tsv:7922` as exact synonyms, and the generated `Erysiphe cichoracearum DC., 1805` related synonym is present in the same source row.

The retained GOLD aggregate supplies four organism assertions. The current native GOLD catalogs have exact organism rows for `Race UCSC1`, `UMSG3`, `UCSC1`, and `UMSG1`; `Race UCSC1` links to four native GOLD projects and the other three organisms each link to one native GOLD project.

No side `data/raw/ncbi_merged_ids.tsv` row, exact NCBI type-material row, exact StrainInfo row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/golovinomyces_cichoracearum.yaml` plus `just validate-strict data/taxa/eukaryota/golovinomyces_cichoracearum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `golovinomyces_cichoracearum` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID, organism GOLD ID, or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
