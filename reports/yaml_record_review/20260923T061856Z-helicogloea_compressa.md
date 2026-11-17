# YAML Record Review: Helicogloea compressa

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/helicogloea_compressa.yaml
- Started UTC: 2026-09-23T06:18:56Z
- Finished UTC: 2026-09-23T06:18:56Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2184188` |
| Label | `Helicogloea compressa` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:48855` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/helicogloea_compressa.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/helicodendron_triglitziense.yaml data/taxa/eukaryota/helicogloea_compressa.yaml data/taxa/eukaryota/helicogloea_dryina.yaml data/taxa/eukaryota/helicostylum_elegans.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with two linked native GOLD projects and no linked native analyses, no exact NCBI type-material rows, two side NCBI merged-ID rows, one direct exact StrainInfo row with one deposit row, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2184188`, `label: Helicogloea compressa`, `rank: SPECIES`, `parent_taxon: NCBITaxon:48855`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:521139`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Helicogloea`; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:20816`, which records one retained direct organism for `NCBITaxon:2184188`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism and two linked projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2184188`. `Dendrodochium compressum`, `Leucogloea compressa`, and `Pleurocolla compressa` are present in `data/raw/ncbitaxon_taxa.tsv:521139` as exact synonyms, and all five generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have an exact `Go0632566` organism for `VC 1915`, linked `Gp0649140` and `Gp0649141` projects in `data/gold/projects.jsonl.gz:484183` through `data/gold/projects.jsonl.gz:484184`, and no native analysis linked by the exact project IDs.

StrainInfo has one direct exact row with one deposit row for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

`data/raw/ncbi_merged_ids.tsv` has two side-inventory old IDs, `NCBITaxon:2321080` and `NCBITaxon:256423`, that merge into `NCBITaxon:2184188`; neither appears as a retained retired row in `data/raw/ncbitaxon_taxa.tsv`, so the generated record correctly has no `replaces` entries.

No NCBI type-material row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/helicogloea_compressa.yaml` plus `just validate-strict data/taxa/eukaryota/helicogloea_compressa.yaml`.

## Additional Notes

No prior exact ignored review report existed for `helicogloea_compressa` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism and project rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
