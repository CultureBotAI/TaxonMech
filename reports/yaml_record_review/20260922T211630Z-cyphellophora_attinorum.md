# YAML Record Review: Cyphellophora attinorum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cyphellophora_attinorum.yaml
- Started UTC: 2026-09-22T21:16:30Z
- Finished UTC: 2026-09-22T21:16:30Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1664694` |
| Label | `Cyphellophora attinorum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:226991` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cyphellophora_attinorum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cyphellophora_attinorum.yaml data/taxa/eukaryota/cyphellophora_europaea.yaml data/taxa/eukaryota/cyphellophora_olivacea.yaml data/taxa/eukaryota/cyphellophora_oxyspora.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism row, one exact native GOLD project row, one exact native GOLD analysis row, two exact NCBI type-material rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1664694`, `label: Cyphellophora attinorum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:226991`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:434604`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cyphellophora` genus; the bounded scan checked all 15 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:14333`, which records one retained organism for `NCBITaxon:1664694`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1664694`. The YAML carries NCBI's exact synonym `Phialophora attinorum Attili-Angelis, Duarte, Stielow & de Hoog, 2014` and the related synonym `Cyphellophora attinorum (Attili-Angelis, A.P.M. Duarte, Stielow & de Hoog) Iturrieta-Gonzalez, Gene & Dania Garcia, 2020`; NCBI supplies no broad synonyms for this row.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot also has exact organism `Go0119041`, exact project `Gp0124601`, and one exact native analysis row tied to project `Gp0124601`; the native GOLD display name is `Phialophora attae CBS 131958`, but its exact `ORGANISM NCBI TAX ID` value ties it to `NCBITaxon:1664694`.

The NCBI type-material inventory contributes two exact `type material` rows for designations `CBS 131958` and `CBS:131958`, under the synonym taxon name `Phialophora attinorum`.

No exact StrainInfo, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cyphellophora_attinorum.yaml` plus `just validate-strict data/taxa/eukaryota/cyphellophora_attinorum.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:1664694`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
