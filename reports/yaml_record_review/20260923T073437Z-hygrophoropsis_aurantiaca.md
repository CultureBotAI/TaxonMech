# YAML Record Review: Hygrophoropsis aurantiaca

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hygrophoropsis_aurantiaca.yaml
- Started UTC: 2026-09-23T07:34:37Z
- Finished UTC: 2026-09-23T07:34:37Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:72124` |
| Label | `Hygrophoropsis aurantiaca` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:72123` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hygrophoropsis_aurantiaca.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hygrophoropsis_aurantiaca.yaml data/taxa/eukaryota/hygrophorus_olivaceoalbus.yaml data/taxa/eukaryota/hygrophorus_pudorinus.yaml data/taxa/eukaryota/hygrophorus_russula.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, two exact current native GOLD organisms with eight linked native GOLD projects and one linked native GOLD analysis, no exact NCBI type-material rows, one side NCBI merged-ID row, 17 exact direct StrainInfo source records, 18 exact StrainInfo deposit matches, no final StrainInfo overlay rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:72124`, `label: Hygrophoropsis aurantiaca`, `rank: SPECIES`, `parent_taxon: NCBITaxon:72123`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:10095`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hygrophoropsis`; the bounded scan checked all 14 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:41978`, which records two retained direct organisms for `NCBITaxon:72124`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs also contain two exact organisms, eight linked projects, and one linked analysis.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:72124`. `Agaricus aurantiacus` and `Cantharellus aurantiacus` are present in `data/raw/ncbitaxon_taxa.tsv:10095` as exact synonyms, and all four authorship-bearing or provisional related synonyms are present in the source row.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have exact `Go0111657` and `Go0531291` organisms for ATCC 28755 and ATCC 42419, eight linked projects spanning `Gp0113718`, `Gp0113719`, and `Gp0467542` through `Gp0467547`, and one native analysis linked by project ID `Gp0113718`.

The raw StrainInfo JSONL contains 17 exact direct source records and 18 exact deposit matches for `NCBITaxon:72124`, but the maintained StrainInfo overlay tables have no exact rows for this taxon.

The side merged-ID inventory maps old `NCBITaxon:2942890` to current `NCBITaxon:72124`, but no retained retired NCBI row has `retired_into: NCBITaxon:72124`, so no generated `replaces` entry is expected.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hygrophoropsis_aurantiaca.yaml` plus `just validate-strict data/taxa/eukaryota/hygrophoropsis_aurantiaca.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hygrophoropsis_aurantiaca` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo only overlays BacDive-derived local strains in the generated final tables, so exact raw StrainInfo JSONL rows without exact final `data/straininfo` output rows are not generated as child strain records here.
