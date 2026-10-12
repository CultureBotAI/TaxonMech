# YAML Record Review: Emergomyces africanus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/emergomyces_africanus.yaml
- Started UTC: 2026-09-22T23:52:53Z
- Finished UTC: 2026-09-22T23:52:53Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1955775` |
| Label | `Emergomyces africanus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1955773` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/emergomyces_africanus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/elytroderma_deformans.yaml data/taxa/eukaryota/elytroderma_sp.yaml data/taxa/eukaryota/emergomyces_africanus.yaml data/taxa/eukaryota/emergomyces_orientalis.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism/project/analysis chain, two NCBI type-material rows, four NCBI merged-ID side rows, no retained retired rows, no exact StrainInfo or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1955775`, `label: Emergomyces africanus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1955773`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:504338`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Emergomyces` genus; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:17984`, which records one retained direct organism for `NCBITaxon:1955775`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1955775`. The YAML carries all five related synonyms filed for this NCBI row: `Emergomyces africanus Dukik, Kenyon, Govender, Schwartz & de Hoog, 2016`, `Emmonsia sp. CAC-2015a`, `Emmonsia sp. CBS 136260`, `Emmonsia sp. CBS 136730`, and `Emmonsia sp. NCPF4164`; NCBI supplies no exact or broad synonyms.

The two NCBI type-material rows preserve `CBS 136260` and `CBS:136260` as holotype designations for `Emergomyces africanus`. The native GOLD catalogs contain one exact organism row, `Go0373178` for `Emergomyces africanus CBS 136260`, with one matching project, `Gp0219979`, and one matching analysis row linked through that project.

The NCBI merged-ID side inventory maps `NCBITaxon:1658172`, `NCBITaxon:1809714`, `NCBITaxon:1809715`, and `NCBITaxon:1809716` to the current target, but none are retained retired rows in `data/raw/ncbitaxon_taxa.tsv`, so the absent `replaces` field is consistent with the generated output. No exact StrainInfo, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, five NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/emergomyces_africanus.yaml` plus `just validate-strict data/taxa/eukaryota/emergomyces_africanus.yaml`.

## Additional Notes

The NCBI merged-ID rows remain only side-inventory old IDs; no generated `replaces` value is expected without retained retired source rows.
