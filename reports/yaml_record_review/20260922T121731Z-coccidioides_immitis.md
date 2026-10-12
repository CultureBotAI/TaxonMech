# YAML Record Review: Coccidioides immitis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/coccidioides_immitis.yaml
- Started UTC: 2026-09-22T12:13:58Z
- Finished UTC: 2026-09-22T12:17:31Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5501` |
| Label | `Coccidioides immitis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5500` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/coccidioides_immitis.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/coccidioides_immitis.yaml` | Passed; the strict validator exited successfully for one file. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained organisms, two exact native GOLD organism/project/analysis chains, eight NCBI type-material rows, exact StrainInfo species/deposit matches, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5501`, `label: Coccidioides immitis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5500`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2443`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Coccidioides`; the bounded scan checked all 15 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:38534`, which records two retained organisms for `NCBITaxon:5501`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5501` with one name assertion. NCBI supplies the related synonym `Coccidioides immitis G.W. Stiles, 1896` present in the YAML, and the curation-history source list agrees with the two retained source attestations.

The native GOLD snapshot has exact organism, project, and analysis rows for `Coccidioides immitis RMSCC 3703` and `Coccidioides immitis WA_211`, matching the aggregate count of two retained organisms.

The NCBI type-material side inventory has eight exact rows for this species. They include culture-from-neotype variants for `CBS 120936` and `RMSCC 2394`, plus neotype variants for `CBS 144.34` and `CBS H-19842`; those rows support external type-material relationships without being embedded directly in the generated `TaxonRecord`.

StrainInfo has exact species-level side inventory rows, including 18 exact deposit matches and 17 direct species matches. Because no generated rows exist for `NCBITaxon:5501` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:5501` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/coccidioides_immitis.yaml` plus `just validate-strict data/taxa/eukaryota/coccidioides_immitis.yaml`.

## Additional Notes

No `data/raw/ncbi_merged_ids.tsv` side rows exist for `NCBITaxon:5501`.
