# YAML Record Review: Gongronella lacrispora

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/gongronella_lacrispora.yaml
- Started UTC: 2026-09-23T05:08:28Z
- Finished UTC: 2026-09-23T05:08:28Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:703015` |
| Label | `Gongronella lacrispora` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:101104` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/gongronella_lacrispora.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/gonapodya_sp.yaml data/taxa/eukaryota/gongronella_butleri.yaml data/taxa/eukaryota/gongronella_lacrispora.yaml data/taxa/eukaryota/goniomonas_pacifica.yaml` | Passed; the strict batch scanned 4 files with 0 error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with four organism assertions, four exact current native GOLD organisms with no linked native GOLD projects or analyses, eight exact NCBI type-material rows, one direct exact StrainInfo row with seven deposit rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:703015`, `label: Gongronella lacrispora`, `rank: SPECIES`, `parent_taxon: NCBITaxon:101104`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:165021`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Gongronella`; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:41678`, which records four retained direct organisms for `NCBITaxon:703015`; this agrees with `source_attestations[1].assertion_count: 4` and its organism assertion unit. The current native GOLD catalogs also contain four exact organisms for `NRRL 2643`, `DSM 1169`, `CBS 244.62`, and `ATCC 24412`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:703015`. `Gongronella lacrispora Hesselt. & J.J. Ellis, 1961` is present in `data/raw/ncbitaxon_taxa.tsv:165021` as a related synonym.

The retained GOLD aggregate supplies four organism assertions. The current native GOLD catalogs contain exact organism rows `Go0627519`, `Go0627520`, `Go0627521`, and `Go0627522`; no native projects or analyses are linked to those organisms in the local native GOLD inputs.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:258975` through `data/raw/ncbi_type_material.tsv:258982` for `ATCC 24412`, `ATCC:24412`, `CBS 244.62`, `CBS:244.62`, `DSM 1169`, `DSM:1169`, `NRRL 2643`, and `NRRL:2643`. StrainInfo also has one direct exact row with seven deposit rows for this taxon, but neither the NCBI type-material side inventory nor the StrainInfo side inventory is joined into a maintained final strain table for this generated record.

No side `data/raw/ncbi_merged_ids.tsv` row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, the NCBI related synonym for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/gongronella_lacrispora.yaml` plus `just validate-strict data/taxa/eukaryota/gongronella_lacrispora.yaml`.

## Additional Notes

No prior exact ignored review report existed for `gongronella_lacrispora` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
