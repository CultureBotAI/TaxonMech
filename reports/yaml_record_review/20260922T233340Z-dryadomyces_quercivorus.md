# YAML Record Review: Dryadomyces quercivorus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/dryadomyces_quercivorus.yaml
- Started UTC: 2026-09-22T23:33:40Z
- Finished UTC: 2026-09-22T23:33:40Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:637633` |
| Label | `Dryadomyces quercivorus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:308908` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/dryadomyces_quercivorus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/drepanopeziza_brunnea_f_sp_monogermtubi.yaml data/taxa/eukaryota/drepanopeziza_brunnea_f_sp_multigermtubi_mb_m1.yaml data/taxa/eukaryota/dryadomyces_quercivorus.yaml data/taxa/eukaryota/dryadomyces_quercus_mongolicae.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, two exact native GOLD organism/project/analysis rows, one exact StrainInfo direct record carrying one matching deposit designation, no NCBI type-material, NCBI merged-ID, or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:637633`, `label: Dryadomyces quercivorus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:308908`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:146723`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Dryadomyces` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:40156`, which records two retained direct organisms for `NCBITaxon:637633`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:637633`. The YAML carries the one exact synonym and both related synonyms filed for this NCBI row; NCBI supplies no broad synonyms.

The native GOLD catalogs contain two exact organism rows: `Go0384417` for `Raffaelea quercivora JCM 11526` and `Go0448967` for `Raffaelea quercivora CBS 122982`. These join to projects `Gp0235513` and `Gp0313357`, respectively, and both projects have matching analysis rows.

The exact StrainInfo side inventory has one direct record and one matching `JCM 11526` deposit designation for `NCBITaxon:637633`, but that record is not present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact NCBI type-material, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/dryadomyces_quercivorus.yaml` plus `just validate-strict data/taxa/eukaryota/dryadomyces_quercivorus.yaml`.

## Additional Notes

The two current native GOLD organism rows match the retained aggregate count. Both use the `Raffaelea quercivora` spelling that NCBI records as an exact synonym of the current `Dryadomyces quercivorus` name.
