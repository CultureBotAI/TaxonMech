# YAML Record Review: Debaryomyces prosopidis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/debaryomyces_prosopidis.yaml
- Started UTC: 2026-09-22T22:07:36Z
- Finished UTC: 2026-09-22T22:07:36Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:148098` |
| Label | `Debaryomyces prosopidis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:4958` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/debaryomyces_prosopidis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/debaryomyces_maramus.yaml data/taxa/eukaryota/debaryomyces_nepalensis.yaml data/taxa/eukaryota/debaryomyces_prosopidis.yaml data/taxa/eukaryota/debaryomyces_psychrophilus.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained direct organism, one exact native GOLD organism linked to two projects and two analyses, 12 exact NCBI type-material rows, three exact StrainInfo direct records carrying 14 matching deposit designations, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:148098`, `label: Debaryomyces prosopidis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:4958`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:30165`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Debaryomyces` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:11461`, which records one retained direct organism for `NCBITaxon:148098`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:148098`. The YAML carries the one related synonym filed for this row, `Debaryomyces prosopidis Phaff, Vaughan-Mart. & Starmer, 1998`; NCBI supplies no exact or broad synonyms for the row.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain one exact organism, `Go0517015` for `Debaryomyces prosopidis NRRL Y-27369`; two projects under that organism, `Gp0441053` and `Gp0780263`; and two analyses named `Debaryomyces prosopidis NRRL Y-27369` that link back through `AP PROJECT GOLD IDS`.

The NCBI type-material inventory contributes 12 exact rows, covering culture-from-type-material variants of `ATCC 201611`, `CBS 8450`, `DVPG 7010`, `JCM 9913`, `NRRL Y-27369`, and `UCD 84-100`.

The exact StrainInfo side inventory has three direct records and 14 matching deposit designations for `NCBITaxon:148098`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI related synonym, genetic code `12`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/debaryomyces_prosopidis.yaml` plus `just validate-strict data/taxa/eukaryota/debaryomyces_prosopidis.yaml`.

## Additional Notes

None.
