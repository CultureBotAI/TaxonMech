# YAML Record Review: Clonostachys samuelsii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/clonostachys_samuelsii.yaml
- Started UTC: 2026-09-22T12:03:02Z
- Finished UTC: 2026-09-22T12:06:37Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:160306` |
| Label | `Clonostachys samuelsii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:110564` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/clonostachys_samuelsii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/clonostachys_samuelsii.yaml` | Passed; the strict validator reported 0 errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, two NCBI merged-ID side rows, no current native GOLD exact rows, no exact StrainInfo species entry, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:160306`, `label: Clonostachys samuelsii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:110564`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:33093`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Clonostachys`; the bounded scan checked all 16 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:12942`, which records one retained organism for `NCBITaxon:160306`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:160306` with one name assertion. NCBI supplies the exact synonym `Bionectria samuelsii` and both related synonyms present in the YAML, `Bionectria sp. CBS700.97` and `Clonostachys samuelsii Schroers, 2001`, and the curation-history source list agrees with the two retained source attestations.

The bounded scan found no exact NCBI type-material rows, no exact StrainInfo species entry, and no generated rows for `NCBITaxon:160306` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:160306` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/clonostachys_samuelsii.yaml` plus `just validate-strict data/taxa/eukaryota/clonostachys_samuelsii.yaml`.

## Additional Notes

The retained aggregate GOLD table has a row for this taxon even though the local native GOLD `organisms.jsonl.gz`, `projects.jsonl.gz`, and `analyses.jsonl.gz` exact joins did not contain a current organism, project, or analysis for `160306`. That difference is confined to the supporting inventories; the YAML only asserts one aggregate `GOLD` source attestation.

`data/raw/ncbi_merged_ids.tsv` records old IDs `NCBITaxon:122409` and `NCBITaxon:160314` as merged into `NCBITaxon:160306`; no retained old-ID rows exist for this target, so the generated YAML correctly omits `replaces`.
