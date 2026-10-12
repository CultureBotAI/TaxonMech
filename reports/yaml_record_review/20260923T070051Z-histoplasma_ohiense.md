# YAML Record Review: Histoplasma ohiense

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/histoplasma_ohiense.yaml
- Started UTC: 2026-09-23T07:00:51Z
- Finished UTC: 2026-09-23T07:00:51Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2902605` |
| Label | `Histoplasma ohiense` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5036` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/histoplasma_ohiense.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/histoplasma_capsulatum_var_duboisii_h88.yaml data/taxa/eukaryota/histoplasma_mississippiense.yaml data/taxa/eukaryota/histoplasma_ohiense.yaml data/taxa/eukaryota/hohenbuehelia_mastrucata.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, two exact current native GOLD organisms with two linked native GOLD projects and two linked native GOLD analyses, four exact NCBI type-material rows, one side NCBI merged-ID row, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2902605`, `label: Histoplasma ohiense`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5036`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:569382`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Histoplasma`; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:28320`, which records two retained direct organisms for `NCBITaxon:2902605`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs contain the same number of exact organisms, linked projects, and linked analyses.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2902605`. `Histoplasma ohiense V.E. Sepulveda, R. Marquez, Turissini, W.E. Goldman & Matute, 2017` is present in `data/raw/ncbitaxon_taxa.tsv:569382` as an exact synonym, and `Ajellomyces capsulatus G217B`, `Histoplasma capsulatum G217B`, and `Histoplasma ohiense V.E. Sepulveda, R. Marquez, Turissini, W.E. Goldman & Matute, 2024` are present in the source row as related synonyms.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have exact organisms `Go0002627` and `Go0632089` for `G217B`; linked projects `Gp0002627` and `Gp0645910`; and two native analyses linked by those exact project IDs.

NCBI carries four exact holotype aliases for `Histoplasma ohiense` at `data/raw/ncbi_type_material.tsv:138466` through `data/raw/ncbi_type_material.tsv:138469`: `CBS 145496`, `CBS-145496`, `CBS145496`, and `CBS:145496`. These aliases do not contradict the generated `strain_count: 0` because no exact BacDive, StrainInfo, or maintained final strain rows are linked to `NCBITaxon:2902605`.

NCBI merged-ID side data maps retired `NCBITaxon:447094` into `NCBITaxon:2902605`, but no retained retired source row exists for that old ID in `data/raw/ncbitaxon_taxa.tsv`, so the absence of a generated `replaces` value is consistent with the generator inputs.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/histoplasma_ohiense.yaml` plus `just validate-strict data/taxa/eukaryota/histoplasma_ohiense.yaml`.

## Additional Notes

No prior exact ignored review report existed for `histoplasma_ohiense` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
