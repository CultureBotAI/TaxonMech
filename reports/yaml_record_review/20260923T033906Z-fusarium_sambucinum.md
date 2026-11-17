# YAML Record Review: Fusarium sambucinum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_sambucinum.yaml
- Started UTC: 2026-09-23T03:39:06Z
- Finished UTC: 2026-09-23T03:39:06Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5128` |
| Label | `Fusarium sambucinum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:569360` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_sambucinum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_redolens.yaml data/taxa/eukaryota/fusarium_robinianum.yaml data/taxa/eukaryota/fusarium_sambucinum.yaml data/taxa/eukaryota/fusarium_sarcochroum.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one current native GOLD organism row with one linked project and one native analysis row, 16 exact NCBI type-material rows, 116 exact StrainInfo records carrying 148 exact deposit rows, two NCBI merged-ID side rows but no retained retired old IDs, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5128`, `label: Fusarium sambucinum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:569360`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2248`, which carries the same label, parent, rank, code, exact synonyms, related synonyms, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Fusarium sambucinum species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37553`, which records one retained direct organism for `NCBITaxon:5128`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism, one linked project, and one analysis linked to that project.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5128`. The YAML preserves all four exact synonyms and all four related synonyms from the NCBI row.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs contain the same exact organism count and include strain `F-4` with linked project `Gp0144734` and one project-linked analysis.

The NCBI type-material table has 16 exact rows for the target, covering normalized variants of epitype culture `CBS 151942`, normalized variants of epitype culture `CPC 45317`, normalized variants of epitype `CBS H-25241`, and normalized variants of lectotype `G 00266369`. StrainInfo has 116 exact target records and 148 exact deposits. These side rows do not create generated child strains by themselves.

The side `data/raw/ncbi_merged_ids.tsv` inventory maps old IDs `NCBITaxon:2081995` and `NCBITaxon:5521` into `NCBITaxon:5128`, but no retained rows in `data/raw/ncbitaxon_taxa.tsv` carry those old IDs with `retired_into`, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, four exact synonyms, four related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_sambucinum.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_sambucinum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_sambucinum` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:5128` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.
