# YAML Record Review: Endochytriaceae sp. JEL 072

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/endochytriaceae_sp_jel_072.yaml
- Started UTC: 2026-09-23T00:03:18Z
- Finished UTC: 2026-09-23T00:03:18Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:546764` |
| Label | `Endochytriaceae sp. JEL 072` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1396814` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/endochytriaceae_sp_jel_072.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/endocarpon_pusillum.yaml data/taxa/eukaryota/endochytriaceae_sp_jel_072.yaml data/taxa/eukaryota/endoconidiophora_laricicola.yaml data/taxa/eukaryota/endoconidiophora_polonica.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, no current native GOLD organism/project/analysis rows, no NCBI type-material or merged-ID rows, no exact StrainInfo or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:546764`, `label: Endochytriaceae sp. JEL 072`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1396814`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:127266`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `unclassified Endochytriaceae` parent; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:38451`, which records one retained direct organism for `NCBITaxon:546764`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:546764`. The YAML carries both related synonyms filed for this NCBI row, `Cladochytriaceae sp. JEL 072` and `Cladochytriaceae sp. JEL072`; NCBI supplies no exact or broad synonyms and no old-ID side rows.

The local native GOLD JSONL catalogs currently contain no exact organism, project, or analysis rows for `NCBITaxon:546764`, so the generated `GOLD` count is grounded by the retained aggregate table rather than a row still present in those native JSONL snapshots.

No exact StrainInfo, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/endochytriaceae_sp_jel_072.yaml` plus `just validate-strict data/taxa/eukaryota/endochytriaceae_sp_jel_072.yaml`.

## Additional Notes

The retained GOLD aggregate count intentionally reflects `data/raw/gold_organisms.tsv`; retained aggregate rows can differ from the current exact native GOLD JSONL rows.
