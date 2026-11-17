# YAML Record Review: Debaryomyces hansenii CBS767

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/debaryomyces_hansenii_cbs767.yaml
- Started UTC: 2026-09-22T22:04:08Z
- Finished UTC: 2026-09-22T22:04:08Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:284592` |
| Label | `Debaryomyces hansenii CBS767` |
| Rank | `STRAIN` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:4959` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/debaryomyces_hansenii_cbs767.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/debaryomyces_fabryi.yaml data/taxa/eukaryota/debaryomyces_hansenii.yaml data/taxa/eukaryota/debaryomyces_hansenii_cbs767.yaml data/taxa/eukaryota/debaryomyces_hansenii_var_hansenii_mtcc_234.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI strain row, one retained GOLD aggregate row with two retained organisms, one exact native GOLD organism/project/analysis chain, no exact NCBI type-material rows, no exact StrainInfo records, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:284592`, `label: Debaryomyces hansenii CBS767`, `rank: STRAIN`, `parent_taxon: NCBITaxon:4959`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:57763`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the parent `Debaryomyces hansenii` species; the bounded scan checked all 14 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:27602`, which records two retained organisms for `NCBITaxon:284592`; this agrees with `source_attestations[1].assertion_count: 2`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:284592`. NCBI supplies no exact, related, or broad synonyms for this strain row, matching the absent `synonyms` block in the YAML.

The retained GOLD aggregate row supports the `GOLD` source attestation. The exact native GOLD chain contains organism `Go0000565`, project `Gp0000565`, and an analysis row named `Debaryomyces hansenii var. hansenii CBS767` that links back through `AP PROJECT GOLD IDS`.

The local NCBI type-material inventory has no exact rows for this strain ID.

The bounded scan found no exact StrainInfo records, no exact BacDive rows, and no maintained final strain-table rows, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded NCBI strain identity, NCBI and GOLD source attestations, genetic code `12`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/debaryomyces_hansenii_cbs767.yaml` plus `just validate-strict data/taxa/eukaryota/debaryomyces_hansenii_cbs767.yaml`.

## Additional Notes

None.
