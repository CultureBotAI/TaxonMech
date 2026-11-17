# YAML Record Review: Curvularia homomorpha

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/curvularia_homomorpha.yaml
- Started UTC: 2026-09-22T20:45:39Z
- Finished UTC: 2026-09-22T20:45:39Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1165373` |
| Label | `Curvularia homomorpha` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5502` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/curvularia_homomorpha.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/curvibasidium_cygneicollum.yaml data/taxa/eukaryota/curvularia_eragrostidis.yaml data/taxa/eukaryota/curvularia_geniculata.yaml data/taxa/eukaryota/curvularia_homomorpha.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with four retained organisms, four exact native GOLD organism rows, no exact native GOLD project rows, eight exact NCBI type-material rows, one exact StrainInfo direct side row covering three deposits, no exact BacDive rows, no final raw strain rows, one NCBI merged-ID side row, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1165373`, `label: Curvularia homomorpha`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5502`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:256970`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Curvularia` genus; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:3515`, which records four retained organisms for `NCBITaxon:1165373`; this agrees with `source_attestations[1].assertion_count: 4`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1165373`. NCBI supplies exact synonyms `Bipolaris homomorpha`, `Bipolaris homomorphus`, `Cochliobolus homomorphus`, `Drechslera homomorpha`, `Helminthosporium homomorphum`, and `Helminthosporium homomorphus`, plus three related synonyms; the YAML `synonyms` block matches those generated synonym sets.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot also has exact organisms `Go0627260`, `Go0627261`, `Go0627262`, and `Go0627263`, all still named as `Cochliobolus homomorphus`; it has no exact native project or analysis rows for those organism IDs.

NCBI lists eight exact type-material side rows, including culture-from-isotype rows for `BRIP 59391` and type-material rows for `ATCC 13409`, `CBS 156.60`, and `DSM 1150`. One exact StrainInfo side row is also present for `DSM 1150`, `ATCC 13409`, and `CBS 156.60`; none are joined into the maintained final StrainInfo or raw strain tables for this target.

No exact BacDive, native GOLD project, native GOLD analysis, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, generated NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/curvularia_homomorpha.yaml` plus `just validate-strict data/taxa/eukaryota/curvularia_homomorpha.yaml`.

## Additional Notes

The bounded scan found one side-inventory old ID in `data/raw/ncbi_merged_ids.tsv:98584`: `NCBITaxon:90977` now maps to `NCBITaxon:1165373`. There are no retained retired rows for that old ID, so the generated YAML correctly has no `replaces` entries.
