# YAML Record Review: Cyphellophora sessilis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cyphellophora_sessilis.yaml
- Started UTC: 2026-09-22T21:19:08Z
- Finished UTC: 2026-09-22T21:19:08Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:293231` |
| Label | `Cyphellophora sessilis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:226991` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cyphellophora_sessilis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cyphellophora_sessilis.yaml data/taxa/eukaryota/cyphellophora_sp.yaml data/taxa/eukaryota/cyrenella_elegans.yaml data/taxa/eukaryota/cystastrum_externum.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, two exact NCBI type-material rows, nine exact StrainInfo records not retained in the final StrainInfo overlay, no exact native GOLD rows keyed to `NCBITaxon:293231`, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:293231`, `label: Cyphellophora sessilis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:226991`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:59851`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cyphellophora` genus; the bounded scan checked all 15 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:28903`, which records one retained organism for `NCBITaxon:293231`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:293231`. The YAML carries NCBI's exact synonym `Phialophora sessilis` and the two NCBI related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. An exact native GOLD scan found no organism rows currently keyed to `NCBITaxon:293231`.

The NCBI type-material inventory contributes two exact `type material` rows for designations `CBS 243.85` and `CBS:243.85`. Exact StrainInfo records are keyed directly to `NCBITaxon:293231`, but none are retained into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`, and no `STRAININFO` source attestation is generated.

No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cyphellophora_sessilis.yaml` plus `just validate-strict data/taxa/eukaryota/cyphellophora_sessilis.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:293231`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
