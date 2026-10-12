# YAML Record Review: Fusarium solani

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_solani.yaml
- Started UTC: 2026-09-23T03:41:56Z
- Finished UTC: 2026-09-23T03:41:56Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:169388` |
| Label | `Fusarium solani` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:232080` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_solani.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/fusarium_scirpi.yaml data/taxa/eukaryota/fusarium_solani.yaml data/taxa/eukaryota/fusarium_sp.yaml data/taxa/eukaryota/fusarium_sp_af_6.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with five organism assertions, four current native GOLD organism rows with five linked projects and three native analysis rows, ten exact NCBI type-material rows, 317 exact StrainInfo records carrying 379 exact deposit rows, 49 NCBI merged-ID side rows but no retained retired old IDs, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:169388`, `label: Fusarium solani`, `rank: SPECIES`, `parent_taxon: NCBITaxon:232080`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:34558`, which carries the same label, parent, rank, code, exact synonyms, related synonyms, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Fusarium solani species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:14616`, which records five retained direct organisms for `NCBITaxon:169388`; this agrees with `source_attestations[1].assertion_count: 5` and its organism assertion unit. The current native GOLD catalogs contain four exact organisms, five linked projects, and three analyses linked to those exact organism projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:169388`. The YAML preserves both exact synonyms and all 58 related synonyms from the NCBI row.

The retained GOLD aggregate supplies five organism assertions. The current native GOLD catalogs contain four exact organisms, with organism strains `FSSC 5 MPI-SDFR-AT-0091`, `JS-169`, `IMV 00293`, and `7.154`; exact native GOLD joins found five linked projects and three project-linked analyses.

The NCBI type-material table has ten exact rows for the target, covering `CBS 140079`, `CBS:140079`, `FRC S-2364`, `FRC:S:2364`, `G.J.S. 09-1466`, `GJS 09-1466`, `NRRL 66304`, `NRRL:66304`, `CBS H-22335`, and `CBS:H:22335`. StrainInfo has 317 exact target records and 379 exact deposits. These side rows do not create generated child strains by themselves.

The side `data/raw/ncbi_merged_ids.tsv` inventory maps 49 old IDs into `NCBITaxon:169388`, but no retained rows in `data/raw/ncbitaxon_taxa.tsv` carry those old IDs with `retired_into`, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, two exact synonyms, 58 related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_solani.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_solani.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_solani` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv` and can differ from the current native GOLD exact rows. Native GOLD organism, project, and analysis rows are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:169388` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.
