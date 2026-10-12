# YAML Record Review: Fusarium redolens

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_redolens.yaml
- Started UTC: 2026-09-23T03:39:06Z
- Finished UTC: 2026-09-23T03:39:06Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:48865` |
| Label | `Fusarium redolens` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2954887` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_redolens.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/fusarium_redolens.yaml data/taxa/eukaryota/fusarium_robinianum.yaml data/taxa/eukaryota/fusarium_sambucinum.yaml data/taxa/eukaryota/fusarium_sarcochroum.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with nine organism assertions, eight current native GOLD organism rows with six linked projects and three native analysis rows, ten exact NCBI type-material rows, 43 exact StrainInfo records carrying 46 exact deposit rows, two NCBI merged-ID side rows but no retained retired old IDs, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:48865`, `label: Fusarium redolens`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2954887`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:6226`, which carries the same label, parent, rank, code, exact synonym, related synonyms, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Fusarium redolens species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37028`, which records nine retained direct organisms for `NCBITaxon:48865`; this agrees with `source_attestations[1].assertion_count: 9` and its organism assertion unit. The current native GOLD catalogs contain eight exact organisms, six linked projects, and three analyses linked to those exact organism projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:48865`. The YAML preserves exact synonym `Fusarium oxysporum var. redolens` and all three related synonyms from the NCBI row.

The retained GOLD aggregate supplies nine organism assertions. The current native GOLD catalogs contain eight exact organisms, with organism strains `MPI-CAGE-AT-0023`, `CORFU0003`, `ATCC 16067`, `CBS 248.61`, `DSM 62390`, `IMB 9525`, `YP04`, and `NRRL 28421`; exact native GOLD joins found six linked projects and three project-linked analyses.

The NCBI type-material table has ten exact culture-from-epitype rows for the target, covering `ATCC 16067`, `ATCC:16067`, `BBA 9526`, `BBA:9526`, `CBS 360.87`, `CBS:360.87`, `NRRL 20426`, `NRRL 25600`, `NRRL:20426`, and `NRRL:25600`. StrainInfo has 43 exact target records and 46 exact deposits. These side rows do not create generated child strains by themselves.

The side `data/raw/ncbi_merged_ids.tsv` inventory maps old IDs `NCBITaxon:1133677` and `NCBITaxon:56678` into `NCBITaxon:48865`, but no retained rows in `data/raw/ncbitaxon_taxa.tsv` carry those old IDs with `retired_into`, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, one exact synonym, three related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_redolens.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_redolens.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_redolens` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv` and can differ from the current native GOLD exact rows. Native GOLD organism, project, and analysis rows are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:48865` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.
