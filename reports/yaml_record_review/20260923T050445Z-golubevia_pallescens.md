# YAML Record Review: Golubevia pallescens

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/golubevia_pallescens.yaml
- Started UTC: 2026-09-23T05:04:45Z
- Finished UTC: 2026-09-23T05:04:45Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:58918` |
| Label | `Golubevia pallescens` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1904613` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/golubevia_pallescens.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/golovinomyces_magnicellulatus.yaml data/taxa/eukaryota/golovinomyces_orontii.yaml data/taxa/eukaryota/golubevia_pallescens.yaml data/taxa/eukaryota/gomphus_bonarii.yaml` | Passed; the strict batch exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with one linked native GOLD project and one linked native analysis, eight exact NCBI type-material rows, three side NCBI merged-ID rows, no retained retired NCBI rows, 20 exact StrainInfo rows, 26 exact StrainInfo deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:58918`, `label: Golubevia pallescens`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1904613`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:7444`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Golubevia`; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:39577`, which records one retained direct organism for `NCBITaxon:58918`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain exact organism `Go0138973` for strain `JCM 5230`, linked project `Gp0144030`, and one native analysis whose `AP PROJECT GOLD IDS` include `Gp0144030`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:58918`. `Tilletiopsis pallescens` is present in `data/raw/ncbitaxon_taxa.tsv:7444` as an exact synonym, and all five generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have one exact organism for `Golubevia pallescens JCM 5230`, one linked project, and one native analysis linked by `AP PROJECT GOLD IDS`.

NCBI type-material rows list `ATCC 24345`, `CBS 606.83`, `JCM 5230`, and `UBC 8007` plus colonized variants under `NCBITaxon:58918`. Exact StrainInfo rows are present as side inventory rows, but there are no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; StrainInfo only overlays BacDive-derived local strains, and this taxon has no generated local strain rows.

The side `data/raw/ncbi_merged_ids.tsv` inventory has `NCBITaxon:311099`, `NCBITaxon:311100`, and `NCBITaxon:311101` merged into `NCBITaxon:58918`, but the retained retired NCBI table contributes no old ID rows for this target. Omitting `replaces` is therefore consistent with the generated source state.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/golubevia_pallescens.yaml` plus `just validate-strict data/taxa/eukaryota/golubevia_pallescens.yaml`.

## Additional Notes

No prior exact ignored review report existed for `golubevia_pallescens` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
