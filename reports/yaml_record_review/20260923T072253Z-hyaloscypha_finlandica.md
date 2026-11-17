# YAML Record Review: Hyaloscypha finlandica

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hyaloscypha_finlandica.yaml
- Started UTC: 2026-09-23T07:22:53Z
- Finished UTC: 2026-09-23T07:22:53Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2482753` |
| Label | `Hyaloscypha finlandica` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:186449` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hyaloscypha_finlandica.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/hyaloraphidium_curvatum.yaml data/taxa/eukaryota/hyaloscypha_bicolor.yaml data/taxa/eukaryota/hyaloscypha_bicolor_e.yaml data/taxa/eukaryota/hyaloscypha_finlandica.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with three organism assertions, three exact current native GOLD organisms with four linked native GOLD projects, no native GOLD analyses, four exact NCBI type-material rows, two side NCBI merged-ID rows, four exact direct StrainInfo source records, four exact StrainInfo deposit matches, no final StrainInfo overlay rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2482753`, `label: Hyaloscypha finlandica`, `rank: SPECIES`, `parent_taxon: NCBITaxon:186449`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:525876`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Hyaloscypha hepaticicola/Rhizoscyphus ericae species complex`; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:22240`, which records three retained direct organisms for `NCBITaxon:2482753`; this agrees with `source_attestations[1].assertion_count: 3` and its organism assertion unit. The current native GOLD catalogs also contain three exact organisms and four linked projects under this direct NCBI taxon ID.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2482753`. `Cadophora finlandica (C.J.K. Wang & H.E. Wilcox) T.C. Harr. & McNew, 2003`, `Chloridium paucisporum`, and `Phialophora finlandica C.J.K. Wang & H.E. Wilcox, 1986` are present in `data/raw/ncbitaxon_taxa.tsv:525876` as exact synonyms, and `Chloridium paucisporum C.J.K.Wang & H.E.Wilcox, 1986` is present as a related synonym.

The retained GOLD aggregate supplies three organism assertions. The current native GOLD catalogs have exact `Go0145903`, `Go0511396`, and `Go0632583` organisms for `PMI_746` and `PMI-PAMB-02`, linked `Gp0154263`, `Gp0401701`, `Gp0649174`, and `Gp0649175` projects, and no linked native GOLD analyses.

NCBI carries four exact type-material rows for `Chloridium paucisporum` and `Phialophora finlandica` at `data/raw/ncbi_type_material.tsv:95549` through `data/raw/ncbi_type_material.tsv:95552`. The raw StrainInfo JSONL also contains four exact direct source records and four exact deposit matches, but the maintained StrainInfo overlay tables have no exact rows for this taxon.

The side merged-ID inventory maps old `NCBITaxon:557719` and `NCBITaxon:62723` to current `NCBITaxon:2482753`, but no retained retired NCBI row has `retired_into: NCBITaxon:2482753`, so no generated `replaces` entry is expected.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hyaloscypha_finlandica.yaml` plus `just validate-strict data/taxa/eukaryota/hyaloscypha_finlandica.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hyaloscypha_finlandica` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism and project rows are exact by NCBI taxon ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo only overlays BacDive-derived local strains in the generated final tables, so exact raw StrainInfo JSONL rows without exact final `data/straininfo` output rows are not generated as child strain records here.
