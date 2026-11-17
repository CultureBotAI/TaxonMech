# YAML Record Review: Hanseniaspora valbyensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hanseniaspora_valbyensis.yaml
- Started UTC: 2026-09-23T05:59:03Z
- Finished UTC: 2026-09-23T05:59:03Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:53685` |
| Label | `Hanseniaspora valbyensis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:29832` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hanseniaspora_valbyensis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hanseniaspora_uvarum.yaml data/taxa/eukaryota/hanseniaspora_valbyensis.yaml data/taxa/eukaryota/hanseniaspora_vineae.yaml data/taxa/eukaryota/hansenula_anomala.yaml` | Passed; the strict batch reported zero ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with seven organism assertions, seven exact current native GOLD organisms with seven linked native GOLD projects and no linked native analyses, 23 exact NCBI type-material rows, one side NCBI merged-ID row, no retained old IDs, 33 direct exact StrainInfo rows with 72 deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:53685`, `label: Hanseniaspora valbyensis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:29832`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:6798`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hanseniaspora`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:38218`, which records seven retained direct organisms for `NCBITaxon:53685`; this agrees with `source_attestations[1].assertion_count: 7` and its organism assertion unit. The current native GOLD catalogs also contain seven exact organisms and seven linked projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:53685`. `Kloeckera japonica` is present in `data/raw/ncbitaxon_taxa.tsv:6798` as an exact synonym, and both generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies seven organism assertions. The current native GOLD catalogs have exact organisms for `HY1`, `yHDO737`, `yHDO738`, `yHDO739`, `yHMicronic5000034955`, `Y532`, and `NRRL Y-1626`; all seven organisms have linked projects, and no exact linked project has a native analysis row.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:230782` through `data/raw/ncbi_type_material.tsv:230804` as 23 spellings for `CBS 479`, `NRRL Y-1626`, `ATCC 10631`, `ATCC 48013`, `BCRC 21396`, `CCRC 21396`, `DBVPG 6774`, `IFO 10834`, `CBS 281`, `DBVPG 6793`, and `NRRL Y-1382`. StrainInfo also has 33 direct exact rows with 72 deposit rows for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

`data/raw/ncbi_merged_ids.tsv:64909` maps side old ID `NCBITaxon:314314` into `NCBITaxon:53685`, but that old ID is not present as a retained retired row in `data/raw/ncbitaxon_taxa.tsv` and no `replaces` value should be generated from it.

No exact BacDive row or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hanseniaspora_valbyensis.yaml` plus `just validate-strict data/taxa/eukaryota/hanseniaspora_valbyensis.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hanseniaspora_valbyensis` before this report was written; the `find` check covered the ignored `reports/` tree.

The side NCBI merged-ID row is not by itself sufficient to generate a `replaces` value. The generator emits `replaces` only from retained retired rows in `data/raw/ncbitaxon_taxa.tsv` with `retired_into`, and the bounded scan found no retained old ID for this record.
