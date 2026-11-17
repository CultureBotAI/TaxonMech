# YAML Record Review: Golovinomyces orontii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/golovinomyces_orontii.yaml
- Started UTC: 2026-09-23T05:04:45Z
- Finished UTC: 2026-09-23T05:04:45Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:62715` |
| Label | `Golovinomyces orontii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:184027` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/golovinomyces_orontii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/golovinomyces_magnicellulatus.yaml data/taxa/eukaryota/golovinomyces_orontii.yaml data/taxa/eukaryota/golubevia_pallescens.yaml data/taxa/eukaryota/gomphus_bonarii.yaml` | Passed; the strict batch exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, two exact current native GOLD organisms with 24 linked native GOLD projects and two linked native analyses, six side NCBI merged-ID rows, no retained retired NCBI rows, no exact NCBI type-material rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:62715`, `label: Golovinomyces orontii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:184027`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:7924`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Golovinomyces`; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:40008`, which records one retained direct organism for `NCBITaxon:62715`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs additionally contain exact organisms `Go0008360` and `Go0111647`, 24 linked projects, and two linked native analyses for project `Gp0113703`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:62715`. `Erysiphe orontii` is present in `data/raw/ncbitaxon_taxa.tsv:7924` as an exact synonym, and all eight generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies one organism assertion. Current native GOLD side evidence has one unstrained organism row plus one `MGH1` row; `MGH1` links to one standard draft, two transcriptome, and 20 gene-expression projects.

The side `data/raw/ncbi_merged_ids.tsv` inventory has six old IDs merged into `NCBITaxon:62715`, but the retained retired NCBI table contributes no old ID rows for this target. Omitting `replaces` is therefore consistent with the generated source state.

No exact NCBI type-material row, exact StrainInfo row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/golovinomyces_orontii.yaml` plus `just validate-strict data/taxa/eukaryota/golovinomyces_orontii.yaml`.

## Additional Notes

No prior exact ignored review report existed for `golovinomyces_orontii` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID, organism GOLD ID, or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
