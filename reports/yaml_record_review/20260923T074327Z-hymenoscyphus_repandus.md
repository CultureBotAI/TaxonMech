# YAML Record Review: Hymenoscyphus repandus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hymenoscyphus_repandus.yaml
- Started UTC: 2026-09-23T07:43:27Z
- Finished UTC: 2026-09-23T07:43:27Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1735280` |
| Label | `Hymenoscyphus repandus` |
| Rank | `SPECIES` |
| Parent Taxon | `NCBITaxon:5182` |
| Taxon Domain | `EUKARYOTA` |
| Grounding Status | `EXACT` |
| Mapping Status | `SEEDED` |
| Strain Count | `0` |

## Validation

- `just validate data/taxa/eukaryota/hymenoscyphus_repandus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/hymenoscyphus_repandus.yaml data/taxa/eukaryota/hymenoscyphus_salicellus.yaml data/taxa/eukaryota/hymenoscyphus_scutula.yaml data/taxa/eukaryota/hymenotorrendiella_dingleyae.yaml` scanned the four-record batch and reported zero ERROR rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/hymenoscyphus_repandus.yaml` completed and emitted the bounded source scan used below.

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1735280`, `label: Hymenoscyphus repandus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5182`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:453094`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hymenoscyphus`; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:15039`, which records one retained direct organism for `NCBITaxon:1735280`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism, one linked project, and one linked analysis.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1735280`. `Calycina repanda` and `Helotium repandum` are present in `data/raw/ncbitaxon_taxa.tsv:453094` as exact synonyms, and both authorship-bearing names in the YAML are present as related synonyms.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have an exact `Go0118896` organism for `CBS 341.76`, a linked `Gp0124456` project, and one native analysis linked by project ID `Gp0124456`.

The raw StrainInfo JSONL contains one exact direct source record and one exact deposit match for `NCBITaxon:1735280`, `siID: 164581` / `CBS 341.76`, but the maintained StrainInfo overlay tables have no exact rows for this taxon. No exact NCBI type-material row, side NCBI merged-ID row, exact BacDive row, or maintained final strain-table row is present.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hymenoscyphus_repandus.yaml` plus `just validate-strict data/taxa/eukaryota/hymenoscyphus_repandus.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hymenoscyphus_repandus` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo only overlays BacDive-derived local strains in the generated final tables, so exact raw StrainInfo JSONL rows without exact final `data/straininfo` output rows are not generated as child strain records here.
