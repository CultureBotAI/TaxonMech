# YAML Record Review: Fusarium oxysporum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_oxysporum.yaml
- Started UTC: 2026-09-23T03:06:44Z
- Finished UTC: 2026-09-23T03:06:44Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5507` |
| Label | `Fusarium oxysporum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:171631` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_oxysporum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_oligoseptatum.yaml data/taxa/eukaryota/fusarium_oxysporum.yaml data/taxa/eukaryota/fusarium_oxysporum_f_sp_albedinis.yaml data/taxa/eukaryota/fusarium_oxysporum_f_sp_cepae.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with 58 organism assertions, 43 current native GOLD organism rows with 80 linked projects and 19 native analysis rows, eight NCBI merged-ID side rows, 795 exact direct StrainInfo entries, 821 exact StrainInfo deposit references, four NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5507`, `label: Fusarium oxysporum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:171631`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2446`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium oxysporum species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:38540`, which records 58 retained direct organisms for `NCBITaxon:5507`; this agrees with `source_attestations[1].assertion_count: 58` and its organism assertion unit. The current native GOLD catalogs contain 43 exact organism rows, 80 linked projects, and 19 analyses linked to those projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5507`. The YAML preserves the exact synonym `Fusarium oxysporum Schltdl., 1824` and eight related NCBI synonyms: `Fusarium sp. Fox56`, `Fusarium sp. Fox59`, `Fusarium sp. GIFUUTR5`, `Fusarium sp. PDBC NPFu1`, `Fusarium sp. PDBC NPFu2`, `Fusarium sp. PDBC NPFu3`, `Trichoderma sp. CDR2P2F1`, and `fungal sp. ZZF51`.

The retained GOLD aggregate supplies 58 organism assertions filed directly under `NCBITaxon:5507`, matching the YAML note that descendant taxa are not gathered. The current native GOLD catalogs have 43 exact organism rows, 80 linked project rows, and 19 project-linked analysis rows; all project and analysis counts were expanded from exact organism IDs and project IDs after the bounded sample.

The NCBI side merge inventory maps eight old IDs to `NCBITaxon:5507`: `NCBITaxon:1471553`, `NCBITaxon:1501447`, `NCBITaxon:1501448`, `NCBITaxon:480706`, `NCBITaxon:685562`, `NCBITaxon:696219`, `NCBITaxon:697218`, and `NCBITaxon:697221`. None of those old IDs are retained in `data/raw/ncbitaxon_taxa.tsv` with `retired_into`, so the YAML correctly has no generated `replaces` entry.

StrainInfo contains 795 exact direct rows and 821 exact deposit references for the target. NCBI has four exact type-material aliases for the target in `typematerial.dmp`: `CBS 144134`, `CBS:144134`, `CBS H-23620`, and `CBS:H-23620`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_oxysporum.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_oxysporum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_oxysporum` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv` and can differ from the current native GOLD exact-row count. The current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
