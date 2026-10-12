# YAML Record Review: Dothidea sambuci

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/dothidea_sambuci.yaml
- Started UTC: 2026-09-22T23:25:08Z
- Finished UTC: 2026-09-22T23:25:08Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:162394` |
| Label | `Dothidea sambuci` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:45096` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/dothidea_sambuci.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/diversispora_eburnea.yaml data/taxa/eukaryota/diversispora_epigaea.yaml data/taxa/eukaryota/donkioporia_expansa.yaml data/taxa/eukaryota/dothidea_sambuci.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, four exact NCBI type-material rows, two exact StrainInfo direct records carrying two matching deposit designations, no exact native GOLD organisms or BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:162394`, `label: Dothidea sambuci`, `rank: SPECIES`, `parent_taxon: NCBITaxon:45096`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:33419`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Dothidea` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:13904`, which records two retained direct organisms for `NCBITaxon:162394`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:162394`. The YAML carries the one exact synonym and both related synonyms filed for this NCBI row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The current local native GOLD organism, project, and analysis catalogs have no exact rows for `NCBITaxon:162394`, so the generated attestation is supported by the aggregate input rather than by a row in `data/gold/organisms.jsonl.gz`.

The NCBI type-material inventory contributes four exact rows under `Dothidea sambuci`, covering separator variants of the `AFTOL-ID 274` and `DAOM 231303` culture-from-epitype designations.

The exact StrainInfo side inventory has two direct records and two matching deposit designations for `NCBITaxon:162394`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/dothidea_sambuci.yaml` plus `just validate-strict data/taxa/eukaryota/dothidea_sambuci.yaml`.

## Additional Notes

The retained GOLD aggregate reports two organism assertions for this NCBI taxon, while the current local native GOLD catalog contains no exact organism rows. The generated attestation is still supported by the maintained aggregate input that seeded the YAML.
