# YAML Record Review: Climacostomum virens

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/climacostomum_virens.yaml
- Started UTC: 2026-09-22T11:23:25Z
- Finished UTC: 2026-09-22T11:27:52Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:49980` |
| Label | `Climacostomum virens` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:49979` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/climacostomum_virens.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/climacostomum_virens.yaml` | Passed; the strict validator exited successfully for one file. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one exact native GOLD organism, no NCBI type-material rows, no final raw strain rows, no StrainInfo exact rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:49980`, `label: Climacostomum virens`, `rank: SPECIES`, `parent_taxon: NCBITaxon:49979`, and `genetic_code: 10` match `data/raw/ncbitaxon_taxa.tsv:6308`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Climacostomum`; the bounded scan checked all 11 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is also supported. `data/raw/gold_organisms.tsv:37292` records one organism for `NCBITaxon:49980`, and the native GOLD snapshot has an exact organism row, `Go0368622`, for strain `Stock W-24`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:49980` with one name assertion. NCBI supplies the exact synonym `Spirostomum virens` and the two related synonyms present in the YAML, and the curation-history source list agrees with the two retained source attestations.

No NCBI type-material, BacDive, StrainInfo, or local generated strain rows are attached to `NCBITaxon:49980`, so `strain_count: 0` is consistent with the maintained inputs inspected.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `10`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:49980` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/climacostomum_virens.yaml` plus `just validate-strict data/taxa/eukaryota/climacostomum_virens.yaml`.

## Additional Notes

The native GOLD snapshot has no exact project or analysis rows for organism `Go0368622`; that is consistent with the YAML, which only records the aggregate organism-level GOLD source attestation.
