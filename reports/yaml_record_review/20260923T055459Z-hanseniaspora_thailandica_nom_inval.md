# YAML Record Review: Hanseniaspora thailandica (nom. inval.)

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hanseniaspora_thailandica_nom_inval.yaml
- Started UTC: 2026-09-23T05:54:59Z
- Finished UTC: 2026-09-23T05:54:59Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:689838` |
| Label | `Hanseniaspora thailandica (nom. inval.)` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2638044` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hanseniaspora_thailandica_nom_inval.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hanseniaspora_pseudoguilliermondii.yaml data/taxa/eukaryota/hanseniaspora_singularis_nom_inval.yaml data/taxa/eukaryota/hanseniaspora_taiwanica_nom_inval.yaml data/taxa/eukaryota/hanseniaspora_thailandica_nom_inval.yaml` | Passed; the strict batch exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with five organism assertions, five exact current native GOLD organisms with five linked native GOLD projects and no linked native analyses, 13 side NCBI merged-ID rows, no retained old IDs, three direct exact StrainInfo rows with three deposit rows, no exact NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:689838`, `label: Hanseniaspora thailandica (nom. inval.)`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2638044`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:161978`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `unclassified Hanseniaspora`; the bounded scan checked all 14 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:41386`, which records five retained direct organisms for `NCBITaxon:689838`; this agrees with `source_attestations[1].assertion_count: 5` and its organism assertion unit. The current native GOLD catalogs also contain five exact organisms and five linked projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:689838`. `Hanseniaspora thailandica` is present in `data/raw/ncbitaxon_taxa.tsv:161978` as an exact synonym, and all 14 generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies five organism assertions. The current native GOLD catalogs have exact organisms for `yHDO734`, `yHDO735`, `yHDO736`, `yHMicronic5000035697`, and `ZIM 2325`; all five organisms have linked projects, and no exact linked project has a native analysis row.

`data/raw/ncbi_merged_ids.tsv` maps 13 side old IDs into `NCBITaxon:689838`: `NCBITaxon:374350`, `NCBITaxon:374351`, `NCBITaxon:374352`, `NCBITaxon:374353`, `NCBITaxon:374355`, `NCBITaxon:374356`, `NCBITaxon:532725`, `NCBITaxon:645136`, `NCBITaxon:645137`, `NCBITaxon:645138`, `NCBITaxon:645139`, `NCBITaxon:645140`, and `NCBITaxon:645141`. None is present as a retained retired row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` value should be generated from them.

StrainInfo has three direct exact rows with three deposit rows for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record. No NCBI type-material row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hanseniaspora_thailandica_nom_inval.yaml` plus `just validate-strict data/taxa/eukaryota/hanseniaspora_thailandica_nom_inval.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hanseniaspora_thailandica_nom_inval` before this report was written; the `find` check covered the ignored `reports/` tree.

The side NCBI merged-ID rows are not by themselves sufficient to generate `replaces` values. The generator emits `replaces` only from retained retired rows in `data/raw/ncbitaxon_taxa.tsv` with `retired_into`, and the bounded scan found no retained old IDs for this record.
