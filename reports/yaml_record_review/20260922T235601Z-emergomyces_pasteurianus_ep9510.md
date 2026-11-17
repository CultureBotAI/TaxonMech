# YAML Record Review: Emergomyces pasteurianus Ep9510

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/emergomyces_pasteurianus_ep9510.yaml
- Started UTC: 2026-09-22T23:56:01Z
- Finished UTC: 2026-09-22T23:56:01Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1447872` |
| Label | `Emergomyces pasteurianus Ep9510` |
| Rank | `STRAIN` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1955774` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/emergomyces_pasteurianus_ep9510.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/emergomyces_pasteurianus_ep9510.yaml data/taxa/eukaryota/emericellopsis_atlantica.yaml data/taxa/eukaryota/emericellopsis_fuci.yaml data/taxa/eukaryota/emericellopsis_maritima.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism/project/analysis chain, no NCBI type-material or merged-ID rows, no exact StrainInfo or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1447872`, `label: Emergomyces pasteurianus Ep9510`, `rank: STRAIN`, `parent_taxon: NCBITaxon:1955774`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:364875`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the parent species, `Emergomyces pasteurianus`; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:10881`, which records one retained direct organism for `NCBITaxon:1447872`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1447872`. The YAML preserves NCBI's exact synonyms `Emergomyces pasteuriana Ep9510` and `Emmonsia pasteuriana UAMH 9510`, plus the related synonym `Emmonsia pasteuriana Ep9510`; NCBI supplies no broad synonyms or old-ID side rows.

The native GOLD catalogs contain one exact organism row, `Go0373217` for `Emergomyces pasteurianus Ep9510`, with the culture collection ID `UAMH 9510`, the strain value `Ep9510`, one matching project, `Gp0220021`, and one matching analysis row linked through that project.

No exact StrainInfo, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI exact synonyms, one NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/emergomyces_pasteurianus_ep9510.yaml` plus `just validate-strict data/taxa/eukaryota/emergomyces_pasteurianus_ep9510.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the one current native GOLD organism row.
