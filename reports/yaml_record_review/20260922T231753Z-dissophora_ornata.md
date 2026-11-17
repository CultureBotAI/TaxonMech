# YAML Record Review: Dissophora ornata

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/dissophora_ornata.yaml
- Started UTC: 2026-09-22T23:17:53Z
- Finished UTC: 2026-09-22T23:17:53Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:979620` |
| Label | `Dissophora ornata` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:101100` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/dissophora_ornata.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/dissophora_decumbens.yaml data/taxa/eukaryota/dissophora_globulifera.yaml data/taxa/eukaryota/dissophora_ornata.yaml data/taxa/eukaryota/ditylum_brightwellii.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, two exact native GOLD organisms linked to three projects and one analysis, six exact NCBI type-material rows, two exact StrainInfo direct records carrying four matching deposit designations, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:979620`, `label: Dissophora ornata`, `rank: SPECIES`, `parent_taxon: NCBITaxon:101100`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:204223`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Dissophora` genus; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:45173`, which records two retained direct organisms for `NCBITaxon:979620`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:979620`. The YAML carries the one exact synonym and both related synonyms filed for this NCBI row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain two exact organisms, `Go0145904` for `Dissophora ornata Z 71` and `Go0370961` for `Dissophora ornata CBS 347.77`; the native project rows link those organisms to `Gp0154264`, `Gp0217348`, and `Gp0251485`, and the analysis table links one `Dissophora ornata CBS 347.77 Minimal Draft` analysis through `Gp0217348`.

The NCBI type-material inventory contributes six exact rows under `Mortierella ornata`, covering separator variants of the `CBS 347.77`, `SZMC 11221`, and `IMI 287529` holotype or type-material designations.

The exact StrainInfo side inventory has two direct records and four matching deposit designations for `NCBITaxon:979620`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/dissophora_ornata.yaml` plus `just validate-strict data/taxa/eukaryota/dissophora_ornata.yaml`.

## Additional Notes

None.
