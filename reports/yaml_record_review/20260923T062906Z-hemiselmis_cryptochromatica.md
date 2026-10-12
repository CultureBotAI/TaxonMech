# YAML Record Review: Hemiselmis cryptochromatica

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hemiselmis_cryptochromatica.yaml
- Started UTC: 2026-09-23T06:29:06Z
- Finished UTC: 2026-09-23T06:29:06Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:464989` |
| Label | `Hemiselmis cryptochromatica` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:77924` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hemiselmis_cryptochromatica.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/hemiselmis_andersenii.yaml data/taxa/eukaryota/hemiselmis_cryptochromatica.yaml data/taxa/eukaryota/hemiselmis_rufescens.yaml data/taxa/eukaryota/hemiselmis_tepida.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with 12 linked native GOLD projects and no linked native analyses, four exact NCBI type-material rows, no side NCBI merged-ID rows, no exact BacDive or StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:464989`, `label: Hemiselmis cryptochromatica`, `rank: SPECIES`, `parent_taxon: NCBITaxon:77924`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:104169`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hemiselmis`; the bounded scan checked all seven lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:36305`, which records one retained direct organism for `NCBITaxon:464989`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism and 12 linked projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:464989`. The generated related synonym `Hemiselmis cryptochromatica C.E.Lane & J.M.Archibald, 2008` is present in `data/raw/ncbitaxon_taxa.tsv:104169`.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have an exact `Go0583108` organism for `CCMP 1181`, with 12 linked transcriptome projects from `Gp0588925` through `Gp0588936` in `data/gold/projects.jsonl.gz:436390` through `data/gold/projects.jsonl.gz:436401`, and no native analysis linked by the exact project IDs.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:217611` through `data/raw/ncbi_type_material.tsv:217614` as four culture-from-holotype spellings for `CCMP 1181`.

No side NCBI merged-ID row, exact BacDive row, exact StrainInfo row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, the NCBI related synonym for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive or StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hemiselmis_cryptochromatica.yaml` plus `just validate-strict data/taxa/eukaryota/hemiselmis_cryptochromatica.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hemiselmis_cryptochromatica` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism and project rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
