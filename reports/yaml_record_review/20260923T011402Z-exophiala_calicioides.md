# YAML Record Review: Exophiala calicioides

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/exophiala_calicioides.yaml
- Started UTC: 2026-09-23T01:14:02Z
- Finished UTC: 2026-09-23T01:14:02Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:135514` |
| Label | `Exophiala calicioides` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5583` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/exophiala_calicioides.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/exophiala_alcalophila.yaml data/taxa/eukaryota/exophiala_calicioides.yaml data/taxa/eukaryota/exophiala_crusticola.yaml data/taxa/eukaryota/exophiala_dermatitidis.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one native GOLD organism/project/analysis chain, two NCBI merged-ID side rows, 16 exact StrainInfo rows with 19 deposits, no NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:135514`, `label: Exophiala calicioides`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5583`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:27039`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Exophiala` genus; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:8625`, which records one retained direct organism for `NCBITaxon:135514`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:135514`. The YAML preserves NCBI's exact synonyms `Caliciopsis calicioides`, `Graphium calicioides`, `Hypothele calicioides`, and `Sporocybe calicioides` plus three related synonyms.

`data/raw/ncbi_merged_ids.tsv:10003` and `data/raw/ncbi_merged_ids.tsv:91659` map the old side-inventory IDs `NCBITaxon:1260756` and `NCBITaxon:67621` to `NCBITaxon:135514`; neither is retained as a row with `retired_into` in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies one organism assertion, and the current native GOLD catalogs still contain one exact organism, project, and analysis chain for the target NCBI taxon.

StrainInfo contains 16 exact target rows with 19 deposit designations for `Exophiala calicioides`; those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive, NCBI type-material, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, four NCBI exact synonyms, three NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/exophiala_calicioides.yaml` plus `just validate-strict data/taxa/eukaryota/exophiala_calicioides.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID but are side evidence only and do not create a generated child strain without a BacDive-derived local strain inventory entry. The NCBI merged-ID rows are side evidence only; generated `replaces` comes from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`.
