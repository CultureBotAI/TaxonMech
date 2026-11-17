# YAML Record Review: Colletotrichum somersetense

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colletotrichum_somersetense.yaml
- Started UTC: 2026-09-22T13:39:21Z
- Finished UTC: 2026-09-22T13:44:36Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1500509` |
| Label | `Colletotrichum somersetense` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2707348` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colletotrichum_somersetense.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/colletotrichum_somersetense.yaml` | Passed; the strict validator exited successfully for this file in a four-file run. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained organisms, one exact native GOLD organism with two projects, seven NCBI type-material rows, no NCBI merged-ID side rows, no exact StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1500509`, `label: Colletotrichum somersetense`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2707348`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:385241`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colletotrichum graminicola species complex`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:11714`, which records two retained organisms for `NCBITaxon:1500509`; this agrees with `source_attestations[1].assertion_count: 2`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1500509` with one name assertion. NCBI supplies the single exact synonym present in the YAML and no related synonyms.

The native GOLD snapshot has one exact organism row for this NCBI taxon, `Go0102818` / `Colletotrichum somersetensis CBS131599`, with projects `Gp0102818` and `Gp0102819`; the generated YAML correctly follows the maintained retained aggregate in `data/raw/gold_organisms.tsv`, which has one additional retained GOLD organism beyond the native exact rows currently visible in the JSONL mirror.

The NCBI type-material side inventory has seven exact `Colletotrichum somersetense` rows: culture-from-holotype designations `CBS 131599`, `CBS:131599`, `JAC 11-11`, `JAC1111`, and `JAC:11-11`, plus holotype designations `BPI 892770` and `BPI:892770`. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated synonym from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:1500509` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colletotrichum_somersetense.yaml` plus `just validate-strict data/taxa/eukaryota/colletotrichum_somersetense.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:1500509`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
