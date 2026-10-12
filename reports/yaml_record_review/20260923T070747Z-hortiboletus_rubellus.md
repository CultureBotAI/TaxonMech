# YAML Record Review: Hortiboletus rubellus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hortiboletus_rubellus.yaml
- Started UTC: 2026-09-23T07:07:47Z
- Finished UTC: 2026-09-23T07:07:47Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:545451` |
| Label | `Hortiboletus rubellus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1689478` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hortiboletus_rubellus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hortaea_werneckii.yaml data/taxa/eukaryota/hortiboletus_rubellus.yaml data/taxa/eukaryota/huiozyma_naganishii_cbs_8797.yaml data/taxa/eukaryota/huiozyma_sinensis.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, no exact current native GOLD organisms, no exact NCBI type-material rows, no side NCBI merged-ID rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:545451`, `label: Hortiboletus rubellus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1689478`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:126762`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hortiboletus`; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:38400`, which records one retained direct organism for `NCBITaxon:545451`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs have no exact organism rows for the same NCBI ID, which is side evidence drift outside the retained aggregate used to generate the record.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:545451`. `Boletus rubellus` is present in `data/raw/ncbitaxon_taxa.tsv:126762` as an exact synonym, and `Boletus rubellus Krombh., 1836` and `Hortiboletus rubellus (Krombh.) Simonini, Vizzini & Gelardi, 2015` are present in the source row as related synonyms.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs do not contain exact organism, project, or analysis rows for `NCBITaxon:545451`.

No NCBI type-material row, side NCBI merged-ID row, exact StrainInfo row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hortiboletus_rubellus.yaml` plus `just validate-strict data/taxa/eukaryota/hortiboletus_rubellus.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hortiboletus_rubellus` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; in this case no exact organism row was present in the current native GOLD snapshot, and no generated child strains exist without BacDive-derived local strain inventory entries.
