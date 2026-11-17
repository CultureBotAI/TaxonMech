# YAML Record Review: Fusarium illudens

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_illudens.yaml
- Started UTC: 2026-09-23T02:46:53Z
- Finished UTC: 2026-09-23T02:46:53Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:131364` |
| Label | `Fusarium illudens` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:232080` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_illudens.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_heterosporum.yaml data/taxa/eukaryota/fusarium_hostae.yaml data/taxa/eukaryota/fusarium_illudens.yaml data/taxa/eukaryota/fusarium_inflexum.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, no current native GOLD organism, project, or analysis rows, no NCBI merged-ID side rows, 11 exact direct StrainInfo rows, 11 StrainInfo deposit rows, two NCBI neotype rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:131364`, `label: Fusarium illudens`, `rank: SPECIES`, `parent_taxon: NCBITaxon:232080`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:25203`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium solani species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:7693`, which records one retained direct organism for `NCBITaxon:131364`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:131364`. The YAML preserves exact synonyms `Haematonectria illudens`, `Nectria illudens`, and `Neocosmospora illudens`, plus four related NCBI synonyms for author-qualified names.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD organism, project, and analysis catalogs no longer contain an exact row for `NCBITaxon:131364`; generated GOLD provenance is tied to the retained aggregate table, so that absence does not contradict the YAML assertion count.

No side-inventory NCBI old IDs merge into `NCBITaxon:131364`, so the YAML correctly has no generated `replaces` entry. StrainInfo contains 11 exact direct rows and 11 exact deposit rows for the target. Those rows do not produce BacDive-derived local strain children for this taxon. NCBI has two neotype aliases, `PAD S00012` and `PAD:S00012`, under synonym name `Nectria illudens` in `typematerial.dmp`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact current native GOLD organism, project, or analysis rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_illudens.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_illudens.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_illudens` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
