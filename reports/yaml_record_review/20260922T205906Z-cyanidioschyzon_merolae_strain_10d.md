# YAML Record Review: Cyanidioschyzon merolae strain 10D

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cyanidioschyzon_merolae_strain_10d.yaml
- Started UTC: 2026-09-22T20:59:06Z
- Finished UTC: 2026-09-22T20:59:06Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:280699` |
| Label | `Cyanidioschyzon merolae strain 10D` |
| Rank | `STRAIN` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:45157` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cyanidioschyzon_merolae_strain_10d.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cutaneotrichosporon_sp_pl3408a.yaml data/taxa/eukaryota/cyanidiococcus_yangmingshanensis.yaml data/taxa/eukaryota/cyanidioschyzon_merolae.yaml data/taxa/eukaryota/cyanidioschyzon_merolae_strain_10d.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism row, twenty-five exact native GOLD project rows, one exact native GOLD analysis row, no NCBI type-material rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:280699`, `label: Cyanidioschyzon merolae strain 10D`, `rank: STRAIN`, `parent_taxon: NCBITaxon:45157`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:57115`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through parent species `Cyanidioschyzon merolae`; the bounded scan checked all 9 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:26909`, which records one retained organism for `NCBITaxon:280699`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:280699`. NCBI supplies no exact, related, or broad synonyms for this row, and the YAML correctly omits a `synonyms` block.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot also has exact organism `Go0000582`, exact project `Gp0000582`, twenty-four expression-profiling projects under the same organism, and one exact native analysis row tied to `Gp0000582` for `Cyanidioschyzon merolae 10D`.

No exact NCBI type-material, StrainInfo, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cyanidioschyzon_merolae_strain_10d.yaml` plus `just validate-strict data/taxa/eukaryota/cyanidioschyzon_merolae_strain_10d.yaml`.

## Additional Notes

The exact native GOLD row for `Go0000582` carries culture collection `NIES 1332`. The bounded scan found no exact StrainInfo row keyed to `NCBITaxon:280699`; the similarly named StrainInfo `NIES-1332` deposit is keyed to parent species `NCBITaxon:45157` and was not joined into this generated strain record.

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:280699`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
