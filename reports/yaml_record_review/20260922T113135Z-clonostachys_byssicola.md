# YAML Record Review: Clonostachys byssicola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/clonostachys_byssicola.yaml
- Started UTC: 2026-09-22T11:27:53Z
- Finished UTC: 2026-09-22T11:31:35Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:160290` |
| Label | `Clonostachys byssicola` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:110564` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/clonostachys_byssicola.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/clonostachys_byssicola.yaml` | Passed; the strict validator scanned one file and reported 0 files with errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one exact native GOLD organism/project/analysis chain, no NCBI type-material rows, no final raw strain rows, no StrainInfo exact rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:160290`, `label: Clonostachys byssicola`, `rank: SPECIES`, `parent_taxon: NCBITaxon:110564`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:33086`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Clonostachys`; the bounded scan checked all 16 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is also supported. `data/raw/gold_organisms.tsv:12931` records one organism for `NCBITaxon:160290`, and the native GOLD chain includes organism `Go0632166`, project `Gp0645990`, and analysis `Clonostachys byssicola CBYS24578`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:160290` with one name assertion. NCBI supplies the exact synonym `Bionectria byssicola` and the related synonym present in the YAML, and the curation-history source list agrees with the two retained source attestations.

No NCBI type-material, BacDive, StrainInfo, or local generated strain rows are attached to `NCBITaxon:160290`, so `strain_count: 0` is consistent with the maintained inputs inspected.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:160290` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/clonostachys_byssicola.yaml` plus `just validate-strict data/taxa/eukaryota/clonostachys_byssicola.yaml`.

## Additional Notes

No additional notes.
