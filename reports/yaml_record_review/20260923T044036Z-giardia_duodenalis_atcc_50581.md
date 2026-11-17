# YAML Record Review: Giardia duodenalis ATCC 50581

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/giardia_duodenalis_atcc_50581.yaml
- Started UTC: 2026-09-23T04:40:36Z
- Finished UTC: 2026-09-23T04:40:36Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:598745` |
| Label | `Giardia duodenalis ATCC 50581` |
| Rank | `STRAIN` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5741` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/giardia_duodenalis_atcc_50581.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/giardia_duodenalis.yaml data/taxa/eukaryota/giardia_duodenalis_assemblage_b.yaml data/taxa/eukaryota/giardia_duodenalis_atcc_50581.yaml data/taxa/eukaryota/giardia_muris.yaml` | Passed; the strict batch exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, two exact current native GOLD organisms with two linked native GOLD projects and one linked native analysis, no exact NCBI type-material rows, no exact StrainInfo rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:598745`, `label: Giardia duodenalis ATCC 50581`, `rank: STRAIN`, `parent_taxon: NCBITaxon:5741`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:142083`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through species `Giardia duodenalis`; the bounded scan checked all 10 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:39742`, which records two retained direct organisms for `NCBITaxon:598745`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs also contain two exact organisms, `Go0004832` and `Go0007131`, both for `Giardia intestinalis ATCC 50581`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:598745`. The NCBI row has no exact, related, or broad synonyms, and the YAML correctly omits a `synonyms` block.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have two exact organisms, two linked projects, and one native analysis whose `AP PROJECT GOLD IDS` include `Gp0007131`.

No side `data/raw/ncbi_merged_ids.tsv` row, exact NCBI type-material row, exact StrainInfo row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded strain identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, no spurious synonym block, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/giardia_duodenalis_atcc_50581.yaml` plus `just validate-strict data/taxa/eukaryota/giardia_duodenalis_atcc_50581.yaml`.

## Additional Notes

No prior exact ignored review report existed for `giardia_duodenalis_atcc_50581` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
