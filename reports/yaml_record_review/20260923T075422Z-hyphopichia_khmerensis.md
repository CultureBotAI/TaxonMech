# YAML Record Review: Hyphopichia khmerensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hyphopichia_khmerensis.yaml
- Started UTC: 2026-09-23T07:54:22Z
- Finished UTC: 2026-09-23T07:54:22Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2697237` |
| Label | `Hyphopichia khmerensis` |
| Rank | `SPECIES` |
| Parent Taxon | `NCBITaxon:507510` |
| Taxon Domain | `EUKARYOTA` |
| Grounding Status | `EXACT` |
| Mapping Status | `SEEDED` |
| Genetic Code | `12` |
| Strain Count | `0` |

## Validation

- `just validate data/taxa/eukaryota/hyphopichia_khmerensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/hyphopichia_khmerensis.yaml data/taxa/eukaryota/hyphopichia_pseudoburtonii.yaml data/taxa/eukaryota/hyphopichia_wangnamkhiaoensis.yaml data/taxa/eukaryota/hypocreales_sp.yaml` scanned the four-record batch and reported zero ERROR rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/hyphopichia_khmerensis.yaml` completed and emitted the bounded source scan used below.

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2697237`, `label: Hyphopichia khmerensis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:507510`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:544678`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hyphopichia`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:24933`, which records one retained direct organism for `NCBITaxon:2697237`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs contain one exact organism and one linked project, with no linked native analyses in the local snapshot.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2697237`. `Candida khmerensis Nagats., H. Kawas., Mikata & Tats. Seki, 2005` is present in `data/raw/ncbitaxon_taxa.tsv:544678` as an exact synonym, and the two other names in the YAML are present as related synonyms.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have an exact `Go0705166` organism for `CBS 9784` and a linked `Gp0831189` project; the scan found no linked native analysis rows.

NCBI carries two exact holotype rows for `Hyphopichia khmerensis` at `data/raw/ncbi_type_material.tsv:111078` through `data/raw/ncbi_type_material.tsv:111079`, covering `CBS 9784` spelling variants.

The side merged-ID inventory maps old `NCBITaxon:260535` and `NCBITaxon:2803305` to current `NCBITaxon:2697237`, but no retained retired NCBI row has `retired_into: NCBITaxon:2697237`, so no generated `replaces` entry is expected.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `12`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hyphopichia_khmerensis.yaml` plus `just validate-strict data/taxa/eukaryota/hyphopichia_khmerensis.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hyphopichia_khmerensis` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism and project rows are exact by NCBI taxon ID, but native GOLD rows are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
