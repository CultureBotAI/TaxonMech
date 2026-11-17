# YAML Record Review: Epichloe uncinata

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/epichloe_uncinata.yaml
- Started UTC: 2026-09-23T00:45:10Z
- Finished UTC: 2026-09-23T00:45:10Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5050` |
| Label | `Epichloe uncinata` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5112` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/epichloe_uncinata.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/epichloe_typhina_subsp_clarkii.yaml data/taxa/eukaryota/epichloe_typhina_subsp_typhina.yaml data/taxa/eukaryota/epichloe_uncinata.yaml data/taxa/eukaryota/epicoccum_andropogonis.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, two exact native GOLD organism/project rows, one linked native GOLD analysis row, two NCBI type-material rows, 16 exact StrainInfo rows with 18 deposits, no exact BacDive rows, no NCBI merged-ID rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5050`, `label: Epichloe uncinata`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5112`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2205`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Epichloe` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37403`, which records two retained direct organisms for `NCBITaxon:5050`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5050`. The YAML preserves NCBI's two exact synonyms, `Acremonium uncinatum` and `Neotyphodium uncinatum`, plus its two related nomenclatural synonyms.

The native GOLD catalogs contain two exact organism rows, `Go0041954` for `Epichloe uncinata CBS 102646` and `Go0116574` for `Epichloe uncinata e167`, with matching projects `Gp0041954` and `Gp0120998`; project `Gp0120998` links to one native GOLD analysis row. NCBI type-material evidence contributes the `CBS 235.89` and `CBS:235.89` holotype aliases for `Acremonium uncinatum`.

StrainInfo contains 16 exact target rows with 18 deposit designations for `Epichloe uncinata`; those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI exact synonyms, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/epichloe_uncinata.yaml` plus `just validate-strict data/taxa/eukaryota/epichloe_uncinata.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the two current native GOLD organism rows. The NCBI type-material table contributes evidence but does not create child strain records by itself.
