# YAML Record Review: Entomortierella echinosphaera

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/entomortierella_echinosphaera.yaml
- Started UTC: 2026-09-23T00:24:47Z
- Finished UTC: 2026-09-23T00:24:47Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:743928` |
| Label | `Entomortierella echinosphaera` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2779859` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/entomortierella_echinosphaera.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/entomortierella_echinosphaera.yaml data/taxa/eukaryota/entomortierella_lignicola.yaml data/taxa/eukaryota/entomortierella_parvispora.yaml data/taxa/eukaryota/entomortierella_sp.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with three organism assertions, three exact native GOLD organism rows, four exact native GOLD project rows, no native GOLD analyses, four NCBI type-material rows, four exact StrainInfo rows with five deposits, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:743928`, `label: Entomortierella echinosphaera`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2779859`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:171412`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Entomortierella` genus; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:42164`, which records three retained direct organisms for `NCBITaxon:743928`; this agrees with `source_attestations[1].assertion_count: 3` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:743928`. The YAML preserves NCBI's exact synonym `Mortierella echinosphaera`, plus both related synonyms filed for this row; NCBI supplies no broad synonyms or old-ID side rows.

The four NCBI type-material rows preserve culture-from-holotype aliases for `CBS 575.75` and type-material aliases for `IMI 242503` under `Mortierella echinosphaera`. The native GOLD catalogs contain three exact organism rows, `Go0141632`, `Go0532376`, and `Go0583337`, with four matching projects and no matching native GOLD analysis rows.

StrainInfo contains four exact target rows with five deposit designations for `Entomortierella echinosphaera`; those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/entomortierella_echinosphaera.yaml` plus `just validate-strict data/taxa/eukaryota/entomortierella_echinosphaera.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the three current native GOLD organism rows. The additional native GOLD project row comes from the `CBS 575.75` organism, which has both genome and transcriptome projects in the local GOLD export.
