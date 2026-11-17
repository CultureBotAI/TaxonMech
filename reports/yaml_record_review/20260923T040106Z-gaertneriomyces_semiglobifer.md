# YAML Record Review: Gaertneriomyces semiglobifer

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/gaertneriomyces_semiglobifer.yaml
- Started UTC: 2026-09-23T04:01:06Z
- Finished UTC: 2026-09-23T04:01:06Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:109897` |
| Label | `Gaertneriomyces semiglobifer` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:109896` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/gaertneriomyces_semiglobifer.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fuscoporia_sp.yaml data/taxa/eukaryota/gaertneriomyces_semiglobifer.yaml data/taxa/eukaryota/gaeumannomyces_tritici_r3_111a_1.yaml data/taxa/eukaryota/gaillardinia_entomophila.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with two linked native GOLD projects and no native analysis rows, four exact StrainInfo records carrying six exact deposit rows, one NCBI merged-ID side row but no retained retired old IDs, no exact NCBI type-material or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:109897`, `label: Gaertneriomyces semiglobifer`, `rank: SPECIES`, `parent_taxon: NCBITaxon:109896`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:19736`, which carries the same label, parent, rank, code, three exact synonyms, one related synonym, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Gaertneriomyces`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:1838`, which records one retained direct organism for `NCBITaxon:109897`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism, `Go0136948` for strain `Barr 43`, with two linked projects, `Gp0141928` and `Gp0215040`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:109897`. The YAML preserves exact synonyms `Gaertneriomyces semiglobiferum`, `Gaertneriomyces semiglobiferus`, and `Phlyctochytrium semiglobiferum`, and it preserves the related synonym from the NCBI row.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have the exact organism `Gaertneriomyces semiglobifer Barr 43`, with one standard-draft project and one transcriptome project, and no native GOLD analysis currently links to those projects.

The NCBI type-material table has no exact rows for the target. StrainInfo has four exact target records and six exact deposits. These side rows do not create generated local strain entries by themselves.

The side `data/raw/ncbi_merged_ids.tsv` inventory maps old ID `NCBITaxon:693118` into `NCBITaxon:109897`, but no retained row in `data/raw/ncbitaxon_taxa.tsv` carries that old ID with `retired_into`, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, three exact synonyms, one related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/gaertneriomyces_semiglobifer.yaml` plus `just validate-strict data/taxa/eukaryota/gaertneriomyces_semiglobifer.yaml`.

## Additional Notes

No prior exact ignored review report existed for `gaertneriomyces_semiglobifer` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:109897` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.
