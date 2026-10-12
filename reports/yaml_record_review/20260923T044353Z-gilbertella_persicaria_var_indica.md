# YAML Record Review: Gilbertella persicaria var. indica

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/gilbertella_persicaria_var_indica.yaml
- Started UTC: 2026-09-23T04:43:53Z
- Finished UTC: 2026-09-23T04:43:53Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:325366` |
| Label | `Gilbertella persicaria var. indica` |
| Rank | `VARIETAS` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:101096` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/gilbertella_persicaria_var_indica.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/gigaspora_margarita.yaml data/taxa/eukaryota/gigaspora_rosea.yaml data/taxa/eukaryota/gilbertella_persicaria.yaml data/taxa/eukaryota/gilbertella_persicaria_var_indica.yaml` | Passed; the strict batch scanned 4 files with 0 error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, no exact current native GOLD organisms, three exact StrainInfo rows, three exact StrainInfo deposit rows, no exact NCBI type-material rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:325366`, `label: Gilbertella persicaria var. indica`, `rank: VARIETAS`, `parent_taxon: NCBITaxon:101096`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:66492`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Gilbertella persicaria`; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy varietas ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:32143`, which records one retained direct organism for `NCBITaxon:325366`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:325366`. The NCBI row has no exact, related, or broad synonyms, and the YAML correctly omits a `synonyms` block.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs do not contain an exact organism, project, or analysis row keyed to `NCBITaxon:325366`, so the direct GOLD support here is limited to the retained generated aggregate.

Exact StrainInfo rows are present as side inventory rows for `CBS 349.64`, `CBS 442.64`, and `IMI 102701`, but there are no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; StrainInfo only overlays BacDive-derived local strains, and this taxon has no generated local strain rows.

No side `data/raw/ncbi_merged_ids.tsv` row, exact NCBI type-material row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded varietas identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, no spurious synonym block, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/gilbertella_persicaria_var_indica.yaml` plus `just validate-strict data/taxa/eukaryota/gilbertella_persicaria_var_indica.yaml`.

## Additional Notes

No prior exact ignored review report existed for `gilbertella_persicaria_var_indica` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
