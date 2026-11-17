# YAML Record Review: Hymenoscyphus fraxineus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hymenoscyphus_fraxineus.yaml
- Started UTC: 2026-09-23T07:39:59Z
- Finished UTC: 2026-09-23T07:39:59Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:746836` |
| Label | `Hymenoscyphus fraxineus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5182` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hymenoscyphus_fraxineus.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/hymenoscyphus_fraxineus.yaml data/taxa/eukaryota/hymenoscyphus_fructigenus.yaml data/taxa/eukaryota/hymenoscyphus_infarciens.yaml data/taxa/eukaryota/hymenoscyphus_laetus.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, two exact current native GOLD organisms with two linked native GOLD projects and two linked native GOLD analyses, 15 exact NCBI type-material rows, two side NCBI merged-ID rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:746836`, `label: Hymenoscyphus fraxineus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5182`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:172125`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hymenoscyphus`; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:42223`, which records two retained direct organisms for `NCBITaxon:746836`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs also contain two exact organisms, two linked projects, and two linked analyses.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:746836`. `Chalara fraxinea` and `Hymenoscyphus pseudoalbidus` are present in `data/raw/ncbitaxon_taxa.tsv:172125` as exact synonyms, and all six authorship-bearing, provisional, or common-name related synonyms are present in the source row.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have exact `Go0118890` and `Go0631542` organisms for `CBS 133217` and `nf4`, linked `Gp0124450` and `Gp0645052` projects, and two native analyses linked by the same project IDs.

NCBI carries 15 exact type-material rows for `Chalara fraxine`, `Chalara fraxinea`, and `Hymenoscyphus pseudoalbidus` at `data/raw/ncbi_type_material.tsv:261659` through `data/raw/ncbi_type_material.tsv:261673`, spanning ZT Myc 2022, CBS 122504, HMIPC 17039, and Oth_01 spelling variants.

The side merged-ID inventory maps old `NCBITaxon:299509` and `NCBITaxon:515165` to current `NCBITaxon:746836`, but no retained retired NCBI row has `retired_into: NCBITaxon:746836`, so no generated `replaces` entry is expected.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hymenoscyphus_fraxineus.yaml` plus `just validate-strict data/taxa/eukaryota/hymenoscyphus_fraxineus.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hymenoscyphus_fraxineus` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
