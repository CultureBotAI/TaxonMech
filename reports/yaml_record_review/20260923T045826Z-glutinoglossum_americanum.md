# YAML Record Review: Glutinoglossum americanum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/glutinoglossum_americanum.yaml
- Started UTC: 2026-09-23T04:58:26Z
- Finished UTC: 2026-09-23T04:58:26Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1670608` |
| Label | `Glutinoglossum americanum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1390972` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/glutinoglossum_americanum.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/glomus_cerebriforme.yaml data/taxa/eukaryota/glonium_stellatum.yaml data/taxa/eukaryota/glucitozyma_multigemmis.yaml data/taxa/eukaryota/glutinoglossum_americanum.yaml` | Passed; the strict batch scanned 4 files with 0 error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with one linked native GOLD project and one linked native analysis, four exact NCBI type-material rows, no exact StrainInfo rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1670608`, `label: Glutinoglossum americanum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1390972`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:435307`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Glutinoglossum`; the bounded scan checked all 14 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:14364`, which records one retained direct organism for `NCBITaxon:1670608`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain exact organism `Go0631279` for strain `GBOQ0MN5Z8`, linked project `Gp0644623`, and one native analysis whose `AP PROJECT GOLD IDS` include `Gp0644623`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1670608`. The sole synonym, `Glutinoglossum americanum Hustad & A.N. Mill., 2015`, is present in `data/raw/ncbitaxon_taxa.tsv:435307` as a related synonym and is preserved with `synonym_type: RELATED_SYNONYM`.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have one exact organism for `Glutinoglossum americanum GBOQ0MN5Z8`, one linked project, and one native analysis linked by `AP PROJECT GOLD IDS`.

NCBI type-material rows list `ILLS 67352` and `ANM 2231` plus colonized variants under `NCBITaxon:1670608`.

No side `data/raw/ncbi_merged_ids.tsv` row, exact StrainInfo row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, one generated NCBI related synonym, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/glutinoglossum_americanum.yaml` plus `just validate-strict data/taxa/eukaryota/glutinoglossum_americanum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `glutinoglossum_americanum` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
