# YAML Record Review: Holtermannia corniformis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/holtermannia_corniformis.yaml
- Started UTC: 2026-09-23T07:03:59Z
- Finished UTC: 2026-09-23T07:03:59Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:71782` |
| Label | `Holtermannia corniformis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:71781` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/holtermannia_corniformis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hohenbuehelia_sp.yaml data/taxa/eukaryota/holtermannia_corniformis.yaml data/taxa/eukaryota/holtermanniella_nyarrowii.yaml data/taxa/eukaryota/hondaea_fermentalgiana.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with one linked native GOLD project and one linked native GOLD analysis, two exact NCBI type-material rows, no side NCBI merged-ID rows, 13 direct exact StrainInfo rows with 30 deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:71782`, `label: Holtermannia corniformis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:71781`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:10050`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Holtermannia`; the bounded scan checked all 11 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:41929`, which records one retained direct organism for `NCBITaxon:71782`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism, one linked project, and one linked analysis.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:71782`. `Holtermannia corniformis Kobayasi, 1937` is present in `data/raw/ncbitaxon_taxa.tsv:10050` as a related synonym, and the source row has no exact synonyms to omit.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have an exact `Go0138958` organism for `JCM 1743`, a linked `Gp0144015` project in `data/gold/projects.jsonl.gz:90158`, and one native analysis linked by the exact project ID.

NCBI carries two exact type-material aliases for `Holtermannia corniformis` at `data/raw/ncbi_type_material.tsv:260225` and `data/raw/ncbi_type_material.tsv:260226`: `CBS 6979` and `CBS:6979`. These aliases do not contradict the generated `strain_count: 0` because no exact BacDive, StrainInfo assembly, or maintained final strain rows are linked to `NCBITaxon:71782`.

StrainInfo has 13 direct exact rows with 30 deposit rows for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

No side NCBI merged-ID row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/holtermannia_corniformis.yaml` plus `just validate-strict data/taxa/eukaryota/holtermannia_corniformis.yaml`.

## Additional Notes

No prior exact ignored review report existed for `holtermannia_corniformis` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
