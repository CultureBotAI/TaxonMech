# YAML Record Review: Giardia duodenalis assemblage B

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/giardia_duodenalis_assemblage_b.yaml
- Started UTC: 2026-09-23T04:40:36Z
- Finished UTC: 2026-09-23T04:40:36Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1394984` |
| Label | `Giardia duodenalis assemblage B` |
| Rank | `CLADE` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:3697922` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/giardia_duodenalis_assemblage_b.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/giardia_duodenalis.yaml data/taxa/eukaryota/giardia_duodenalis_assemblage_b.yaml data/taxa/eukaryota/giardia_duodenalis_atcc_50581.yaml data/taxa/eukaryota/giardia_muris.yaml` | Passed; the strict batch exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with one linked native GOLD project and one linked native analysis, no exact NCBI type-material rows, no exact StrainInfo rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1394984`, `label: Giardia duodenalis assemblage B`, `rank: CLADE`, `parent_taxon: NCBITaxon:3697922`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:342874`, which carries the same label, parent, rank, code, two exact synonyms, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through species `Giardia enterica`; the bounded scan checked all 10 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy clade ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:9316`, which records one retained direct organism for `NCBITaxon:1394984`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain exact organism `Go0114147` for strain `BAH15c1`, with linked project `Gp0117886` and one linked native analysis.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1394984`. The YAML preserves exact synonyms `Giardia intestinalis assemblage B` and `Giardia lamblia (assemblage B)` from the NCBI row.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have one exact organism for `Giardia intestinalis assemblage B`, one linked project, and one native analysis whose `AP PROJECT GOLD IDS` include `Gp0117886`.

No side `data/raw/ncbi_merged_ids.tsv` row, exact NCBI type-material row, exact StrainInfo row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded clade identity, NCBI and GOLD source attestations, two exact synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/giardia_duodenalis_assemblage_b.yaml` plus `just validate-strict data/taxa/eukaryota/giardia_duodenalis_assemblage_b.yaml`.

## Additional Notes

No prior exact ignored review report existed for `giardia_duodenalis_assemblage_b` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
