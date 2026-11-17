# YAML Record Review: Dioszegia dumuzii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/dioszegia_dumuzii.yaml
- Started UTC: 2026-09-22T23:00:29Z
- Finished UTC: 2026-09-22T23:00:29Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2878329` |
| Label | `Dioszegia dumuzii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:165440` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/dioszegia_dumuzii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/dioszegia_aurantiaca.yaml data/taxa/eukaryota/dioszegia_crocea.yaml data/taxa/eukaryota/dioszegia_cryoxerica.yaml data/taxa/eukaryota/dioszegia_dumuzii.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with four retained direct organisms, four exact native GOLD organisms with no linked local native projects or analyses, two exact NCBI type-material rows, one exact StrainInfo direct record carrying one matching deposit designation, no exact BacDive rows, no final raw strain rows, one NCBI merged-ID side row, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2878329`, `label: Dioszegia dumuzii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:165440`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:566960`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Dioszegia` genus; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:27995`, which records four retained direct organisms for `NCBITaxon:2878329`; this agrees with `source_attestations[1].assertion_count: 4` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2878329`. The YAML carries the one exact synonym and one related synonym filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain four exact organisms, `Go0620353` for `Dioszegia dumuzii TSN-530`, `Go0620354` for `Dioszegia dumuzii PYCC 6248`, `Go0620355` for `Dioszegia dumuzii DSM 102964`, and `Go0620356` for `Dioszegia dumuzii CBS 12501`; the local native GOLD project and analysis tables have no exact rows linked through those organisms.

The NCBI type-material inventory contributes two exact rows under `Dioszegia dumuzii`, covering both spelling variants of the `DSM 102964` holotype designation.

The exact StrainInfo side inventory has one direct record and one matching deposit designation for `NCBITaxon:2878329`, but that record is not present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/dioszegia_dumuzii.yaml` plus `just validate-strict data/taxa/eukaryota/dioszegia_dumuzii.yaml`.

## Additional Notes

The bounded scan found a side-inventory `data/raw/ncbi_merged_ids.tsv` mapping from `NCBITaxon:1826643` into `NCBITaxon:2878329`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` would generate a `replaces` entry.
