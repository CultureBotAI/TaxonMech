# YAML Record Review: Fusarium phaseoli

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_phaseoli.yaml
- Started UTC: 2026-09-23T03:30:07Z
- Finished UTC: 2026-09-23T03:30:07Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:120645` |
| Label | `Fusarium phaseoli` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:232080` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_phaseoli.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_papillatum.yaml data/taxa/eukaryota/fusarium_phaseoli.yaml data/taxa/eukaryota/fusarium_phyllophilum.yaml data/taxa/eukaryota/fusarium_pininemorale.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, one current native GOLD organism row with one linked project and one native analysis row, one NCBI merged-ID side row but no retained retired old IDs, no NCBI type-material rows, no exact BacDive or StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:120645`, `label: Fusarium phaseoli`, `rank: SPECIES`, `parent_taxon: NCBITaxon:232080`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:22619`, which carries the same label, parent, rank, code, exact synonyms, related synonyms, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Fusarium solani species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:4909`, which records two retained direct organisms for `NCBITaxon:120645`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs contain one exact organism, one linked project, and one analysis linked to that project.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:120645`. The YAML preserves all five exact synonyms and all three related synonyms from the NCBI row.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs contain one exact organism, strain `NRRL 31156`, with linked project `Gp0219960` and one project-linked analysis.

The side `data/raw/ncbi_merged_ids.tsv` inventory maps old ID `NCBITaxon:108887` into `NCBITaxon:120645`, but no retained row in `data/raw/ncbitaxon_taxa.tsv` carries that old ID with `retired_into`, so the YAML correctly has no generated `replaces` entry. No exact NCBI type-material, exact BacDive, exact StrainInfo, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, five exact synonyms, three related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive or StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_phaseoli.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_phaseoli.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_phaseoli` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv` and can differ from the current native GOLD exact rows. Native GOLD organism, project, and analysis rows are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
