# YAML Record Review: Cryphonectria carpinicola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cryphonectria_carpinicola.yaml
- Started UTC: 2026-09-22T16:07:59Z
- Finished UTC: 2026-09-22T16:07:59Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2725329` |
| Label | `Cryphonectria carpinicola` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5115` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cryphonectria_carpinicola.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cryphonectria_carpinicola.yaml` | Passed; the strict validator reported 0 total ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained organisms, two exact native GOLD organism rows, two exact native GOLD project rows, two exact native GOLD analysis rows, four exact NCBI type-material side rows, no exact StrainInfo rows, no final raw strain rows, two NCBI merged-ID side rows, no retained retired rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2725329`, `label: Cryphonectria carpinicola`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5115`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:547818`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cryphonectria` genus; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:25311`, which records two retained organisms for `NCBITaxon:2725329`; this agrees with `source_attestations[1].assertion_count: 2`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2725329`. NCBI supplies related synonyms `Cryphonectria carpinicola D. Rigling, T. Cech, Cornejo & L. Beenken, 2020`, `Cryphonectria sp. CC-2020a`, `Cryphonectria sp. CS3`, and `Cryphonectria sp. M9290`, matching the YAML synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot also has exact organisms `Go0676160` and `Go0676161`, exact projects `Gp0777908` and `Gp0777909`, and two native analysis rows for `Cryphonectria carpinicola M9290` and `Cryphonectria carpinicola CS3` tied to those projects.

The NCBI type-material side inventory has four exact rows for this taxon: two `ZT Myc 61307` holotype spellings and two `CBS 147194` culture-from-holotype spellings. No exact StrainInfo or maintained final strain-table rows are present, so `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cryphonectria_carpinicola.yaml` plus `just validate-strict data/taxa/eukaryota/cryphonectria_carpinicola.yaml`.

## Additional Notes

The bounded scan found two rows in `data/raw/ncbi_merged_ids.tsv` that map old `NCBITaxon:2771286` and `NCBITaxon:2771287` into `NCBITaxon:2725329`; those old IDs are only present in the side inventory, and there are no retained retired rows that would generate `replaces` entries.
