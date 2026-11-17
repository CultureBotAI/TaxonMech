# YAML Record Review: Curvularia inaequalis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/curvularia_inaequalis.yaml
- Started UTC: 2026-09-22T20:48:14Z
- Finished UTC: 2026-09-22T20:48:14Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:38902` |
| Label | `Curvularia inaequalis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5502` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/curvularia_inaequalis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/curvularia_inaequalis.yaml data/taxa/eukaryota/curvularia_kusanoi.yaml data/taxa/eukaryota/curvularia_papendorfii.yaml data/taxa/eukaryota/cutaneotrichosporon_arboriforme.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism row, two exact native GOLD project rows, no exact native GOLD analysis rows, 28 exact StrainInfo direct side rows covering 46 deposits, no NCBI type-material rows, no exact BacDive rows, no final raw strain rows, one NCBI merged-ID side row, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:38902`, `label: Curvularia inaequalis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5502`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:4423`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Curvularia` genus; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:34066`, which records one retained organism for `NCBITaxon:38902`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:38902`. NCBI supplies exact synonym `Helminthosporium inaequale` and related synonyms `Curvularia inaequalis (Shear) Boedijn 1907` and `Helminthosporium inaequale Shear, 1907`, matching the YAML `synonyms` block.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot also has exact organism `Go0529083` with exact projects `Gp0457391` and `Gp0533779` for `Curvularia inaequalis DSE1156`.

Exact StrainInfo side rows are present, covering 46 deposits across 28 direct StrainInfo records; none are joined into the maintained final StrainInfo or raw strain tables for this target.

No exact NCBI type-material, BacDive, native GOLD analysis, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, generated NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/curvularia_inaequalis.yaml` plus `just validate-strict data/taxa/eukaryota/curvularia_inaequalis.yaml`.

## Additional Notes

The bounded scan found one side-inventory old ID in `data/raw/ncbi_merged_ids.tsv:37225`: `NCBITaxon:2082011` now maps to `NCBITaxon:38902`. There are no retained retired rows for that old ID, so the generated YAML correctly has no `replaces` entries.
