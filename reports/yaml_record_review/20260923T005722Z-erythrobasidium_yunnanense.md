# YAML Record Review: Erythrobasidium yunnanense

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/erythrobasidium_yunnanense.yaml
- Started UTC: 2026-09-23T00:57:22Z
- Finished UTC: 2026-09-23T00:57:22Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:114840` |
| Label | `Erythrobasidium yunnanense` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5413` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/erythrobasidium_yunnanense.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/erythrobasidium_yunnanense.yaml data/taxa/eukaryota/erythrolobus_australicus.yaml data/taxa/eukaryota/erythrolobus_madagascarensis.yaml data/taxa/eukaryota/escovopsis_weberi.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism/project/analysis row, nine NCBI type-material rows, one exact StrainInfo row with five deposits, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:114840`, `label: Erythrobasidium yunnanense`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5413`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:20888`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Erythrobasidium` genus; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:3018`, which records one retained direct organism for `NCBITaxon:114840`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:114840`. The YAML preserves NCBI's exact synonym `Sporobolomyces yunnanensis` plus two related nomenclatural synonyms; NCBI supplies no broad synonyms and no old-ID side rows.

The native GOLD catalogs contain one exact organism row, `Go0138939` for `Erythrobasidium yunnanense JCM 10687`, with one matching project, `Gp0143996`, and one native GOLD analysis row linked through `AP PROJECT GOLD IDS: Gp0143996`.

NCBI type-material evidence contributes nine aliases for `Sporobolomyces yunnanensis`, spanning AS 2.2090, CBS 8906, CGMCC 2.2090, and JCM 10687 variants. StrainInfo contains one exact target row with five deposit designations for `Erythrobasidium yunnanense`; that side row does not produce BacDive-derived local strain children for this taxon.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/erythrobasidium_yunnanense.yaml` plus `just validate-strict data/taxa/eukaryota/erythrobasidium_yunnanense.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the one current native GOLD organism row. The native GOLD analysis row links through `AP PROJECT GOLD IDS` to current project `Gp0143996`.
