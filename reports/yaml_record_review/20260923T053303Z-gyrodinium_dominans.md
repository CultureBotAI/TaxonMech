# YAML Record Review: Gyrodinium dominans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/gyrodinium_dominans.yaml
- Started UTC: 2026-09-23T05:33:03Z
- Finished UTC: 2026-09-23T05:33:03Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:285985` |
| Label | `Gyrodinium dominans` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:60594` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/gyrodinium_dominans.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/gyrodinium_dominans.yaml data/taxa/eukaryota/gyrodon_lividus.yaml data/taxa/eukaryota/gyromitra_esculenta.yaml data/taxa/eukaryota/haemoproteus_tartakovskyi.yaml` | Passed; the strict batch reported zero ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with no linked native GOLD projects or analyses, no exact NCBI type-material rows, no side NCBI merged-ID rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:285985`, `label: Gyrodinium dominans`, `rank: SPECIES`, `parent_taxon: NCBITaxon:60594`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:58485`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Gyrodinium`; the bounded scan checked all 9 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:27764`, which records one retained direct organism for `NCBITaxon:285985`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain exact organism `Go0368687` for strain `SPMC 103` with no linked native projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:285985`. `data/raw/ncbitaxon_taxa.tsv:58485` has no exact or broad synonyms for this species, and the generated related synonym `Gyrodinium dominans Hulburt, 1957` is present in the source row as a related synonym.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have one exact organism for `Gyrodinium dominans SPMC 103` and no linked native project or analysis rows.

No exact NCBI type-material row, side NCBI merged-ID row, exact StrainInfo row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, the one NCBI related synonym for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/gyrodinium_dominans.yaml` plus `just validate-strict data/taxa/eukaryota/gyrodinium_dominans.yaml`.

## Additional Notes

No prior exact ignored review report existed for `gyrodinium_dominans` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
