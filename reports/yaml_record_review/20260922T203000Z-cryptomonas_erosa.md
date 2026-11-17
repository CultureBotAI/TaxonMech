# YAML Record Review: Cryptomonas erosa

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cryptomonas_erosa.yaml
- Started UTC: 2026-09-22T20:30:00Z
- Finished UTC: 2026-09-22T20:30:00Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:400142` |
| Label | `Cryptomonas erosa` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:3030` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cryptomonas_erosa.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cryptomonas_curvata.yaml data/taxa/eukaryota/cryptomonas_erosa.yaml data/taxa/eukaryota/cryptomonas_lucens.yaml data/taxa/eukaryota/cryptomonas_obovoidea.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism row, one exact native GOLD project row, no exact native GOLD analysis rows, no NCBI type-material rows, three exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, NCBI merged-ID side rows but no retained retired rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:400142`, `label: Cryptomonas erosa`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3030`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:85764`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cryptomonas` genus; the bounded scan checked all 7 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:34439`, which records one retained organism for `NCBITaxon:400142`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:400142`. NCBI supplies related synonyms `Cryptomonas erosa Ehrenberg, 1832`, `Cryptomonas sp. CCAC 0018`, `Cryptomonas sp. CCAP 979/67`, and `Cryptomonas sp. M0741` on the same row, matching the YAML `synonyms` block.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot also has exact organism `Go0587215` and exact project `Gp0594831` for `Cryptomonas erosa CCAC 0740B`; no exact native analysis rows are tied to that project in this snapshot.

The bounded scan found three exact StrainInfo taxon rows, but no exact joined rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv` and no maintained final strain-table rows for `NCBITaxon:400142`; `strain_count: 0` is therefore consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, generated NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cryptomonas_erosa.yaml` plus `just validate-strict data/taxa/eukaryota/cryptomonas_erosa.yaml`.

## Additional Notes

The bounded scan found side-inventory old IDs `NCBITaxon:279062`, `NCBITaxon:279785`, and `NCBITaxon:279792` in `data/raw/ncbi_merged_ids.tsv`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` that would generate `replaces` entries.
