# YAML Record Review: Hanseniaspora jakobsenii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hanseniaspora_jakobsenii.yaml
- Started UTC: 2026-09-23T05:45:20Z
- Finished UTC: 2026-09-23T05:45:20Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1926583` |
| Label | `Hanseniaspora jakobsenii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:29832` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hanseniaspora_jakobsenii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hanseniaspora_hatyaiensis_nom_inval.yaml data/taxa/eukaryota/hanseniaspora_jakobsenii.yaml data/taxa/eukaryota/hanseniaspora_lachancei.yaml data/taxa/eukaryota/hanseniaspora_lindneri.yaml` | Passed; the strict batch reported zero ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with nine organism assertions, nine exact current native GOLD organisms with five linked native GOLD projects and no linked native analyses, five exact NCBI type-material rows, two side NCBI merged-ID rows with no retained old IDs, one direct exact StrainInfo row with one deposit row, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1926583`, `label: Hanseniaspora jakobsenii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:29832`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:495837`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hanseniaspora`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:17624`, which records nine retained direct organisms for `NCBITaxon:1926583`; this agrees with `source_attestations[1].assertion_count: 9` and its organism assertion unit. The current native GOLD catalogs also contain nine exact organisms, five of which have linked native GOLD projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1926583`. `data/raw/ncbitaxon_taxa.tsv:495837` has no exact or broad synonyms for this species, and all four generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies nine organism assertions. The current native GOLD catalogs have exact organism rows for `yHDO713`, `yHDO714`, `yHDO715`, `yHMicronic5000035692`, `YAV17`, `NCYC 3828`, `DSM 26339`, `CBS 12942`, and `ZIM 2603`, with five linked projects and no linked native analysis rows.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:71947` through `data/raw/ncbi_type_material.tsv:71951` as `CBS 12942`, `CBS:12942`, `YAV17`, `YAV:17`, and `collector:YAV:17`. The NCBI merged side inventory maps `NCBITaxon:1408590` and `NCBITaxon:1680636` into `NCBITaxon:1926583`, but neither old ID is retained in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected in the generated YAML.

StrainInfo also has one direct exact row, `siID 399169`, with one type `DSM 26339` deposit for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hanseniaspora_jakobsenii.yaml` plus `just validate-strict data/taxa/eukaryota/hanseniaspora_jakobsenii.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hanseniaspora_jakobsenii` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
