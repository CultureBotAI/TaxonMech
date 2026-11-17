# YAML Record Review: Hansenula lynferdii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hansenula_lynferdii.yaml
- Started UTC: 2026-09-23T06:01:41Z
- Finished UTC: 2026-09-23T06:01:41Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1041609` |
| Label | `Hansenula lynferdii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:34359` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hansenula_lynferdii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hansenula_ciferrii.yaml data/taxa/eukaryota/hansenula_lynferdii.yaml data/taxa/eukaryota/hansenula_queroliae.yaml data/taxa/eukaryota/hansenula_silvicultrix.yaml` | Passed; the strict batch reported zero ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with one linked native GOLD project and no linked native analyses, 11 exact NCBI type-material rows, one side NCBI merged-ID row, no retained old IDs, two direct exact StrainInfo rows with 11 deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1041609`, `label: Hansenula lynferdii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:34359`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:223683`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hansenula`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:589`, which records one retained direct organism for `NCBITaxon:1041609`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism and one linked project.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1041609`. `Pichia lynferdii` and `Wickerhamomyces lynferdii` are present in `data/raw/ncbitaxon_taxa.tsv:223683` as exact synonyms, and all three generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have an exact organism for `NRRL Y-7723`, a linked `Gp0831690` project in `data/gold/projects.jsonl.gz:610245`, and no native analysis linked by the exact project ID.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:2558` through `data/raw/ncbi_type_material.tsv:2568` as 11 spellings for `BCRC 22676`, `ATCC 58367`, `CBS 6695`, `IFO 10724`, and `NRRL Y-7723`. StrainInfo also has two direct exact rows with 11 deposit rows for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

`data/raw/ncbi_merged_ids.tsv:85103` maps side old ID `NCBITaxon:53605` into `NCBITaxon:1041609`, but that old ID is not present as a retained retired row in `data/raw/ncbitaxon_taxa.tsv` and no `replaces` value should be generated from it.

No exact BacDive row or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hansenula_lynferdii.yaml` plus `just validate-strict data/taxa/eukaryota/hansenula_lynferdii.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hansenula_lynferdii` before this report was written; the `find` check covered the ignored `reports/` tree.

The side NCBI merged-ID row is not by itself sufficient to generate a `replaces` value. The generator emits `replaces` only from retained retired rows in `data/raw/ncbitaxon_taxa.tsv` with `retired_into`, and the bounded scan found no retained old ID for this record.
