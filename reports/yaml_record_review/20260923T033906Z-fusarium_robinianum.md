# YAML Record Review: Fusarium robinianum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_robinianum.yaml
- Started UTC: 2026-09-23T03:39:06Z
- Finished UTC: 2026-09-23T03:39:06Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1634941` |
| Label | `Fusarium robinianum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2800332` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_robinianum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_redolens.yaml data/taxa/eukaryota/fusarium_robinianum.yaml data/taxa/eukaryota/fusarium_sambucinum.yaml data/taxa/eukaryota/fusarium_sarcochroum.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one current native GOLD organism row with two linked projects and no native analysis rows, four exact NCBI type-material rows, no NCBI merged-ID side rows, no exact BacDive or StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1634941`, `label: Fusarium robinianum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2800332`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:425583`, which carries the same label, parent, rank, code, exact synonym, related synonyms, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Fusarium ventricosum species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:14000`, which records one retained direct organism for `NCBITaxon:1634941`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism and two linked projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1634941`. The YAML preserves exact synonym `Rectifusarium robinianum` and both related synonyms from the NCBI row.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs contain the same exact organism count and include organism `Go0586047`, labeled `Fusarium ventricosum NRRL 25729` but keyed by exact NCBI taxon `1634941`; it has standard-draft and transcriptome projects and no linked native GOLD analysis rows.

The NCBI type-material table has four exact culture-from-holotype rows for the target, covering `CBS 430.91`, `CBS:430.91`, `NRRL 25729`, and `NRRL:25729`. No side-inventory NCBI old IDs merge into `NCBITaxon:1634941`, so the YAML correctly has no generated `replaces` entry.

No exact BacDive, exact StrainInfo, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, one exact synonym, two related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive or StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_robinianum.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_robinianum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_robinianum` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
