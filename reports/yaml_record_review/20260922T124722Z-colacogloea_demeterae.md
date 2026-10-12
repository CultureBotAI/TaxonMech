# YAML Record Review: Colacogloea demeterae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colacogloea_demeterae.yaml
- Started UTC: 2026-09-22T12:43:20Z
- Finished UTC: 2026-09-22T12:47:22Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2878297` |
| Label | `Colacogloea demeterae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:34419` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colacogloea_demeterae.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/colacogloea_demeterae.yaml` | Passed; the strict validator reported 0 errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with six retained organisms, six current native GOLD organism rows, two NCBI type-material rows, one NCBI merged-ID side row, exact StrainInfo species/deposit rows, no native GOLD projects or analyses, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2878297`, `label: Colacogloea demeterae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:34419`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:566953`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colacogloea`; the bounded scan checked all 12 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:27988`, which records six retained organisms for `NCBITaxon:2878297`; this agrees with `source_attestations[1].assertion_count: 6`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2878297` with one name assertion. NCBI supplies all three related synonyms present in the YAML, `Colacogloea demeterae A.M. Yurkov, A.M. Schafer & D. Begerow, 2016`, `Colacogloea sp. AY165`, and `Rhodotorula sp. AY165`; the curation-history source list agrees with the two retained source attestations.

The native GOLD snapshot has six exact organism rows for this NCBI taxon: `PYCC 6223`, `MUCL 54081`, `DSM 26786`, `CBS 12500`, `AY569`, and `AY165`. No native GOLD projects or analyses are currently linked to those organisms.

The NCBI type-material side inventory has two exact holotype rows for this species, `DSM 26786` and `DSM:26786`. Those rows support an external type-material relationship for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

StrainInfo has one exact species-level side inventory row for `DSM 26786`. Because no generated rows exist for `NCBITaxon:2878297` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:2878297` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colacogloea_demeterae.yaml` plus `just validate-strict data/taxa/eukaryota/colacogloea_demeterae.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:657498` into `NCBITaxon:2878297`, but this is only a side-inventory old ID; no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
