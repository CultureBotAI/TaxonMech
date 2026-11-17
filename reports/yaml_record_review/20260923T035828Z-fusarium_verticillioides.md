# YAML Record Review: Fusarium verticillioides

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_verticillioides.yaml
- Started UTC: 2026-09-23T03:58:28Z
- Finished UTC: 2026-09-23T03:58:28Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:117187` |
| Label | `Fusarium verticillioides` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:171627` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_verticillioides.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/fusarium_verticillioides.yaml data/taxa/eukaryota/fusarium_virguliforme.yaml data/taxa/eukaryota/fusarium_xylarioides.yaml data/taxa/eukaryota/fusarium_zealandicum.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with eight organism assertions, 10 exact current native GOLD organisms with 22 linked native GOLD projects and four linked native analysis rows, no exact NCBI type-material rows, 949 exact StrainInfo records carrying 1006 exact deposit rows, three NCBI merged-ID side rows but no retained retired old IDs, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:117187`, `label: Fusarium verticillioides`, `rank: SPECIES`, `parent_taxon: NCBITaxon:171627`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:21682`, which carries the same label, parent, rank, code, three exact synonyms, three related synonyms, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Fusarium fujikuroi species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:3697`, which records eight retained direct organisms for `NCBITaxon:117187`; this agrees with `source_attestations[1].assertion_count: 8` and its organism assertion unit. A complete current native GOLD sweep found 10 exact organisms and 22 linked projects for the same NCBI taxon ID.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:117187`. The YAML preserves the three exact synonyms and three related synonyms from the NCBI row.

The retained GOLD aggregate supplies eight organism assertions. The current native GOLD catalogs have 10 exact organisms filed directly under `NCBITaxon:117187`, including `Fusarium verticillioides M-3125`, `Fusarium verticillioides ITEM 10027`, `Fusarium verticillioides BRIP53590`, and other exact rows; the complete exact sweep found 22 linked projects and four native GOLD analysis rows.

The NCBI type-material table has no exact rows for the target. StrainInfo has 949 exact target records and 1006 exact deposits. These side rows do not create generated local strain entries by themselves.

The side `data/raw/ncbi_merged_ids.tsv` inventory maps old IDs `NCBITaxon:1335946`, `NCBITaxon:2773093`, and `NCBITaxon:42664` into `NCBITaxon:117187`, but no retained row in `data/raw/ncbitaxon_taxa.tsv` carries those old IDs with `retired_into`, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, three exact synonyms, three related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_verticillioides.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_verticillioides.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_verticillioides` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:117187` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.
