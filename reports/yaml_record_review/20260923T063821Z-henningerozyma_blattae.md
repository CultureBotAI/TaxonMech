# YAML Record Review: Henningerozyma blattae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/henningerozyma_blattae.yaml
- Started UTC: 2026-09-23T06:38:21Z
- Finished UTC: 2026-09-23T06:38:21Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1071379` |
| Label | `Henningerozyma blattae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:3163253` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/henningerozyma_blattae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hemisphaericaspora_xylofermentans.yaml data/taxa/eukaryota/henningerozyma_blattae.yaml data/taxa/eukaryota/henningerozyma_blattae_cbs_6284.yaml data/taxa/eukaryota/hepatocystis_sp_ex_piliocolobus_tephrosceles.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one direct organism assertion, one exact current native GOLD organism with one linked native GOLD project and no linked native analyses, 18 exact NCBI type-material rows, one side NCBI merged-ID row, three direct exact StrainInfo rows with 22 deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1071379`, `label: Henningerozyma blattae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3163253`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:229355`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Henningerozyma`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:1218`, which records one retained direct organism for `NCBITaxon:1071379`; this agrees with `source_attestations[1].assertion_count: 1` and its note that descendant taxa are not gathered. The current native GOLD catalogs also contain one exact direct organism and one linked project.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1071379`. `Kluyveromyces blattae` and `Tetrapisispora blattae` are present in `data/raw/ncbitaxon_taxa.tsv:229355` as exact synonyms, and all three generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies one direct organism assertion. The child strain `Henningerozyma blattae CBS 6284` is recorded separately under `NCBITaxon:1071380`, so it is correctly excluded from this species-level direct count. The current native GOLD catalogs have an exact `Go0705200` organism for `NRRL Y-10934`, a linked `Gp0831224` project in `data/gold/projects.jsonl.gz:609779`, and no native analysis linked by the exact project ID.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:4504` through `data/raw/ncbi_type_material.tsv:4521` as 18 spellings for `ATCC 34711`, `BCRC 22016`, `CBS 6284`, `CCRC 22016`, `DBVPG 6231`, `DSM 70876`, `IFO 10599`, `NRRL Y-10934`, and `UCD 77-7`.

StrainInfo has three direct exact rows with 22 deposit rows for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

`data/raw/ncbi_merged_ids.tsv` has one side-inventory old ID, `NCBITaxon:51659`, that merges into `NCBITaxon:1071379`; it does not appear as a retained retired row in `data/raw/ncbitaxon_taxa.tsv`, so the generated record correctly has no `replaces` entries.

No exact BacDive row or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/henningerozyma_blattae.yaml` plus `just validate-strict data/taxa/eukaryota/henningerozyma_blattae.yaml`.

## Additional Notes

No prior exact ignored review report existed for `henningerozyma_blattae` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism and project rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
