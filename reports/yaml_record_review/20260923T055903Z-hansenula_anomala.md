# YAML Record Review: Hansenula anomala

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hansenula_anomala.yaml
- Started UTC: 2026-09-23T05:59:03Z
- Finished UTC: 2026-09-23T05:59:03Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:4927` |
| Label | `Hansenula anomala` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:34359` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hansenula_anomala.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hanseniaspora_uvarum.yaml data/taxa/eukaryota/hanseniaspora_valbyensis.yaml data/taxa/eukaryota/hanseniaspora_vineae.yaml data/taxa/eukaryota/hansenula_anomala.yaml` | Passed; the strict batch reported zero ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with five organism assertions, two exact current native GOLD organisms with two linked native GOLD projects and two linked native analyses, nine exact NCBI type-material rows, seven side NCBI merged-ID rows, no retained old IDs, 373 direct exact StrainInfo rows with 548 deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:4927`, `label: Hansenula anomala`, `rank: SPECIES`, `parent_taxon: NCBITaxon:34359`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2148`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hansenula`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37152`, which records five retained direct organisms for `NCBITaxon:4927`; this agrees with `source_attestations[1].assertion_count: 5` and its organism assertion unit. The current native GOLD catalogs contain two exact organisms, two linked projects, and two native analyses linked by `AP PROJECT GOLD IDS`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:4927`. All seven generated exact synonyms and all 15 generated related synonyms are present in `data/raw/ncbitaxon_taxa.tsv:2148`.

The retained GOLD aggregate supplies five organism assertions. The current native GOLD catalogs have exact organisms for `H01_10C` and `B1607`; both organisms have linked projects and both exact linked projects have native analysis rows.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:223224` through `data/raw/ncbi_type_material.tsv:223232` as nine spellings for `BCRC 22583`, `CBS 5759`, `DSM 6766`, and `NRRL Y-366`. StrainInfo also has 373 direct exact rows with 548 deposit rows for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

`data/raw/ncbi_merged_ids.tsv` maps seven side old IDs into `NCBITaxon:4927`: `NCBITaxon:1050175`, `NCBITaxon:1050176`, `NCBITaxon:1050177`, `NCBITaxon:1050178`, `NCBITaxon:1278006`, `NCBITaxon:683960`, and `NCBITaxon:885923`. None is present as a retained retired row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` value should be generated from them.

No exact BacDive row or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hansenula_anomala.yaml` plus `just validate-strict data/taxa/eukaryota/hansenula_anomala.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hansenula_anomala` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

The side NCBI merged-ID rows are not by themselves sufficient to generate `replaces` values. The generator emits `replaces` only from retained retired rows in `data/raw/ncbitaxon_taxa.tsv` with `retired_into`, and the bounded scan found no retained old IDs for this record.
