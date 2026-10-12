# YAML Record Review: Helicogloea dryina

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/helicogloea_dryina.yaml
- Started UTC: 2026-09-23T06:18:56Z
- Finished UTC: 2026-09-23T06:18:56Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2184190` |
| Label | `Helicogloea dryina` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:48855` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/helicogloea_dryina.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/helicodendron_triglitziense.yaml data/taxa/eukaryota/helicogloea_compressa.yaml data/taxa/eukaryota/helicogloea_dryina.yaml data/taxa/eukaryota/helicostylum_elegans.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, no exact current native GOLD organisms, one exact NCBI holotype row, no side NCBI merged-ID rows, no exact BacDive or StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2184190`, `label: Helicogloea dryina`, `rank: SPECIES`, `parent_taxon: NCBITaxon:48855`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:521140`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Helicogloea`; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:20817`, which records one retained direct organism for `NCBITaxon:2184190`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2184190`. The generated related synonym `Helicogloea dryina Spirin & Miettinen, 2018` is present in `data/raw/ncbitaxon_taxa.tsv:521140`.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs do not have exact organism rows for `NCBITaxon:2184190`, so there are no linked native projects or analyses for the target in the local native GOLD side evidence.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:87270` as a holotype designation for `O:collector:Svantesson:786`.

No side NCBI merged-ID row, exact BacDive row, exact StrainInfo row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, the NCBI related synonym for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive or StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/helicogloea_dryina.yaml` plus `just validate-strict data/taxa/eukaryota/helicogloea_dryina.yaml`.

## Additional Notes

No prior exact ignored review report existed for `helicogloea_dryina` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; it can differ from the current native GOLD catalog scan, and native GOLD side rows do not create generated child strains without BacDive-derived local strain inventory entries.
