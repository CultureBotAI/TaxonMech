# YAML Record Review: Fusarium anguioides

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_anguioides.yaml
- Started UTC: 2026-09-23T02:08:30Z
- Finished UTC: 2026-09-23T02:08:30Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:183586` |
| Label | `Fusarium anguioides` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2692620` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_anguioides.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_albosuccineum.yaml data/taxa/eukaryota/fusarium_algeriense.yaml data/taxa/eukaryota/fusarium_ambrosium.yaml data/taxa/eukaryota/fusarium_anguioides.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one current native GOLD organism row with one linked project, one native GOLD analysis row linked by project ID, three direct StrainInfo rows, five StrainInfo deposit rows, seven NCBI type-material rows, no NCBI merged-ID side rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:183586`, `label: Fusarium anguioides`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2692620`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:36584`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium concolor species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:16270`, which records one retained direct organism for `NCBITaxon:183586`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:183586`. The YAML preserves NCBI's related synonym `Fusarium anguioides Sherb., 1915`.

No NCBI merged-ID side rows point to `NCBITaxon:183586`, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies one organism assertion; the current native GOLD catalogs still contain one exact organism row, one linked project row, and one linked analysis row for the target NCBI taxon.

NCBI type-material rows 63194-63200 list seven culture-from-neotype designations for `Fusarium anguioides`, covering ATCC 66485, MRC 7143, and NRRL 25385 variants; StrainInfo contains exact side evidence for the target in both the direct SI-ID view and the deposit view. Those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_anguioides.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_anguioides.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
