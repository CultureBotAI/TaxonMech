# YAML Record Review: Dryadomyces quercus-mongolicae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/dryadomyces_quercus_mongolicae.yaml
- Started UTC: 2026-09-22T23:33:40Z
- Finished UTC: 2026-09-22T23:33:40Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1423150` |
| Label | `Dryadomyces quercus-mongolicae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:308908` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/dryadomyces_quercus_mongolicae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/drepanopeziza_brunnea_f_sp_monogermtubi.yaml data/taxa/eukaryota/drepanopeziza_brunnea_f_sp_multigermtubi_mb_m1.yaml data/taxa/eukaryota/dryadomyces_quercivorus.yaml data/taxa/eukaryota/dryadomyces_quercus_mongolicae.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism/project/analysis row, two NCBI type-material rows, no exact StrainInfo, NCBI merged-ID, or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1423150`, `label: Dryadomyces quercus-mongolicae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:308908`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:354417`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Dryadomyces` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:10120`, which records one retained direct organism for `NCBITaxon:1423150`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1423150`. The YAML carries the one exact synonym and both related synonyms filed for this NCBI row; NCBI supplies no broad synonyms.

The two NCBI type-material rows preserve `KACC 44405` and `KACC:44405` as duplicate spellings of the `Raffaelea quercus-mongolicae` holotype. There are no old-ID side rows in `data/raw/ncbi_merged_ids.tsv` for this taxon.

The native GOLD catalogs contain one exact organism row, `Go0384211` for `Raffaelea quercus-mongolicae KACC44405`, one matching project, `Gp0235301`, and one analysis for that project. These rows agree with the one-organism GOLD aggregate count.

There are no exact rows for this taxon in the StrainInfo side inventory, BacDive, or the maintained final strain tables. `strain_count: 0` is therefore consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/dryadomyces_quercus_mongolicae.yaml` plus `just validate-strict data/taxa/eukaryota/dryadomyces_quercus_mongolicae.yaml`.

## Additional Notes

The native GOLD project and analysis use the `Raffaelea quercus-mongolicae` spelling that NCBI records as an exact synonym of the current `Dryadomyces quercus-mongolicae` name.
