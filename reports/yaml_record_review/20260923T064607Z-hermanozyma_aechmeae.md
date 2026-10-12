# YAML Record Review: Hermanozyma aechmeae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hermanozyma_aechmeae.yaml
- Started UTC: 2026-09-23T06:46:07Z
- Finished UTC: 2026-09-23T06:46:07Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:535747` |
| Label | `Hermanozyma aechmeae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:3312683` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hermanozyma_aechmeae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hermanozyma_aechmeae.yaml data/taxa/eukaryota/hermanssonia_centrifuga.yaml data/taxa/eukaryota/herpomyces_periplanetae.yaml data/taxa/eukaryota/hesseltinella_vesiculosa.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with one linked native GOLD project and no linked native analyses, seven exact NCBI type-material rows, no side NCBI merged-ID rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:535747`, `label: Hermanozyma aechmeae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3312683`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:123229`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hermanozyma`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:38177`, which records one retained direct organism for `NCBITaxon:535747`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism and one linked project.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:535747`. `Candida aechmeae` is present in `data/raw/ncbitaxon_taxa.tsv:123229` as an exact synonym, and `Candida aechmeae Landell & Valente, 2010`, `Candida sp. BI153`, and `Hermanozyma aechmeae (Landell & P. Valente) Q.M. Wang, Yurkov, Boekhout & F.Y. Bai, 2024` are present in the source row as related synonyms.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have an exact `Go0705540` organism for `NRRL Y-48456`, a linked `Gp0831583` project in `data/gold/projects.jsonl.gz:610138`, and no native analysis linked by the exact project ID.

NCBI carries seven exact type-material aliases for `Candida aechmeae` at `data/raw/ncbi_type_material.tsv:230368` through `data/raw/ncbi_type_material.tsv:230374`: `BI153`, `BI:153`, `CBS 10831`, `CBS:10831`, `NRRL Y-48456`, `NRRL:Y-48456`, and `NRRL:Y:48456`. These aliases do not contradict the generated `strain_count: 0` because no exact BacDive, StrainInfo, or maintained final strain rows are linked to `NCBITaxon:535747`.

No side NCBI merged-ID row, exact BacDive row, exact StrainInfo row, or maintained final strain-table row is present.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `12`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hermanozyma_aechmeae.yaml` plus `just validate-strict data/taxa/eukaryota/hermanozyma_aechmeae.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hermanozyma_aechmeae` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism and project rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
