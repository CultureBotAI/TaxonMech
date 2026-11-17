# YAML Record Review: Diplogelasinospora princeps

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/diplogelasinospora_princeps.yaml
- Started UTC: 2026-09-22T23:09:02Z
- Finished UTC: 2026-09-22T23:09:02Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1646524` |
| Label | `Diplogelasinospora princeps` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:303324` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/diplogelasinospora_princeps.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/diplogelasinospora_grovesii.yaml data/taxa/eukaryota/diplogelasinospora_inaequalis.yaml data/taxa/eukaryota/diplogelasinospora_princeps.yaml data/taxa/eukaryota/diplonema_papillatum.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained direct organism, one exact native GOLD organism linked to two projects and no analyses, no exact NCBI type-material rows, four exact StrainInfo direct records carrying 11 matching deposit designations, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1646524`, `label: Diplogelasinospora princeps`, `rank: SPECIES`, `parent_taxon: NCBITaxon:303324`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:430475`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Diplogelasinospora` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:14131`, which records one retained direct organism for `NCBITaxon:1646524`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1646524`. The YAML carries the one related synonym filed for this row; NCBI supplies no exact or broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain one exact organism, `Go0651391` for `Diplogelasinospora princeps CBS 135879`, and two projects, `Gp0688295` and `Gp0699284`, under that organism; the native GOLD analysis table has no exact linked analyses for those project IDs.

The exact StrainInfo side inventory has four direct records and 11 matching deposit designations for `NCBITaxon:1646524`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact NCBI type-material rows, exact BacDive rows, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/diplogelasinospora_princeps.yaml` plus `just validate-strict data/taxa/eukaryota/diplogelasinospora_princeps.yaml`.

## Additional Notes

None.
