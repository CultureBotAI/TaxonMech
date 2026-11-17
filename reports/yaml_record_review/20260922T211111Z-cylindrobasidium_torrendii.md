# YAML Record Review: Cylindrobasidium torrendii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cylindrobasidium_torrendii.yaml
- Started UTC: 2026-09-22T21:11:11Z
- Finished UTC: 2026-09-22T21:11:11Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:394432` |
| Label | `Cylindrobasidium torrendii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:139105` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cylindrobasidium_torrendii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cylindricascospora_bacillisporus_cbs_7720.yaml data/taxa/eukaryota/cylindrobasidium_torrendii.yaml data/taxa/eukaryota/cylindrocarpon_sp.yaml data/taxa/eukaryota/cylindrodendrum_hubeiense.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, no exact native GOLD rows keyed to `NCBITaxon:394432`, six exact StrainInfo records not retained in the final StrainInfo overlay, no NCBI type-material rows, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:394432`, `label: Cylindrobasidium torrendii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:139105`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:83894`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cylindrobasidium` genus; the bounded scan checked all 14 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:34242`, which records one retained organism for `NCBITaxon:394432`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:394432`. The YAML carries NCBI's exact synonym `Peniophora torrendii` and the two NCBI related synonyms `Cylindrobasidium torrendii (Bres.) Hjortstam` and `Peniophora torrendii Bres., 1913`; NCBI supplies no broad synonyms for this row.

The retained GOLD aggregate row supports the `GOLD` source attestation. An exact native GOLD scan found no organism row keyed to `NCBITaxon:394432`; a bounded native name search found `Cylindrobasidium torrendii FP15055 ss-10` still keyed to `NCBITaxon:1314674`, which is not present in this snapshot's NCBI merge table as a redirect to `NCBITaxon:394432`.

Exact StrainInfo records are keyed directly to `NCBITaxon:394432`, but none are retained into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`, and no `STRAININFO` source attestation is generated.

No exact NCBI type-material, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cylindrobasidium_torrendii.yaml` plus `just validate-strict data/taxa/eukaryota/cylindrobasidium_torrendii.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:394432`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
