# YAML Record Review: Hanseniaspora nectarophila

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hanseniaspora_nectarophila.yaml
- Started UTC: 2026-09-23T05:47:50Z
- Finished UTC: 2026-09-23T05:47:50Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1443074` |
| Label | `Hanseniaspora nectarophila` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:29832` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hanseniaspora_nectarophila.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hanseniaspora_meyeri.yaml data/taxa/eukaryota/hanseniaspora_mollemarum.yaml data/taxa/eukaryota/hanseniaspora_nectarophila.yaml data/taxa/eukaryota/hanseniaspora_occidentalis.yaml` | Passed; the strict batch reported zero ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with five organism assertions, five exact current native GOLD organisms with six linked native GOLD projects and no linked native analyses, five exact NCBI type-material rows, no side NCBI merged-ID rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1443074`, `label: Hanseniaspora nectarophila`, `rank: SPECIES`, `parent_taxon: NCBITaxon:29832`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:362502`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hanseniaspora`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:10543`, which records five retained direct organisms for `NCBITaxon:1443074`; this agrees with `source_attestations[1].assertion_count: 5` and its organism assertion unit. The current native GOLD catalogs also contain exact organisms for `yHDO717`, `yHDO718`, `yHMicronic5000035693`, `Y1191`, and `CBS 13383`, with six linked projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1443074`. `data/raw/ncbitaxon_taxa.tsv:362502` has no exact or broad synonyms for this species, and both generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies five organism assertions. The current native GOLD catalogs have five exact organism rows for `Hanseniaspora nectarophila`, three resequencing projects, two projects for `Y1191`, and one project for `CBS 13383`; no linked native analysis rows are present.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:31440` through `data/raw/ncbi_type_material.tsv:31444` as `CBS 13383`, `CBS:13383`, `UFMG POG a.1`, `ZIM 2311`, and `ZIM:2311`. No side NCBI merged-ID row, exact StrainInfo row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, both NCBI related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hanseniaspora_nectarophila.yaml` plus `just validate-strict data/taxa/eukaryota/hanseniaspora_nectarophila.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hanseniaspora_nectarophila` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
