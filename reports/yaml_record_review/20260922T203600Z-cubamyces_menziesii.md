# YAML Record Review: Cubamyces menziesii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cubamyces_menziesii.yaml
- Started UTC: 2026-09-22T20:36:00Z
- Finished UTC: 2026-09-22T20:36:00Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2136021` |
| Label | `Cubamyces menziesii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2939270` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cubamyces_menziesii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cryptotrichosporon_steropae.yaml data/taxa/eukaryota/cubamyces_lactineus.yaml data/taxa/eukaryota/cubamyces_menziesii.yaml data/taxa/eukaryota/cucumispora_dikerogammari.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism row, eleven exact native GOLD project rows, one exact native GOLD analysis row, no NCBI type-material rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, NCBI merged-ID side rows but no retained retired rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2136021`, `label: Cubamyces menziesii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2939270`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:518920`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cubamyces` genus; the bounded scan checked all 13 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:20306`, which records one retained organism for `NCBITaxon:2136021`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2136021`. NCBI supplies exact synonyms `Leiotrametes menziesii`, `Polyporus menziesii`, and `Trametes menziesii` plus four related synonyms on the same row, matching the YAML `synonyms` block.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot also has exact organism `Go0367354`, exact standard-draft project `Gp0207321`, ten exact transcriptome projects `Gp0247954` through `Gp0247963`, and one exact native analysis row tied to project `Gp0207321` for `Leiotrametes menziesii CIRM-BRFM 1781`.

No exact NCBI type-material, StrainInfo, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, generated NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cubamyces_menziesii.yaml` plus `just validate-strict data/taxa/eukaryota/cubamyces_menziesii.yaml`.

## Additional Notes

The bounded scan found side-inventory old ID `NCBITaxon:1140397` in `data/raw/ncbi_merged_ids.tsv`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` that would generate `replaces` entries.
