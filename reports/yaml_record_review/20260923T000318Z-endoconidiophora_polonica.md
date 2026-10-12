# YAML Record Review: Endoconidiophora polonica

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/endoconidiophora_polonica.yaml
- Started UTC: 2026-09-23T00:03:18Z
- Finished UTC: 2026-09-23T00:03:18Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1580850` |
| Label | `Endoconidiophora polonica` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1580844` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/endoconidiophora_polonica.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/endocarpon_pusillum.yaml data/taxa/eukaryota/endochytriaceae_sp_jel_072.yaml data/taxa/eukaryota/endoconidiophora_laricicola.yaml data/taxa/eukaryota/endoconidiophora_polonica.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism/project/analysis chain, four NCBI type-material rows, one NCBI merged-ID side row, no retained retired rows, 28 exact StrainInfo direct records carrying 29 matching deposit designations, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1580850`, `label: Endoconidiophora polonica`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1580844`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:407567`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Endoconidiophora` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:12754`, which records one retained direct organism for `NCBITaxon:1580850`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1580850`. The YAML preserves NCBI's exact synonyms `Ceratocystis polonica` and `Ophiostoma polonicum`, plus both related synonyms, `Endoconidiophora polonica (Siemaszko) Z.W. de Beer, T.A. Duong & M.J. Wingf., 2014` and `Ophiostoma polonicum Siemaszko, 1939`; NCBI supplies no broad synonyms.

The four NCBI type-material rows preserve `CBS 133.38` and `CMW 672` aliases as type material for `Endoconidiophora polonica`. The native GOLD catalogs contain one exact organism row, `Go0384454` for `Endoconidiophora polonica CBS100205`, with one matching project, `Gp0235559`, and one matching analysis row linked through that project.

The NCBI merged-ID side inventory maps `NCBITaxon:54189` to the current target, but it is not a retained retired row in `data/raw/ncbitaxon_taxa.tsv`, so the absent `replaces` field is consistent with the generated output. The exact StrainInfo side inventory has 28 direct records carrying 29 matching deposit designations, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI exact synonyms, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/endoconidiophora_polonica.yaml` plus `just validate-strict data/taxa/eukaryota/endoconidiophora_polonica.yaml`.

## Additional Notes

The NCBI merged-ID row remains only a side-inventory old ID; no generated `replaces` value is expected without a retained retired source row.
