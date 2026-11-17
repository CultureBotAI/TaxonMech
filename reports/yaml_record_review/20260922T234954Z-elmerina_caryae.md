# YAML Record Review: Elmerina caryae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/elmerina_caryae.yaml
- Started UTC: 2026-09-22T23:49:54Z
- Finished UTC: 2026-09-22T23:49:54Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1211726` |
| Label | `Elmerina caryae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:264000` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/elmerina_caryae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/elmerina_caryae.yaml data/taxa/eukaryota/elsinoe_ampelina.yaml data/taxa/eukaryota/elsinoe_australis.yaml data/taxa/eukaryota/elsinoe_fawcettii.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with three organism assertions, one exact native GOLD organism, five native GOLD projects, one native GOLD analysis, three exact StrainInfo direct records carrying four matching deposit designations, no exact NCBI type-material, NCBI merged-ID, or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1211726`, `label: Elmerina caryae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:264000`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:274203`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Elmerina` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:5034`, which records three retained direct organisms for `NCBITaxon:1211726`; this agrees with `source_attestations[1].assertion_count: 3` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1211726`. The YAML carries all four exact synonyms and all three related synonyms filed for this NCBI row; NCBI supplies no broad synonyms or old-ID side rows.

The current native GOLD catalogs contain one exact organism row, `Go0033151` for `Elmerina caryae L-13461`, five linked native projects, and one analysis for the base `Gp0033151` project. The exact StrainInfo side inventory has three direct records and four matching deposit designations for `NCBITaxon:1211726`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`.

No exact NCBI type-material, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, four NCBI exact synonyms, three NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/elmerina_caryae.yaml` plus `just validate-strict data/taxa/eukaryota/elmerina_caryae.yaml`.

## Additional Notes

The retained GOLD aggregate count of three is larger than the one current exact row in the local native GOLD organism catalog. The generated YAML follows the retained aggregate input that seeded the record.
