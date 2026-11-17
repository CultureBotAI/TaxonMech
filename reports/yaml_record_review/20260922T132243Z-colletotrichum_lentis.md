# YAML Record Review: Colletotrichum lentis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colletotrichum_lentis.yaml
- Started UTC: 2026-09-22T13:18:00Z
- Finished UTC: 2026-09-22T13:22:43Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1585795` |
| Label | `Colletotrichum lentis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2707350` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colletotrichum_lentis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/colletotrichum_lentis.yaml` | Passed; the strict validator scanned one file with zero errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one native GOLD organism/project/analysis chain, seven NCBI type-material rows, one NCBI merged-ID side row, exact StrainInfo species/deposit rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1585795`, `label: Colletotrichum lentis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2707350`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:410398`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colletotrichum destructivum species complex`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:12807`, which records one retained organism for `NCBITaxon:1585795`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1585795` with one name assertion. NCBI supplies the exact synonym `Glomerella truncata` and both related synonyms present in the YAML.

The native GOLD snapshot has one exact organism row for this NCBI taxon, `Go0591044` / `Colletotrichum lentis CT-30`, with project `Gp0604989` / `Colletotrichum lentis CT-30` and one linked analysis row.

The NCBI type-material side inventory has seven exact rows for `Colletotrichum lentis`, covering `CBS 127604`, `DAOM 235318`, `CBS H-21649`, and `ICMP:21083` designations plus colon-normalized aliases where NCBI supplies them. Those rows support external holotype-culture, holotype, and isotype relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

StrainInfo has exact species-level side inventory rows, including four exact deposit matches and four direct species matches. Because no generated rows exist for `NCBITaxon:1585795` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:1585795` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colletotrichum_lentis.yaml` plus `just validate-strict data/taxa/eukaryota/colletotrichum_lentis.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` maps old `NCBITaxon:713004` into `NCBITaxon:1585795`, but this is only a side-inventory old ID; no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
