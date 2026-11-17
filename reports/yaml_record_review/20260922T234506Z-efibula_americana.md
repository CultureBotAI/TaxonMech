# YAML Record Review: Efibula americana

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/efibula_americana.yaml
- Started UTC: 2026-09-22T23:45:06Z
- Finished UTC: 2026-09-22T23:45:06Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1647773` |
| Label | `Efibula americana` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1647770` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/efibula_americana.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/efibula_americana.yaml data/taxa/eukaryota/eimeria_maxima.yaml data/taxa/eukaryota/eimeria_tenella.yaml data/taxa/eukaryota/eimeria_tenella_strain_houghton.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, five NCBI type-material rows, no exact native GOLD, StrainInfo, NCBI merged-ID, or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1647773`, `label: Efibula americana`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1647770`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:430745`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Efibula` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:14139`, which records one retained direct organism for `NCBITaxon:1647773`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1647773`. The YAML carries the one related synonym filed for this NCBI row; NCBI supplies no exact or broad synonyms.

The five NCBI type-material rows preserve `CFMR FP-102165`, hyphen/colon-normalized spellings, and `FP-102165` as holotype designations for `Efibula americana`.

The retained GOLD aggregate row supports the generated `GOLD` source attestation. The current local native GOLD organism, project, and analysis catalogs have no exact rows for `NCBITaxon:1647773`, so the generated attestation is supported by the aggregate input rather than by a row in `data/gold/organisms.jsonl.gz`.

There are no exact rows for this taxon in the StrainInfo side inventory, NCBI merged-ID table, BacDive, or the maintained final strain tables. `strain_count: 0` is therefore consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/efibula_americana.yaml` plus `just validate-strict data/taxa/eukaryota/efibula_americana.yaml`.

## Additional Notes

The retained GOLD aggregate reports one organism assertion for this NCBI taxon, while the current local native GOLD catalog contains no exact organism rows. The generated attestation is still supported by the maintained aggregate input that seeded the YAML.
