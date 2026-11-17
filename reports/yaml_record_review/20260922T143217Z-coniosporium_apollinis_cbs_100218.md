# YAML Record Review: Coniosporium apollinis CBS 100218

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/coniosporium_apollinis_cbs_100218.yaml
- Started UTC: 2026-09-22T14:32:13Z
- Finished UTC: 2026-09-22T14:32:17Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1168221` |
| Label | `Coniosporium apollinis CBS 100218` |
| Rank | `STRAIN` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:61459` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/coniosporium_apollinis_cbs_100218.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/coniosporium_apollinis_cbs_100218.yaml` | Passed; the strict validator scanned one file with zero errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism/project/analysis chain, no NCBI type-material rows, no NCBI merged-ID side rows, no exact StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1168221`, `label: Coniosporium apollinis CBS 100218`, `rank: STRAIN`, `parent_taxon: NCBITaxon:61459`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:258145`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Coniosporium apollinis` species; the bounded scan checked all 15 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:3601`, which records one retained organism for `NCBITaxon:1168221`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1168221`. NCBI supplies the related synonym `Coniosporium apollinis CBS 352.97`, matching the YAML synonym.

The native GOLD snapshot has one exact organism row for this NCBI taxon, `Go0037641` / `Coniosporium apollinis CBS 352.97`, with project `Gp0037641` and one linked analysis row under the same CBS 352.97 label; this agrees with the retained aggregate count and the NCBI synonym.

The bounded scan found no exact StrainInfo rows for this NCBI taxon, so there are no StrainInfo side deposits to join into the maintained final strain tables.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no NCBI type-material rows for `NCBITaxon:1168221`; no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/coniosporium_apollinis_cbs_100218.yaml` plus `just validate-strict data/taxa/eukaryota/coniosporium_apollinis_cbs_100218.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:1168221`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
