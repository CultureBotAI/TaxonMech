# YAML Record Review: Heterocapsa arctica

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/heterocapsa_arctica.yaml
- Started UTC: 2026-09-23T06:49:37Z
- Finished UTC: 2026-09-23T06:49:37Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:192219` |
| Label | `Heterocapsa arctica` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2918` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/heterocapsa_arctica.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/heterobasidion_annosum.yaml data/taxa/eukaryota/heterobasidion_irregulare.yaml data/taxa/eukaryota/heterobasidion_parviporum.yaml data/taxa/eukaryota/heterocapsa_arctica.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with no linked native GOLD projects or analyses, no exact NCBI type-material rows, no side NCBI merged-ID rows, one direct exact StrainInfo row with two deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:192219`, `label: Heterocapsa arctica`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2918`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:38236`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Heterocapsa`; the bounded scan checked all 9 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:17573`, which records one retained direct organism for `NCBITaxon:192219`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:192219`. `Heterocapsa arctica Horiguchi, 1997` is present in `data/raw/ncbitaxon_taxa.tsv:38236` as a related synonym, and the source row has no exact synonyms to omit.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have an exact `Go0368699` organism for `CCMP 445` and no linked native GOLD project or analysis rows.

StrainInfo has one direct exact row for this taxon, with `CCMP445` and `CCMP35` as deposits. That side-inventory row is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

No NCBI type-material row, side NCBI merged-ID row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/heterocapsa_arctica.yaml` plus `just validate-strict data/taxa/eukaryota/heterocapsa_arctica.yaml`.

## Additional Notes

No prior exact ignored review report existed for `heterocapsa_arctica` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism row is exact by NCBI taxon ID but is side evidence only and does not create generated child strains without BacDive-derived local strain inventory entries.
