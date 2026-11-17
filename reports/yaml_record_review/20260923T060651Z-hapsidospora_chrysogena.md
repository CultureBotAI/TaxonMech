# YAML Record Review: Hapsidospora chrysogena

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hapsidospora_chrysogena.yaml
- Started UTC: 2026-09-23T06:06:51Z
- Finished UTC: 2026-09-23T06:06:51Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5044` |
| Label | `Hapsidospora chrysogena` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:95323` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hapsidospora_chrysogena.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/haplosporangium_sp_z_27.yaml data/taxa/eukaryota/hapsidospora_chrysogena.yaml data/taxa/eukaryota/haptolina_brevifila.yaml data/taxa/eukaryota/haptolina_ericina.yaml` | Passed; the strict batch exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, three exact current native GOLD organisms with two linked native GOLD projects and one linked native analysis, 14 exact NCBI type-material rows, one side NCBI merged-ID row, no retained old IDs, one exact StrainInfo deposit-side row and no direct exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5044`, `label: Hapsidospora chrysogena`, `rank: SPECIES`, `parent_taxon: NCBITaxon:95323`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2202`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hapsidospora`; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37381`, which records two retained direct organisms for `NCBITaxon:5044`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs contain three exact organisms, two linked projects, and one native analysis linked by `AP PROJECT GOLD IDS`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5044`. `Cephalosporium acremonium`, `Cephalosporium chrysogenum`, and `Hapsidospora sp. LH-2022a` are present in `data/raw/ncbitaxon_taxa.tsv:2202` as exact synonyms, and all three generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have exact organisms for two unnamed records and `ATCC 11550`; `Go0005662` and `Go0095146` have linked projects, and the `Gp0095146` project has a native analysis row.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:225124` through `data/raw/ncbi_type_material.tsv:225137` as 14 spellings for `ATCC 14615`, `CBS 144.62`, `CECT 2718`, `HACC 113`, `IFO 30055`, `IMI 091579`, and `MUCL 9718`. StrainInfo also has one exact deposit-side row for this taxon, but no direct exact StrainInfo rows and no joins into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

`data/raw/ncbi_merged_ids.tsv:60247` maps side old ID `NCBITaxon:3003027` into `NCBITaxon:5044`, but that old ID is not present as a retained retired row in `data/raw/ncbitaxon_taxa.tsv` and no `replaces` value should be generated from it.

No exact BacDive row or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hapsidospora_chrysogena.yaml` plus `just validate-strict data/taxa/eukaryota/hapsidospora_chrysogena.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hapsidospora_chrysogena` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

The side NCBI merged-ID row is not by itself sufficient to generate a `replaces` value. The generator emits `replaces` only from retained retired rows in `data/raw/ncbitaxon_taxa.tsv` with `retired_into`, and the bounded scan found no retained old ID for this record.
