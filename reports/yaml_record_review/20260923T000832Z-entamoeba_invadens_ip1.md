# YAML Record Review: Entamoeba invadens IP1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/entamoeba_invadens_ip1.yaml
- Started UTC: 2026-09-23T00:08:32Z
- Finished UTC: 2026-09-23T00:08:32Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:370355` |
| Label | `Entamoeba invadens IP1` |
| Rank | `STRAIN` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:33085` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/entamoeba_invadens_ip1.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/entamoeba_histolytica.yaml data/taxa/eukaryota/entamoeba_invadens_ip1.yaml data/taxa/eukaryota/entamoeba_moshkovskii.yaml data/taxa/eukaryota/entamoeba_terrapinae.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism/project/analysis chain, no NCBI type-material or merged-ID rows, no exact StrainInfo or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:370355`, `label: Entamoeba invadens IP1`, `rank: STRAIN`, `parent_taxon: NCBITaxon:33085`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:77705`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the parent species, `Entamoeba invadens`; the bounded scan checked all 10 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:33568`, which records one retained direct organism for `NCBITaxon:370355`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:370355`. The YAML preserves NCBI's exact synonym `Entamoeba invadens strain IP1`; NCBI supplies no broad or related synonyms and no old-ID side rows.

The native GOLD catalogs contain one exact organism row, `Go0002382`, with one matching project, `Gp0002382`, and one matching analysis row linked through that project. The native GOLD name fields render the strain as `Entamoeba invadens IP-1`, while the records remain keyed to exact NCBI Taxon ID `370355`.

No exact StrainInfo, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/entamoeba_invadens_ip1.yaml` plus `just validate-strict data/taxa/eukaryota/entamoeba_invadens_ip1.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the one current native GOLD organism row.
