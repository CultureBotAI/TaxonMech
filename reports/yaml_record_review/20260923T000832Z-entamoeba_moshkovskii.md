# YAML Record Review: Entamoeba moshkovskii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/entamoeba_moshkovskii.yaml
- Started UTC: 2026-09-23T00:08:32Z
- Finished UTC: 2026-09-23T00:08:32Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:41668` |
| Label | `Entamoeba moshkovskii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5758` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/entamoeba_moshkovskii.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/entamoeba_histolytica.yaml data/taxa/eukaryota/entamoeba_invadens_ip1.yaml data/taxa/eukaryota/entamoeba_moshkovskii.yaml data/taxa/eukaryota/entamoeba_terrapinae.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, one current native GOLD organism/project/analysis chain, 12 exact StrainInfo direct records carrying 12 matching deposit designations, no NCBI type-material or merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:41668`, `label: Entamoeba moshkovskii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5758`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:4856`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Entamoeba` genus; the bounded scan checked all 9 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:34901`, which records two retained direct organisms for `NCBITaxon:41668`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:41668`. The YAML preserves NCBI's exact synonym `Entamoeba moskovskii` and the related synonym `Entamoeba moshkovskii Calaja, 1941`; NCBI supplies no broad synonyms or old-ID side rows.

The native GOLD catalogs contain one current exact organism row, `Go0571946` for `Entamoeba moshkovskii Laredo`, with one matching project, `Gp0546439`, and one matching analysis row linked through that project.

The exact StrainInfo side inventory has 12 direct records carrying 12 matching deposit designations, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, one NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/entamoeba_moshkovskii.yaml` plus `just validate-strict data/taxa/eukaryota/entamoeba_moshkovskii.yaml`.

## Additional Notes

The retained GOLD aggregate count can differ from the current exact native GOLD JSONL rows; in this snapshot, the aggregate retained table carries two organism assertions while the native organism JSONL has one exact row.
