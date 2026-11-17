# YAML Record Review: Furcasterigmium furcatum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/furcasterigmium_furcatum.yaml
- Started UTC: 2026-09-23T02:05:40Z
- Finished UTC: 2026-09-23T02:05:40Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2710536` |
| Label | `Furcasterigmium furcatum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2710535` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/furcasterigmium_furcatum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/funneliformis_mosseae.yaml data/taxa/eukaryota/furcasterigmium_furcatum.yaml data/taxa/eukaryota/fusarium_acuminatum.yaml data/taxa/eukaryota/fusarium_agapanthi.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one current native GOLD organism row with one linked project, one native GOLD analysis row linked by project ID, 28 direct StrainInfo rows, 35 StrainInfo deposit rows, six NCBI type-material rows, one NCBI merged-ID side row, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2710536`, `label: Furcasterigmium furcatum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2710535`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:545963`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Furcasterigmium` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:25087`, which records one retained direct organism for `NCBITaxon:2710536`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2710536`. The YAML preserves NCBI's exact synonym `Acremonium furcatum` plus the related synonyms `Acremonium furcatum C. Moreau & Moreau ex W. Gams, 1969` and `Furcasterigmium furcatum (C. Moreau & Moreau ex W. Gams) Giraldo Lopez & Crous, 2019`.

`data/raw/ncbi_merged_ids.tsv:78817` maps the old side-inventory ID `NCBITaxon:45276` to `NCBITaxon:2710536`; it is not retained as a row with `retired_into` in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies one organism assertion; the current native GOLD catalogs still contain one exact organism row, one linked project row, and one linked analysis row for the target NCBI taxon.

NCBI type-material rows 112266-112271 list six type-material designations for `Acremonium furcatum`, covering CBS 122.42, IAM 14647, and MUCL 9745 variants; StrainInfo contains exact side evidence for the target in both the direct SI-ID view and the deposit view. Those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/furcasterigmium_furcatum.yaml` plus `just validate-strict data/taxa/eukaryota/furcasterigmium_furcatum.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries. The NCBI merged-ID side row is side evidence only; generated `replaces` comes from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`.
