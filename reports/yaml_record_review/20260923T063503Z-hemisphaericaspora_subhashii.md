# YAML Record Review: Hemisphaericaspora subhashii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hemisphaericaspora_subhashii.yaml
- Started UTC: 2026-09-23T06:35:03Z
- Finished UTC: 2026-09-23T06:35:03Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:561895` |
| Label | `Hemisphaericaspora subhashii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:3712552` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hemisphaericaspora_subhashii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hemisphaericaspora_lyxosophila.yaml data/taxa/eukaryota/hemisphaericaspora_nanyangensis.yaml data/taxa/eukaryota/hemisphaericaspora_subhashii.yaml data/taxa/eukaryota/hemisphaericaspora_xylanilytica.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, one exact current native GOLD organism with two linked native GOLD projects and two linked native analyses, five exact NCBI type-material rows, no side NCBI merged-ID rows, no exact BacDive or StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:561895`, `label: Hemisphaericaspora subhashii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3712552`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:131857`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hemisphaericaspora`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:38860`, which records two retained direct organisms for `NCBITaxon:561895`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism, two linked projects, and two linked analyses.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:561895`. `Candida subhashii` is present in `data/raw/ncbitaxon_taxa.tsv:131857` as an exact synonym, and both generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have an exact `Go0631688` organism for `CBS 10753`, linked `Gp0645236` and `Gp0780231` projects, and one native analysis linked by each exact project ID.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:235588` through `data/raw/ncbi_type_material.tsv:235592` as holotype spellings for `CBS 10753` and isotype spellings for `UAMH 10744`.

No side NCBI merged-ID row, exact BacDive row, exact StrainInfo row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `12`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive or StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hemisphaericaspora_subhashii.yaml` plus `just validate-strict data/taxa/eukaryota/hemisphaericaspora_subhashii.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hemisphaericaspora_subhashii` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
