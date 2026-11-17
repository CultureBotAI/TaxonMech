# YAML Record Review: Cryptococcus deneoformans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cryptococcus_deneoformans.yaml
- Started UTC: 2026-09-22T16:20:27Z
- Finished UTC: 2026-09-22T16:20:27Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:40410` |
| Label | `Cryptococcus deneoformans` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1897064` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cryptococcus_deneoformans.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cryptococcus_deneoformans.yaml` | Passed; the strict validator exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with three retained organisms, no exact native GOLD organism/project/analysis rows, ten exact NCBI type-material side rows, 79 exact StrainInfo direct side rows and 110 exact StrainInfo deposit side rows without joined final StrainInfo rows, no final raw strain rows, five NCBI merged-ID side rows, no retained retired rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:40410`, `label: Cryptococcus deneoformans`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1897064`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:4592`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Cryptococcus neoformans species complex`; the bounded scan checked all 13 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:34528`, which records three retained organisms for `NCBITaxon:40410`; this agrees with `source_attestations[1].assertion_count: 3` and with the direct-filing note in the YAML.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:40410`. NCBI supplies exact synonyms `Cryptococcus neoformans var. neoformans` and `Filobasidiella neoformans var. neoformans`, plus six related synonyms for `Cryptococcus deneoformans` and the older `neoformans var. neoformans` names; these match the YAML synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The bounded scan did not find any exact native GOLD organism, project, or analysis rows for this taxon in the local `data/gold/*.jsonl.gz` snapshot.

The NCBI type-material side inventory has ten exact rows for this taxon: eight B-3501, CBS, and DBVPG culture-from-holotype spellings and two `CBS H-21965` holotype spellings. The StrainInfo side inventory has 79 exact direct rows and 110 exact deposit rows, but none joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; no maintained final strain-table rows are present, so `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cryptococcus_deneoformans.yaml` plus `just validate-strict data/taxa/eukaryota/cryptococcus_deneoformans.yaml`.

## Additional Notes

The bounded scan found five rows in `data/raw/ncbi_merged_ids.tsv` that map old `NCBITaxon:1296041`, `NCBITaxon:1296042`, `NCBITaxon:1296043`, `NCBITaxon:135857`, and `NCBITaxon:1859123` into `NCBITaxon:40410`; those old IDs are only present in the side inventory, and there are no retained retired rows that would generate `replaces` entries.

The retained GOLD aggregate row has three organisms for this species, while the bounded scan found no exact native GOLD JSONL rows under `NCBITaxon:40410`; the generated record follows the retained aggregate TSV for its source attestation count.
