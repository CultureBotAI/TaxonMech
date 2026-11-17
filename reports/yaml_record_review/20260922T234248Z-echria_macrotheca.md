# YAML Record Review: Echria macrotheca

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/echria_macrotheca.yaml
- Started UTC: 2026-09-22T23:42:48Z
- Finished UTC: 2026-09-22T23:42:48Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:438768` |
| Label | `Echria macrotheca` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1538025` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/echria_macrotheca.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/echria_macrotheca.yaml data/taxa/eukaryota/ectocarpus_siliculosus.yaml data/taxa/eukaryota/ectophoma_multirostrata.yaml data/taxa/eukaryota/ecytonucleospora_hepatopenaei.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism, two native GOLD projects, one exact StrainInfo direct record carrying one matching deposit designation, no native GOLD analyses, no exact NCBI type-material, NCBI merged-ID, or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:438768`, `label: Echria macrotheca`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1538025`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:97387`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Echria` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:35489`, which records one retained direct organism for `NCBITaxon:438768`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:438768`. The YAML carries both exact synonyms and both related synonyms filed for this NCBI row; NCBI supplies no broad synonyms or old-ID side rows.

The native GOLD catalogs contain one exact organism row, `Go0583354` for `Echria macrotheca PSN4`, and two linked projects: `Gp0587303` for a minimal draft and `Gp0587304` for a transcriptome. The exact StrainInfo side inventory has one direct record and one matching `ATCC 42488` deposit designation for `NCBITaxon:438768`, but that record is not present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`.

No exact native GOLD analysis, NCBI type-material, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI exact synonyms, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/echria_macrotheca.yaml` plus `just validate-strict data/taxa/eukaryota/echria_macrotheca.yaml`.

## Additional Notes

The one retained GOLD organism can have multiple native GOLD projects without changing the generated organism assertion count.
