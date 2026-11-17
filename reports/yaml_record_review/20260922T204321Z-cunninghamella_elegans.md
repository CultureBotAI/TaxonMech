# YAML Record Review: Cunninghamella elegans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cunninghamella_elegans.yaml
- Started UTC: 2026-09-22T20:43:21Z
- Finished UTC: 2026-09-22T20:43:21Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:4853` |
| Label | `Cunninghamella elegans` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:4852` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cunninghamella_elegans.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cunninghamella_elegans.yaml data/taxa/eukaryota/cunninghamella_homothallica.yaml data/taxa/eukaryota/cunninghamella_japonica.yaml data/taxa/eukaryota/cunninghamella_polymorpha.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with eight retained organisms, seven exact native GOLD organism rows, seven exact native GOLD project rows, no exact native GOLD analysis rows, two exact NCBI type-material rows, 80 exact StrainInfo direct side rows covering 109 deposits, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:4853`, `label: Cunninghamella elegans`, `rank: SPECIES`, `parent_taxon: NCBITaxon:4852`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2099`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cunninghamella` genus; the bounded scan checked all 12 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:36865`, which records eight retained organisms for `NCBITaxon:4853`; this agrees with `source_attestations[1].assertion_count: 8`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:4853`. NCBI supplies related synonym `Cunninghamella elegans Lendn., 1907`, matching the YAML `synonyms` block.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot has seven exact organism rows for `Go0002480`, `Go0470838`, `Go0470839`, `Go0470840`, `Go0470841`, `Go0470842`, and `Go0527590`, with seven exact projects tied to those organism IDs. A complete follow-up scan across the seven project IDs found no exact native GOLD analysis rows. The one-count difference between the retained aggregate and native GOLD snapshots is local to those side inputs; the generated YAML follows the retained aggregate row.

NCBI lists two exact type-material side rows for `CBS 160.28` and `CBS:160.28`. Exact StrainInfo side rows are also present, covering 109 deposits across 80 direct StrainInfo records; none are joined into the maintained final StrainInfo or raw strain tables for this target.

No exact BacDive, native GOLD analysis, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cunninghamella_elegans.yaml` plus `just validate-strict data/taxa/eukaryota/cunninghamella_elegans.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:4853`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
