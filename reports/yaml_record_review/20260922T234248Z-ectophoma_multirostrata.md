# YAML Record Review: Ectophoma multirostrata

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/ectophoma_multirostrata.yaml
- Started UTC: 2026-09-22T23:42:48Z
- Finished UTC: 2026-09-22T23:42:48Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:73003` |
| Label | `Ectophoma multirostrata` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2078543` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/ectophoma_multirostrata.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/echria_macrotheca.yaml data/taxa/eukaryota/ectocarpus_siliculosus.yaml data/taxa/eukaryota/ectophoma_multirostrata.yaml data/taxa/eukaryota/ecytonucleospora_hepatopenaei.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism, two native GOLD projects, one native GOLD analysis, four NCBI type-material rows, one exact StrainInfo direct record carrying one matching deposit designation, one NCBI merged-ID side row, no BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:73003`, `label: Ectophoma multirostrata`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2078543`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:10245`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Ectophoma` genus; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:42037`, which records one retained direct organism for `NCBITaxon:73003`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:73003`. The YAML carries both exact synonyms and both related synonyms filed for this NCBI row; NCBI supplies no broad synonyms.

The single row in `data/raw/ncbi_merged_ids.tsv` retires `NCBITaxon:1696688` into this species ID. That old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`, so omitting `replaces` is expected.

The four NCBI type-material rows preserve `CBS 274.60` and `FMR 15335` plus colon-delimited spellings as cultures from type material for `Ectophoma multirostrata`. The native GOLD catalogs contain one exact organism row, `Go0411473` for `Phoma multirostrata 7a`, with two linked projects and one analysis for the standard-draft project.

The exact StrainInfo side inventory has one direct record and one matching `ICMP 24838` deposit designation for `NCBITaxon:73003`, but that record is not present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI exact synonyms, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/ectophoma_multirostrata.yaml` plus `just validate-strict data/taxa/eukaryota/ectophoma_multirostrata.yaml`.

## Additional Notes

The native GOLD organism and project rows use the `Phoma multirostrata` synonym spelling that NCBI records as an exact synonym of the current `Ectophoma multirostrata` name.
