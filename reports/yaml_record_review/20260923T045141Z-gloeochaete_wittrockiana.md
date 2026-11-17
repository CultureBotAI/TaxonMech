# YAML Record Review: Gloeochaete wittrockiana

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/gloeochaete_wittrockiana.yaml
- Started UTC: 2026-09-23T04:51:41Z
- Finished UTC: 2026-09-23T04:51:41Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:38269` |
| Label | `Gloeochaete wittrockiana` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:38268` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/gloeochaete_wittrockiana.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/globomyces_pollinis_pini.yaml data/taxa/eukaryota/gloeochaete_wittrockiana.yaml data/taxa/eukaryota/gloeomyces_thailandicus.yaml data/taxa/eukaryota/gloeopeniophorella_convolvens.yaml` | Passed; the strict batch exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism, no linked native GOLD projects or analyses, one exact StrainInfo row with one exact StrainInfo deposit row, no exact NCBI type-material rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:38269`, `label: Gloeochaete wittrockiana`, `rank: SPECIES`, `parent_taxon: NCBITaxon:38268`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:4342`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Gloeochaete`; the bounded scan checked all seven lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:33936`, which records one retained direct organism for `NCBITaxon:38269`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain exact organism `Go0368680` for strain `SAG 46.84`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:38269`. The sole synonym, `Gloeochaete wittrockiana Lagerheim, 1883`, is present in `data/raw/ncbitaxon_taxa.tsv:4342` as a related synonym and is preserved with `synonym_type: RELATED_SYNONYM`.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have one exact organism for `Gloeochaete wittrockiana SAG 46.84`; that exact organism does not currently have linked native project rows.

The exact StrainInfo row for `SAG 46.84` is present as side inventory only. There are no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; StrainInfo only overlays BacDive-derived local strains, and this taxon has no generated local strain rows.

No side `data/raw/ncbi_merged_ids.tsv` row, exact NCBI type-material row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, one generated NCBI related synonym, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/gloeochaete_wittrockiana.yaml` plus `just validate-strict data/taxa/eukaryota/gloeochaete_wittrockiana.yaml`.

## Additional Notes

No prior exact ignored review report existed for `gloeochaete_wittrockiana` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism row is exact by NCBI taxon ID but is side evidence only and does not create generated child strains without BacDive-derived local strain inventory entries.
