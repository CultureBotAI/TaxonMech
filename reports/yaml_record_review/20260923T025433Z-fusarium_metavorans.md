# YAML Record Review: Fusarium metavorans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_metavorans.yaml
- Started UTC: 2026-09-23T02:54:33Z
- Finished UTC: 2026-09-23T02:54:33Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2421284` |
| Label | `Fusarium metavorans` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:232080` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_metavorans.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/fusarium_marasasianum.yaml data/taxa/eukaryota/fusarium_meridionale.yaml data/taxa/eukaryota/fusarium_metavorans.yaml data/taxa/eukaryota/fusarium_miscanthi.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one current native GOLD organism row with one linked project, one native GOLD analysis row linked by project ID, 19 NCBI merged-ID side rows, four exact direct StrainInfo rows, four StrainInfo deposit rows, four NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2421284`, `label: Fusarium metavorans`, `rank: SPECIES`, `parent_taxon: NCBITaxon:232080`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:525432`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium solani species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:22043`, which records one retained direct organism for `NCBITaxon:2421284`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs still contain the exact organism `Go0384166`, linked project `Gp0235255`, and one linked analysis for `FSSC_6`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2421284`. The YAML preserves exact synonyms `Fusarium solani species complex 6`, `Fusarium sp. FSSC 6`, `Fusarium sp. FSSC_6a`, and `Neocosmospora metavorans`, plus 21 related NCBI synonyms covering the author-qualified metavorans names and NRRL/FSSC provisional names.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs still contain the exact organism, project, and analysis chain for `Fusarium metavorans FSSC_6`.

The `data/raw/ncbi_merged_ids.tsv` side inventory has 19 old IDs merged into `NCBITaxon:2421284`: `NCBITaxon:1582859`, `NCBITaxon:1590595`, `NCBITaxon:391679`, `NCBITaxon:451915`, `NCBITaxon:451916`, `NCBITaxon:451917`, `NCBITaxon:451918`, `NCBITaxon:453802`, `NCBITaxon:487285`, `NCBITaxon:503880`, `NCBITaxon:503881`, `NCBITaxon:503884`, `NCBITaxon:503889`, `NCBITaxon:503892`, `NCBITaxon:503908`, `NCBITaxon:569393`, `NCBITaxon:694286`, `NCBITaxon:694289`, and `NCBITaxon:875438`. None are retained in `data/raw/ncbitaxon_taxa.tsv` for generated replacement provenance, so the YAML correctly has no generated `replaces` entry.

StrainInfo contains four exact direct rows and four exact deposit rows for the target. Those rows do not produce BacDive-derived local strain children for this taxon. NCBI has four culture-from-holotype aliases for the target in `typematerial.dmp`: `CBS 135789`, `CBS-135789`, `CBS135789`, and `CBS:135789`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_metavorans.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_metavorans.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_metavorans` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
