# YAML Record Review: Coleophoma cylindrospora

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/coleophoma_cylindrospora.yaml
- Started UTC: 2026-09-22T12:43:20Z
- Finished UTC: 2026-09-22T12:47:22Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1849047` |
| Label | `Coleophoma cylindrospora` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:453209` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/coleophoma_cylindrospora.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/coleophoma_cylindrospora.yaml` | Passed; the strict validator reported 0 errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one native GOLD organism/project/analysis chain, one NCBI merged-ID side row, exact StrainInfo species/deposit rows, no NCBI type-material rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1849047`, `label: Coleophoma cylindrospora`, `rank: SPECIES`, `parent_taxon: NCBITaxon:453209`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:482078`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Coleophoma`; the bounded scan checked all 15 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:16416`, which records one retained organism for `NCBITaxon:1849047`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1849047` with one name assertion. NCBI supplies the three exact synonyms and three related synonyms present in the YAML, and the curation-history source list agrees with the two retained source attestations.

The native GOLD snapshot has one exact organism/project/analysis chain for this NCBI taxon: `BP6252`, organism `Go0520721`, project `Gp0444919`, and analysis `Coleophoma cylindrospora BP6252`.

StrainInfo has exact species-level side inventory rows, including nine exact deposit matches and nine direct species matches. Because no generated rows exist for `NCBITaxon:1849047` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:1849047` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/coleophoma_cylindrospora.yaml` plus `just validate-strict data/taxa/eukaryota/coleophoma_cylindrospora.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:1484971` into `NCBITaxon:1849047`, but this is only a side-inventory old ID; no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
