# YAML Record Review: Huntiella moniliformis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/huntiella_moniliformis.yaml
- Started UTC: 2026-09-23T07:16:51Z
- Finished UTC: 2026-09-23T07:16:51Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1580861` |
| Label | `Huntiella moniliformis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1580853` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/huntiella_moniliformis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/huntiella_moniliformis.yaml data/taxa/eukaryota/huntiella_omanensis.yaml data/taxa/eukaryota/huntiella_savannae.yaml data/taxa/eukaryota/huntiella_tyalla.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, two exact current native GOLD organisms with two linked native GOLD projects and one linked native GOLD analysis, four exact NCBI type-material rows, one side NCBI merged-ID row, no retained old-ID rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1580861`, `label: Huntiella moniliformis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1580853`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:407571`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Huntiella`; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:12757`, which records two retained direct organisms for `NCBITaxon:1580861`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs also contain two exact organisms, two linked projects, and one linked analysis.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1580861`. `Ceratocystis moniliformis`, `Ceratostomella moniliformis`, `Endoconidiophora moniliformis`, and `Ophiostoma moniliforme` are present in `data/raw/ncbitaxon_taxa.tsv:407571` as exact synonyms, and the two longer authorship-bearing names in the YAML are present as related synonyms.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have exact `Go0012465` and `Go0094242` organisms for `CMW10134` and `CBS 118127`, linked `Gp0012465` and `Gp0094242` projects, and one native analysis linked by project ID `Gp0094242`.

NCBI carries four exact isotype rows for `Ceratostomella moniliformis` at `data/raw/ncbi_type_material.tsv:44103` through `data/raw/ncbi_type_material.tsv:44106`, all representing `MICH 13921` spelling variants. These aliases do not contradict the generated `strain_count: 0` because no exact BacDive, StrainInfo, or maintained final strain rows are linked to `NCBITaxon:1580861`.

The side merged-ID inventory maps old `NCBITaxon:72030` to current `NCBITaxon:1580861`, but no retained retired NCBI row has `retired_into: NCBITaxon:1580861`, so no generated `replaces` entry is expected.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/huntiella_moniliformis.yaml` plus `just validate-strict data/taxa/eukaryota/huntiella_moniliformis.yaml`.

## Additional Notes

No prior exact ignored review report existed for `huntiella_moniliformis` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
