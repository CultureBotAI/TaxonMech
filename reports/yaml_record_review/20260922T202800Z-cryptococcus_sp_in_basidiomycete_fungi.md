# YAML Record Review: Cryptococcus sp. (in: basidiomycete fungi)

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cryptococcus_sp_in_basidiomycete_fungi.yaml
- Started UTC: 2026-09-22T20:28:00Z
- Finished UTC: 2026-09-22T20:28:00Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2046349` |
| Label | `Cryptococcus sp. (in: basidiomycete fungi)` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2591751` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cryptococcus_sp_in_basidiomycete_fungi.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cryptococcus_neoformans_wm629.yaml data/taxa/eukaryota/cryptococcus_neoformans_ze90_1.yaml data/taxa/eukaryota/cryptococcus_sp_05_00.yaml data/taxa/eukaryota/cryptococcus_sp_in_basidiomycete_fungi.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, no exact native GOLD organism rows, no exact native GOLD project rows, no exact native GOLD analysis rows, no NCBI type-material rows, no exact StrainInfo rows, no final raw strain rows, NCBI merged-ID side rows but no retained retired rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2046349`, `label: Cryptococcus sp. (in: basidiomycete fungi)`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2591751`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:513612`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `unclassified Cryptococcus (in: basidiomycete fungi)`; the bounded scan checked all 13 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:19453`, which records one retained organism for `NCBITaxon:2046349`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2046349`. NCBI supplies exact synonym `Filobasidiella sp.` and related synonyms `Cryptococcus sp. (Cryptococcaceae)` and `Cryptococcus sp. (Tremellomycetidae)` on the same row, matching the YAML `synonyms` block.

The retained GOLD aggregate row supports the `GOLD` source attestation. The bounded scan found no exact current native GOLD organism, project, or analysis rows for `NCBITaxon:2046349` in the local JSONL snapshots.

No exact NCBI type-material, StrainInfo, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, generated NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cryptococcus_sp_in_basidiomycete_fungi.yaml` plus `just validate-strict data/taxa/eukaryota/cryptococcus_sp_in_basidiomycete_fungi.yaml`.

## Additional Notes

The bounded scan found side-inventory old IDs `NCBITaxon:2046348`, `NCBITaxon:2046350`, `NCBITaxon:2530091`, and `NCBITaxon:52038` in `data/raw/ncbi_merged_ids.tsv`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` that would generate `replaces` entries.
