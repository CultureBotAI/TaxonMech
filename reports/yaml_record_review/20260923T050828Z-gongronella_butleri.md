# YAML Record Review: Gongronella butleri

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/gongronella_butleri.yaml
- Started UTC: 2026-09-23T05:08:28Z
- Finished UTC: 2026-09-23T05:08:28Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:101105` |
| Label | `Gongronella butleri` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:101104` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/gongronella_butleri.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/gonapodya_sp.yaml data/taxa/eukaryota/gongronella_butleri.yaml data/taxa/eukaryota/gongronella_lacrispora.yaml data/taxa/eukaryota/goniomonas_pacifica.yaml` | Passed; the strict batch scanned 4 files with 0 error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with 13 organism assertions, 12 exact current native GOLD organisms with 11 linked native GOLD projects and no linked native analyses, no exact NCBI type-material rows, 50 direct exact StrainInfo rows with 69 deposit rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:101105`, `label: Gongronella butleri`, `rank: SPECIES`, `parent_taxon: NCBITaxon:101104`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:17424`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Gongronella`; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:247`, which records 13 retained direct organisms for `NCBITaxon:101105`; this agrees with `source_attestations[1].assertion_count: 13` and its organism assertion unit. The current native GOLD catalogs contain 12 exact organisms for this NCBI taxon, including `Go0141634` for `CBS 227.36`, `Go0452976` for `NRRL A-9973`, `Go0452977` for `NRRL A-9978`, `Go0470846` for `NRRL A-23795`, and `Go0470916` for `NRRL 1340`, with 11 linked native projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:101105`. `Absidia butleri` is present in `data/raw/ncbitaxon_taxa.tsv:17424` as an exact synonym, and `Absidia butleri Lendn., 1926` is present as a related synonym.

The retained GOLD aggregate supplies 13 organism assertions. The current native GOLD catalogs contain 12 exact organism rows and 11 linked projects; the one-row difference between the retained aggregate and the current native side evidence does not affect the generated YAML because the record stores the retained aggregate assertion count.

StrainInfo contains exact side evidence for this taxon, including 50 direct rows and 69 deposit rows, but none of those rows is joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record. No side `data/raw/ncbi_merged_ids.tsv` row, exact NCBI type-material row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/gongronella_butleri.yaml` plus `just validate-strict data/taxa/eukaryota/gongronella_butleri.yaml`.

## Additional Notes

No prior exact ignored review report existed for `gongronella_butleri` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
