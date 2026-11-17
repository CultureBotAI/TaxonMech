# YAML Record Review: Fusarium odoratissimum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_odoratissimum.yaml
- Started UTC: 2026-09-23T03:02:34Z
- Finished UTC: 2026-09-23T03:02:34Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2502994` |
| Label | `Fusarium odoratissimum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:171631` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_odoratissimum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_nurragi.yaml data/taxa/eukaryota/fusarium_nygamai.yaml data/taxa/eukaryota/fusarium_odoratissimum.yaml data/taxa/eukaryota/fusarium_odoratissimum_nrrl_54006.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, two current native GOLD organism rows with two linked projects and one native analysis row, two NCBI merged-ID side rows, three NCBI type-material rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2502994`, `label: Fusarium odoratissimum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:171631`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:528245`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium oxysporum species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:22663`, which records two retained direct organisms for `NCBITaxon:2502994`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs still contain the exact organisms `Go0005664` and `Go0037032`, their two linked projects, and one analysis linked to `Gp0037032`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2502994`. The YAML preserves the exact synonym `Fusarium oxysporum f. sp. cubense tropical race 4` and four related NCBI synonyms: `Foc TR4`, `Fusarium odoratissimum Maryani, L. Lombard, Kema & Crous, 2018`, `Fusarium oxysporum f. sp. cubense race 4`, and `Fusarium oxysporum f. sp. cubense tropical race 4 (Foc TR4)`.

The retained GOLD aggregate supplies two organism assertions filed directly under `NCBITaxon:2502994`, matching the YAML note that descendant taxa are not gathered. The current native GOLD catalogs still contain two exact organism rows, two linked project rows, and one analysis row linked to `Gp0037032`.

The NCBI side merge inventory maps old IDs `NCBITaxon:1229665` and `NCBITaxon:2749759` to `NCBITaxon:2502994`, but neither old ID is retained in `data/raw/ncbitaxon_taxa.tsv` with `retired_into`, so the YAML correctly has no generated `replaces` entry. NCBI has three holotype aliases for the target in `typematerial.dmp`: `INACC F822`, `INACC:F822`, and `Indo8`. No exact StrainInfo, exact BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_odoratissimum.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_odoratissimum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_odoratissimum` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
