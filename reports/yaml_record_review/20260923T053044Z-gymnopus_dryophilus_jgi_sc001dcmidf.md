# YAML Record Review: Gymnopus dryophilus JGI SC001DCMIDF

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/gymnopus_dryophilus_jgi_sc001dcmidf.yaml
- Started UTC: 2026-09-23T05:30:44Z
- Finished UTC: 2026-09-23T05:30:44Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1379295` |
| Label | `Gymnopus dryophilus JGI SC001DCMIDF` |
| Rank | `STRAIN` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:206318` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/gymnopus_dryophilus_jgi_sc001dcmidf.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/gymnopilus_junonius.yaml data/taxa/eukaryota/gymnopus_androsaceus.yaml data/taxa/eukaryota/gymnopus_dryophilus_jgi_sc001dcmidf.yaml data/taxa/eukaryota/gymnopus_earleae.yaml` | Passed; the strict batch reported zero ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, no exact current native GOLD organism rows, no exact NCBI type-material rows, no side NCBI merged-ID rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1379295`, `label: Gymnopus dryophilus JGI SC001DCMIDF`, `rank: STRAIN`, `parent_taxon: NCBITaxon:206318`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:336758`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through parent species `Gymnopus dryophilus`; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:8908`, which records one retained direct organism for `NCBITaxon:1379295`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1379295`. `data/raw/ncbitaxon_taxa.tsv:336758` has no exact, broad, or related synonyms for this strain, and the generated record correctly has no `synonyms` block.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs in this checkout have no exact organism row, linked project, or linked analysis for `NCBITaxon:1379295`; the retained aggregate row is still sufficient for the generated `GOLD` source attestation.

No exact NCBI type-material row, side NCBI merged-ID row, exact StrainInfo row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded strain identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/gymnopus_dryophilus_jgi_sc001dcmidf.yaml` plus `just validate-strict data/taxa/eukaryota/gymnopus_dryophilus_jgi_sc001dcmidf.yaml`.

## Additional Notes

No prior exact ignored review report existed for `gymnopus_dryophilus_jgi_sc001dcmidf` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
