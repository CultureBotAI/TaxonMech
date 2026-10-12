# YAML Record Review: Clitopilus hobsonii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/clitopilus_hobsonii.yaml
- Started UTC: 2026-09-22T11:23:25Z
- Finished UTC: 2026-09-22T11:27:52Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:648681` |
| Label | `Clitopilus hobsonii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:71935` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/clitopilus_hobsonii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/clitopilus_hobsonii.yaml` | Passed; the strict validator exited successfully for one file. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one exact native GOLD organism/project/analysis chain, four NCBI type-material rows, exact StrainInfo entries, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:648681`, `label: Clitopilus hobsonii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:71935`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:149711`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Clitopilus`; the bounded scan checked all 14 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is also supported. `data/raw/gold_organisms.tsv:40397` records one organism for `NCBITaxon:648681`, and the native GOLD chain includes organism `Go0589422`, project `Gp0603368`, and analysis `Clitopilus hobsonii QYL-10`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:648681` with one name assertion. NCBI supplies the exact synonym `Agaricus hobsonii` and the six related synonyms present in the YAML, and the curation-history source list agrees with the two retained source attestations.

The NCBI type-material side inventory has four exact rows for this species under the synonym `Agaricus hobsonii`: epitype spellings for `K(M) 122842` and holotype spellings for `K(M) 39990`. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

StrainInfo has four exact species-level entries with one non-type deposit each. Because no generated rows exist for `NCBITaxon:648681` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:648681` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/clitopilus_hobsonii.yaml` plus `just validate-strict data/taxa/eukaryota/clitopilus_hobsonii.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` records old IDs `NCBITaxon:1332779`, `NCBITaxon:1332780`, `NCBITaxon:1332781`, and `NCBITaxon:1332782` as merged into `NCBITaxon:648681`; no retained old-ID row exists for this target, so the generated YAML correctly omits `replaces`.
