# YAML Record Review: Ephemerocybe angulata

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/ephemerocybe_angulata.yaml
- Started UTC: 2026-09-23T00:30:41Z
- Finished UTC: 2026-09-23T00:30:41Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:980116` |
| Label | `Ephemerocybe angulata` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:3440528` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/ephemerocybe_angulata.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/eocronartium_muscicola.yaml data/taxa/eukaryota/ephemerocybe_angulata.yaml data/taxa/eukaryota/ephemerocybe_pellucida.yaml data/taxa/eukaryota/epichloe_aotearoae.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, two exact native GOLD organism rows, three exact native GOLD project rows, two linked native GOLD analysis rows, nine exact StrainInfo rows with 10 deposits, no NCBI type-material rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:980116`, `label: Ephemerocybe angulata`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3440528`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:204341`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Ephemerocybe` genus; the bounded scan checked all 14 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:45210`, which records two retained direct organisms for `NCBITaxon:980116`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:980116`. The YAML preserves NCBI's exact synonyms `Coprinellus angulatus`, `Coprinus angulatus`, and `Tulosesus angulatus`, plus all four related synonyms filed for this row; NCBI supplies no broad synonyms or old-ID side rows.

The native GOLD catalogs contain two exact organism rows for `Tulosesus angulatus`, `Go0401821` and `Go0631440`, with three matching projects. Two current projects, `Gp0272391` and `Gp0644895`, link to native GOLD analysis rows.

StrainInfo contains nine exact target rows with 10 deposit designations for `Ephemerocybe angulata`; those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive, NCBI type-material, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, three NCBI exact synonyms, four NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/ephemerocybe_angulata.yaml` plus `just validate-strict data/taxa/eukaryota/ephemerocybe_angulata.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the two current native GOLD organism rows. The native GOLD analysis rows link through `AP PROJECT GOLD IDS` to current projects `Gp0272391` and `Gp0644895`.
