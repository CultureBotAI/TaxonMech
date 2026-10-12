# YAML Record Review: Drechmeria coniospora

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/drechmeria_coniospora.yaml
- Started UTC: 2026-09-22T23:30:43Z
- Finished UTC: 2026-09-22T23:30:43Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:98403` |
| Label | `Drechmeria coniospora` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:98402` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/drechmeria_coniospora.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/dothiorella_sarmentorum.yaml data/taxa/eukaryota/dothistroma_septosporum.yaml data/taxa/eukaryota/drechmeria_coniospora.yaml data/taxa/eukaryota/drechslerella_stenobrocha.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, the retained GOLD aggregate row, two exact native GOLD organisms, three native GOLD projects, two native GOLD analyses, two NCBI type-material rows, 13 exact StrainInfo direct records carrying 13 matching deposit designations, no NCBI merged-ID side rows, no lineage mismatches, no BacDive rows, and no final raw strain rows. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:98403`, `label: Drechmeria coniospora`, `rank: SPECIES`, `parent_taxon: NCBITaxon:98402`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:16777`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Drechmeria` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:45268`, which records two retained direct organisms for `NCBITaxon:98403`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:98403`. The YAML carries the one exact synonym and both related synonyms filed for this NCBI row; NCBI supplies no broad synonyms.

The two NCBI type-material rows preserve `CBS 615.82` and `CBS:615.82` as duplicate spellings of the `Meria coniospora` neotype. There are no old-ID side rows in `data/raw/ncbi_merged_ids.tsv` for this taxon.

The native GOLD catalogs contain two exact organism rows, `Go0116324` for `Drechmeria coniospora ATCC 96282` and `Go0144681` for `Drechmeria coniospora ARSEF 6962`; these join to three projects because the ATCC organism also has `Gp0236216`, a transcriptome project. Two analysis rows are linked through the organism projects.

The exact StrainInfo side inventory has 13 direct records and 13 matching deposit designations for `NCBITaxon:98403`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/drechmeria_coniospora.yaml` plus `just validate-strict data/taxa/eukaryota/drechmeria_coniospora.yaml`.

## Additional Notes

The native GOLD and retained aggregate counts both support two organism assertions. The extra native GOLD project is a transcriptome project for the existing `Go0116324` ATCC organism, not an extra organism assertion.
