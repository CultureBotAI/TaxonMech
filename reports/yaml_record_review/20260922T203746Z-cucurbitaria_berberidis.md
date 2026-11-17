# YAML Record Review: Cucurbitaria berberidis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cucurbitaria_berberidis.yaml
- Started UTC: 2026-09-22T20:37:46Z
- Finished UTC: 2026-09-22T20:37:46Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:45142` |
| Label | `Cucurbitaria berberidis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:45141` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cucurbitaria_berberidis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cucurbitaria_berberidis.yaml data/taxa/eukaryota/cudoniella_acicularis.yaml data/taxa/eukaryota/cunninghamella_albida.yaml data/taxa/eukaryota/cunninghamella_antarctica.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism row, two exact native GOLD project rows, one exact native GOLD analysis row, 14 exact NCBI type-material rows, three exact StrainInfo side rows, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:45142`, `label: Cucurbitaria berberidis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:45141`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:5494`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cucurbitaria` genus; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:35866`, which records one retained organism for `NCBITaxon:45142`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:45142`. NCBI supplies exact synonyms `Gibberidea berberidis`, `Hypoxylon berberidis`, `Pyrenochaeta berberidis`, and `Sphaeria berberidis`; it supplies related synonyms `Cucurbitaria berberidis (Pers.) Gray, 1821` and `Sphaeria berberidis Pers., 1794`. The YAML `synonyms` block matches those generated synonym sets.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot also has exact organism `Go0019409` for `Cucurbitaria berberidis CBS 394.84`, exact projects `Gp0019330` and `Gp0019409`, and one exact native analysis row tied to project `Gp0019330`.

The NCBI type-material side inventory has 14 exact rows for `NCBITaxon:45142`, covering epitype, isoepitype, lectotype, culture-from-epitype, and culture-from-type-material designations on the synonym `Sphaeria berberidis`. Exact StrainInfo side rows are also present for `MUCL 41727`, `CBS 363.93`, and `CBS 394.84`; none of those rows are joined into the maintained final strain tables for this target.

No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, generated NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cucurbitaria_berberidis.yaml` plus `just validate-strict data/taxa/eukaryota/cucurbitaria_berberidis.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:45142`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
