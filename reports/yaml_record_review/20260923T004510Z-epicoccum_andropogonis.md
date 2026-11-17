# YAML Record Review: Epicoccum andropogonis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/epicoccum_andropogonis.yaml
- Started UTC: 2026-09-23T00:45:10Z
- Finished UTC: 2026-09-23T00:45:10Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:124084` |
| Label | `Epicoccum andropogonis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:104397` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/epicoccum_andropogonis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/epichloe_typhina_subsp_clarkii.yaml data/taxa/eukaryota/epichloe_typhina_subsp_typhina.yaml data/taxa/eukaryota/epichloe_uncinata.yaml data/taxa/eukaryota/epicoccum_andropogonis.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, one NCBI merged-ID side row, 11 exact StrainInfo rows with 12 deposits, no current exact native GOLD organism rows, no NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:124084`, `label: Epicoccum andropogonis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:104397`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:23621`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Epicoccum` genus; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:5755`, which records two retained direct organisms for `NCBITaxon:124084`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:124084`. The YAML preserves NCBI's exact synonym `Cerebella andropogonis` plus the related synonyms `Cerebella andropogonis Ces., 1851` and `Epicoccum andropogonis (Ces.) Schol-Schwarz, 1959`.

`data/raw/ncbi_merged_ids.tsv:9420` maps the old side-inventory ID `NCBITaxon:124083` to `NCBITaxon:124084`; it is not retained as a row with `retired_into` in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies two organism assertions; the current native GOLD `organisms`, `projects`, and `analyses` catalogs have no exact rows for `NCBITaxon:124084`.

StrainInfo contains 11 exact target rows with 12 deposit designations for `Epicoccum andropogonis`; those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive, NCBI type-material, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/epicoccum_andropogonis.yaml` plus `just validate-strict data/taxa/eukaryota/epicoccum_andropogonis.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD JSONL inputs no longer contain exact organism/project/analysis rows for this taxon. The NCBI merged-ID side row is side evidence only; generated `replaces` comes from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`.
