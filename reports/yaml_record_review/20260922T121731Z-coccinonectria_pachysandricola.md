# YAML Record Review: Coccinonectria pachysandricola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/coccinonectria_pachysandricola.yaml
- Started UTC: 2026-09-22T12:13:58Z
- Finished UTC: 2026-09-22T12:17:31Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1634537` |
| Label | `Coccinonectria pachysandricola` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1634536` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/coccinonectria_pachysandricola.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/coccinonectria_pachysandricola.yaml` | Passed; the strict validator reported 0 errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one current native GOLD organism/project/analysis chain, one NCBI merged-ID side row, exact StrainInfo species/deposit matches, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1634537`, `label: Coccinonectria pachysandricola`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1634536`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:425225`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Coccinonectria`; the bounded scan checked all 16 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:13996`, which records one retained organism for `NCBITaxon:1634537`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1634537` with one name assertion. NCBI supplies the two exact synonyms and three related synonyms in the YAML, and the curation-history source list agrees with the two retained source attestations.

The native GOLD snapshot has one exact organism row for `Coccinonectria pachysandricola JAC16-16` on organism `Go0520188`, one project row on `Gp0444382`, and one matching analysis row.

StrainInfo has exact species-level side inventory rows, including six exact deposit matches and five direct species matches. Because no generated rows exist for `NCBITaxon:1634537` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:1634537` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/coccinonectria_pachysandricola.yaml` plus `just validate-strict data/taxa/eukaryota/coccinonectria_pachysandricola.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv:1772` records old ID `NCBITaxon:1052025` as merged into `NCBITaxon:1634537`; no retained old-ID row exists for this target, so the generated YAML correctly omits `replaces`.
