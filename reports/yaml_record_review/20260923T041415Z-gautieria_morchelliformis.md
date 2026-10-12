# YAML Record Review: Gautieria morchelliformis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/gautieria_morchelliformis.yaml
- Started UTC: 2026-09-23T04:14:15Z
- Finished UTC: 2026-09-23T04:14:15Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:112417` |
| Label | `Gautieria morchelliformis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:80643` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/gautieria_morchelliformis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/ganoderma_resinaceum.yaml data/taxa/eukaryota/gautieria_morchelliformis.yaml data/taxa/eukaryota/geastrum_triplex.yaml data/taxa/eukaryota/gelasinospora_brevispora.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, one exact current native GOLD organism with two linked native GOLD projects and no native analysis rows, no exact NCBI type-material rows, no exact StrainInfo rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:112417`, `label: Gautieria morchelliformis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:80643`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:20420`, which carries the same label, parent, rank, code, one exact synonym, one related synonym, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Gautieria`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:2380`, which records two retained direct organisms for `NCBITaxon:112417`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs contain one exact organism, `Go0036273` for strain `GMNE.BST`, with linked projects `Gp0036273` and `Gp0036274`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:112417`. The YAML preserves the exact synonym `Gautieria morchellaeformis` and the related synonym `Gautieria morchelliformis Vittad., 1831` from the NCBI row.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have one exact organism for `Gautieria morchelliformis GMNE.BST`, two linked projects, and no native GOLD analysis currently links to those projects.

No side `data/raw/ncbi_merged_ids.tsv` row, exact NCBI type-material row, exact StrainInfo row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, one exact synonym, one related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/gautieria_morchelliformis.yaml` plus `just validate-strict data/taxa/eukaryota/gautieria_morchelliformis.yaml`.

## Additional Notes

No prior exact ignored review report existed for `gautieria_morchelliformis` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
