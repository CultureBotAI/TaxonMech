# YAML Record Review: Exophiala dermatitidis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/exophiala_dermatitidis.yaml
- Started UTC: 2026-09-23T01:14:02Z
- Finished UTC: 2026-09-23T01:14:02Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5970` |
| Label | `Exophiala dermatitidis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5583` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/exophiala_dermatitidis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/exophiala_alcalophila.yaml data/taxa/eukaryota/exophiala_calicioides.yaml data/taxa/eukaryota/exophiala_crusticola.yaml data/taxa/eukaryota/exophiala_dermatitidis.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with 105 direct organism assertions, 105 exact native GOLD organisms with 180 linked projects and two linked analyses, 217 exact StrainInfo rows with 250 deposits, 16 NCBI type-material rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5970`, `label: Exophiala dermatitidis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5583`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2631`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Exophiala` genus; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:39705`, which records 105 retained direct organisms for `NCBITaxon:5970`; this agrees with `source_attestations[1].assertion_count: 105`, its organism assertion unit, and its note that records filed directly under this taxon are counted without gathering descendant taxa.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5970`. The YAML preserves NCBI's exact synonyms `Hormiscium dermatitidis` and `Wangiella dermatitidis` plus two related synonyms.

No NCBI merged-ID rows target `NCBITaxon:5970`, and no retained old IDs in `data/raw/ncbitaxon_taxa.tsv` retire into it, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies 105 organism assertions. Exact scans of the current native GOLD catalogs confirmed all 105 target organism IDs, all 180 linked projects for those organism IDs, and two linked analyses by project ID.

NCBI type-material rows 240521-240536 list 16 type-material or culture-from-type-material designations for `Hormiscium dermatitidis`, and StrainInfo contains 217 exact target rows with 250 deposit designations for `Exophiala dermatitidis`. Those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI exact synonyms, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/exophiala_dermatitidis.yaml` plus `just validate-strict data/taxa/eukaryota/exophiala_dermatitidis.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; exact scans of the current native GOLD `organisms` and `projects` catalogs were needed because this taxon has a large direct fanout. Those rows are still side evidence and do not create generated child strains without BacDive-derived local strain inventory entries.
