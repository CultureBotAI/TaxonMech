# YAML Record Review: Epichloe aotearoae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/epichloe_aotearoae.yaml
- Started UTC: 2026-09-23T00:30:41Z
- Finished UTC: 2026-09-23T00:30:41Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:170559` |
| Label | `Epichloe aotearoae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5112` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/epichloe_aotearoae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/eocronartium_muscicola.yaml data/taxa/eukaryota/ephemerocybe_angulata.yaml data/taxa/eukaryota/ephemerocybe_pellucida.yaml data/taxa/eukaryota/epichloe_aotearoae.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with seven organism assertions, two current exact native GOLD organism rows, seven current exact native GOLD project rows, one linked native GOLD analysis row, eight NCBI merged-ID side rows, six exact StrainInfo rows with six deposits, no NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:170559`, `label: Epichloe aotearoae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5112`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:34723`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Epichloe` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:14761`, which records seven retained direct organisms for `NCBITaxon:170559`; this agrees with `source_attestations[1].assertion_count: 7` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:170559`. The YAML preserves NCBI's exact synonym `Neotyphodium aotearoae`, plus all 11 related synonyms filed for this row.

The old side-inventory IDs `NCBITaxon:170560`, `NCBITaxon:170561`, `NCBITaxon:170562`, `NCBITaxon:170563`, `NCBITaxon:170564`, `NCBITaxon:170565`, `NCBITaxon:170566`, and `NCBITaxon:170567` all map to `NCBITaxon:170559` in `data/raw/ncbi_merged_ids.tsv`; none are retained as rows with `retired_into` in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly has no generated `replaces` entries.

The retained GOLD aggregate row carries seven organism assertions. The current exact native GOLD catalogs contain two organism rows, `Go0070855` and `Go0098765`, seven matching project rows, and one analysis row linked through project `Gp0070855`. StrainInfo contains six exact target rows with six deposit designations; those side rows do not produce BacDive-derived local strain children for this taxon.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, 11 NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/epichloe_aotearoae.yaml` plus `just validate-strict data/taxa/eukaryota/epichloe_aotearoae.yaml`.

## Additional Notes

The native GOLD sample was expanded by exact ID to account for all 7 current native project rows. The retained GOLD aggregate count is higher than the current native exact organism-row count, but `source_attestations[1].assertion_count: 7` matches the retained aggregate row used by the generator.
