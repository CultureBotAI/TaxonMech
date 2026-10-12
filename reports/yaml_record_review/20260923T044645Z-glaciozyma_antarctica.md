# YAML Record Review: Glaciozyma antarctica

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/glaciozyma_antarctica.yaml
- Started UTC: 2026-09-23T04:46:45Z
- Finished UTC: 2026-09-23T04:46:45Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:105987` |
| Label | `Glaciozyma antarctica` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1074866` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/glaciozyma_antarctica.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/glaciozyma_antarctica.yaml data/taxa/eukaryota/glaciozyma_litoralis.yaml data/taxa/eukaryota/gliomastix_tumulicola.yaml data/taxa/eukaryota/globigerina_bulloides.yaml` | Passed; the strict batch scanned 4 files with 0 error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, no exact current native GOLD organisms, 2 exact NCBI type-material rows, 10 exact StrainInfo rows, 30 exact StrainInfo deposit rows, 10 side NCBI merged-ID rows, no retained retired NCBI rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:105987`, `label: Glaciozyma antarctica`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1074866`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:19031`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Glaciozyma`; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:1086`, which records one retained direct organism for `NCBITaxon:105987`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:105987`. `Leucosporidium antarcticum` is present in `data/raw/ncbitaxon_taxa.tsv:19031` as an exact synonym, and the 12 related synonyms in the YAML are present in the source row as related synonyms.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs do not contain an exact organism, project, or analysis row keyed to `NCBITaxon:105987`, so the direct GOLD support here is limited to the retained generated aggregate.

NCBI type-material rows list `CBS 5942` and `CBS:5942` under `NCBITaxon:105987`. Exact StrainInfo rows are present as side inventory rows, but there are no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; StrainInfo only overlays BacDive-derived local strains, and this taxon has no generated local strain rows.

The side `data/raw/ncbi_merged_ids.tsv` inventory has 10 old IDs merged into `NCBITaxon:105987`, but the retained retired NCBI table contributes no old ID rows for this target. Omitting `replaces` is therefore consistent with the generated source state.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/glaciozyma_antarctica.yaml` plus `just validate-strict data/taxa/eukaryota/glaciozyma_antarctica.yaml`.

## Additional Notes

No prior exact ignored review report existed for `glaciozyma_antarctica` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
