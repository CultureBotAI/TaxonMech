# YAML Record Review: Hyaloscypha hepaticicola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hyaloscypha_hepaticicola.yaml
- Started UTC: 2026-09-23T07:25:54Z
- Finished UTC: 2026-09-23T07:25:54Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2082293` |
| Label | `Hyaloscypha hepaticicola` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:186449` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hyaloscypha_hepaticicola.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hyaloscypha_hepaticicola.yaml data/taxa/eukaryota/hyaloscypha_sp_pmi_1271.yaml data/taxa/eukaryota/hyaloscypha_variabilis.yaml data/taxa/eukaryota/hyaloscypha_variabilis_f.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, one exact current native GOLD organism with two linked native GOLD projects and one linked native GOLD analysis, ten exact NCBI type-material rows, six side NCBI merged-ID rows, 39 exact direct StrainInfo source records, 41 exact StrainInfo deposit matches, no final StrainInfo overlay rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2082293`, `label: Hyaloscypha hepaticicola`, `rank: SPECIES`, `parent_taxon: NCBITaxon:186449`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:517720`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Hyaloscypha hepaticicola/Rhizoscyphus ericae species complex`; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:19935`, which records two retained direct organisms for `NCBITaxon:2082293`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs contain one exact organism, two linked projects, and one linked analysis under this NCBI taxon ID.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2082293`. `Hymenoscyphus ericae`, `Pezoloma ericae`, `Rhizoscyphus ericae`, and `Scytalidium vaccinii` are present in `data/raw/ncbitaxon_taxa.tsv:517720` as exact synonyms, and all seven authorship-bearing or provisional related synonyms are present in the source row.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have an exact `Go0019396` organism for `UAMH 7357`, linked `Gp0019258` and `Gp0019396` projects, and one native analysis linked by project ID `Gp0019396`.

NCBI carries ten exact type-material rows for `Pezizella ericae` and `Scytalidium vaccinii` at `data/raw/ncbi_type_material.tsv:83450` through `data/raw/ncbi_type_material.tsv:83459`. The raw StrainInfo JSONL also contains 39 exact direct source records and 41 exact deposit matches, but the maintained StrainInfo overlay tables have no exact rows for this taxon.

The side merged-ID inventory maps old `NCBITaxon:1745343`, `NCBITaxon:5183`, `NCBITaxon:585634`, `NCBITaxon:585673`, `NCBITaxon:657307`, and `NCBITaxon:80710` to current `NCBITaxon:2082293`, but no retained retired NCBI row has `retired_into: NCBITaxon:2082293`, so no generated `replaces` entry is expected.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hyaloscypha_hepaticicola.yaml` plus `just validate-strict data/taxa/eukaryota/hyaloscypha_hepaticicola.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hyaloscypha_hepaticicola` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo only overlays BacDive-derived local strains in the generated final tables, so exact raw StrainInfo JSONL rows without exact final `data/straininfo` output rows are not generated as child strain records here.
