# YAML Record Review: Hymenopellis radicata

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hymenopellis_radicata.yaml
- Started UTC: 2026-09-23T07:37:17Z
- Finished UTC: 2026-09-23T07:37:17Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:937743` |
| Label | `Hymenopellis radicata` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:937605` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hymenopellis_radicata.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/hymenomonas_coronata.yaml data/taxa/eukaryota/hymenopellis_radicata.yaml data/taxa/eukaryota/hymenopellis_raphanipes.yaml data/taxa/eukaryota/hymenoscyphus_albidus.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, three exact current native GOLD organisms with three linked native GOLD projects and one linked native GOLD analysis, no exact NCBI type-material rows, two side NCBI merged-ID rows, 16 exact direct StrainInfo source records, 17 exact StrainInfo deposit matches, no final StrainInfo overlay rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:937743`, `label: Hymenopellis radicata`, `rank: SPECIES`, `parent_taxon: NCBITaxon:937605`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:198939`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hymenopellis`; the bounded scan checked all 14 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:44847`, which records two retained direct organisms for `NCBITaxon:937743`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs contain three exact organisms, three linked projects, and one linked analysis under this NCBI taxon ID.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:937743`. All seven exact synonyms and all eight related synonyms in `data/raw/ncbitaxon_taxa.tsv:198939` are present in the YAML, spanning Agaricus, Collybia, Gymnopus, Mucidula, Oudemansiella, Xerula, the current Hymenopellis combination, and the `rooting shank` common name.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have exact `Go0111658`, `Go0111659`, and `Go0518082` organisms, linked `Gp0113721`, `Gp0113722`, and `Gp0442151` projects, and one native analysis linked by project ID `Gp0442151`.

The raw StrainInfo JSONL contains 16 exact direct source records and 17 exact deposit matches for `NCBITaxon:937743`, but the maintained StrainInfo overlay tables have no exact rows for this taxon.

The side merged-ID inventory maps old `NCBITaxon:170858` and `NCBITaxon:357591` to current `NCBITaxon:937743`, but no retained retired NCBI row has `retired_into: NCBITaxon:937743`, so no generated `replaces` entry is expected.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hymenopellis_radicata.yaml` plus `just validate-strict data/taxa/eukaryota/hymenopellis_radicata.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hymenopellis_radicata` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo only overlays BacDive-derived local strains in the generated final tables, so exact raw StrainInfo JSONL rows without exact final `data/straininfo` output rows are not generated as child strain records here.
