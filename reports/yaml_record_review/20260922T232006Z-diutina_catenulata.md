# YAML Record Review: Diutina catenulata

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/diutina_catenulata.yaml
- Started UTC: 2026-09-22T23:20:06Z
- Finished UTC: 2026-09-22T23:20:06Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:45537` |
| Label | `Diutina catenulata` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1910789` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/diutina_catenulata.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/diutina_catenulata.yaml data/taxa/eukaryota/diutina_mesorugosa.yaml data/taxa/eukaryota/diutina_neorugosa.yaml data/taxa/eukaryota/diutina_pseudorugosa.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, two exact native GOLD organisms linked to two projects and one analysis, 19 exact NCBI type-material rows, 20 exact StrainInfo direct records carrying 24 matching deposit designations, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:45537`, `label: Diutina catenulata`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1910789`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:5595`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Diutina` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:36047`, which records two retained direct organisms for `NCBITaxon:45537`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:45537`. The YAML carries both exact synonyms and the one related synonym filed for this NCBI row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain two exact organisms, `Go0520310` for `Diutina catenulata WY3-10-4` and `Go0705245` for `Diutina catenulata NRRL Y-1508`; the native project rows link those organisms to `Gp0444505` and `Gp0831277`, and the analysis table links one `Diutina catenulata WY3-10-4` analysis through `Gp0444505`.

The NCBI type-material inventory contributes 19 exact rows under `Candida catenulata`, covering separator variants of `CBS 565`, `ATCC 10565`, `BCRC 22316` or `CCRC 22316`, `DBVPG 6135`, `IFO 0745`, `JCM 1604`, `NRRL Y-1508`, and `VKM Y-36`.

The exact StrainInfo side inventory has 20 direct records and 24 matching deposit designations for `NCBITaxon:45537`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI exact synonyms, one NCBI related synonym, genetic code `12`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/diutina_catenulata.yaml` plus `just validate-strict data/taxa/eukaryota/diutina_catenulata.yaml`.

## Additional Notes

None.
