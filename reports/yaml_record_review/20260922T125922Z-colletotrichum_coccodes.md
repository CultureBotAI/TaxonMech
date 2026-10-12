# YAML Record Review: Colletotrichum coccodes

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colletotrichum_coccodes.yaml
- Started UTC: 2026-09-22T12:56:00Z
- Finished UTC: 2026-09-22T12:59:22Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:27358` |
| Label | `Colletotrichum coccodes` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5455` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colletotrichum_coccodes.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/colletotrichum_coccodes.yaml` | Passed; the strict validator reported 0 errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained organisms, two native GOLD organism/project/analysis chains, two NCBI type-material rows, exact StrainInfo species/deposit rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:27358`, `label: Colletotrichum coccodes`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5455`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2752`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colletotrichum`; the bounded scan checked all 16 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:25523`, which records two retained organisms for `NCBITaxon:27358`; this agrees with `source_attestations[1].assertion_count: 2`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:27358` with one name assertion. NCBI supplies the exact synonym `Chaetomium coccodes` and both related synonyms, `Chaetomium coccodes Wallr., 1833` and `Colletotrichum coccodes (Wallr.) S. Hughes, 1958`, present in the YAML. The curation-history source list agrees with the two retained source attestations.

The native GOLD snapshot has two exact organism/project/analysis chains for this NCBI taxon: `NJ-RT1` / `Go0390096` / `Gp0252493` and `RP180a` / `Go0390100` / `Gp0252498`.

The NCBI type-material side inventory has two exact culture-from-neotype rows for this taxon ID under the synonymous taxon name `Chaetomium coccodes`: `CBS 369.75` and `CBS:369.75`. Those rows support an external type-material relationship for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

StrainInfo has exact species-level side inventory rows, including 69 exact deposit matches and 65 direct species matches. Because no generated rows exist for `NCBITaxon:27358` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:27358` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colletotrichum_coccodes.yaml` plus `just validate-strict data/taxa/eukaryota/colletotrichum_coccodes.yaml`.

## Additional Notes

No `data/raw/ncbi_merged_ids.tsv` side rows exist for `NCBITaxon:27358`.
