# YAML Record Review: Geotrichum fermentans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/geotrichum_fermentans.yaml
- Started UTC: 2026-09-23T04:31:09Z
- Finished UTC: 2026-09-23T04:31:09Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:44066` |
| Label | `Geotrichum fermentans` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:43987` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/geotrichum_fermentans.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/geotrichum_fermentans.yaml data/taxa/eukaryota/geotrichum_ghanense.yaml data/taxa/eukaryota/geotrichum_histeridarum.yaml data/taxa/eukaryota/geotrichum_klebahnii.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, two exact current native GOLD organisms with two linked native GOLD projects and one linked native analysis, 13 exact NCBI type-material rows, seven exact StrainInfo records carrying 26 exact deposit rows, one NCBI merged-ID side row but no retained retired old IDs, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:44066`, `label: Geotrichum fermentans`, `rank: SPECIES`, `parent_taxon: NCBITaxon:43987`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:5323`, which carries the same label, parent, rank, code, two exact synonyms, three related synonyms, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Geotrichum`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:35568`, which records two retained direct organisms for `NCBITaxon:44066`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs also contain exact organisms `Go0384603` and `Go0705240`, with linked projects `Gp0235713` and `Gp0831272`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:44066`. The YAML preserves exact synonyms `Dipodascus fermentans` and `Trichosporon fermentans`, and it preserves all three related synonyms from the NCBI row.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have one exact organism named `Dipodascus fermentans` for strain `CICC1368`, one exact organism for `Geotrichum fermentans NRRL Y-1492`, two linked projects, and one native analysis named `Dipodascus fermentans` whose `AP PROJECT GOLD IDS` include `Gp0235713`.

The NCBI type-material table has 13 exact rows for the target under `Trichosporon fermentans`: `ATCC 10675`, `ATCC 56301`, `ATCC:10675`, `ATCC:56301`, `CBS 439.83`, `CBS:439.83`, `IFO 1199`, `IFO:1199`, `MUCL 28635`, `MUCL:28635`, `NRRL Y-1492`, `NRRL:Y-1492`, and `NRRL:Y:1492`. StrainInfo has seven exact target records and 26 exact deposits. These side rows do not create generated local strain entries by themselves.

The side `data/raw/ncbi_merged_ids.tsv` inventory maps old ID `NCBITaxon:56544` into `NCBITaxon:44066`, but no retained row in `data/raw/ncbitaxon_taxa.tsv` carries that old ID with `retired_into`, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, two exact synonyms, three related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/geotrichum_fermentans.yaml` plus `just validate-strict data/taxa/eukaryota/geotrichum_fermentans.yaml`.

## Additional Notes

No prior exact ignored review report existed for `geotrichum_fermentans` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:44066` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.

The NCBI merged-ID hit for `NCBITaxon:56544` is a side-inventory old ID only. Generated `replaces` values come from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`, not directly from every side row in `data/raw/ncbi_merged_ids.tsv`.
