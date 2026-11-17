# YAML Record Review: Cryptococcus deneoformans B-3501A

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cryptococcus_deneoformans_b_3501a.yaml
- Started UTC: 2026-09-22T16:25:00Z
- Finished UTC: 2026-09-22T16:25:00Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:283643` |
| Label | `Cryptococcus deneoformans B-3501A` |
| Rank | `STRAIN` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:40410` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cryptococcus_deneoformans_b_3501a.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cryptococcus_deneoformans_b_3501a.yaml` | Passed; the strict validator reported 0 total ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained organisms, one exact native GOLD organism row, two exact native GOLD project rows, one exact native GOLD analysis row, no NCBI type-material rows, no exact StrainInfo rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:283643`, `label: Cryptococcus deneoformans B-3501A`, `rank: STRAIN`, `parent_taxon: NCBITaxon:40410`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:57612`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cryptococcus deneoformans` species; the bounded scan checked all 14 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:27457`, which records two retained organisms for `NCBITaxon:283643`; this agrees with `source_attestations[1].assertion_count: 2`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:283643`. NCBI supplies no exact, broad, or related synonyms for this taxon, matching the absence of a YAML `synonyms` block.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot has exact organism `Go0002612`, exact projects `Gp0002612` and `Gp0002613`, and one native analysis row for `Cryptococcus neoformans var. neoformans B-3501A` tied to `Gp0002613`.

No exact NCBI type-material, StrainInfo, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, no generated synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cryptococcus_deneoformans_b_3501a.yaml` plus `just validate-strict data/taxa/eukaryota/cryptococcus_deneoformans_b_3501a.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:283643`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
