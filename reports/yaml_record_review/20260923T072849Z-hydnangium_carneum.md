# YAML Record Review: Hydnangium carneum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hydnangium_carneum.yaml
- Started UTC: 2026-09-23T07:28:49Z
- Finished UTC: 2026-09-23T07:28:49Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:604282` |
| Label | `Hydnangium carneum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:330900` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hydnangium_carneum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hyaloscypha_vitreola.yaml data/taxa/eukaryota/hydnangium_carneum.yaml data/taxa/eukaryota/hydnangium_sp.yaml data/taxa/eukaryota/hydnomerulius_pinastri_md_312.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with six linked native GOLD projects, no native GOLD analyses, no exact NCBI type-material rows, no side NCBI merged-ID rows, one exact direct StrainInfo source record, one exact StrainInfo deposit match, no final StrainInfo overlay rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:604282`, `label: Hydnangium carneum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:330900`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:142465`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hydnangium`; the bounded scan checked all 14 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:39792`, which records one retained direct organism for `NCBITaxon:604282`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism and six linked projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:604282`. `Hydnangium carneum Wallr., 1839` is present in `data/raw/ncbitaxon_taxa.tsv:142465` as a related synonym, and the source row has no exact synonyms to omit.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have an exact `Go0389708` organism for `KIS1` and six linked `KIS1` gene-expression projects, `Gp0251365` through `Gp0251370`; no native GOLD analysis is linked to those projects.

The raw StrainInfo JSONL contains one exact direct source record and one exact deposit match for `NCBITaxon:604282`, but the maintained StrainInfo overlay tables have no exact rows for this taxon. No exact NCBI type-material row, side NCBI merged-ID row, exact BacDive row, or maintained final strain-table row is present.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, the NCBI related synonym for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hydnangium_carneum.yaml` plus `just validate-strict data/taxa/eukaryota/hydnangium_carneum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hydnangium_carneum` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism and project rows are exact by NCBI taxon ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo only overlays BacDive-derived local strains in the generated final tables, so exact raw StrainInfo JSONL rows without exact final `data/straininfo` output rows are not generated as child strain records here.
