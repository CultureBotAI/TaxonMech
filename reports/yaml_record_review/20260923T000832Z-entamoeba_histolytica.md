# YAML Record Review: Entamoeba histolytica

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/entamoeba_histolytica.yaml
- Started UTC: 2026-09-23T00:08:32Z
- Finished UTC: 2026-09-23T00:08:32Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5759` |
| Label | `Entamoeba histolytica` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5758` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/entamoeba_histolytica.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/entamoeba_histolytica.yaml data/taxa/eukaryota/entamoeba_invadens_ip1.yaml data/taxa/eukaryota/entamoeba_moshkovskii.yaml data/taxa/eukaryota/entamoeba_terrapinae.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with five organism assertions, five exact native GOLD organisms, five matching native GOLD projects, two native GOLD analyses, 44 exact StrainInfo direct records carrying 45 matching deposit designations, no NCBI type-material or merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5759`, `label: Entamoeba histolytica`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5758`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2562`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Entamoeba` genus; the bounded scan checked all 9 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:39282`, which records five retained direct organisms for `NCBITaxon:5759`; this agrees with `source_attestations[1].assertion_count: 5` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5759`. The YAML carries the only related synonym filed for this NCBI row, `Entamoeba histolytica Schaudinn, 1903`; NCBI supplies no exact or broad synonyms and no old-ID side rows.

The native GOLD catalogs contain five exact organism rows for `Entamoeba histolytica` strains `KU50`, `KU48`, `HM3:IMSS-A`, `HM3:IMSS-B`, and `DS4-868`. Each exact organism has one matching project, and `HM3:IMSS-A` plus `HM3:IMSS-B` have matching native GOLD analysis rows.

The exact StrainInfo side inventory has 44 direct records carrying 45 matching deposit designations, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/entamoeba_histolytica.yaml` plus `just validate-strict data/taxa/eukaryota/entamoeba_histolytica.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the five current native GOLD organism rows.
