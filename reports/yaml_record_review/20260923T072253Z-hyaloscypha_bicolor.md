# YAML Record Review: Hyaloscypha bicolor

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hyaloscypha_bicolor.yaml
- Started UTC: 2026-09-23T07:22:53Z
- Finished UTC: 2026-09-23T07:22:53Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2482752` |
| Label | `Hyaloscypha bicolor` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:186449` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hyaloscypha_bicolor.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hyaloraphidium_curvatum.yaml data/taxa/eukaryota/hyaloscypha_bicolor.yaml data/taxa/eukaryota/hyaloscypha_bicolor_e.yaml data/taxa/eukaryota/hyaloscypha_finlandica.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, two exact current native GOLD organisms with four linked native GOLD projects and one linked native GOLD analysis, three exact NCBI type-material rows, five side NCBI merged-ID rows, two exact direct StrainInfo source records, two exact StrainInfo deposit matches, no final StrainInfo overlay rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2482752`, `label: Hyaloscypha bicolor`, `rank: SPECIES`, `parent_taxon: NCBITaxon:186449`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:525875`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Hyaloscypha hepaticicola/Rhizoscyphus ericae species complex`; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:22239`, which records two retained direct organisms for `NCBITaxon:2482752`; this agrees with `source_attestations[1].assertion_count: 2`, its organism assertion unit, and its descendant-exclusion note. The current native GOLD catalogs also contain two exact organisms, four linked projects, and one linked analysis under this direct NCBI taxon ID.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2482752`. `Meliniomyces bicolor` is present in `data/raw/ncbitaxon_taxa.tsv:525875` as an exact synonym, and all eight Helotiales, Hyaloscypha, Hymenoscyphus, Meliniomyces, and Rhizoscyphus related synonyms are present in the source row.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have exact `Go0009599` and `Go0568411` organisms for strains `E` and `P9C40`, linked `Gp0009599`, `Gp0010107`, `Gp0539710`, and `Gp0543358` projects, and one native analysis linked by project ID `Gp0009599`.

NCBI carries three exact culture-from-holotype rows for `Meliniomyces bicolor` at `data/raw/ncbi_type_material.tsv:95546` through `data/raw/ncbi_type_material.tsv:95548`. The raw StrainInfo JSONL also contains two exact direct source records and two exact deposit matches, but the maintained StrainInfo overlay tables have no exact rows for this taxon.

The side merged-ID inventory maps old `NCBITaxon:170963`, `NCBITaxon:170964`, `NCBITaxon:373870`, `NCBITaxon:99667`, and `NCBITaxon:99669` to current `NCBITaxon:2482752`, but no retained retired NCBI row has `retired_into: NCBITaxon:2482752`, so no generated `replaces` entry is expected.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, the direct-records-only GOLD note, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hyaloscypha_bicolor.yaml` plus `just validate-strict data/taxa/eukaryota/hyaloscypha_bicolor.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hyaloscypha_bicolor` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo only overlays BacDive-derived local strains in the generated final tables, so exact raw StrainInfo JSONL rows without exact final `data/straininfo` output rows are not generated as child strain records here.
