# YAML Record Review: Ellisomyces anomalus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/ellisomyces_anomalus.yaml
- Started UTC: 2026-09-22T23:47:12Z
- Finished UTC: 2026-09-22T23:47:12Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:101134` |
| Label | `Ellisomyces anomalus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:101133` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/ellisomyces_anomalus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/elaphomyces_granulatus.yaml data/taxa/eukaryota/elaphomyces_muricatus.yaml data/taxa/eukaryota/elasticomyces_elasticus.yaml data/taxa/eukaryota/ellisomyces_anomalus.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with three organism assertions, three exact native GOLD organisms, four native GOLD projects, 12 NCBI type-material rows, eight exact StrainInfo direct records carrying 19 matching deposit designations, no native GOLD analyses, no NCBI merged-ID or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:101134`, `label: Ellisomyces anomalus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:101133`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:17447`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Ellisomyces` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:261`, which records three retained direct organisms for `NCBITaxon:101134`; this agrees with `source_attestations[1].assertion_count: 3` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:101134`. The YAML carries the one exact synonym and both related synonyms filed for this NCBI row; NCBI supplies no broad synonyms or old-ID side rows.

The 12 NCBI type-material rows preserve duplicate spellings for `ATCC 32879`, `CBS 243.57`, `IFO 6151`, `IMI 211277`, `NRRL 2465`, and `RSA 88` as `Thamnidium anomalum` type material.

The native GOLD catalogs contain three exact organism rows, `Go0411509`, `Go0470772`, and `Go0470773`, with four linked projects between them. The exact StrainInfo side inventory has eight direct records and 19 matching deposit designations for `NCBITaxon:101134`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/ellisomyces_anomalus.yaml` plus `just validate-strict data/taxa/eukaryota/ellisomyces_anomalus.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the three current native GOLD organism rows. The absence of native GOLD analyses is consistent with `strain_count: 0` because native GOLD projects and analyses do not generate child strain records here.
