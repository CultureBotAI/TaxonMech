# YAML Record Review: Hansenula ciferrii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hansenula_ciferrii.yaml
- Started UTC: 2026-09-23T06:01:41Z
- Finished UTC: 2026-09-23T06:01:41Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1041607` |
| Label | `Hansenula ciferrii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:34359` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hansenula_ciferrii.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/hansenula_ciferrii.yaml data/taxa/eukaryota/hansenula_lynferdii.yaml data/taxa/eukaryota/hansenula_queroliae.yaml data/taxa/eukaryota/hansenula_silvicultrix.yaml` | Passed; the strict batch reported zero ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, one exact current native GOLD organism with one linked native GOLD project and no linked native analyses, 17 exact NCBI type-material rows, two side NCBI merged-ID rows, no retained old IDs, 12 direct exact StrainInfo rows with 42 deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1041607`, `label: Hansenula ciferrii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:34359`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:223681`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hansenula`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:587`, which records two retained direct organisms for `NCBITaxon:1041607`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs contain one exact organism and one linked project.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1041607`. `Pichia ciferrii` and `Wickerhamomyces ciferrii` are present in `data/raw/ncbitaxon_taxa.tsv:223681` as exact synonyms, and all four generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have an exact organism for `NRRL Y-1031`, a linked `Gp0831223` project in `data/gold/projects.jsonl.gz:609778`, and no native analysis linked by the exact project ID.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:2529` through `data/raw/ncbi_type_material.tsv:2545` as 17 spellings for `BCRC 22168`, `CCRC 22168`, `ATCC 14091`, `CBS 111`, `IFO 0793`, `JCM 3599`, `NCYC 2651`, and `NRRL Y-1031`. StrainInfo also has 12 direct exact rows with 42 deposit rows for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

`data/raw/ncbi_merged_ids.tsv` maps side old IDs `NCBITaxon:1206466` and `NCBITaxon:36020` into `NCBITaxon:1041607`, but neither is present as a retained retired row in `data/raw/ncbitaxon_taxa.tsv` and no `replaces` value should be generated from them.

No exact BacDive row or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hansenula_ciferrii.yaml` plus `just validate-strict data/taxa/eukaryota/hansenula_ciferrii.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hansenula_ciferrii` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism and project rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

The side NCBI merged-ID rows are not by themselves sufficient to generate `replaces` values. The generator emits `replaces` only from retained retired rows in `data/raw/ncbitaxon_taxa.tsv` with `retired_into`, and the bounded scan found no retained old IDs for this record.
