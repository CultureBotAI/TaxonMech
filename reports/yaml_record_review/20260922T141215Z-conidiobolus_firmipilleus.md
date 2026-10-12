# YAML Record Review: Conidiobolus firmipilleus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/conidiobolus_firmipilleus.yaml
- Started UTC: 2026-09-22T14:08:12Z
- Finished UTC: 2026-09-22T14:12:15Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:181043` |
| Label | `Conidiobolus firmipilleus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:34487` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/conidiobolus_firmipilleus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/conidiobolus_firmipilleus.yaml` | Passed; the strict validator exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained organisms, two exact native GOLD organism/project chains, no NCBI type-material rows, no NCBI merged-ID side rows, three exact StrainInfo side deposits, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:181043`, `label: Conidiobolus firmipilleus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:34487`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:36344`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Conidiobolus` genus; the bounded scan checked all 12 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:15992`, which records two retained organisms for `NCBITaxon:181043`; this agrees with `source_attestations[1].assertion_count: 2`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:181043`. NCBI supplies the single related synonym present in the YAML and no exact synonyms.

The native GOLD snapshot has two exact organism rows for this NCBI taxon, `Go0402574` / `Conidiobolus firmipilleus ARSEF 6384` and `Go0402577` / `Conidiobolus firmipilleus ARSEF 2731`, with projects `Gp0290199` and `Gp0290202`; this agrees with the retained aggregate count.

The exact StrainInfo side inventory has three deposits and two direct DOI records for the same NCBI taxon; one side deposit, `ATCC 12242`, is marked type strain in StrainInfo but does not currently join into the maintained final strain tables. `strain_count: 0` is therefore consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated synonym from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no NCBI type-material rows for `NCBITaxon:181043`; no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/conidiobolus_firmipilleus.yaml` plus `just validate-strict data/taxa/eukaryota/conidiobolus_firmipilleus.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:181043`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
