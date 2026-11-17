# YAML Record Review: Dujonia railenensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/dujonia_railenensis.yaml
- Started UTC: 2026-09-22T23:36:08Z
- Finished UTC: 2026-09-22T23:36:08Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:45579` |
| Label | `Dujonia railenensis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:3712547` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/dujonia_railenensis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/dryadomyces_sulphureus.yaml data/taxa/eukaryota/dujonia_boleticola.yaml data/taxa/eukaryota/dujonia_oleophila.yaml data/taxa/eukaryota/dujonia_railenensis.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism and project, 13 NCBI type-material rows, 11 exact StrainInfo direct records carrying 22 matching deposit designations, no NCBI merged-ID side rows, no native GOLD analyses, no BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:45579`, `label: Dujonia railenensis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3712547`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:5624`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Dujonia` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:36079`, which records one retained direct organism for `NCBITaxon:45579`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:45579`. The YAML carries the one exact synonym and both related synonyms filed for this NCBI row; NCBI supplies no broad synonyms or old-ID side rows.

The 13 NCBI type-material rows preserve `ATCC 58897`, `IJFM 6014`, `NCYC 2583`, and `NRRL Y-17762` culture-from-holotype spellings plus `CBS 8164` holotype spellings for `Candida railenensis`. The exact StrainInfo side inventory has 11 direct records and 22 matching deposit designations for `NCBITaxon:45579`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`.

The native GOLD catalogs contain one exact organism row, `Go0705347` for `Candida railenensis NRRL Y-17762`, and one matching project, `Gp0831383`. No native GOLD analysis, exact BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, two NCBI related synonyms, genetic code `12`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/dujonia_railenensis.yaml` plus `just validate-strict data/taxa/eukaryota/dujonia_railenensis.yaml`.

## Additional Notes

The single native GOLD organism uses the `Candida railenensis` synonym spelling that NCBI records as an exact synonym of the current `Dujonia railenensis` name.
