# YAML Record Review: Hansenula queroliae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hansenula_queroliae.yaml
- Started UTC: 2026-09-23T06:01:41Z
- Finished UTC: 2026-09-23T06:01:41Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:517408` |
| Label | `Hansenula queroliae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:34359` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hansenula_queroliae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hansenula_ciferrii.yaml data/taxa/eukaryota/hansenula_lynferdii.yaml data/taxa/eukaryota/hansenula_queroliae.yaml data/taxa/eukaryota/hansenula_silvicultrix.yaml` | Passed; the strict batch reported zero ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with one linked native GOLD project and no linked native analyses, nine exact NCBI type-material rows, no side NCBI merged-ID rows, no exact BacDive or StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:517408`, `label: Hansenula queroliae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:34359`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:117374`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hansenula`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37649`, which records one retained direct organism for `NCBITaxon:517408`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism and one linked project.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:517408`. `Wickerhamomyces queroliae` is present in `data/raw/ncbitaxon_taxa.tsv:117374` as an exact synonym, and all four generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have an exact organism for `NRRL Y-48478`, a linked `Gp0831587` project in `data/gold/projects.jsonl.gz:610142`, and no native analysis linked by the exact project ID.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:226892` through `data/raw/ncbi_type_material.tsv:226900` as nine spellings for `NRRL Y-48478`, `UFMG-T05-200.1`, and `CBS 10936`.

No side NCBI merged-ID row, exact BacDive row, direct exact StrainInfo row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive or StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hansenula_queroliae.yaml` plus `just validate-strict data/taxa/eukaryota/hansenula_queroliae.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hansenula_queroliae` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism and project rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
