# YAML Record Review: Helvella lacunosa

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/helvella_lacunosa.yaml
- Started UTC: 2026-09-23T06:25:39Z
- Finished UTC: 2026-09-23T06:25:39Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:44625` |
| Label | `Helvella lacunosa` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:44624` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/helvella_lacunosa.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/helotiales_sp_ef0021.yaml data/taxa/eukaryota/helvella_lacunosa.yaml data/taxa/eukaryota/hemiaulus_hauckii.yaml data/taxa/eukaryota/hemileccinum_impolitum.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, no exact current native GOLD organisms, two exact NCBI epitype rows, no side NCBI merged-ID rows, one direct exact StrainInfo row with two deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:44625`, `label: Helvella lacunosa`, `rank: SPECIES`, `parent_taxon: NCBITaxon:44624`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:5422`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Helvella`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:35727`, which records two retained direct organisms for `NCBITaxon:44625`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:44625`. Both generated related synonyms are present in `data/raw/ncbitaxon_taxa.tsv:5422` as related synonyms.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs do not have exact organism rows for `NCBITaxon:44625`, so there are no linked native projects or analyses for the target in the local native GOLD side evidence.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:212740` and `data/raw/ncbi_type_material.tsv:212741` as epitype designations for `C Fungi Exs. Suec. 2065 (H407)` and `C-Fungi Exs. Suec. 2065`.

StrainInfo has one direct exact row with two deposit rows for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

No side NCBI merged-ID row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/helvella_lacunosa.yaml` plus `just validate-strict data/taxa/eukaryota/helvella_lacunosa.yaml`.

## Additional Notes

No prior exact ignored review report existed for `helvella_lacunosa` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; it can differ from the current native GOLD catalog scan, and native GOLD side rows do not create generated child strains without BacDive-derived local strain inventory entries.
