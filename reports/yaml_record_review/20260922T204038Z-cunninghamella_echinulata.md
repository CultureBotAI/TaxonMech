# YAML Record Review: Cunninghamella echinulata

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cunninghamella_echinulata.yaml
- Started UTC: 2026-09-22T20:40:38Z
- Finished UTC: 2026-09-22T20:40:38Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:76405` |
| Label | `Cunninghamella echinulata` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:4852` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cunninghamella_echinulata.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cunninghamella_bertholletiae.yaml data/taxa/eukaryota/cunninghamella_blakesleeana.yaml data/taxa/eukaryota/cunninghamella_brunnea.yaml data/taxa/eukaryota/cunninghamella_echinulata.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with nine retained organisms, nine exact native GOLD organism rows, 10 exact native GOLD project rows, no exact native GOLD analysis rows, 83 exact StrainInfo direct side rows covering 117 deposits, no NCBI type-material rows, no exact BacDive rows, no final raw strain rows, one NCBI merged-ID side row, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:76405`, `label: Cunninghamella echinulata`, `rank: SPECIES`, `parent_taxon: NCBITaxon:4852`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:10954`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cunninghamella` genus; the bounded scan checked all 12 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:42518`, which records nine retained organisms for `NCBITaxon:76405`; this agrees with `source_attestations[1].assertion_count: 9`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:76405`. NCBI supplies no exact, related, or broad synonyms for this row, and the YAML correctly omits a `synonyms` block.

The retained GOLD aggregate row supports the `GOLD` source attestation. The complete local native GOLD JSONL snapshot has nine exact organism rows for `Go0118596`, `Go0470798`, `Go0470837`, `Go0470905`, `Go0470932`, `Go0470938`, `Go0470996`, `Go0527611`, and `Go0527615`, with 10 exact projects tied to those organism IDs. A complete follow-up scan across the 10 project IDs found no exact native GOLD analysis rows.

Exact StrainInfo side rows are present for this target, covering 117 deposits across 83 direct StrainInfo records; none are joined into the maintained final StrainInfo or raw strain tables for this target.

No exact NCBI type-material, BacDive, native GOLD analysis, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cunninghamella_echinulata.yaml` plus `just validate-strict data/taxa/eukaryota/cunninghamella_echinulata.yaml`.

## Additional Notes

The bounded scan found one side-inventory old ID in `data/raw/ncbi_merged_ids.tsv:24512`: `NCBITaxon:169017` now maps to `NCBITaxon:76405`. There are no retained retired rows for that old ID, so the generated YAML correctly has no `replaces` entries.
