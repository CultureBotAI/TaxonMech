# YAML Record Review: Geotrichum klebahnii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/geotrichum_klebahnii.yaml
- Started UTC: 2026-09-23T04:31:09Z
- Finished UTC: 2026-09-23T04:31:09Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:44065` |
| Label | `Geotrichum klebahnii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:43987` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/geotrichum_klebahnii.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/geotrichum_fermentans.yaml data/taxa/eukaryota/geotrichum_ghanense.yaml data/taxa/eukaryota/geotrichum_histeridarum.yaml data/taxa/eukaryota/geotrichum_klebahnii.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with one linked native GOLD project and no native analysis rows, eight exact NCBI type-material rows, 13 exact StrainInfo records carrying 33 exact deposit rows, three NCBI merged-ID side rows but no retained retired old IDs, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:44065`, `label: Geotrichum klebahnii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:43987`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:5322`, which carries the same label, parent, rank, code, four exact synonyms, five related synonyms, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Geotrichum`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:35567`, which records one retained direct organism for `NCBITaxon:44065`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain exact organism `Go0705300` for strain `NRRL Y-17568`, with linked project `Gp0831336`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:44065`. The YAML preserves exact synonyms `Dipodascus klebahnii`, `Geotrichum penicillatum`, `Oospora klebahnii`, and `Trichosporon penicillatum`, and it preserves all five related synonyms from the NCBI row.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have one exact organism for `Geotrichum klebahnii NRRL Y-17568`, one linked project, and no native GOLD analysis currently links to that project.

The NCBI type-material table has eight exact rows for the target under `Oospora klebahnii`: `CBS 179.30`, `CBS-179.30`, `CBS179.30`, `CBS:179.30`, `NRRL Y-17568`, `NRRL-Y-17568`, `NRRL:Y-17568`, and `NRRLY-17568`. StrainInfo has 13 exact target records and 33 exact deposits. These side rows do not create generated local strain entries by themselves.

The side `data/raw/ncbi_merged_ids.tsv` inventory maps old IDs `NCBITaxon:227032`, `NCBITaxon:29005`, and `NCBITaxon:70818` into `NCBITaxon:44065`, but no retained row in `data/raw/ncbitaxon_taxa.tsv` carries those old IDs with `retired_into`, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, four exact synonyms, five related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/geotrichum_klebahnii.yaml` plus `just validate-strict data/taxa/eukaryota/geotrichum_klebahnii.yaml`.

## Additional Notes

No prior exact ignored review report existed for `geotrichum_klebahnii` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:44065` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.

The NCBI merged-ID hits for `NCBITaxon:227032`, `NCBITaxon:29005`, and `NCBITaxon:70818` are side-inventory old IDs only. Generated `replaces` values come from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`, not directly from every side row in `data/raw/ncbi_merged_ids.tsv`.
