# YAML Record Review: Fusarium fredkrugeri

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_fredkrugeri.yaml
- Started UTC: 2026-09-23T02:40:41Z
- Finished UTC: 2026-09-23T02:40:41Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2267552` |
| Label | `Fusarium fredkrugeri` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:171627` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_fredkrugeri.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_floridanum.yaml data/taxa/eukaryota/fusarium_foetens.yaml data/taxa/eukaryota/fusarium_fredkrugeri.yaml data/taxa/eukaryota/fusarium_fujikuroi.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, no current native GOLD organism, project, or analysis rows, no NCBI merged-ID side rows, no exact StrainInfo rows, six NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2267552`, `label: Fusarium fredkrugeri`, `rank: SPECIES`, `parent_taxon: NCBITaxon:171627`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:522379`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium fujikuroi species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:21316`, which records one retained direct organism for `NCBITaxon:2267552`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2267552`. The YAML preserves the one related author-qualified NCBI synonym, `Fusarium fredkrugeri Sand.-Den., Crous & W.J. Swart, 2018`.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD organism, project, and analysis catalogs no longer contain an exact row for `NCBITaxon:2267552`; generated GOLD provenance is tied to the retained aggregate table, so that absence does not contradict the YAML assertion count.

No side-inventory NCBI old IDs merge into `NCBITaxon:2267552`, so the YAML correctly has no generated `replaces` entry. NCBI has six holotype or culture-from-holotype aliases for the target in `typematerial.dmp`: `CBS 144209`, `CBS:144209`, `CPC 33747`, `CPC:33747`, `CBS H-23496`, and `CBS:H:23496`. No exact BacDive, StrainInfo, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; no exact current native GOLD organism, project, or analysis rows; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_fredkrugeri.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_fredkrugeri.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_fredkrugeri` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
