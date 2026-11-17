# YAML Record Review: Debaryomyces fabryi

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/debaryomyces_fabryi.yaml
- Started UTC: 2026-09-22T22:04:08Z
- Finished UTC: 2026-09-22T22:04:08Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:58627` |
| Label | `Debaryomyces fabryi` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:4958` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/debaryomyces_fabryi.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/debaryomyces_fabryi.yaml data/taxa/eukaryota/debaryomyces_hansenii.yaml data/taxa/eukaryota/debaryomyces_hansenii_cbs767.yaml data/taxa/eukaryota/debaryomyces_hansenii_var_hansenii_mtcc_234.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained organisms, two exact native GOLD organisms linked to 18 projects and two analyses, 21 exact NCBI type-material rows, 20 exact StrainInfo direct records carrying 44 matching deposit designations that were not retained in the final StrainInfo overlay, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:58627`, `label: Debaryomyces fabryi`, `rank: SPECIES`, `parent_taxon: NCBITaxon:4958`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:7422`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Debaryomyces` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:39513`, which records two retained organisms for `NCBITaxon:58627`; this agrees with `source_attestations[1].assertion_count: 2`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:58627`. The YAML carries the one exact synonym and both related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The exact native GOLD rows contain organisms `Go0116585` and `Go0517009`; projects `Gp0121009`, `Gp0441046`, and `Gp0595834` through `Gp0595849`; and two analysis rows named `Debaryomyces fabryi CBS 789` and `Debaryomyces fabryi NRRL Y-17914` that link back through `AP PROJECT GOLD IDS`.

The NCBI type-material inventory contributes 21 exact rows under `Debaryomyces fabryi`, covering culture-from-type-material variants of `ATCC 20278`, `BCRC 21710`, `CBS 789`, `CECT 11370`, `IFO 0015`, `JCM 2104`, `KCTC 7603`, `NBRC 0015`, and `NRRL Y-17914`.

Twenty exact StrainInfo direct records are keyed to `NCBITaxon:58627` and together carry 44 matching deposit designations, including retained GOLD strains `CBS 789` and `NRRL Y-17914`, but none have been retained into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; no `STRAININFO` source attestation is generated. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `12`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/debaryomyces_fabryi.yaml` plus `just validate-strict data/taxa/eukaryota/debaryomyces_fabryi.yaml`.

## Additional Notes

None.
