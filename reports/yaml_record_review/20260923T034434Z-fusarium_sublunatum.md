# YAML Record Review: Fusarium sublunatum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_sublunatum.yaml
- Started UTC: 2026-09-23T03:44:34Z
- Finished UTC: 2026-09-23T03:44:34Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:86547` |
| Label | `Fusarium sublunatum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2305846` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_sublunatum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_sporotrichioides.yaml data/taxa/eukaryota/fusarium_stilboides.yaml data/taxa/eukaryota/fusarium_subglutinans.yaml data/taxa/eukaryota/fusarium_sublunatum.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with four organism assertions, four current native GOLD organism rows with two linked projects and no native analysis rows, 11 exact NCBI type-material rows, two exact StrainInfo records carrying six exact deposit rows, one NCBI merged-ID side row but no retained retired old IDs, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:86547`, `label: Fusarium sublunatum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2305846`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:13412`, which carries the same label, parent, rank, code, exact synonym, related synonym, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Fusarium buharicum species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:43474`, which records four retained direct organisms for `NCBITaxon:86547`; this agrees with `source_attestations[1].assertion_count: 4` and its organism assertion unit. The current native GOLD catalogs also contain four exact organisms and two linked projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:86547`. The YAML preserves exact synonym `Fusarium sublunatum var. sublunatum` and the related synonym from the NCBI row.

The retained GOLD aggregate supplies four organism assertions. The current native GOLD catalogs contain the same exact organism count and include strains `CBS 189.34`, `DSM 62431`, `IMB 5238`, and `NRRL 13384`; only `NRRL 13384` currently has linked native GOLD projects, one standard-draft and one transcriptome, and no native GOLD analysis currently links to those projects.

The NCBI type-material table has 11 exact rows for the target, covering `BBA 62431`, `BBA:62431`, `CBS 189.34`, `CBS 189.34; BBA 62431`, `CBS:189.34`, `DSM 62431`, `DSM:62431`, `NRRL 13384`, `NRRL 20840`, `NRRL:13384`, and `NRRL:20840`. StrainInfo has two exact target records and six exact deposits. These side rows do not create generated child strains by themselves.

The side `data/raw/ncbi_merged_ids.tsv` inventory maps old ID `NCBITaxon:86548` into `NCBITaxon:86547`, but no retained row in `data/raw/ncbitaxon_taxa.tsv` carries that old ID with `retired_into`, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, one exact synonym, one related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_sublunatum.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_sublunatum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_sublunatum` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:86547` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.
