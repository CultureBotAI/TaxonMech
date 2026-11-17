# YAML Record Review: Giardia duodenalis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/giardia_duodenalis.yaml
- Started UTC: 2026-09-23T04:40:36Z
- Finished UTC: 2026-09-23T04:40:36Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5741` |
| Label | `Giardia duodenalis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5740` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/giardia_duodenalis.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/giardia_duodenalis.yaml data/taxa/eukaryota/giardia_duodenalis_assemblage_b.yaml data/taxa/eukaryota/giardia_duodenalis_atcc_50581.yaml data/taxa/eukaryota/giardia_muris.yaml` | Passed; the strict batch exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with five organism assertions, three exact current native GOLD organisms with six linked native GOLD projects and four linked native analysis rows, no exact NCBI type-material rows, 15 exact StrainInfo records carrying 15 exact deposit rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5741`, `label: Giardia duodenalis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5740`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2553`, which carries the same label, parent, rank, code, three exact synonyms, one related synonym, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Giardia`; the bounded scan checked all nine lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:39217`, which records five retained direct organisms for `NCBITaxon:5741`; this agrees with `source_attestations[1].assertion_count: 5` and its organism assertion unit. The current native GOLD catalogs contain three exact organisms, `Go0008835`, `Go0008836`, and `Go0038768`, with six linked projects and four linked analysis rows.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5741`. The YAML preserves exact synonyms `Giardia intestinalis`, `Giardia lamblia`, and `Lamblia intestinalis`, and it preserves the related synonym from the NCBI row.

The retained GOLD aggregate supplies five organism assertions. The current native GOLD catalogs have exact organisms for `Giardia intestinalis assemblage A, AS175`, `Giardia intestinalis assemblage A, AS98`, and `Giardia intestinalis GS`; the GS organism has four linked projects, `Gp0038768`, `Gp0038769`, `Gp0039324`, and `Gp0779587`, and native analyses link to all but `Gp0039324`.

StrainInfo has 15 exact target records and 15 exact deposits. These side rows do not create generated local strain entries by themselves.

No side `data/raw/ncbi_merged_ids.tsv` row, exact NCBI type-material row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries directly under this species.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, three exact synonyms, one related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/giardia_duodenalis.yaml` plus `just validate-strict data/taxa/eukaryota/giardia_duodenalis.yaml`.

## Additional Notes

No prior exact ignored review report existed for `giardia_duodenalis` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:5741` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.
