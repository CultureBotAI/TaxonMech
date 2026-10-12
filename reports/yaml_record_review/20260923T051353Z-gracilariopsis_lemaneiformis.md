# YAML Record Review: Gracilariopsis lemaneiformis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/gracilariopsis_lemaneiformis.yaml
- Started UTC: 2026-09-23T05:13:53Z
- Finished UTC: 2026-09-23T05:13:53Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2782` |
| Label | `Gracilariopsis lemaneiformis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2781` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/gracilariopsis_lemaneiformis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/gracilariophila_oryzoides.yaml data/taxa/eukaryota/gracilariopsis_andersonii.yaml data/taxa/eukaryota/gracilariopsis_chorda.yaml data/taxa/eukaryota/gracilariopsis_lemaneiformis.yaml` | Passed; the strict batch scanned 4 files with 0 error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, two exact current native GOLD organisms with two linked native GOLD projects and one linked native analysis, no exact NCBI type-material rows, one side NCBI merged-ID row with no retained old ID, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2782`, `label: Gracilariopsis lemaneiformis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2781`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:1940`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Gracilariopsis`; the bounded scan checked all 9 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:26509`, which records one retained direct organism for `NCBITaxon:2782`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs contain two exact organism rows for this NCBI taxon, with linked projects `Gp0047543` and `Gp0549502` and one native analysis for `Gp0549502`; those current native rows are side evidence and do not drive the stored retained aggregate assertion count.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2782`. `Cordylecladia lemanaeformis`, `Gigartina lemaneiformis`, and `Gracilaria lemaneiformis` are present in `data/raw/ncbitaxon_taxa.tsv:1940` as exact synonyms, and all four generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs contain exact organisms `Go0047543` and `Go0574779`; `Go0574779` is linked to a native analysis for the `Gracilariopsis lemaneiformis long_DNAseq` project.

The NCBI merged side inventory maps `NCBITaxon:2778` into `NCBITaxon:2782`, but that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected in the generated YAML.

No exact NCBI type-material row, exact StrainInfo row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/gracilariopsis_lemaneiformis.yaml` plus `just validate-strict data/taxa/eukaryota/gracilariopsis_lemaneiformis.yaml`.

## Additional Notes

No prior exact ignored review report existed for `gracilariopsis_lemaneiformis` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
