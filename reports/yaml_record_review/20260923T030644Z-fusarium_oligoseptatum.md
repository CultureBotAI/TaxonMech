# YAML Record Review: Fusarium oligoseptatum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_oligoseptatum.yaml
- Started UTC: 2026-09-23T03:06:44Z
- Finished UTC: 2026-09-23T03:06:44Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2604345` |
| Label | `Fusarium oligoseptatum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:232080` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_oligoseptatum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_oligoseptatum.yaml data/taxa/eukaryota/fusarium_oxysporum.yaml data/taxa/eukaryota/fusarium_oxysporum_f_sp_albedinis.yaml data/taxa/eukaryota/fusarium_oxysporum_f_sp_cepae.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one current native GOLD organism row with one linked project and one native analysis row, two NCBI merged-ID side rows, ten NCBI type-material rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2604345`, `label: Fusarium oligoseptatum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:232080`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:535948`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium solani species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:23941`, which records one retained direct organism for `NCBITaxon:2604345`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs still contain the exact organism `Go0631997`, the linked project `Gp0645818`, and one analysis linked to that project for strain `NRRL62579`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2604345`. The YAML preserves the exact synonym `Neocosmospora oligoseptata` and four related NCBI synonyms: `Fusarium cf. solani NRRL 62579`, `Fusarium oligoseptatum T. Aoki, Kasson, S. Freeman, Geiser & O'Donnell, 2018`, `Fusarium sp. AF-4`, and `Neocosmospora oligoseptata (T. Aoki, M.T. Kasson, S. Freeman, D.M. Geiser & K. O'Donnell) Sand.-Den. & Crous, 2019`.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs still contain one exact organism row, one linked project row, and one project-linked analysis row.

The NCBI side merge inventory maps old IDs `NCBITaxon:1325735` and `NCBITaxon:1833830` to `NCBITaxon:2604345`, but neither old ID is retained in `data/raw/ncbitaxon_taxa.tsv` with `retired_into`, so the YAML correctly has no generated `replaces` entry. NCBI has ten exact type-material aliases for the target in `typematerial.dmp`: `CBS 143241`, `CBS:143241`, `FRC S-2581`, `FRC:S-2581`, `MAFF 246283`, `MAFF:246283`, `NRRL 62579`, `NRRL:62579`, `BPI 910525`, and `BPI:910525`. No exact StrainInfo, exact BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_oligoseptatum.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_oligoseptatum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_oligoseptatum` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
