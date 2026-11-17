# YAML Record Review: Corethron hystrix

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/corethron_hystrix.yaml
- Started UTC: 2026-09-22T14:55:18Z
- Finished UTC: 2026-09-22T14:55:18Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:216773` |
| Label | `Corethron hystrix` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:49242` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/corethron_hystrix.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/corethron_hystrix.yaml` | Passed; the strict validator scanned one file with zero errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism and no exact native GOLD project rows, no NCBI type-material rows, no NCBI merged-ID side rows, two exact StrainInfo side deposits, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:216773`, `label: Corethron hystrix`, `rank: SPECIES`, `parent_taxon: NCBITaxon:49242`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:42676`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Corethron` genus; the bounded scan checked all 12 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:20657`, which records one retained organism for `NCBITaxon:216773`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:216773`. NCBI supplies the related synonym `Corethron hystrix Hensen, 1887`, matching the YAML synonym.

The native GOLD snapshot has one exact organism row for this NCBI taxon, `Go0368626` / `Corethron hystrix 308`; the local native GOLD projects snapshot does not contain exact project rows linked to that organism. The retained aggregate row supports the generated one-organism `GOLD` assertion count.

The exact StrainInfo side inventory has two deposits and two direct DOI records for the same NCBI taxon. They do not currently join into the maintained final strain tables, so `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no NCBI type-material rows for `NCBITaxon:216773`; no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/corethron_hystrix.yaml` plus `just validate-strict data/taxa/eukaryota/corethron_hystrix.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:216773`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
