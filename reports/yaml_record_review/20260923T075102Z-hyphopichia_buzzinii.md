# YAML Record Review: Hyphopichia buzzinii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hyphopichia_buzzinii.yaml
- Started UTC: 2026-09-23T07:51:02Z
- Finished UTC: 2026-09-23T07:51:02Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1979430` |
| Label | `Hyphopichia buzzinii` |
| Rank | `SPECIES` |
| Parent Taxon | `NCBITaxon:507510` |
| Taxon Domain | `EUKARYOTA` |
| Grounding Status | `EXACT` |
| Mapping Status | `SEEDED` |
| Genetic Code | `12` |
| Strain Count | `0` |

## Validation

- `just validate data/taxa/eukaryota/hyphopichia_buzzinii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/hyphopichia_burtonii.yaml data/taxa/eukaryota/hyphopichia_buzzinii.yaml data/taxa/eukaryota/hyphopichia_fennica.yaml data/taxa/eukaryota/hyphopichia_homilentoma.yaml` scanned the four-record batch and reported zero ERROR rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/hyphopichia_buzzinii.yaml` completed and emitted the bounded source scan used below.

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1979430`, `label: Hyphopichia buzzinii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:507510`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:507583`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hyphopichia`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:18312`, which records one retained direct organism for `NCBITaxon:1979430`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs contain one exact organism and one linked project, with no linked native analyses in the local snapshot.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1979430`. The YAML's authorship-bearing `Hyphopichia buzzinii` synonym is present in `data/raw/ncbitaxon_taxa.tsv:507583` as the only related synonym for the source row, and NCBI has no exact synonyms for this taxon.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have an exact `Go0705102` organism for `CBS 14300` and a linked `Gp0831124` project; the scan found no linked native analysis rows.

NCBI carries eight exact type-material rows for `Hyphopichia buzzinii` at `data/raw/ncbi_type_material.tsv:76194` through `data/raw/ncbi_type_material.tsv:76201`, spanning `CBS 14300` and `CLIB 1739` holotype spelling variants.

The scan found no exact side NCBI merged-ID rows, exact StrainInfo rows, exact BacDive rows, or maintained final strain-table rows. `strain_count: 0` is therefore consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `12`, a complete generated lineage, the NCBI related synonym for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hyphopichia_buzzinii.yaml` plus `just validate-strict data/taxa/eukaryota/hyphopichia_buzzinii.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hyphopichia_buzzinii` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism and project rows are exact by NCBI taxon ID, but native GOLD rows are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
