# YAML Record Review: Dictyostelium gargantuum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/dictyostelium_gargantuum.yaml
- Started UTC: 2026-09-22T22:44:03Z
- Finished UTC: 2026-09-22T22:44:03Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:882403` |
| Label | `Dictyostelium gargantuum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5782` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/dictyostelium_gargantuum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/dictyostelium_discoideum.yaml data/taxa/eukaryota/dictyostelium_gargantuum.yaml data/taxa/eukaryota/dictyostelium_purpureum.yaml data/taxa/eukaryota/dictyostelium_rosarium.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained direct organism, one exact native GOLD organism linked to one project and one analysis, no exact NCBI type-material rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:882403`, `label: Dictyostelium gargantuum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5782`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:187644`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Dictyostelium` genus; the bounded scan checked all ten lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:43780`, which records one retained direct organism for `NCBITaxon:882403`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:882403`. The YAML carries the single related synonym filed for this row; NCBI supplies no exact or broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain one exact organism, `Go0573418` for `Dictyostelium gargantuum MYA-3825`; one project, `Gp0548070`, under that organism; and one analysis named `Dictyostelium gargantuum MYA-3825` that links back through `AP PROJECT GOLD IDS`.

No NCBI type-material, StrainInfo, BacDive, or maintained final strain-table rows are present for the exact target, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/dictyostelium_gargantuum.yaml` plus `just validate-strict data/taxa/eukaryota/dictyostelium_gargantuum.yaml`.

## Additional Notes

The bounded scan found no side-inventory `data/raw/ncbi_merged_ids.tsv` mappings into `NCBITaxon:882403`.
