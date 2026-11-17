# YAML Record Review: Geopyxis carbonaria

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/geopyxis_carbonaria.yaml
- Started UTC: 2026-09-23T04:23:36Z
- Finished UTC: 2026-09-23T04:23:36Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:49969` |
| Label | `Geopyxis carbonaria` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:49968` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/geopyxis_carbonaria.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/geopyxis_carbonaria.yaml data/taxa/eukaryota/geosiphon_pyriformis.yaml data/taxa/eukaryota/geotrichum_armillariae.yaml data/taxa/eukaryota/geotrichum_candidum.yaml` | Passed; the strict batch exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with two linked native GOLD projects and one linked native analysis, no exact NCBI type-material rows, one exact StrainInfo record carrying one exact deposit row, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:49969`, `label: Geopyxis carbonaria`, `rank: SPECIES`, `parent_taxon: NCBITaxon:49968`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:6305`, which carries the same label, parent, rank, code, one exact synonym, three related synonyms, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Geopyxis`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37291`, which records one retained direct organism for `NCBITaxon:49969`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain exact organism `Go0401820` for strain `CBS 144460`, with linked projects `Gp0272390` and `Gp0325670`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:49969`. The YAML preserves the exact synonym `Peziza carbonaria` and three related synonyms from the NCBI row.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have one exact organism for `Geopyxis carbonaria CBS 144460`, two linked projects, and one native analysis for the standard-draft project `Gp0272390`.

StrainInfo has one exact target record carrying one exact deposit, `CBS 655.92`. This side row does not create a generated local strain entry by itself.

No side `data/raw/ncbi_merged_ids.tsv` row, exact NCBI type-material row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, one exact synonym, three related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/geopyxis_carbonaria.yaml` plus `just validate-strict data/taxa/eukaryota/geopyxis_carbonaria.yaml`.

## Additional Notes

No prior exact ignored review report existed for `geopyxis_carbonaria` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:49969` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.
