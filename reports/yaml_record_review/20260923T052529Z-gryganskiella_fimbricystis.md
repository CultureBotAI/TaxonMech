# YAML Record Review: Gryganskiella fimbricystis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/gryganskiella_fimbricystis.yaml
- Started UTC: 2026-09-23T05:25:29Z
- Finished UTC: 2026-09-23T05:25:29Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:743929` |
| Label | `Gryganskiella fimbricystis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2779860` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/gryganskiella_fimbricystis.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/gryganskiella_fimbricystis.yaml data/taxa/eukaryota/gryganskiella_sp.yaml data/taxa/eukaryota/guillardia_theta_ccmp2712.yaml data/taxa/eukaryota/guyanagaster_necrorhizus.yaml` | Passed; the strict batch scanned 4 files with 0 error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, one exact current native GOLD organism with one linked native GOLD project and no linked native analyses, two exact NCBI type-material rows, one direct exact StrainInfo row with one deposit row, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:743929`, `label: Gryganskiella fimbricystis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2779860`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:171413`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Gryganskiella`; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:42165`, which records two retained direct organisms for `NCBITaxon:743929`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs contain one exact organism, `Go0583266` for strain `FSU 11180`, linked to project `Gp0586855`; those current native rows are side evidence and do not drive the stored retained aggregate assertion count.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:743929`. `Mortierella fimbricystis` is present in `data/raw/ncbitaxon_taxa.tsv:171413` as an exact synonym, and both generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have one exact organism for `Gryganskiella fimbricystis FSU 11180`, one linked project, and no native analyses linked to that project in the local native GOLD inputs.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:261437` and `data/raw/ncbi_type_material.tsv:261438` as `CBS 943.70` and `CBS:943.70`, both marked type material for `Mortierella fimbricystis`. StrainInfo also has one direct exact row with one deposit row for this taxon, but neither the NCBI type-material side inventory nor the StrainInfo side inventory is joined into a maintained final strain table for this generated record.

No side `data/raw/ncbi_merged_ids.tsv` row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/gryganskiella_fimbricystis.yaml` plus `just validate-strict data/taxa/eukaryota/gryganskiella_fimbricystis.yaml`.

## Additional Notes

No prior exact ignored review report existed for `gryganskiella_fimbricystis` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
