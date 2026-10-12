# YAML Record Review: Fusarium longipes

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_longipes.yaml
- Started UTC: 2026-09-23T02:52:05Z
- Finished UTC: 2026-09-23T02:52:05Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:694270` |
| Label | `Fusarium longipes` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:569360` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_longipes.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_liriodendri.yaml data/taxa/eukaryota/fusarium_longipes.yaml data/taxa/eukaryota/fusarium_luffae.yaml data/taxa/eukaryota/fusarium_mangiferae.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, two current native GOLD organism rows with two linked projects, two native GOLD analysis rows linked by project ID, no NCBI merged-ID side rows, 17 exact direct StrainInfo rows, 25 StrainInfo deposit rows, four NCBI neotype-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:694270`, `label: Fusarium longipes`, `rank: SPECIES`, `parent_taxon: NCBITaxon:569360`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:163069`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium sambucinum species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:41476`, which records two retained direct organisms for `NCBITaxon:694270`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs still contain exact organism, project, and analysis rows for strains `NRRL 20695` and `NRRL 13374`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:694270`. The YAML preserves exact synonyms `Fusarium equiseti var. longipes` and `Fusarium scirpi var. longipes`, plus the related author-qualified NCBI synonym `Fusarium longipes Wollenw. & Reinking, 1925`.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs still contain two exact organism rows, one linked project per organism, and one linked analysis per project.

No side-inventory NCBI old IDs merge into `NCBITaxon:694270`, so the YAML correctly has no generated `replaces` entry. StrainInfo contains 17 exact direct rows and 25 exact deposit rows for the target. Those rows do not produce BacDive-derived local strain children for this taxon. NCBI has four culture-from-neotype aliases for the target in `typematerial.dmp`: `CBS 476.77`, `CBS:476.77`, `NRRL 20695`, and `NRRL:20695`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_longipes.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_longipes.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_longipes` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
