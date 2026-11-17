# YAML Record Review: Hepatospora eriocheir

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hepatospora_eriocheir.yaml
- Started UTC: 2026-09-23T06:41:48Z
- Finished UTC: 2026-09-23T06:41:48Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1081669` |
| Label | `Hepatospora eriocheir` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1081667` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hepatospora_eriocheir.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hepatospora_eriocheir.yaml data/taxa/eukaryota/hericium_alpestre.yaml data/taxa/eukaryota/hericium_coralloides.yaml data/taxa/eukaryota/hericium_erinaceus.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, two exact current native GOLD organisms with two linked native GOLD projects and two linked native analyses, no exact NCBI type-material rows, no side NCBI merged-ID rows, no exact BacDive or StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1081669`, `label: Hepatospora eriocheir`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1081667`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:232409`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hepatospora`; the bounded scan checked all 10 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:1514`, which records two retained direct organisms for `NCBITaxon:1081669`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs also contain two exact organisms, two linked projects, and two linked analyses.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1081669`. `Endoreticulatus eriocheir` is present in `data/raw/ncbitaxon_taxa.tsv:232409` as an exact synonym, and both generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have exact `Go0048107` and `Go0373201` organisms for `GB1` and `canceri`, linked `Gp0048107` and `Gp0220005` projects, and one native analysis linked by each exact project ID.

No NCBI type-material row, side NCBI merged-ID row, exact BacDive row, exact StrainInfo row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive or StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hepatospora_eriocheir.yaml` plus `just validate-strict data/taxa/eukaryota/hepatospora_eriocheir.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hepatospora_eriocheir` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
