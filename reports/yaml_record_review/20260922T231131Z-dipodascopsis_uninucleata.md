# YAML Record Review: Dipodascopsis uninucleata

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/dipodascopsis_uninucleata.yaml
- Started UTC: 2026-09-22T23:11:31Z
- Finished UTC: 2026-09-22T23:11:31Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:27313` |
| Label | `Dipodascopsis uninucleata` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:27312` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/dipodascopsis_uninucleata.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/dipodascopsis_uninucleata.yaml data/taxa/eukaryota/dipodascopsis_uninucleata_var_uninucleata.yaml data/taxa/eukaryota/dipodascopsis_uninucleata_var_wickerhamii.yaml data/taxa/eukaryota/dipodascus_aggregatus.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism linked to two projects and no analyses, 12 exact NCBI type-material rows, 11 exact StrainInfo direct records carrying 20 matching deposit designations, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:27313`, `label: Dipodascopsis uninucleata`, `rank: SPECIES`, `parent_taxon: NCBITaxon:27312`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2727`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Dipodascopsis` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:25448`, which records one retained direct organism for `NCBITaxon:27313`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:27313`. The YAML carries both exact synonyms and the one related synonym filed for this NCBI row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain one exact organism, `Go0583974` for `Dipodascopsis uninucleata UCDFST 50-6`, and two projects, `Gp0588867` and `Gp0595890`, under that organism; the native GOLD analysis table has no exact linked analyses for those project IDs.

The NCBI type-material inventory contributes 12 exact rows under `Dipodascus uninucleatus`, covering separator variants of the `ATCC 7445`, `CBS 190.37`, and `NRRL Y-17583` type-material designations.

The exact StrainInfo side inventory has 11 direct records and 20 matching deposit designations for `NCBITaxon:27313`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI exact synonyms, one NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/dipodascopsis_uninucleata.yaml` plus `just validate-strict data/taxa/eukaryota/dipodascopsis_uninucleata.yaml`.

## Additional Notes

None.
