# YAML Record Review: Epicoccum nigrum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/epicoccum_nigrum.yaml
- Started UTC: 2026-09-23T00:48:43Z
- Finished UTC: 2026-09-23T00:48:43Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:105696` |
| Label | `Epicoccum nigrum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:104397` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/epicoccum_nigrum.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/epicoccum_nigrum.yaml data/taxa/eukaryota/epicoccum_sorghinum.yaml data/taxa/eukaryota/epithele_typhae.yaml data/taxa/eukaryota/eremothecium_coryli.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with 12 organism assertions, five current exact native GOLD organism rows, seven exact native GOLD project rows, two linked native GOLD analysis rows, six NCBI type-material rows, three NCBI merged-ID side rows, 146 exact StrainInfo rows with 169 deposits, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:105696`, `label: Epicoccum nigrum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:104397`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:18956`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Epicoccum` genus; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:1065`, which records 12 retained direct organisms for `NCBITaxon:105696`; this agrees with `source_attestations[1].assertion_count: 12` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:105696`. The YAML preserves NCBI's two exact synonyms, `Epicoccum purpurascens` and `Phoma epicoccina`, plus its four related synonyms.

`data/raw/ncbi_merged_ids.tsv` maps the old side-inventory IDs `NCBITaxon:115135`, `NCBITaxon:2763897`, and `NCBITaxon:582723` to `NCBITaxon:105696`; none are retained as rows with `retired_into` in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate has 12 organism assertions, while the current native GOLD catalogs contain five exact organisms, seven linked projects, and two linked native GOLD analysis rows.

NCBI type-material evidence contributes six aliases for `Phoma epicoccina`: the `CBS 173.73` and `CBS:173.73` cultures from holotype, plus the `ATCC 24428`, `ATCC:24428`, `IMI 164070`, and `IMI:164070` type-material aliases. StrainInfo contains 146 exact target rows with 169 deposit designations for `Epicoccum nigrum`; those side rows do not produce BacDive-derived local strain children for this taxon.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI exact synonyms, four NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/epicoccum_nigrum.yaml` plus `just validate-strict data/taxa/eukaryota/epicoccum_nigrum.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD JSONL inputs have five current organism rows for this taxon. The NCBI merged-ID side rows are side evidence only; generated `replaces` comes from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`.
