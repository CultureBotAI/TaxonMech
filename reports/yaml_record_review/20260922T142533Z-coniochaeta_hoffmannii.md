# YAML Record Review: Coniochaeta hoffmannii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/coniochaeta_hoffmannii.yaml
- Started UTC: 2026-09-22T14:20:14Z
- Finished UTC: 2026-09-22T14:25:33Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:91930` |
| Label | `Coniochaeta hoffmannii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:79808` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/coniochaeta_hoffmannii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/coniochaeta_hoffmannii.yaml` | Passed; the strict validator scanned one file with zero errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained organisms, two exact native GOLD organisms with 16 projects and one analysis, four NCBI type-material rows, one NCBI merged-ID side row, 58 exact StrainInfo side deposits, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:91930`, `label: Coniochaeta hoffmannii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:79808`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:14871`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Coniochaeta` genus; the bounded scan checked all 16 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:44490`, which records two retained organisms for `NCBITaxon:91930`; this agrees with `source_attestations[1].assertion_count: 2`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:91930`. NCBI supplies all four exact synonyms and both related synonyms present in the YAML.

The native GOLD snapshot has two exact organism rows for this NCBI taxon, `Go0454583` / `Coniochaeta hoffmannii CBS 245.38` and `Go0710377` / `Coniochaeta hoffmannii EDT4_R2A_F_24`; an exact organism-ID expansion found 16 projects and one linked analysis. The native exact organism count agrees with the retained aggregate count.

The NCBI type-material side inventory has four exact rows for the same NCBI taxon under `Margarinomyces hoffmannii`: `CBS 245.38`, `CBS-245.38`, `CBS245.38`, and `CBS:245.38`. Those rows support external type-material relationships for a synonym of the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

The exact StrainInfo side inventory has 58 deposits and 50 direct DOI records for the same NCBI taxon. They do not currently join into the maintained final strain tables, so `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:91930` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/coniochaeta_hoffmannii.yaml` plus `just validate-strict data/taxa/eukaryota/coniochaeta_hoffmannii.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` has one side-inventory old ID that now maps into `NCBITaxon:91930`: `NCBITaxon:1163517`. The retained retired-row inventory is empty for this target, so the absence of `replaces` values in the YAML is expected.
