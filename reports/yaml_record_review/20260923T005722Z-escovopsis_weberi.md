# YAML Record Review: Escovopsis weberi

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/escovopsis_weberi.yaml
- Started UTC: 2026-09-23T00:57:22Z
- Finished UTC: 2026-09-23T00:57:22Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:150374` |
| Label | `Escovopsis weberi` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:150372` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/escovopsis_weberi.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/erythrobasidium_yunnanense.yaml data/taxa/eukaryota/erythrolobus_australicus.yaml data/taxa/eukaryota/erythrolobus_madagascarensis.yaml data/taxa/eukaryota/escovopsis_weberi.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with four organism assertions, one exact native GOLD organism row, two exact native GOLD project rows, one linked native GOLD analysis row, 10 NCBI type-material rows, two NCBI merged-ID side rows, three exact StrainInfo rows with three deposits, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:150374`, `label: Escovopsis weberi`, `rank: SPECIES`, `parent_taxon: NCBITaxon:150372`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:31005`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Escovopsis` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:11790`, which records four retained direct organisms for `NCBITaxon:150374`; this agrees with `source_attestations[1].assertion_count: 4` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:150374`. The YAML preserves NCBI's two exact synonyms, `Escovopsis microspora` and `Escovopsis microspora H.C. Evans & J.O. Augustin, 2014`, plus its three related synonyms.

`data/raw/ncbi_merged_ids.tsv` maps the old side-inventory IDs `NCBITaxon:1208871` and `NCBITaxon:1351544` to `NCBITaxon:150374`; neither is retained as a row with `retired_into` in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate has four organism assertions, while the current native GOLD catalogs contain one exact organism row, `Go0116517` for `Escovopsis weberi CC031208-10`, with two matching projects and one linked native GOLD analysis row.

NCBI type-material evidence contributes 10 aliases: eight `Escovopsis microspora` culture-from-holotype, holotype, and isotype aliases, plus the `ATCC 64542` and `ATCC:64542` cultures from type material for `Escovopsis weberi`. StrainInfo contains three exact target rows with three deposit designations for `Escovopsis weberi`; those side rows do not produce BacDive-derived local strain children for this taxon.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI exact synonyms, three NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/escovopsis_weberi.yaml` plus `just validate-strict data/taxa/eukaryota/escovopsis_weberi.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD JSONL inputs have one current organism row for this taxon. The NCBI merged-ID side rows are side evidence only; generated `replaces` comes from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`.
