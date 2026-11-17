# YAML Record Review: Epichloe festucae var. lolii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/epichloe_festucae_var_lolii.yaml
- Started UTC: 2026-09-23T00:38:35Z
- Finished UTC: 2026-09-23T00:38:35Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:73839` |
| Label | `Epichloe festucae var. lolii` |
| Rank | `VARIETAS` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:35717` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/epichloe_festucae_var_lolii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/epichloe_festucae.yaml data/taxa/eukaryota/epichloe_festucae_fl1.yaml data/taxa/eukaryota/epichloe_festucae_var_lolii.yaml data/taxa/eukaryota/epichloe_funkii.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism/project row, no native GOLD analyses, five NCBI type-material rows, two NCBI merged-ID side rows, 17 exact StrainInfo rows with 20 deposits, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:73839`, `label: Epichloe festucae var. lolii`, `rank: VARIETAS`, `parent_taxon: NCBITaxon:35717`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:10380`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the parent species `Epichloe festucae`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy varietas ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:42076`, which records one retained direct organism for `NCBITaxon:73839`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:73839`. The YAML preserves NCBI's exact synonyms `Acremonium lolii` and `Neotyphodium lolii`, plus all three related synonyms filed for this row.

`data/raw/ncbi_merged_ids.tsv:12205` and `data/raw/ncbi_merged_ids.tsv:82529` map the old side-inventory IDs `NCBITaxon:1328102` and `NCBITaxon:5048` to `NCBITaxon:73839`; neither is retained as a row with `retired_into` in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly has no generated `replaces` entries.

The five NCBI type-material rows preserve a culture-from-type-material alias for `ICMP:8360` and type-material aliases for `CBS 229.84` and `PDD 44517` under `Acremonium lolii`. The native GOLD catalogs contain one exact organism row, `Go0002875`, with one matching project and no matching native GOLD analysis rows.

StrainInfo contains 17 exact target rows with 20 deposit designations for `Epichloe festucae var. lolii`; those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI exact synonyms, three NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/epichloe_festucae_var_lolii.yaml` plus `just validate-strict data/taxa/eukaryota/epichloe_festucae_var_lolii.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the one current native GOLD organism row. The NCBI merged-ID side rows are side evidence only; generated `replaces` comes from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`.
