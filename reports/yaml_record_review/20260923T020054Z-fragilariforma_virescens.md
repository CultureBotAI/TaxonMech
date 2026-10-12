# YAML Record Review: Fragilariforma virescens

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fragilariforma_virescens.yaml
- Started UTC: 2026-09-23T02:00:54Z
- Finished UTC: 2026-09-23T02:00:54Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:216617` |
| Label | `Fragilariforma virescens` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:216616` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fragilariforma_virescens.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fragilariforma_virescens.yaml data/taxa/eukaryota/fragilariopsis_cylindrus.yaml data/taxa/eukaryota/fragilariopsis_kerguelensis.yaml data/taxa/eukaryota/fragosphaeria_purpurea.yaml` | Passed; the strict batch scanned 4 files and exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, no current native GOLD exact rows, one direct StrainInfo row, one StrainInfo deposit row, no NCBI type-material rows, no NCBI merged-ID side rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:216617`, `label: Fragilariforma virescens`, `rank: SPECIES`, `parent_taxon: NCBITaxon:216616`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:42606`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fragilariforma` genus; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:20656`, which records one retained direct organism for `NCBITaxon:216617`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:216617`. The YAML preserves NCBI's exact synonym `Fragilaria virescens` plus the related synonyms `Fragilaria virescens Ralfs, 1843` and `Fragilariforma virescens (Ralfs) D.M.Williams & Round, 1988`.

No NCBI merged-ID side rows point to `NCBITaxon:216617`, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies one organism assertion; the current native GOLD catalogs no longer contain an exact organism, project, or analysis row for the target NCBI taxon, but the retained aggregate is the maintained source for the generated `GOLD` count.

StrainInfo contains one exact side row in both the direct SI-ID view and the deposit view. That side row does not produce a BacDive-derived local strain child for this taxon. No exact BacDive, NCBI type-material, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fragilariforma_virescens.yaml` plus `just validate-strict data/taxa/eukaryota/fragilariforma_virescens.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; current native GOLD organism, project, and analysis rows are side evidence only and can be absent even when the retained aggregate used to generate `source_attestations` still has a count.
