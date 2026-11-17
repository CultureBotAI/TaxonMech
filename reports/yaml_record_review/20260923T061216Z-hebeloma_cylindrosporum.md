# YAML Record Review: Hebeloma cylindrosporum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hebeloma_cylindrosporum.yaml
- Started UTC: 2026-09-23T06:12:16Z
- Finished UTC: 2026-09-23T06:12:16Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:76867` |
| Label | `Hebeloma cylindrosporum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:34453` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hebeloma_cylindrosporum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hawksworthiomyces_lignivorus.yaml data/taxa/eukaryota/hebeloma_cylindrosporum.yaml data/taxa/eukaryota/hebeloma_velutipes.yaml data/taxa/eukaryota/helenozyma_melibiosica.yaml` | Passed; the strict batch exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, one exact current native GOLD organism with one linked native GOLD project and no linked native analyses, eight exact NCBI type-material rows, one side NCBI merged-ID row, no retained old IDs, two direct exact StrainInfo rows with two deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:76867`, `label: Hebeloma cylindrosporum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:34453`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:11060`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hebeloma`; the bounded scan checked all 14 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:42639`, which records two retained direct organisms for `NCBITaxon:76867`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs contain one exact organism and one linked project.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:76867`. Both generated related synonyms are present in `data/raw/ncbitaxon_taxa.tsv:11060`, and there are no NCBI exact synonyms for this source row.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have an exact organism and a linked `Gp0002641` project for `Hebeloma cylindrosporum`; no exact linked project has a native analysis row.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:263879` through `data/raw/ncbi_type_material.tsv:263886` as eight spellings for `PC PC0088805` and `L 0054087`. StrainInfo also has two direct exact rows with two deposit rows for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

`data/raw/ncbi_merged_ids.tsv:92241` maps side old ID `NCBITaxon:686832` into `NCBITaxon:76867`, but that old ID is not present as a retained retired row in `data/raw/ncbitaxon_taxa.tsv` and no `replaces` value should be generated from it.

No exact BacDive row or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hebeloma_cylindrosporum.yaml` plus `just validate-strict data/taxa/eukaryota/hebeloma_cylindrosporum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hebeloma_cylindrosporum` before this report was written; the `find` check covered the ignored `reports/` tree.

The side NCBI merged-ID row is not by itself sufficient to generate a `replaces` value. The generator emits `replaces` only from retained retired rows in `data/raw/ncbitaxon_taxa.tsv` with `retired_into`, and the bounded scan found no retained old ID for this record.
