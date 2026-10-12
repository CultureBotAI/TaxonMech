# YAML Record Review: Galdieria daedala

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/galdieria_daedala.yaml
- Started UTC: 2026-09-23T04:04:25Z
- Finished UTC: 2026-09-23T04:04:25Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:178532` |
| Label | `Galdieria daedala` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:83373` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/galdieria_daedala.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/galdieria_daedala.yaml data/taxa/eukaryota/galdieria_partita.yaml data/taxa/eukaryota/galdieria_phlegrea.yaml data/taxa/eukaryota/galdieria_sulphuraria.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, no current exact native GOLD organism, no exact NCBI type-material, StrainInfo, BacDive, or NCBI merged-ID rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:178532`, `label: Galdieria daedala`, `rank: SPECIES`, `parent_taxon: NCBITaxon:83373`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:35827`, which carries the same label, parent, rank, code, one related synonym, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Galdieria`; the bounded scan checked all 8 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:15610`, which records two retained direct organisms for `NCBITaxon:178532`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:178532`. The YAML preserves the related synonym from the NCBI row and correctly has no exact-synonym entries because the exact-synonym field is empty upstream.

The retained GOLD aggregate supplies two organism assertions. The bounded scan did not find a current exact native GOLD organism for `NCBITaxon:178532`, so the retained raw aggregate is the evidence for the generated `GOLD` source attestation.

The NCBI type-material table and StrainInfo inventories have no exact rows for the target.

No side `data/raw/ncbi_merged_ids.tsv` row maps an old ID into `NCBITaxon:178532`, and no retained row in `data/raw/ncbitaxon_taxa.tsv` carries a retired ID for this target, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, one related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/galdieria_daedala.yaml` plus `just validate-strict data/taxa/eukaryota/galdieria_daedala.yaml`.

## Additional Notes

No prior exact ignored review report existed for `galdieria_daedala` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; current native GOLD organism, project, and analysis rows are side evidence only and can differ from the retained aggregate used to seed this generated record.
