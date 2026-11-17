# YAML Record Review: Conidiobolus brefeldianus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/conidiobolus_brefeldianus.yaml
- Started UTC: 2026-09-22T14:08:12Z
- Finished UTC: 2026-09-22T14:12:15Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:181042` |
| Label | `Conidiobolus brefeldianus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:34487` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/conidiobolus_brefeldianus.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/conidiobolus_brefeldianus.yaml` | Passed; the strict validator scanned one file with zero errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, no exact native GOLD organism rows, two NCBI type-material rows, no NCBI merged-ID side rows, three exact StrainInfo side deposits, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:181042`, `label: Conidiobolus brefeldianus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:34487`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:36343`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Conidiobolus` genus; the bounded scan checked all 12 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:15991`, which records one retained organism for `NCBITaxon:181042`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:181042`. NCBI supplies the single related synonym present in the YAML and no exact synonyms.

The native GOLD snapshot currently has no exact organism rows for this NCBI taxon, while the maintained `data/raw/gold_organisms.tsv` aggregate row records one retained GOLD organism. The generated YAML follows that retained aggregate source, so the `GOLD` attestation count is consistent with the generated input used by this record.

The NCBI type-material side inventory has two exact `Conidiobolus brefeldianus` type-material rows, `ARSEF 452` and `ARSEF:452`. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

The exact StrainInfo side inventory has three deposits and one direct DOI record for the same NCBI taxon. They do not currently join into the maintained final strain tables, so `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated synonym from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:181042` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/conidiobolus_brefeldianus.yaml` plus `just validate-strict data/taxa/eukaryota/conidiobolus_brefeldianus.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:181042`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
