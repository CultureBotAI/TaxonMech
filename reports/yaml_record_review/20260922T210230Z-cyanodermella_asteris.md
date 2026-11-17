# YAML Record Review: Cyanodermella asteris

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cyanodermella_asteris.yaml
- Started UTC: 2026-09-22T21:02:30Z
- Finished UTC: 2026-09-22T21:02:30Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1986089` |
| Label | `Cyanodermella asteris` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:56761` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cyanodermella_asteris.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cyanodermella_asteris.yaml data/taxa/eukaryota/cyanophora_paradoxa.yaml data/taxa/eukaryota/cyanoptyche_gloeocystis.yaml data/taxa/eukaryota/cyathus_pallidus.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with three retained organisms, three exact native GOLD organism rows, two exact NCBI type-material rows, one exact StrainInfo record not retained in the final StrainInfo overlay, no exact native GOLD project or analysis rows, no exact BacDive rows, no final raw strain rows, one NCBI merged-ID side row not retained into generated `replaces`, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1986089`, `label: Cyanodermella asteris`, `rank: SPECIES`, `parent_taxon: NCBITaxon:56761`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:508154`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cyanodermella` genus; the bounded scan checked all 16 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:18391`, which records three retained organisms for `NCBITaxon:1986089`; this agrees with `source_attestations[1].assertion_count: 3`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1986089`. The YAML carries the two NCBI related synonyms from the raw snapshot, `Cyanodermella asteris L. Jahn & Ludw.-Mull., 2017` and `Ostropales sp. LJ-2016`, and NCBI supplies no exact or broad synonyms for this row.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot also has exact organisms `Go0619501`, `Go0619502`, and `Go0619503` for strains `DSM 100826`, `DR 043292`, and `03HOR06-2-4`; no exact native GOLD projects or analysis rows were linked to those organisms.

The NCBI type-material inventory contributes two exact `holotype` rows for designations `DR 043292` and `DR:043292`. The exact StrainInfo record for `NCBITaxon:1986089` carries a type deposit for `DSM 100826`, but it has not been retained into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`, and no `STRAININFO` source attestation is generated.

No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cyanodermella_asteris.yaml` plus `just validate-strict data/taxa/eukaryota/cyanodermella_asteris.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv:29252` maps old ID `NCBITaxon:1824915` into `NCBITaxon:1986089`, but the old ID is not retained as a retired source row that would generate a `replaces` entry.
