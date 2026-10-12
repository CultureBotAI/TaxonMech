# YAML Record Review: Cryptomonas obovoidea

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cryptomonas_obovoidea.yaml
- Started UTC: 2026-09-22T20:30:00Z
- Finished UTC: 2026-09-22T20:30:00Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:400143` |
| Label | `Cryptomonas obovoidea` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:3030` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cryptomonas_obovoidea.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cryptomonas_curvata.yaml data/taxa/eukaryota/cryptomonas_erosa.yaml data/taxa/eukaryota/cryptomonas_lucens.yaml data/taxa/eukaryota/cryptomonas_obovoidea.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism row, no exact native GOLD project or analysis rows, no NCBI type-material rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, NCBI merged-ID side rows but no retained retired rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:400143`, `label: Cryptomonas obovoidea`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3030`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:85765`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cryptomonas` genus; the bounded scan checked all 7 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:34440`, which records one retained organism for `NCBITaxon:400143`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:400143`. NCBI supplies related synonyms `Cryptomonas obovoidea Pascher, 1913`, `Cryptomonas sp. ASW 09006`, `Cryptomonas sp. CCAC 0031`, `Cryptomonas sp. CCAP 979/46`, `Cryptomonas sp. M1088`, `Cryptomonas sp. M1094`, and `Cryptomonas sp. UTEX LB2194` on the same row, matching the YAML `synonyms` block.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot also has exact organism `Go0587218` for `Cryptomonas obovoidea CCAC 0031`; no exact native project or analysis rows are tied to that organism in this snapshot.

No exact NCBI type-material, StrainInfo, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, generated NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cryptomonas_obovoidea.yaml` plus `just validate-strict data/taxa/eukaryota/cryptomonas_obovoidea.yaml`.

## Additional Notes

The bounded scan found side-inventory old IDs `NCBITaxon:179799`, `NCBITaxon:279063`, `NCBITaxon:279786`, `NCBITaxon:279787`, `NCBITaxon:279788`, and `NCBITaxon:279789` in `data/raw/ncbi_merged_ids.tsv`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` that would generate `replaces` entries.
