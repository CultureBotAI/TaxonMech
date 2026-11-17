# YAML Record Review: Epichloe hybrida

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/epichloe_hybrida.yaml
- Started UTC: 2026-09-23T00:41:20Z
- Finished UTC: 2026-09-23T00:41:20Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1915362` |
| Label | `Epichloe hybrida` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5112` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/epichloe_hybrida.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/epichloe_gansuensis_e7080.yaml data/taxa/eukaryota/epichloe_hybrida.yaml data/taxa/eukaryota/epichloe_sylvatica.yaml data/taxa/eukaryota/epichloe_typhina.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, one current exact native GOLD organism row, two current exact native GOLD project rows, no native GOLD analyses, three NCBI type-material rows, one NCBI merged-ID side row, no exact StrainInfo or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1915362`, `label: Epichloe hybrida`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5112`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:494054`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Epichloe` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:17467`, which records two retained direct organisms for `NCBITaxon:1915362`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1915362`. The YAML preserves NCBI's three exact hybrid synonyms, plus all four related synonyms filed for this row.

`data/raw/ncbi_merged_ids.tsv:93398` maps the old side-inventory ID `NCBITaxon:71426` to `NCBITaxon:1915362`; it is not retained as a row with `retired_into` in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly has no generated `replaces` entry. The three NCBI type-material rows preserve holotype aliases for `ATCC-TSD-66` and type-material support for `Lp1`.

The retained GOLD aggregate row carries two organism assertions. The current exact native GOLD catalogs contain one organism row, `Go0098831`, with two matching projects and no matching native GOLD analysis rows. No exact StrainInfo, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, three NCBI exact synonyms, four NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/epichloe_hybrida.yaml` plus `just validate-strict data/taxa/eukaryota/epichloe_hybrida.yaml`.

## Additional Notes

The retained GOLD aggregate row has two organism assertions, while the local native GOLD export currently has one exact organism row for this taxon ID. The NCBI merged-ID side row is side evidence only; generated `replaces` comes from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`.
