# YAML Record Review: Colletotrichum sansevieriae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colletotrichum_sansevieriae.yaml
- Started UTC: 2026-09-22T13:36:00Z
- Finished UTC: 2026-09-22T13:39:20Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:328473` |
| Label | `Colletotrichum sansevieriae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2870525` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colletotrichum_sansevieriae.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/colletotrichum_sansevieriae.yaml` | Passed; the strict validator scanned one file with zero errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one native GOLD organism/project/analysis chain, three NCBI type-material rows, no NCBI merged-ID side rows, exact StrainInfo species/deposit rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:328473`, `label: Colletotrichum sansevieriae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2870525`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:67138`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colletotrichum agaves species complex`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:32206`, which records one retained organism for `NCBITaxon:328473`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:328473` with one name assertion. NCBI supplies the one related synonym present in the YAML and no exact synonyms.

The native GOLD snapshot has one exact organism row for this NCBI taxon, `Go0455032` / `Colletotrichum sansevieriae Sa-1-2`, with project `Gp0323358` / `Colletotrichum sansevieriae Sa-1-2` and one linked analysis row.

The NCBI type-material side inventory has three exact `Colletotrichum sansevieriae` rows: `MAFF 239721` and `MAFF:239721` as holotype cultures and `Sa-1-2` as type material. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

StrainInfo has exact species-level side inventory rows, including two exact deposit matches and two direct species matches. Because no generated rows exist for `NCBITaxon:328473` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:328473` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colletotrichum_sansevieriae.yaml` plus `just validate-strict data/taxa/eukaryota/colletotrichum_sansevieriae.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:328473`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
