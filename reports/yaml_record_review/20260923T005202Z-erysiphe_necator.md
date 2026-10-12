# YAML Record Review: Erysiphe necator

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/erysiphe_necator.yaml
- Started UTC: 2026-09-23T00:52:02Z
- Finished UTC: 2026-09-23T00:52:02Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:52586` |
| Label | `Erysiphe necator` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5121` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/erysiphe_necator.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/eremothecium_gossypii.yaml data/taxa/eukaryota/eremothecium_sinecaudum.yaml data/taxa/eukaryota/erysiphe_necator.yaml data/taxa/eukaryota/erysiphe_neolycopersici.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with six organism assertions, six exact native GOLD organism/project/analysis rows, no NCBI type-material rows, no NCBI merged-ID rows, no exact StrainInfo or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:52586`, `label: Erysiphe necator`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5121`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:6595`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Erysiphe` genus; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37904`, which records six retained direct organisms for `NCBITaxon:52586`; this agrees with `source_attestations[1].assertion_count: 6` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:52586`. The YAML preserves NCBI's exact synonym `Uncinula necator` plus the related synonyms `Erysiphe necator Schwein., 1832`, `Uncinula necator (Schwein.) Burrill, 1892`, and `grape powdery mildew`; NCBI supplies no broad synonyms and no old-ID side rows.

The native GOLD catalogs contain six exact organism rows for `Erysiphe necator`, with six matching projects and six native GOLD analysis rows. Five entries cover strains `branching`, `e1-101`, `lodi`, `ranch-9`, and `c` through `Go0114045` to `Go0114049`; the sixth covers `EnFRAME01` through `Go0677429`, project `Gp0779245`, and its linked native GOLD analysis.

No exact StrainInfo, BacDive, NCBI type-material, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, three NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/erysiphe_necator.yaml` plus `just validate-strict data/taxa/eukaryota/erysiphe_necator.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the six current native GOLD organism rows. Native GOLD analysis rows link through `AP PROJECT GOLD IDS`; this record has no StrainInfo side rows in the local exact-target inventory.
