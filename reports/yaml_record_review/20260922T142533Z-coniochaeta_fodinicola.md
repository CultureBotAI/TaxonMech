# YAML Record Review: Coniochaeta fodinicola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/coniochaeta_fodinicola.yaml
- Started UTC: 2026-09-22T14:20:14Z
- Finished UTC: 2026-09-22T14:25:33Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1199094` |
| Label | `Coniochaeta fodinicola` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:79808` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/coniochaeta_fodinicola.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/coniochaeta_fodinicola.yaml` | Passed; the strict validator scanned one file with zero errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, no exact native GOLD organism rows, seven NCBI type-material rows, four NCBI merged-ID side rows, no exact StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1199094`, `label: Coniochaeta fodinicola`, `rank: SPECIES`, `parent_taxon: NCBITaxon:79808`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:270169`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Coniochaeta` genus; the bounded scan checked all 16 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:4805`, which records one retained organism for `NCBITaxon:1199094`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1199094`. NCBI supplies all six related synonyms present in the YAML and no exact synonyms.

The native GOLD snapshot currently has no exact organism rows for this NCBI taxon, while the maintained `data/raw/gold_organisms.tsv` aggregate row records one retained GOLD organism. The generated YAML follows that retained aggregate source, so the `GOLD` attestation count is consistent with the generated input used by this record.

The NCBI type-material side inventory has seven exact `Coniochaeta fodinicola` rows: culture-from-holotype designations `CBS 136963`, `CBS:136963`, and `FRL`, plus holotype designations `LY 13.2082`, `LY-13.2082`, `LY13.2082`, and `LY:13.2082`. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:1199094` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/coniochaeta_fodinicola.yaml` plus `just validate-strict data/taxa/eukaryota/coniochaeta_fodinicola.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` has four side-inventory old IDs that now map into `NCBITaxon:1199094`: `NCBITaxon:1199093`, `NCBITaxon:1199095`, `NCBITaxon:1199096`, and `NCBITaxon:1506145`. The retained retired-row inventory is empty for this target, so the absence of `replaces` values in the YAML is expected.
