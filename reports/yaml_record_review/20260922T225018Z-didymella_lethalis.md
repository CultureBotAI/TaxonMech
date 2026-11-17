# YAML Record Review: Didymella lethalis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/didymella_lethalis.yaml
- Started UTC: 2026-09-22T22:50:18Z
- Finished UTC: 2026-09-22T22:50:18Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:749627` |
| Label | `Didymella lethalis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:55170` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/didymella_lethalis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/didymella_heteroderae.yaml data/taxa/eukaryota/didymella_keratinophila.yaml data/taxa/eukaryota/didymella_lethalis.yaml data/taxa/eukaryota/didymella_pomorum.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained direct organisms, two exact native GOLD organisms linked to two projects and two analyses, no exact NCBI type-material rows, three exact StrainInfo direct records carrying three matching deposit designations, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:749627`, `label: Didymella lethalis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:55170`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:173302`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Didymella` genus; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:42284`, which records two retained direct organisms for `NCBITaxon:749627`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:749627`. The YAML carries all four exact synonyms and all three related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain two exact organisms, `Go0527422` for `Didymella lethalis FOR-16-620` and `Go0527423` for `Didymella lethalis GRM-16-623`; two projects, `Gp0454597` and `Gp0454598`, under those organisms; and two analyses with the same organism names that link back through `AP PROJECT GOLD IDS`.

The exact StrainInfo side inventory has three direct records and three matching deposit designations for `NCBITaxon:749627`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact NCBI type-material rows, exact BacDive rows, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/didymella_lethalis.yaml` plus `just validate-strict data/taxa/eukaryota/didymella_lethalis.yaml`.

## Additional Notes

None.
