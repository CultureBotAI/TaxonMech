# YAML Record Review: Eimeria tenella strain Houghton

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/eimeria_tenella_strain_houghton.yaml
- Started UTC: 2026-09-22T23:45:06Z
- Finished UTC: 2026-09-22T23:45:06Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:413949` |
| Label | `Eimeria tenella strain Houghton` |
| Rank | `STRAIN` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5802` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/eimeria_tenella_strain_houghton.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/efibula_americana.yaml data/taxa/eukaryota/eimeria_maxima.yaml data/taxa/eukaryota/eimeria_tenella.yaml data/taxa/eukaryota/eimeria_tenella_strain_houghton.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with three organism assertions, one exact native GOLD organism, three native GOLD projects, two native GOLD analyses, no exact StrainInfo, NCBI type-material, NCBI merged-ID, or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:413949`, `label: Eimeria tenella strain Houghton`, `rank: STRAIN`, `parent_taxon: NCBITaxon:5802`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:90511`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Eimeria tenella`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:34821`, which records three retained direct organisms for `NCBITaxon:413949`; this agrees with `source_attestations[1].assertion_count: 3` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:413949`. The YAML carries the one exact synonym filed for this NCBI row; NCBI supplies no related or broad synonyms and no old-ID side rows.

The current native GOLD catalogs contain one exact organism row, `Go0002374` for `Eimeria tenella Houghton`, three linked projects, and two analyses tied to `Gp0002378` and `Gp0100794`.

There are no exact rows for this taxon in the StrainInfo side inventory, NCBI type-material table, BacDive, or the maintained final strain tables. `strain_count: 0` is therefore consistent with no generated child strains in the output.

The parent `Eimeria tenella` record does not gather descendant evidence, so this strain-level record owns the Houghton-specific NCBI and GOLD evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/eimeria_tenella_strain_houghton.yaml` plus `just validate-strict data/taxa/eukaryota/eimeria_tenella_strain_houghton.yaml`.

## Additional Notes

The retained GOLD aggregate count of three is larger than the one current exact row in the local native GOLD organism catalog. The generated YAML follows the retained aggregate input that seeded the record.
