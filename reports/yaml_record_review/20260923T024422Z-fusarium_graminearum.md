# YAML Record Review: Fusarium graminearum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_graminearum.yaml
- Started UTC: 2026-09-23T02:44:22Z
- Finished UTC: 2026-09-23T02:44:22Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5518` |
| Label | `Fusarium graminearum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:569360` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_graminearum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_gaditjirri.yaml data/taxa/eukaryota/fusarium_globosum.yaml data/taxa/eukaryota/fusarium_graminearum.yaml data/taxa/eukaryota/fusarium_graminum.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with 23 organism assertions, 24 current native GOLD organism rows with 73 linked projects, 18 native GOLD analysis rows linked by project ID, no NCBI merged-ID side rows, 384 exact direct StrainInfo rows, 485 StrainInfo deposit rows, two NCBI epitype-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5518`, `label: Fusarium graminearum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:569360`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2451`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium sambucinum species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:38568`, which records 23 retained direct organisms for `NCBITaxon:5518`; this agrees with `source_attestations[1].assertion_count: 23` and its organism assertion unit. The current native GOLD catalogs contain 24 exact organism rows, 73 linked project rows, and 18 analysis rows linked through those project IDs.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5518`. The YAML preserves exact synonyms `Gibberella zeae` and `Sphaeria zeae`, plus three related NCBI synonyms for author-qualified names.

The retained GOLD aggregate supplies 23 organism assertions. Exact expansion of `data/gold/organisms.jsonl.gz`, `data/gold/projects.jsonl.gz`, and `data/gold/analyses.jsonl.gz` found 24 current native organism rows, 73 projects linked to those organisms, and 18 analyses linked by `AP PROJECT GOLD IDS`. The one-row difference between the retained aggregate table and the current native organism catalog is side-evidence drift and does not contradict the generated assertion count.

No side-inventory NCBI old IDs merge into `NCBITaxon:5518`, so the YAML correctly has no generated `replaces` entry. StrainInfo contains 384 exact direct rows and 485 exact deposit rows for the target. Those rows do not produce BacDive-derived local strain children for this taxon. NCBI has two culture-from-epitype aliases for the target in `typematerial.dmp`: `CBS 136009` and `CBS:136009`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_graminearum.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_graminearum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_graminearum` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
