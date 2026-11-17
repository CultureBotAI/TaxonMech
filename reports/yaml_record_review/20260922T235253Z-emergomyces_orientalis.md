# YAML Record Review: Emergomyces orientalis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/emergomyces_orientalis.yaml
- Started UTC: 2026-09-22T23:52:53Z
- Finished UTC: 2026-09-22T23:52:53Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1972497` |
| Label | `Emergomyces orientalis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1955773` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/emergomyces_orientalis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/elytroderma_deformans.yaml data/taxa/eukaryota/elytroderma_sp.yaml data/taxa/eukaryota/emergomyces_africanus.yaml data/taxa/eukaryota/emergomyces_orientalis.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism/project/analysis chain, seven NCBI type-material rows, two NCBI merged-ID side rows, no retained retired rows, no exact StrainInfo or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1972497`, `label: Emergomyces orientalis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1955773`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:506242`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Emergomyces` genus; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:18215`, which records one retained direct organism for `NCBITaxon:1972497`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1972497`. The YAML carries all three related synonyms filed for this NCBI row: `Emergomyces orientalis P. Wang, Y.C. Xu & H.W. Fan, 2017`, `Emmonsia sp. 5z489`, and `Emmonsia sp. JBS-2016a`; NCBI supplies no exact or broad synonyms.

The seven NCBI type-material rows preserve all designations for `Emergomyces orientalis`: `CBS 124587`, `CBS:124587`, `CGMCC 2.4011`, and `CGMCC:2.4011` as cultures from the holotype, plus `5z489`, `Peng 5Z489`, and `personal:Peng:5Z489` as type material. The native GOLD catalogs contain one exact organism row, `Go0384688` for `Emergomyces orientalis 5z489`, with one matching project, `Gp0235805`, and one matching analysis row linked through that project.

The NCBI merged-ID side inventory maps `NCBITaxon:1809708` and `NCBITaxon:549828` to the current target, but neither is a retained retired row in `data/raw/ncbitaxon_taxa.tsv`, so the absent `replaces` field is consistent with the generated output. No exact StrainInfo, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, three NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/emergomyces_orientalis.yaml` plus `just validate-strict data/taxa/eukaryota/emergomyces_orientalis.yaml`.

## Additional Notes

The NCBI type-material sample was expanded with an exact `NCBITaxon:1972497` lookup in `data/raw/ncbi_type_material.tsv` to account for all seven designations. The two NCBI merged-ID rows remain only side-inventory old IDs; no generated `replaces` value is expected without retained retired source rows.
