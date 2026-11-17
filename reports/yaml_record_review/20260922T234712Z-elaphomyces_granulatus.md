# YAML Record Review: Elaphomyces granulatus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/elaphomyces_granulatus.yaml
- Started UTC: 2026-09-22T23:47:12Z
- Finished UTC: 2026-09-22T23:47:12Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:519963` |
| Label | `Elaphomyces granulatus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:36046` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/elaphomyces_granulatus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/elaphomyces_granulatus.yaml data/taxa/eukaryota/elaphomyces_muricatus.yaml data/taxa/eukaryota/elasticomyces_elasticus.yaml data/taxa/eukaryota/ellisomyces_anomalus.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, two exact native GOLD organisms, three native GOLD projects, one native GOLD analysis, no exact StrainInfo, NCBI type-material, NCBI merged-ID, or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:519963`, `label: Elaphomyces granulatus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:36046`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:118129`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Elaphomyces` genus; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37711`, which records two retained direct organisms for `NCBITaxon:519963`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:519963`. The YAML carries both related synonyms filed for this NCBI row; NCBI supplies no exact or broad synonyms and no old-ID side rows.

The native GOLD catalogs contain two exact organism rows, `Go0095167` for `Elaphomyces granulatus OSC145934` and `Go0640107` for `Elaphomyces granulatus Maridalen`; these join to three native projects, and only the `Go0095167` project has a linked native analysis.

There are no exact rows for this taxon in the StrainInfo side inventory, NCBI type-material table, BacDive, or the maintained final strain tables. `strain_count: 0` is therefore consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/elaphomyces_granulatus.yaml` plus `just validate-strict data/taxa/eukaryota/elaphomyces_granulatus.yaml`.

## Additional Notes

The two current native GOLD organism rows match the retained aggregate count. The Maridalen organism has both a standard-draft and transcriptome project, so the project count is larger than the organism count without changing the generated organism assertion count.
