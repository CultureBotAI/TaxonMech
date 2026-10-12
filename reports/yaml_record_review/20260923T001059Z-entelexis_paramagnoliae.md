# YAML Record Review: Entelexis paramagnoliae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/entelexis_paramagnoliae.yaml
- Started UTC: 2026-09-23T00:10:59Z
- Finished UTC: 2026-09-23T00:10:59Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5490` |
| Label | `Entelexis paramagnoliae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:3712600` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/entelexis_paramagnoliae.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/entelexis_apis.yaml data/taxa/eukaryota/entelexis_geochares.yaml data/taxa/eukaryota/entelexis_gropengiesseri.yaml data/taxa/eukaryota/entelexis_paramagnoliae.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with 10 organism assertions, 10 exact native GOLD organisms, one matching native GOLD project, no native GOLD analyses, 23 NCBI type-material rows, 35 exact StrainInfo direct records carrying 100 matching deposit designations, no NCBI merged-ID or exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5490`, `label: Entelexis paramagnoliae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3712600`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2436`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Entelexis` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:38508`, which records 10 retained direct organisms for `NCBITaxon:5490`; this agrees with `source_attestations[1].assertion_count: 10` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5490`. The YAML preserves NCBI's exact synonyms `Candida magnoliae`, `Starmerella magnoliae`, and `Torulopsis magnoliae`, plus all four related synonyms filed for this row; NCBI supplies no broad synonyms or old-ID side rows.

The 23 NCBI type-material rows preserve culture-from-holotype aliases for `ATCC 56463`, `CCRC 21703`, `IFO 0705`, `JCM 1446`, `NCYC 2620`, `NRRL Y-2024`, `PYCC 2903`, and `VKM Y-1685` under `Torulopsis magnoliae`, plus holotype aliases for `CBS 166`. The native GOLD catalogs contain 10 exact organism rows, all still named `Candida magnoliae`, and one matching project, `Gp0831408`, for the `NRRL Y-2024` organism row.

The exact StrainInfo side inventory has 35 direct records carrying 100 matching deposit designations, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, three NCBI exact synonyms, four NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/entelexis_paramagnoliae.yaml` plus `just validate-strict data/taxa/eukaryota/entelexis_paramagnoliae.yaml`.

## Additional Notes

The NCBI type-material sample was expanded with an exact `NCBITaxon:5490` lookup in `data/raw/ncbi_type_material.tsv` to account for all 23 designations. The native GOLD organism rows were expanded with an exact `NCBITaxon:5490` lookup in `data/gold/organisms.jsonl.gz` to account for all 10 rows beyond the bounded sample.
