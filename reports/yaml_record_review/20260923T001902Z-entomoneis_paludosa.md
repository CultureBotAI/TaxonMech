# YAML Record Review: Entomoneis paludosa

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/entomoneis_paludosa.yaml
- Started UTC: 2026-09-23T00:19:02Z
- Finished UTC: 2026-09-23T00:19:02Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:265537` |
| Label | `Entomoneis paludosa` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:186042` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/entomoneis_paludosa.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/entoloma_gasteromycetoides.yaml data/taxa/eukaryota/entoloma_vernum.yaml data/taxa/eukaryota/entomoneis_paludosa.yaml data/taxa/eukaryota/entomoneis_sp.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism row, one NCBI merged-ID side row, two exact StrainInfo rows with two deposits, no native GOLD project or analysis rows, no NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:265537`, `label: Entomoneis paludosa`, `rank: SPECIES`, `parent_taxon: NCBITaxon:186042`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:54353`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Entomoneis` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:24370`, which records one retained direct organism for `NCBITaxon:265537`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:265537`. The YAML preserves NCBI's exact synonym `Amphiprora paludosa`, plus both related synonyms filed for this row.

`data/raw/ncbi_merged_ids.tsv:90443` maps the old side-inventory ID `NCBITaxon:650509` to `NCBITaxon:265537`; it is not retained as a row with `retired_into` in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly has no generated `replaces` entry. The native GOLD catalogs contain one exact organism row, `Go0368567` for `Amphiprora paludosa CCMP 125`, and no matching native GOLD project or analysis rows.

StrainInfo contains two exact target rows, `siID 210813` with deposit `CCMP125` and `siID 353641` with deposit `SAG 15.83`; those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive, NCBI type-material, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/entomoneis_paludosa.yaml` plus `just validate-strict data/taxa/eukaryota/entomoneis_paludosa.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the one current native GOLD organism row. The NCBI merged-ID side row is side evidence only; generated `replaces` comes from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`.
