# YAML Record Review: Exophiala dermatitidis NIH/UT8656

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/exophiala_dermatitidis_nih_ut8656.yaml
- Started UTC: 2026-09-23T01:16:43Z
- Finished UTC: 2026-09-23T01:16:43Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:858893` |
| Label | `Exophiala dermatitidis NIH/UT8656` |
| Rank | `STRAIN` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5970` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/exophiala_dermatitidis_nih_ut8656.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/exophiala_dermatitidis_nih_ut8656.yaml data/taxa/eukaryota/exophiala_lecanii_corni.yaml data/taxa/eukaryota/exophiala_mesophila.yaml data/taxa/eukaryota/exophiala_oligosperma.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with five organism assertions, three current native GOLD organisms with three linked projects and one linked analysis, one NCBI merged-ID side row, no exact StrainInfo rows, no NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:858893`, `label: Exophiala dermatitidis NIH/UT8656`, `rank: STRAIN`, `parent_taxon: NCBITaxon:5970`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:180607`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the parent `Exophiala dermatitidis` species; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:43309`, which records five retained direct organisms for `NCBITaxon:858893`; this agrees with `source_attestations[1].assertion_count: 5` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:858893`. The YAML preserves NCBI's two exact synonyms: `Exophiala dermatitidis NIH 8656` and `Wangiella dermatitidis NIH 8656`.

`data/raw/ncbi_merged_ids.tsv:37` maps the old side-inventory ID `NCBITaxon:1001381` to `NCBITaxon:858893`; it is not retained as a row with `retired_into` in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies five organism assertions; the current native GOLD catalogs contain three exact organism rows, three linked project rows, and one linked analysis row for the target NCBI taxon.

No exact StrainInfo, BacDive, NCBI type-material, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded NCBI strain identity, NCBI and GOLD source attestations, two NCBI exact synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/exophiala_dermatitidis_nih_ut8656.yaml` plus `just validate-strict data/taxa/eukaryota/exophiala_dermatitidis_nih_ut8656.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD exact row count is lower than the retained aggregate count but remains side evidence only. The NCBI merged-ID side row is side evidence only; generated `replaces` comes from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`.
