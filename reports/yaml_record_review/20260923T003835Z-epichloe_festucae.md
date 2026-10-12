# YAML Record Review: Epichloe festucae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/epichloe_festucae.yaml
- Started UTC: 2026-09-23T00:38:35Z
- Finished UTC: 2026-09-23T00:38:35Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:35717` |
| Label | `Epichloe festucae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5112` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/epichloe_festucae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/epichloe_festucae.yaml data/taxa/eukaryota/epichloe_festucae_fl1.yaml data/taxa/eukaryota/epichloe_festucae_var_lolii.yaml data/taxa/eukaryota/epichloe_funkii.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with four organism assertions, three current exact native GOLD organism rows, six current exact native GOLD project rows, two linked native GOLD analysis rows, 33 exact StrainInfo rows with 36 deposits, no NCBI type-material rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:35717`, `label: Epichloe festucae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5112`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:3931`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Epichloe` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:33119`, which records four retained direct organisms for `NCBITaxon:35717`; this agrees with `source_attestations[1].assertion_count: 4` and the note that records are filed directly under this taxon rather than gathered from descendants.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:35717`. The YAML preserves NCBI's one related synonym, `Epichloe festucae Leuchtm., Schardl & M.R. Siegel, 1995`; NCBI supplies no exact or broad synonyms and no old-ID side rows.

The retained GOLD aggregate row carries four direct organism assertions. The current exact native GOLD catalogs contain three organism rows, `Go0003234`, `Go0098776`, and `Go0384522`, six matching project rows, and two analysis rows linked through projects `Gp0235629` and `Gp0444359`.

StrainInfo contains 33 exact target rows with 36 deposit designations for `Epichloe festucae`; those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive, NCBI type-material, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/epichloe_festucae.yaml` plus `just validate-strict data/taxa/eukaryota/epichloe_festucae.yaml`.

## Additional Notes

The native GOLD sample was expanded by exact ID to account for all 6 current native project rows. The retained GOLD aggregate count is higher than the current native exact organism-row count, but `source_attestations[1].assertion_count: 4` matches the retained aggregate row used by the generator.
