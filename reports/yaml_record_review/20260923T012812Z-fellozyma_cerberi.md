# YAML Record Review: Fellozyma cerberi

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fellozyma_cerberi.yaml
- Started UTC: 2026-09-23T01:28:12Z
- Finished UTC: 2026-09-23T01:28:12Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2878325` |
| Label | `Fellozyma cerberi` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1801533` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fellozyma_cerberi.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/favolaschia_calocera.yaml data/taxa/eukaryota/fellomyces_borneensis.yaml data/taxa/eukaryota/fellomyces_polyborus.yaml data/taxa/eukaryota/fellozyma_cerberi.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with five organism assertions, five current native GOLD organism rows, one exact StrainInfo row with one deposit, two NCBI type-material rows, one NCBI merged-ID side row, no current exact native GOLD project/analysis rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2878325`, `label: Fellozyma cerberi`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1801533`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:566956`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fellozyma` genus; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:27991`, which records five retained direct organisms for `NCBITaxon:2878325`; this agrees with `source_attestations[1].assertion_count: 5` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2878325`. The YAML preserves NCBI's exact synonym `Hamamotoa cerberi` plus three related synonyms.

`data/raw/ncbi_merged_ids.tsv:90766` maps the old side-inventory ID `NCBITaxon:657501` to `NCBITaxon:2878325`; it is not retained as a row with `retired_into` in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies five organism assertions; the current native GOLD `organisms` catalog still contains five exact organism rows for the target NCBI taxon, while the current native `projects` and `analyses` catalogs have no exact linked rows.

NCBI type-material rows 135050-135051 list two holotype designations for `Hamamotoa cerberi`, and StrainInfo contains one exact target row with one deposit designation. Those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, three NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fellozyma_cerberi.yaml` plus `just validate-strict data/taxa/eukaryota/fellozyma_cerberi.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD exact rows are side evidence only and can differ from the retained aggregate used to generate source attestations. The NCBI merged-ID side row is side evidence only; generated `replaces` comes from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`.
