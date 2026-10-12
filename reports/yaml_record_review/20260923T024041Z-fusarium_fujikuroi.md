# YAML Record Review: Fusarium fujikuroi

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_fujikuroi.yaml
- Started UTC: 2026-09-23T02:40:41Z
- Finished UTC: 2026-09-23T02:40:41Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5127` |
| Label | `Fusarium fujikuroi` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:171627` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_fujikuroi.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_floridanum.yaml data/taxa/eukaryota/fusarium_foetens.yaml data/taxa/eukaryota/fusarium_fredkrugeri.yaml data/taxa/eukaryota/fusarium_fujikuroi.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with 21 organism assertions, 21 current native GOLD organism rows with 21 linked projects, 18 native GOLD analysis rows linked by project ID, four NCBI merged-ID side rows, 91 exact direct StrainInfo rows, 145 StrainInfo deposit rows, 21 NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5127`, `label: Fusarium fujikuroi`, `rank: SPECIES`, `parent_taxon: NCBITaxon:171627`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2247`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium fujikuroi species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37549`, which records 21 retained direct organisms for `NCBITaxon:5127`; this agrees with `source_attestations[1].assertion_count: 21` and its organism assertion unit. The current native GOLD catalogs still contain 21 exact organism rows, 21 linked project rows, and 18 analysis rows linked through those project IDs.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5127`. The YAML preserves exact synonyms `Gibberella fujikuroi` and `Lisea fujikuroi`, plus four related NCBI synonyms for author-qualified names and `Fusarium sp. RB-01`.

The retained GOLD aggregate supplies 21 organism assertions. Exact expansion of `data/gold/organisms.jsonl.gz`, `data/gold/projects.jsonl.gz`, and `data/gold/analyses.jsonl.gz` found 21 current native organism rows, one project for each organism, and 18 analyses linked by `AP PROJECT GOLD IDS`. The three native projects without a matched analysis row are `Gp0039747`, `Gp0098797`, and `Gp0098811`; their absence from the analysis catalog is not represented in the generated taxon record.

The `data/raw/ncbi_merged_ids.tsv` side inventory has four old IDs merged into `NCBITaxon:5127`: `NCBITaxon:146992`, `NCBITaxon:1516068`, `NCBITaxon:171628`, and `NCBITaxon:42670`. None are retained in `data/raw/ncbitaxon_taxa.tsv` for generated replacement provenance, so the YAML correctly has no generated `replaces` entry.

StrainInfo contains 91 exact direct rows and 145 exact deposit rows for the target. Those rows do not produce BacDive-derived local strain children for this taxon. NCBI has 21 type-material aliases for the target in `typematerial.dmp`: `BBA 12428`, `BBA 63630`, `BBA:12428`, `BBA:63630`, `BCCM/IHEM:3821`, `CBS 221.76`, `CBS:221.76`, `IHEM 3821`, `IHEM:3821`, `IMI 196086`, `IMI 202879`, `IMI:196086`, `IMI:202879`, `LCP 58.3353`, `LCP:58.3353`, `NRRL 13620`, `NRRL 13998`, `NRRL 22174`, `NRRL:13620`, `NRRL:13998`, and `NRRL:22174`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI related and exact synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_fujikuroi.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_fujikuroi.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_fujikuroi` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
