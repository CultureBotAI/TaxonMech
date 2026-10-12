# YAML Record Review: Debaryomyces subglobosus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/debaryomyces_subglobosus.yaml
- Started UTC: 2026-09-22T22:10:25Z
- Finished UTC: 2026-09-22T22:10:25Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:522693` |
| Label | `Debaryomyces subglobosus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:4958` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/debaryomyces_subglobosus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/debaryomyces_robertsiae.yaml data/taxa/eukaryota/debaryomyces_singareniensis.yaml data/taxa/eukaryota/debaryomyces_subglobosus.yaml data/taxa/eukaryota/debaryomyces_udenii.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained direct organisms, two exact native GOLD organisms linked to 13 projects and one analysis, 14 exact NCBI type-material rows, four exact StrainInfo direct records carrying 12 matching deposit designations, no exact BacDive rows, no final raw strain rows, one NCBI merged-ID side row, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:522693`, `label: Debaryomyces subglobosus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:4958`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:119403`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Debaryomyces` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37843`, which records two retained direct organisms for `NCBITaxon:522693`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:522693`. The YAML carries all four exact synonyms and all four related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain two exact organisms: `Go0517010` for `Debaryomyces subglobosus NRRL Y-6666` and `Go0536090` for `Debaryomyces subglobosus dep8`. Native GOLD has `Gp0441047` under the NRRL organism, 12 expression-profiling projects `Gp0484579` through `Gp0484590` under the dep8 organism, and one analysis named `Debaryomyces subglobosus NRRL Y-6666` that links back through `AP PROJECT GOLD IDS`.

The NCBI type-material inventory contributes 14 exact rows under the synonym taxon name `Eutorulopsis subglobosa`, covering variants of `CBS 792`, `IFO 0794`, `JCM 1989`, `NRRL Y-6666`, `NRRL Y-7859`, and `UCD 75-17`.

The exact StrainInfo side inventory has four direct records and 12 matching deposit designations for `NCBITaxon:522693`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `12`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/debaryomyces_subglobosus.yaml` plus `just validate-strict data/taxa/eukaryota/debaryomyces_subglobosus.yaml`.

## Additional Notes

The bounded scan found a side-inventory `data/raw/ncbi_merged_ids.tsv` mapping from `NCBITaxon:571602` into `NCBITaxon:522693`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` would generate a `replaces` entry.
