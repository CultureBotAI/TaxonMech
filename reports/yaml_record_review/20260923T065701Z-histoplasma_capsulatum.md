# YAML Record Review: Histoplasma capsulatum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/histoplasma_capsulatum.yaml
- Started UTC: 2026-09-23T06:57:01Z
- Finished UTC: 2026-09-23T06:57:01Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5037` |
| Label | `Histoplasma capsulatum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5036` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/histoplasma_capsulatum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hirsutella_rhossiliensis.yaml data/taxa/eukaryota/hirsutella_tunicata.yaml data/taxa/eukaryota/histomonas_meleagridis.yaml data/taxa/eukaryota/histoplasma_capsulatum.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, two exact current native GOLD organisms with two linked native GOLD projects and two linked native GOLD analyses, four exact NCBI type-material rows, one side NCBI merged-ID row, 66 direct exact StrainInfo rows with 70 deposit rows, three exact StrainInfo related-record side rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5037`, `label: Histoplasma capsulatum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5036`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2198`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Histoplasma`; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37370`, which records two retained direct organisms for `NCBITaxon:5037`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The attestation note correctly says descendant taxa are not gathered, and the current native GOLD catalogs contain two exact direct organisms, two linked projects, and two linked analyses.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5037`. `Ajellomyces capsulatus (Kwon-Chung) McGinnis & Katz, 1979`, `Cryptococcus capsulatus`, and `Emmonsiella capsulata` are present in `data/raw/ncbitaxon_taxa.tsv:2198` as exact synonyms, and `Cryptococcus capsulatus (Darling) Castell. & Chalm., 1919`, `Emmonsiella capsulata Kwon-Chung, 1972`, and `Histoplasma capsulatum Darling, 1906` are present in the source row as related synonyms.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have exact organisms `Go0593449` for `WU24` and `Go0632136` for `G184AR`; linked projects `Gp0607394` and `Gp0645957`; and two native analyses linked by those exact project IDs.

NCBI carries four exact type-material rows for `Emmonsiella capsulata` at `data/raw/ncbi_type_material.tsv:225090` through `data/raw/ncbi_type_material.tsv:225093`: `CBS 136.72`, `CBS:136.72`, `ATCC 22635`, and `ATCC:22635`. These rows include both `culture from holotype` and `type material` designations and do not contradict the generated `strain_count: 0`.

NCBI merged-ID side data maps retired `NCBITaxon:61255` into `NCBITaxon:5037`, but no retained retired source row exists for that old ID in `data/raw/ncbitaxon_taxa.tsv`, so the absence of a generated `replaces` value is consistent with the generator inputs.

StrainInfo has 66 direct exact rows with 70 deposit rows for this taxon. The three exact rows in `data/straininfo/related_records.tsv.gz` point at `straininfo.strain:389499` / `CBS 137.72`, whose `straininfo/strain_links.tsv` match is attached to `kgmicrobe.strain:bacdive_15280`; that BacDive strain is `NCBITaxon:1910` in the maintained raw strain tables, so it is not a local `NCBITaxon:5037` strain and is not propagated into `data/raw/strain_related_records.tsv` for this target.

No exact BacDive row or maintained final strain-table row is present for `NCBITaxon:5037`, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv` or `data/straininfo/exclusions.tsv`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/histoplasma_capsulatum.yaml` plus `just validate-strict data/taxa/eukaryota/histoplasma_capsulatum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `histoplasma_capsulatum` before this report was written; the `find` check covered the ignored `reports/` tree. The cross-data check for `bacdive_15280`, `CBS 137.72`, and `straininfo.strain:389499` also used `rg --no-ignore --hidden` to include ignored files.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
