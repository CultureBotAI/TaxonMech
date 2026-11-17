# YAML Record Review: Geotrichum reessii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/geotrichum_reessii.yaml
- Started UTC: 2026-09-23T04:34:41Z
- Finished UTC: 2026-09-23T04:34:41Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:43985` |
| Label | `Geotrichum reessii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:43987` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/geotrichum_reessii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/geotrichum_macrosporum.yaml data/taxa/eukaryota/geotrichum_phurueaensis.yaml data/taxa/eukaryota/geotrichum_reessii.yaml data/taxa/eukaryota/geotrichum_restrictum.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, two exact current native GOLD organisms with two linked native GOLD projects and one linked native analysis, nine exact NCBI type-material rows, 10 exact StrainInfo records carrying 24 exact deposit rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:43985`, `label: Geotrichum reessii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:43987`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:5294`, which carries the same label, parent, rank, code, three exact synonyms, four related synonyms, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Geotrichum`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:35537`, which records two retained direct organisms for `NCBITaxon:43985`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs also contain exact organisms `Go0590803` and `Go0705299`, with linked projects `Gp0604748` and `Gp0831335`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:43985`. The YAML preserves exact synonyms `Dipodascus reessii`, `Endomyces reessii`, and `Galactomyces reessii`, and it preserves all four related synonyms from the NCBI row.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have one exact organism for `Galactomyces reessii LMA-1148`, one exact organism for `Geotrichum reessii NRRL Y-17566`, two linked projects, and one native analysis named `Galactomyces reessii LMA-1148` whose `AP PROJECT GOLD IDS` include `Gp0604748`.

The NCBI type-material table has nine exact rows for the target under `Endomyces reessii`: culture-from-holotype rows `NRRL Y-17566`, `NRRL Y-17566T`, `NRRL-Y-17566`, `NRRL:Y-17566`, and `NRRLY-17566`, plus type-material rows `CBS 179.60`, `CBS:179.60`, `MUCL 14512`, and `MUCL:14512`. StrainInfo has 10 exact target records and 24 exact deposits. These side rows do not create generated local strain entries by themselves.

No side `data/raw/ncbi_merged_ids.tsv` row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, three exact synonyms, four related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/geotrichum_reessii.yaml` plus `just validate-strict data/taxa/eukaryota/geotrichum_reessii.yaml`.

## Additional Notes

No prior exact ignored review report existed for `geotrichum_reessii` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:43985` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.
