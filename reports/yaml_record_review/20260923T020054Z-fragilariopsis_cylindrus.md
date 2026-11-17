# YAML Record Review: Fragilariopsis cylindrus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fragilariopsis_cylindrus.yaml
- Started UTC: 2026-09-23T02:00:54Z
- Finished UTC: 2026-09-23T02:00:54Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:186039` |
| Label | `Fragilariopsis cylindrus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:186035` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fragilariopsis_cylindrus.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/fragilariforma_virescens.yaml data/taxa/eukaryota/fragilariopsis_cylindrus.yaml data/taxa/eukaryota/fragilariopsis_kerguelensis.yaml data/taxa/eukaryota/fragosphaeria_purpurea.yaml` | Passed; the strict batch scanned 4 files and exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, one current native GOLD organism row with two linked projects, two native GOLD analysis rows linked by project ID, four direct StrainInfo rows, four StrainInfo deposit rows, no NCBI type-material rows, no NCBI merged-ID side rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:186039`, `label: Fragilariopsis cylindrus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:186035`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:36955`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fragilariopsis` genus; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:16613`, which records two retained direct organisms for `NCBITaxon:186039`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:186039`. The YAML preserves NCBI's exact synonyms `Fragilaria cylindrus` and `Nitzschia cylindrus` plus two related synonyms.

No NCBI merged-ID side rows point to `NCBITaxon:186039`, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies two organism assertions; the current native GOLD catalogs still contain one exact organism row, two linked project rows, and two linked analysis rows for the target NCBI taxon.

StrainInfo contains exact side evidence for the target in both the direct SI-ID view and the deposit view. Those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive, NCBI type-material, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI exact synonyms, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fragilariopsis_cylindrus.yaml` plus `just validate-strict data/taxa/eukaryota/fragilariopsis_cylindrus.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
