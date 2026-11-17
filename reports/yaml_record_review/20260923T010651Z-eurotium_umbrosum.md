# YAML Record Review: Eurotium umbrosum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/eurotium_umbrosum.yaml
- Started UTC: 2026-09-23T01:06:51Z
- Finished UTC: 2026-09-23T01:06:51Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:469284` |
| Label | `Eurotium umbrosum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:28569` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/eurotium_umbrosum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/eurotium_umbrosum.yaml data/taxa/eukaryota/eutreptiella_gymnastica.yaml data/taxa/eukaryota/eutypa_lata.yaml data/taxa/eukaryota/eutypa_leptoplaca.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism row, three exact native GOLD project rows, 15 exact StrainInfo rows with 35 deposits, no NCBI type-material rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:469284`, `label: Eurotium umbrosum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:28569`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:104766`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Eurotium` genus; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:36379`, which records one retained direct organism for `NCBITaxon:469284`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:469284`. The YAML preserves NCBI's exact synonym `Aspergillus umbrosus` plus the related synonyms `Aspergillus umbrosus Bainier & Sartory, 1912` and `Eurotium umbrosum (Bainier & Sartory) Malloch & Cain, 1972`; NCBI supplies no broad synonyms and no old-ID side rows.

The native GOLD catalogs contain one exact organism row, `Go0446064` for `Aspergillus umbrosus CBS 117.46`, with three matching projects and no linked native GOLD analysis rows.

StrainInfo contains 15 exact target rows with 35 deposit designations for `Eurotium umbrosum`; those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive, NCBI type-material, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/eurotium_umbrosum.yaml` plus `just validate-strict data/taxa/eukaryota/eurotium_umbrosum.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the one current native GOLD organism row.
