# YAML Record Review: Harringtonia lauricola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/harringtonia_lauricola.yaml
- Started UTC: 2026-09-23T06:09:39Z
- Finished UTC: 2026-09-23T06:09:39Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:483707` |
| Label | `Harringtonia lauricola` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2933754` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/harringtonia_lauricola.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/harpochytrium_sp.yaml data/taxa/eukaryota/harringtonia_lauricola.yaml data/taxa/eukaryota/hasegawazyma_lactosa.yaml data/taxa/eukaryota/haslea_ostrearia.yaml` | Passed; the strict batch reported zero ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, two exact current native GOLD organisms with two linked native GOLD projects and two linked native analyses, two exact NCBI type-material rows, five side NCBI merged-ID rows, no retained old IDs, no exact BacDive or StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:483707`, `label: Harringtonia lauricola`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2933754`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:108144`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Harringtonia`; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:36826`, which records two retained direct organisms for `NCBITaxon:483707`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs also contain two exact organisms, two linked projects, and two native analyses linked by `AP PROJECT GOLD IDS`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:483707`. `Raffaelea lauricola` is present in `data/raw/ncbitaxon_taxa.tsv:108144` as an exact synonym, and all eight generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have exact organisms for `RL570` and `CBS 129006`; both organisms have linked projects and both exact linked projects have native analysis rows.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:221243` and `data/raw/ncbi_type_material.tsv:221244` as two spellings for `CBS 121567`.

`data/raw/ncbi_merged_ids.tsv` maps five side old IDs into `NCBITaxon:483707`: `NCBITaxon:481540`, `NCBITaxon:481541`, `NCBITaxon:490148`, `NCBITaxon:490149`, and `NCBITaxon:490880`. None is present as a retained retired row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` value should be generated from them.

No exact BacDive row, direct exact StrainInfo row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive or StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/harringtonia_lauricola.yaml` plus `just validate-strict data/taxa/eukaryota/harringtonia_lauricola.yaml`.

## Additional Notes

No prior exact ignored review report existed for `harringtonia_lauricola` before this report was written; the `find` check covered the ignored `reports/` tree.

The side NCBI merged-ID rows are not by themselves sufficient to generate `replaces` values. The generator emits `replaces` only from retained retired rows in `data/raw/ncbitaxon_taxa.tsv` with `retired_into`, and the bounded scan found no retained old IDs for this record.
