# YAML Record Review: Cortinarius pilatii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cortinarius_pilatii.yaml
- Started UTC: 2026-09-22T15:22:52Z
- Finished UTC: 2026-09-22T15:22:52Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2764429` |
| Label | `Cortinarius pilatii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:34451` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cortinarius_pilatii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cortinarius_gentilis.yaml data/taxa/eukaryota/cortinarius_persplendidus.yaml data/taxa/eukaryota/cortinarius_pilatii.yaml data/taxa/eukaryota/cortinarius_purpureus.yaml` | Passed; the strict validator scanned four files with zero errors, including this record. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, no exact native GOLD organism rows, one NCBI type-material row, no NCBI merged-ID side rows, no exact StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2764429`, `label: Cortinarius pilatii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:34451`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:552172`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cortinarius` genus; the bounded scan checked all 14 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:26223`, which records one retained organism for `NCBITaxon:2764429`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2764429`. NCBI supplies the related synonym `Cortinarius pilatii Svrcek, 1968`, matching the YAML synonym.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot does not contain exact organism, project, or analysis rows filed under NCBI taxon `2764429`, so there are no native project or analysis details to reconcile for this generated record.

NCBI has one exact type-material side row for this taxon, `data/raw/ncbi_type_material.tsv:119801`, which records holotype `PRM:655887`. No exact StrainInfo rows or maintained final strain-table rows are present, so `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cortinarius_pilatii.yaml` plus `just validate-strict data/taxa/eukaryota/cortinarius_pilatii.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:2764429`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
