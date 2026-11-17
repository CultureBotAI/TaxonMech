# YAML Record Review: Gotozyma montana

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/gotozyma_montana.yaml
- Started UTC: 2026-09-23T05:11:26Z
- Finished UTC: 2026-09-23T05:11:26Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:49329` |
| Label | `Gotozyma montana` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:3712550` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/gotozyma_montana.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/gonyaulax_spinifera.yaml data/taxa/eukaryota/gorgonomyces_haynaldii.yaml data/taxa/eukaryota/gotozyma_montana.yaml data/taxa/eukaryota/gotozyma_siamensis.yaml` | Passed; the strict batch scanned 4 files with 0 error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with one linked native GOLD project and one linked native analysis, 15 exact NCBI type-material rows, two direct exact StrainInfo rows with 12 deposit rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:49329`, `label: Gotozyma montana`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3712550`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:6279`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Gotozyma`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37172`, which records one retained direct organism for `NCBITaxon:49329`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain exact organism `Go0517092` for strain `NRRL Y-17326`, linked project `Gp0441130`, and one native analysis linked by `AP PROJECT GOLD IDS`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:49329`. `Candida montana` is present in `data/raw/ncbitaxon_taxa.tsv:6279` as an exact synonym, and both generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have one exact organism for `Barnettozyma montana NRRL Y-17326`, one linked project, and one native analysis linked to that project.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:223537` through `data/raw/ncbi_type_material.tsv:223551` for `ATCC 52819`, `ATCC:52819`, `IFO 10104`, `IFO:10104`, `JCM 2323`, `JCM:2323`, `NRRL Y-17326`, `NRRL:Y-17326`, `NRRL:Y:17326`, `RIFY 4865`, `RIFY:4865`, and four `CBS 8057` spellings. StrainInfo also has two direct exact rows with 12 deposit rows for this taxon, but neither the NCBI type-material side inventory nor the StrainInfo side inventory is joined into a maintained final strain table for this generated record.

No side `data/raw/ncbi_merged_ids.tsv` row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/gotozyma_montana.yaml` plus `just validate-strict data/taxa/eukaryota/gotozyma_montana.yaml`.

## Additional Notes

No prior exact ignored review report existed for `gotozyma_montana` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
