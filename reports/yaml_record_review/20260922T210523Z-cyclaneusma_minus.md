# YAML Record Review: Cyclaneusma minus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cyclaneusma_minus.yaml
- Started UTC: 2026-09-22T21:05:23Z
- Finished UTC: 2026-09-22T21:05:23Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:64355` |
| Label | `Cyclaneusma minus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1758688` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cyclaneusma_minus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cyathus_stercoreus.yaml data/taxa/eukaryota/cyathus_striatus.yaml data/taxa/eukaryota/cyclaneusma_minus.yaml data/taxa/eukaryota/cyclocybe_cylindracea.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with four retained organisms, four exact native GOLD organism rows, three exact NCBI type-material rows, nine exact StrainInfo records not retained in the final StrainInfo overlay, no exact native GOLD project or analysis rows, no exact BacDive rows, no final raw strain rows, three NCBI merged-ID side rows not retained into generated `replaces`, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:64355`, `label: Cyclaneusma minus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1758688`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:8150`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cyclaneusma` genus; the bounded scan checked all 15 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:40247`, which records four retained organisms for `NCBITaxon:64355`; this agrees with `source_attestations[1].assertion_count: 4`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:64355`. The YAML carries NCBI's three exact synonyms, `Cyclaneusma minus simile`, `Cyclaneusma minus verum`, and `Naemacyclus minor`, plus the four NCBI related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot also has four exact organism rows for `NCBITaxon:64355`; those rows still use the `Naemacyclus minor` synonym in organism names for strains `N 209`, `DSM 5046`, `CBS 496.73`, and `392`. No exact native GOLD projects or analysis rows were linked to these organisms.

The NCBI type-material inventory contributes three exact `type material` rows for `CBS 496.73`, `CBS:496.73`, and `ICMP:20937`, all under the synonym taxon name `Naemacyclus minor`. Exact StrainInfo records are keyed to `NCBITaxon:64355`, but none are retained into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`, and no `STRAININFO` source attestation is generated.

No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cyclaneusma_minus.yaml` plus `just validate-strict data/taxa/eukaryota/cyclaneusma_minus.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` maps old IDs `NCBITaxon:1488139`, `NCBITaxon:1488140`, and `NCBITaxon:1524415` into `NCBITaxon:64355`, but the old IDs are not retained as retired source rows that would generate `replaces` entries.
