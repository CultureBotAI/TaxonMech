# YAML Record Review: Halamphora coffeiformis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/halamphora_coffeiformis.yaml
- Started UTC: 2026-09-23T05:35:13Z
- Finished UTC: 2026-09-23T05:35:13Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1487565` |
| Label | `Halamphora coffeiformis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1242273` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/halamphora_coffeiformis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hagleromyces_aurorensis.yaml data/taxa/eukaryota/haglerozyma_chiarellii.yaml data/taxa/eukaryota/halamphora_coffeiformis.yaml data/taxa/eukaryota/halenospora_varia.yaml` | Passed; the strict batch reported zero ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, no exact current native GOLD organism rows, no exact NCBI type-material rows, no side NCBI merged-ID rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1487565`, `label: Halamphora coffeiformis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1242273`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:380553`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Halamphora`; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:11529`, which records one retained direct organism for `NCBITaxon:1487565`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1487565`. `Frustulia coffeiformis` and `Halamphora coffeaeformis` are present in `data/raw/ncbitaxon_taxa.tsv:380553` as exact synonyms, and all three generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs in this checkout have no exact organism row, linked project, or linked analysis for `NCBITaxon:1487565`; the retained aggregate row is still sufficient for the generated `GOLD` source attestation.

No exact NCBI type-material row, side NCBI merged-ID row, exact StrainInfo row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/halamphora_coffeiformis.yaml` plus `just validate-strict data/taxa/eukaryota/halamphora_coffeiformis.yaml`.

## Additional Notes

No prior exact ignored review report existed for `halamphora_coffeiformis` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
