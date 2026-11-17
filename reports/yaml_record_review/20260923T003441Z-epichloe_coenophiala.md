# YAML Record Review: Epichloe coenophiala

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/epichloe_coenophiala.yaml
- Started UTC: 2026-09-23T00:34:41Z
- Finished UTC: 2026-09-23T00:34:41Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5047` |
| Label | `Epichloe coenophiala` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5112` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/epichloe_coenophiala.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/epichloe_baconii.yaml data/taxa/eukaryota/epichloe_brachyelytri.yaml data/taxa/eukaryota/epichloe_bromicola.yaml data/taxa/eukaryota/epichloe_coenophiala.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with seven organism assertions, four current exact native GOLD organism rows, eight current exact native GOLD project rows, no native GOLD analyses, two NCBI type-material rows, 31 exact StrainInfo rows with 37 deposits, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5047`, `label: Epichloe coenophiala`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5112`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2204`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Epichloe` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37392`, which records seven retained direct organisms for `NCBITaxon:5047`; this agrees with `source_attestations[1].assertion_count: 7` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5047`. The YAML preserves NCBI's exact synonyms `Acremonium coenophialum` and `Neotyphodium coenophialum`, plus both related synonyms filed for this row; NCBI supplies no broad synonyms or old-ID side rows.

The two NCBI type-material rows preserve aliases for `CBS 494.82` under `Epichloe coenophiala`. The retained GOLD aggregate row carries seven organism assertions; the current exact native GOLD catalogs contain four organism rows and eight matching project rows, with no linked native GOLD analysis rows.

StrainInfo contains 31 exact target rows with 37 deposit designations for `Epichloe coenophiala`; those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI exact synonyms, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/epichloe_coenophiala.yaml` plus `just validate-strict data/taxa/eukaryota/epichloe_coenophiala.yaml`.

## Additional Notes

The native GOLD sample was expanded by exact ID to account for all 8 current native project rows. The retained GOLD aggregate count is higher than the current native exact organism-row count, but `source_attestations[1].assertion_count: 7` matches the retained aggregate row used by the generator.
