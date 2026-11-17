# YAML Record Review: Cunninghamella homothallica

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cunninghamella_homothallica.yaml
- Started UTC: 2026-09-22T20:43:21Z
- Finished UTC: 2026-09-22T20:43:21Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:155729` |
| Label | `Cunninghamella homothallica` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:4852` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cunninghamella_homothallica.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cunninghamella_elegans.yaml data/taxa/eukaryota/cunninghamella_homothallica.yaml data/taxa/eukaryota/cunninghamella_japonica.yaml data/taxa/eukaryota/cunninghamella_polymorpha.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with nine retained organisms, nine exact native GOLD organism rows, no exact native GOLD project rows, no exact native GOLD analysis rows, 17 exact NCBI type-material rows, three exact StrainInfo direct side rows covering 15 deposits, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:155729`, `label: Cunninghamella homothallica`, `rank: SPECIES`, `parent_taxon: NCBITaxon:4852`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:32256`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cunninghamella` genus; the bounded scan checked all 12 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:12456`, which records nine retained organisms for `NCBITaxon:155729`; this agrees with `source_attestations[1].assertion_count: 9`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:155729`. NCBI supplies related synonym `Cunninghamella homothallica Komin. & Tubaki, 1952`, matching the YAML `synonyms` block.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot also has nine exact organism rows for strains `VKM F-930`, `NRRL 2365`, `NI 1151`, `NBRC 6736`, `KN-138`, `IFO 6736`, `DSM 1156`, `CBS 168.53`, and `ATCC 16161`; it has no exact native project or analysis rows for those organism IDs.

NCBI lists 17 exact type-material side rows, with plain and colonized designations for `ATCC 16161`, `CBS 168.53`, `DSM 1156`, `IFO 6736`, `LCP 55.611`, `NI 1151`, `NRRL 2365`, and `VKM F-930`. Exact StrainInfo side rows are also present, covering 15 deposits across three direct StrainInfo records; none are joined into the maintained final StrainInfo or raw strain tables for this target.

No exact BacDive, native GOLD project, native GOLD analysis, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cunninghamella_homothallica.yaml` plus `just validate-strict data/taxa/eukaryota/cunninghamella_homothallica.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:155729`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
