# YAML Record Review: Hemiselmis andersenii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hemiselmis_andersenii.yaml
- Started UTC: 2026-09-23T06:29:06Z
- Finished UTC: 2026-09-23T06:29:06Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:464988` |
| Label | `Hemiselmis andersenii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:77924` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hemiselmis_andersenii.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/hemiselmis_andersenii.yaml data/taxa/eukaryota/hemiselmis_cryptochromatica.yaml data/taxa/eukaryota/hemiselmis_rufescens.yaml data/taxa/eukaryota/hemiselmis_tepida.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with five organism assertions, six exact current native GOLD organisms with two linked native GOLD projects and one linked native analysis, no exact NCBI type-material rows, one side NCBI merged-ID row, no exact BacDive or StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:464988`, `label: Hemiselmis andersenii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:77924`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:104168`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hemiselmis`; the bounded scan checked all seven lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:36304`, which records five retained direct organisms for `NCBITaxon:464988`; this agrees with `source_attestations[1].assertion_count: 5` and its organism assertion unit. The current native GOLD catalogs contain six exact organisms, two linked projects, and one linked analysis.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:464988`. Both generated related synonyms are present in `data/raw/ncbitaxon_taxa.tsv:104168` as related synonyms.

The retained GOLD aggregate supplies five organism assertions. The current native GOLD catalogs have exact organism rows for `CCMP 644 (nucleomorph)`, `Hemiselmis andersenii`, `CCMP 1180`, `CCMP 439`, `CCMP 441`, and `CCMP 644`; linked `Gp0000018` and `Gp0037804` projects; and one native analysis linked by `Gp0000018`.

`data/raw/ncbi_merged_ids.tsv` has one side-inventory old ID, `NCBITaxon:386304`, that merges into `NCBITaxon:464988`; it does not appear as a retained retired row in `data/raw/ncbitaxon_taxa.tsv`, so the generated record correctly has no `replaces` entries.

No NCBI type-material row, exact BacDive row, exact StrainInfo row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive or StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hemiselmis_andersenii.yaml` plus `just validate-strict data/taxa/eukaryota/hemiselmis_andersenii.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hemiselmis_andersenii` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
