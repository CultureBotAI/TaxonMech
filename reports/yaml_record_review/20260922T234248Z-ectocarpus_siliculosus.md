# YAML Record Review: Ectocarpus siliculosus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/ectocarpus_siliculosus.yaml
- Started UTC: 2026-09-22T23:42:48Z
- Finished UTC: 2026-09-22T23:42:48Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2880` |
| Label | `Ectocarpus siliculosus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2879` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/ectocarpus_siliculosus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/echria_macrotheca.yaml data/taxa/eukaryota/ectocarpus_siliculosus.yaml data/taxa/eukaryota/ectophoma_multirostrata.yaml data/taxa/eukaryota/ecytonucleospora_hepatopenaei.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, two exact native GOLD organisms and projects, one native GOLD analysis, 199 exact StrainInfo direct records carrying 205 matching deposit designations, no exact NCBI type-material, NCBI merged-ID, or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2880`, `label: Ectocarpus siliculosus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2879`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:1978`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Ectocarpus` genus; the bounded scan checked all 11 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:28033`, which records one retained direct organism for `NCBITaxon:2880`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2880`. The YAML carries the one exact synonym and both related synonyms filed for this NCBI row; NCBI supplies no broad synonyms or old-ID side rows.

The current native GOLD catalogs contain two exact organism rows, `Go0002809` for `Ectocarpus siliculosus Ec 32 (CCAP 1310/04)` and `Go0082573` for unstrained `Ectocarpus siliculosus`; each has one linked project, and only the `Go0002809` project has a linked native analysis.

The exact StrainInfo side inventory has 199 direct records and 205 matching deposit designations for `NCBITaxon:2880`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact NCBI type-material, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/ectocarpus_siliculosus.yaml` plus `just validate-strict data/taxa/eukaryota/ectocarpus_siliculosus.yaml`.

## Additional Notes

The retained GOLD aggregate count of one differs from the two current exact rows in the local native GOLD organism catalog. The generated YAML follows the retained aggregate input that seeded the record.
