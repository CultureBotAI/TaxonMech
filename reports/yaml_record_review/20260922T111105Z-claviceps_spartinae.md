# YAML Record Review: Claviceps spartinae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/claviceps_spartinae.yaml
- Started UTC: 2026-09-22T11:05:00Z
- Finished UTC: 2026-09-22T11:11:05Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1294630` |
| Label | `Claviceps spartinae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5110` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/claviceps_spartinae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/claviceps_spartinae.yaml` | Passed; the strict validator exited successfully for one file. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one exact native GOLD organism/project/analysis chain, two NCBI type-material rows, no raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1294630`, `label: Claviceps spartinae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5110`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:304409`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Claviceps`; the bounded scan checked all 16 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is also supported. `data/raw/gold_organisms.tsv:6935` records one organism for `NCBITaxon:1294630`, and the native GOLD chain includes organism `Go0631396`, project `Gp0644824`, and analysis `Claviceps spartinae CCC 535` for taxon `1294630`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1294630` with one name assertion. NCBI supplies the exact synonym `Claviceps purpurea var. spartinae` and the three related synonyms present in the YAML, and the curation-history source list agrees with the two retained source attestations.

The NCBI type-material side inventory has two exact rows for this species, both holotype spellings of `RUTPP 3419`. Those rows support an external type-material relationship for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

StrainInfo has an exact species-level entry, `siID 404356`, with one non-type DSM deposit. Because no generated rows exist for `NCBITaxon:1294630` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:1294630` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/claviceps_spartinae.yaml` plus `just validate-strict data/taxa/eukaryota/claviceps_spartinae.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv:91647` records old ID `NCBITaxon:676012` as merged into `NCBITaxon:1294630`; no retained old-ID row exists for this target, so the generated YAML correctly omits `replaces`.
