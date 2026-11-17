# YAML Record Review: Cryphonectria parasitica

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cryphonectria_parasitica.yaml
- Started UTC: 2026-09-22T16:07:59Z
- Finished UTC: 2026-09-22T16:07:59Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5116` |
| Label | `Cryphonectria parasitica` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5115` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cryphonectria_parasitica.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cryphonectria_parasitica.yaml` | Passed; the strict validator reported 0 total ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with 93 retained organisms, 93 exact native GOLD organism rows, 93 exact native GOLD project rows, 92 exact native GOLD analysis rows, no NCBI type-material rows, 235 exact StrainInfo direct side rows, 240 exact StrainInfo deposit side rows, two joined StrainInfo related-record side rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5116`, `label: Cryphonectria parasitica`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5115`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2242`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cryphonectria` genus; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37511`, which records 93 retained organisms for `NCBITaxon:5116`; this agrees with `source_attestations[1].assertion_count: 93`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5116`. NCBI supplies the exact synonyms `Diaporthe parasitica` and `Endothia parasitica` and the related synonyms `Cryphonectria parasitica (Murrill) M.E. Barr, 1978`, `Diaporthe parasitica Murrill, 1906`, `Endothia parasitica (Murrill) P.J. Anderson & H.W. Anderson, 1912`, and `chestnut blight fungus`, matching the YAML synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. A full exact native GOLD join found 93 exact organisms, 93 exact projects, and 92 native analysis rows tied to those projects through `AP PROJECT GOLD IDS`, matching the bounded scan counts.

The StrainInfo side inventory has 235 exact direct rows and 240 exact deposit rows for `NCBITaxon:5116`; two joined related-record rows for `KCTC 6466` are present in `data/straininfo/related_records.tsv.gz`, but no exact rows are present in `data/straininfo/assemblies.tsv` or `data/straininfo/exclusions.tsv`. No exact NCBI type-material or maintained final strain-table rows are present, so `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv` or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cryphonectria_parasitica.yaml` plus `just validate-strict data/taxa/eukaryota/cryphonectria_parasitica.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:5116`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
