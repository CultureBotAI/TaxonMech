# YAML Record Review: Curvularia eragrostidis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/curvularia_eragrostidis.yaml
- Started UTC: 2026-09-22T20:45:39Z
- Finished UTC: 2026-09-22T20:45:39Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:418125` |
| Label | `Curvularia eragrostidis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5502` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/curvularia_eragrostidis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/curvibasidium_cygneicollum.yaml data/taxa/eukaryota/curvularia_eragrostidis.yaml data/taxa/eukaryota/curvularia_geniculata.yaml data/taxa/eukaryota/curvularia_homomorpha.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with three retained organisms, one exact native GOLD organism row, one exact native GOLD project row, no exact native GOLD analysis rows, 39 exact StrainInfo direct side rows covering 46 deposits, no NCBI type-material rows, no exact BacDive rows, no final raw strain rows, one NCBI merged-ID side row, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:418125`, `label: Curvularia eragrostidis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5502`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:91522`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Curvularia` genus; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:34960`, which records three retained organisms for `NCBITaxon:418125`; this agrees with `source_attestations[1].assertion_count: 3`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:418125`. NCBI supplies exact synonyms `Brachysporium eragrostidis`, `Cochliobolus eragrostidis`, and `Pseudocochliobolus eragrostidis`, plus five related synonyms; the YAML `synonyms` block matches those generated synonym sets.

The retained GOLD aggregate row supports the `GOLD` source attestation. The current local native GOLD JSONL snapshot has one exact organism row, `Go0667412`, and one exact project row, `Gp0744493`, for `Curvularia eragrostidis C52`; the generated YAML follows the retained aggregate row from `data/raw/gold_organisms.tsv`.

Exact StrainInfo side rows are present, covering 46 deposits across 39 direct StrainInfo records; none are joined into the maintained final StrainInfo or raw strain tables for this target.

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

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/curvularia_eragrostidis.yaml` plus `just validate-strict data/taxa/eukaryota/curvularia_eragrostidis.yaml`.

## Additional Notes

The bounded scan found one side-inventory old ID in `data/raw/ncbi_merged_ids.tsv:11874`: `NCBITaxon:131382` now maps to `NCBITaxon:418125`. There are no retained retired rows for that old ID, so the generated YAML correctly has no `replaces` entries.
