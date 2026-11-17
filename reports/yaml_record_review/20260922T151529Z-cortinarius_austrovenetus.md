# YAML Record Review: Cortinarius austrovenetus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cortinarius_austrovenetus.yaml
- Started UTC: 2026-09-22T15:15:34Z
- Finished UTC: 2026-09-22T15:15:34Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:742016` |
| Label | `Cortinarius austrovenetus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:34451` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cortinarius_austrovenetus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cortinarius_austrovenetus.yaml` | Passed; the strict validator exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained organisms, two exact native GOLD organisms with ten projects and one linked analysis, no NCBI type-material rows, one NCBI merged-ID side row, no exact StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:742016`, `label: Cortinarius austrovenetus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:34451`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:170921`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cortinarius` genus; the bounded scan checked all 14 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:42099`, which records two retained organisms for `NCBITaxon:742016`; this agrees with `source_attestations[1].assertion_count: 2`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:742016`. NCBI supplies the exact synonym `Dermocybe austroveneta` and the related synonym present in the YAML.

A complete exact native GOLD scan for this taxon found two organism IDs, `Go0389706` / `Cortinarius austrovenetus KIS7` and `Go0452927` / `Cortinarius austrovenetus TL2843-KIS7R`, and ten projects linked to those organisms. One exact analysis row links through the project `Gp0317549`; this supports the retained aggregate organism count.

The bounded scan found no exact StrainInfo rows for this NCBI taxon, so there are no StrainInfo side deposits to join into the maintained final strain tables.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated NCBI synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no NCBI type-material rows for `NCBITaxon:742016`; no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cortinarius_austrovenetus.yaml` plus `just validate-strict data/taxa/eukaryota/cortinarius_austrovenetus.yaml`.

## Additional Notes

The bounded scan found one side row in `data/raw/ncbi_merged_ids.tsv` mapping old ID `NCBITaxon:112257` into `NCBITaxon:742016`, but there are no side-inventory old IDs and no retained retired rows that would generate a `replaces` entry.
