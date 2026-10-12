# YAML Record Review: Euglena gracilis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/euglena_gracilis.yaml
- Started UTC: 2026-09-23T01:00:19Z
- Finished UTC: 2026-09-23T01:00:19Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:3039` |
| Label | `Euglena gracilis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:3038` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/euglena_gracilis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/esteya_vermicola.yaml data/taxa/eukaryota/eucampia_antarctica.yaml data/taxa/eukaryota/euglena_gracilis.yaml data/taxa/eukaryota/euglena_gracilis_var_bacillaris.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with 12 organism assertions, 12 exact native GOLD organism rows, 17 exact native GOLD project rows, no exact native GOLD analysis rows, 37 exact StrainInfo rows with 56 deposits, no NCBI type-material rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:3039`, `label: Euglena gracilis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3038`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2035`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the euglenid genus `Euglena`; the bounded scan checked all 11 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:30443`, which records 12 retained direct organisms for `NCBITaxon:3039`; this agrees with `source_attestations[1].assertion_count: 12` and its organism assertion unit. The YAML correctly keeps this as a direct-taxonomy assertion and notes that descendant taxa are not gathered.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:3039`. The YAML preserves NCBI's exact synonym `Euglena gracilis bacillaris` plus the related synonym `Euglena gracilis Klebs, 1883`; NCBI supplies no broad synonyms and no old-ID side rows.

The current native GOLD catalogs contain 12 exact organism rows for `NCBITaxon:3039`: the base `Z1` organism plus 11 `Z1` MAT/MA resequencing organisms. Those current rows have 17 exact linked projects, including 11 resequencing projects and six `Z1` gene-expression profiling projects, with no current native GOLD analysis rows linked.

StrainInfo contains 37 exact target rows with 56 deposit designations for `Euglena gracilis`; those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive, NCBI type-material, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, one NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/euglena_gracilis.yaml` plus `just validate-strict data/taxa/eukaryota/euglena_gracilis.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the 12 current native GOLD organism rows filed directly under `NCBITaxon:3039`; the generated source note correctly excludes descendant variety `NCBITaxon:158060`.
