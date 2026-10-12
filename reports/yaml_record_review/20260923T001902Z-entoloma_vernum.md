# YAML Record Review: Entoloma vernum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/entoloma_vernum.yaml
- Started UTC: 2026-09-23T00:19:02Z
- Finished UTC: 2026-09-23T00:19:02Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:527498` |
| Label | `Entoloma vernum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:71937` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/entoloma_vernum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/entoloma_gasteromycetoides.yaml data/taxa/eukaryota/entoloma_vernum.yaml data/taxa/eukaryota/entomoneis_paludosa.yaml data/taxa/eukaryota/entomoneis_sp.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, one NCBI merged-ID side row, one exact StrainInfo row with one deposit, no current exact native GOLD organism/project/analysis rows, no NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:527498`, `label: Entoloma vernum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:71937`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:120346`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Entoloma` genus; the bounded scan checked all 14 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37975`, which records two retained direct organisms for `NCBITaxon:527498`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:527498`. The YAML preserves NCBI's exact synonyms `Nolanea verna`, `Nolanea verna var. isodiametrica`, and `Rhodophyllus vernus`, plus both related synonyms filed for this row.

`data/raw/ncbi_merged_ids.tsv:8209` maps the old side-inventory ID `NCBITaxon:1217159` to `NCBITaxon:527498`; it is not retained as a row with `retired_into` in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly has no generated `replaces` entry. The current native GOLD catalogs in the local export contain no exact organism, project, or analysis rows for `NCBITaxon:527498`, leaving the GOLD seed support represented by the retained aggregate row.

StrainInfo contains one exact target row, `siID 161631`, with one deposit designation, `CBS 238.50`; that side row does not produce a BacDive-derived local strain child for this taxon. No exact BacDive, NCBI type-material, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, three NCBI exact synonyms, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/entoloma_vernum.yaml` plus `just validate-strict data/taxa/eukaryota/entoloma_vernum.yaml`.

## Additional Notes

The retained GOLD aggregate row has two organism assertions, but the local native GOLD export currently has no exact organism rows for this taxon ID. The NCBI merged-ID side row is side evidence only; generated `replaces` comes from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`.
