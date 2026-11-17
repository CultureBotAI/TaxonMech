# YAML Record Review: Cryomyces antarcticus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cryomyces_antarcticus.yaml
- Started UTC: 2026-09-22T16:03:04Z
- Finished UTC: 2026-09-22T16:03:04Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:329879` |
| Label | `Cryomyces antarcticus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:329878` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cryomyces_antarcticus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cryomyces_antarcticus.yaml` | Passed; the strict validator reported 0 total ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with 16 retained organisms, two exact native GOLD organism rows, four exact native GOLD project rows, no exact native GOLD analysis rows, seven exact NCBI type-material side rows, no exact StrainInfo rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:329879`, `label: Cryomyces antarcticus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:329878`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:67358`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cryomyces` genus; the bounded scan checked all 14 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:32230`, which records 16 retained organisms for `NCBITaxon:329879`; this agrees with `source_attestations[1].assertion_count: 16` and with the direct-filing note in the YAML.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:329879`. NCBI supplies the related synonym `Cryomyces antarcticus Selbmann, de Hoog, Mazzaglia, Friedmann & Onofri, 2005`, matching the YAML synonym.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot has exact organisms `Go0005338` and `Go0583367` and exact projects `Gp0005338`, `Gp0005493`, `Gp0587330`, and `Gp0891538`; no native analysis rows are filed under those projects.

The NCBI type-material side inventory has seven exact rows for this taxon: three `ATCC MYA-4880` spellings as culture from type material, two `CBS 116301` spellings as type material, and two `CCFEE 534` spellings as type material. No exact StrainInfo or maintained final strain-table rows are present, so `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cryomyces_antarcticus.yaml` plus `just validate-strict data/taxa/eukaryota/cryomyces_antarcticus.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:329879`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.

The retained GOLD aggregate count for this taxon is larger than the exact native rows currently present in `data/gold/organisms.jsonl.gz`; the generated record follows the retained aggregate TSV for its source attestation count.
