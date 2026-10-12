# YAML Record Review: Hanseniaspora gamundiae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hanseniaspora_gamundiae.yaml
- Started UTC: 2026-09-23T05:42:56Z
- Finished UTC: 2026-09-23T05:42:56Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2094518` |
| Label | `Hanseniaspora gamundiae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:29832` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hanseniaspora_gamundiae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hamiltosporidium_tvaerminnensis.yaml data/taxa/eukaryota/hanseniaspora_clermontiae.yaml data/taxa/eukaryota/hanseniaspora_gamundiae.yaml data/taxa/eukaryota/hanseniaspora_guilliermondii.yaml` | Passed; the strict batch reported zero ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with five organism assertions, five exact current native GOLD organisms with five linked native GOLD projects and no linked native analyses, eight exact NCBI type-material rows, no side NCBI merged-ID rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2094518`, `label: Hanseniaspora gamundiae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:29832`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:518074`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hanseniaspora`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:20061`, which records five retained direct organisms for `NCBITaxon:2094518`; this agrees with `source_attestations[1].assertion_count: 5` and its organism assertion unit. The current native GOLD catalogs also contain exact organisms for `yHDO707`, `yHDO708`, `yHDO709`, `yHMicronic5000035685`, and `CRUB 1928`, each with one linked project.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2094518`. `data/raw/ncbitaxon_taxa.tsv:518074` has no exact or broad synonyms for this species, and both generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies five organism assertions. The current native GOLD catalogs have five exact organism rows for `Hanseniaspora gamundiae`, five linked projects, and no linked native analysis rows.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:84014` through `data/raw/ncbi_type_material.tsv:84021` as `NRRL Y-63793`, `NRRL:Y-63793`, `PYCC 7262`, `PYCC:7262`, `ZIM 2545`, `ZIM:2545`, `CRUB 1928`, and `CRUB:1928`. No side NCBI merged-ID row, exact StrainInfo row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, both NCBI related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hanseniaspora_gamundiae.yaml` plus `just validate-strict data/taxa/eukaryota/hanseniaspora_gamundiae.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hanseniaspora_gamundiae` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
