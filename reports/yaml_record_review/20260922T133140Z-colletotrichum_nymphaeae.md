# YAML Record Review: Colletotrichum nymphaeae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colletotrichum_nymphaeae.yaml
- Started UTC: 2026-09-22T13:27:30Z
- Finished UTC: 2026-09-22T13:31:40Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:306554` |
| Label | `Colletotrichum nymphaeae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2707335` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colletotrichum_nymphaeae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/colletotrichum_nymphaeae.yaml` | Passed; the strict validator scanned one file with zero errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with nine retained organisms, nine native GOLD organisms, 17 native GOLD projects, no native GOLD analyses, two NCBI type-material rows, one NCBI merged-ID side row, exact StrainInfo species/deposit rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:306554`, `label: Colletotrichum nymphaeae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2707335`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:62794`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colletotrichum acutatum species complex`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:30820`, which records nine retained organisms for `NCBITaxon:306554`; this agrees with `source_attestations[1].assertion_count: 9`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:306554` with one name assertion. NCBI supplies both exact synonyms and both related synonyms present in the YAML.

The native GOLD snapshot has nine exact organism rows for this NCBI taxon. Exact native project lookup found 17 project rows: one resequencing project for each of the first eight GOLD organisms and nine gene-expression projects for `IMI504889`; none have linked native analysis rows.

The NCBI type-material side inventory has two exact rows for synonymous `Ascochyta nymphaeae`, `CBS 515.78` and `CBS:515.78` as epitype cultures. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

StrainInfo has exact species-level side inventory rows, including 17 exact deposit matches and 13 direct species matches. Because no generated rows exist for `NCBITaxon:306554` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:306554` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colletotrichum_nymphaeae.yaml` plus `just validate-strict data/taxa/eukaryota/colletotrichum_nymphaeae.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` maps old `NCBITaxon:2082201` into `NCBITaxon:306554`, but this is only a side-inventory old ID; no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
