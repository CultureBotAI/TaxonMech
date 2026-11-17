# YAML Record Review: Fodinomyces uranophilus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fodinomyces_uranophilus.yaml
- Started UTC: 2026-09-23T01:48:59Z
- Finished UTC: 2026-09-23T01:48:59Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1199092` |
| Label | `Fodinomyces uranophilus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1578798` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fodinomyces_uranophilus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/florenciella_parvula.yaml data/taxa/eukaryota/fodinomyces_uranophilus.yaml data/taxa/eukaryota/fomes_fomentarius.yaml data/taxa/eukaryota/fomitiporia_mediterranea.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, one current native GOLD organism row with two linked projects, five NCBI type-material rows, one NCBI merged-ID side row, no current exact native GOLD analyses, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1199092`, `label: Fodinomyces uranophilus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1578798`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:270168`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fodinomyces` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:4804`, which records two retained direct organisms for `NCBITaxon:1199092`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1199092`. The YAML preserves three NCBI related synonyms for the current name and source `Teratosphaeriaceae sp.` labels.

`data/raw/ncbi_merged_ids.tsv:18149` maps the old side-inventory ID `NCBITaxon:1505964` to `NCBITaxon:1199092`; it is not retained as a row with `retired_into` in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies two organism assertions, and the current native GOLD catalogs still contain one exact organism row and two linked project rows for the target NCBI taxon.

NCBI type-material rows 13282-13286 list five holotype designations for `Fodinomyces uranophilus`. No exact BacDive, StrainInfo, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, three NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive or StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI or GOLD inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fodinomyces_uranophilus.yaml` plus `just validate-strict data/taxa/eukaryota/fodinomyces_uranophilus.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism and project rows are exact by NCBI taxon ID but are side evidence only and can differ from the retained aggregate used to generate source attestations. The NCBI merged-ID side row is side evidence only; generated `replaces` comes from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`.
