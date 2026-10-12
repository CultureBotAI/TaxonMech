# YAML Record Review: Entomortierella parvispora

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/entomortierella_parvispora.yaml
- Started UTC: 2026-09-23T00:24:47Z
- Finished UTC: 2026-09-23T00:24:47Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:205924` |
| Label | `Entomortierella parvispora` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2779859` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/entomortierella_parvispora.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/entomortierella_echinosphaera.yaml data/taxa/eukaryota/entomortierella_lignicola.yaml data/taxa/eukaryota/entomortierella_parvispora.yaml data/taxa/eukaryota/entomortierella_sp.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with 12 organism assertions, nine exact native GOLD organism/project rows, one linked native GOLD analysis row, two NCBI type-material rows, 16 exact StrainInfo rows with 21 deposits, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:205924`, `label: Entomortierella parvispora`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2779859`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:40610`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Entomortierella` genus; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:19681`, which records 12 retained direct organisms for `NCBITaxon:205924`; this agrees with `source_attestations[1].assertion_count: 12` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:205924`. The YAML preserves NCBI's exact synonym `Mortierella parvispora`, plus both related synonyms filed for this row; NCBI supplies no broad synonyms or old-ID side rows.

The two NCBI type-material rows preserve culture-from-syntype aliases for `CBS 311.52` under `Mortierella parvispora`. The retained GOLD aggregate row carries 12 organism assertions; the current exact native GOLD catalogs contain nine organism rows and nine matching project rows, and the `Entomortierella parvispora E1425` analysis links through current project `Gp0645978`.

StrainInfo contains 16 exact target rows with 21 deposit designations for `Entomortierella parvispora`; those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/entomortierella_parvispora.yaml` plus `just validate-strict data/taxa/eukaryota/entomortierella_parvispora.yaml`.

## Additional Notes

The native GOLD sample was expanded by exact ID to account for all 9 current native organism rows and all 9 current native project rows. The retained GOLD aggregate count is higher than the current native exact row count, but `source_attestations[1].assertion_count: 12` matches the retained aggregate row used by the generator.
