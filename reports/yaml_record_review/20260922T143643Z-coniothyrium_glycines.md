# YAML Record Review: Coniothyrium glycines

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/coniothyrium_glycines.yaml
- Started UTC: 2026-09-22T14:36:48Z
- Finished UTC: 2026-09-22T14:36:48Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1077358` |
| Label | `Coniothyrium glycines` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:78388` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/coniothyrium_glycines.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/coniothyrium_glycines.yaml` | Passed; the strict validator scanned one file with zero errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with three retained organisms, three exact native GOLD organisms with three projects, no native GOLD analyses, no NCBI type-material rows, one NCBI merged-ID side row, five exact StrainInfo side deposits, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1077358`, `label: Coniothyrium glycines`, `rank: SPECIES`, `parent_taxon: NCBITaxon:78388`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:230985`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Coniothyrium` genus; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:1406`, which records three retained organisms for `NCBITaxon:1077358`; this agrees with `source_attestations[1].assertion_count: 3`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1077358`. NCBI supplies all three exact synonyms and all four related synonyms present in the YAML.

The native GOLD snapshot has three exact organism rows for this NCBI taxon: `Go0520700` / `Coniothyrium glycines 13`, `Go0520701` / `Coniothyrium glycines 17`, and `Go0520702` / `Coniothyrium glycines 18`. Those rows link to projects `Gp0444898`, `Gp0444899`, and `Gp0444900`, respectively; this supports the retained aggregate organism count.

The exact StrainInfo side inventory has five deposits and five direct DOI records for the same NCBI taxon. They do not currently join into the maintained final strain tables, so `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated NCBI synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no NCBI type-material rows for `NCBITaxon:1077358`; no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/coniothyrium_glycines.yaml` plus `just validate-strict data/taxa/eukaryota/coniothyrium_glycines.yaml`.

## Additional Notes

The bounded scan found one side row in `data/raw/ncbi_merged_ids.tsv` mapping old ID `NCBITaxon:798077` into `NCBITaxon:1077358`, but there are no side-inventory old IDs and no retained retired rows that would generate a `replaces` entry.
