# YAML Record Review: Clonostachys pityrodes

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/clonostachys_pityrodes.yaml
- Started UTC: 2026-09-22T11:51:55Z
- Finished UTC: 2026-09-22T11:55:07Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:110584` |
| Label | `Clonostachys pityrodes` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:110564` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/clonostachys_pityrodes.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/clonostachys_pityrodes.yaml` | Passed; the strict validator exited successfully for one file. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one NCBI merged-ID side row, exact StrainInfo species/deposit matches, no current native GOLD exact rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:110584`, `label: Clonostachys pityrodes`, `rank: SPECIES`, `parent_taxon: NCBITaxon:110564`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:19926`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Clonostachys`; the bounded scan checked all 16 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:1959`, which records one retained organism for `NCBITaxon:110584`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:110584` with one name assertion. NCBI supplies the two exact synonyms `Bionectria pityrodes` and `Nectria pityrodes`, plus the related synonym `Clonostachys pityrodes Schroers, 2001`, and the curation-history source list agrees with the two retained source attestations.

The NCBI type-material side inventory has no exact rows for this taxon.

StrainInfo has exact species-level side inventory rows, including deposits for `CBS 102033`, `CBS 381.77`, `CBS 246.78`, `CBS 249.78`, and `CBS 322.78` among the sampled rows. Because no generated rows exist for `NCBITaxon:110584` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:110584` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/clonostachys_pityrodes.yaml` plus `just validate-strict data/taxa/eukaryota/clonostachys_pityrodes.yaml`.

## Additional Notes

The retained aggregate GOLD table has a row for this taxon even though the local native GOLD `organisms.jsonl.gz`, `projects.jsonl.gz`, and `analyses.jsonl.gz` exact joins did not contain a current organism, project, or analysis for `110584`. That difference is confined to the supporting inventories; the YAML only asserts one aggregate `GOLD` source attestation.

`data/raw/ncbi_merged_ids.tsv:21428` records old ID `NCBITaxon:160301` as merged into `NCBITaxon:110584`; no retained old-ID row exists for this target, so the generated YAML correctly omits `replaces`.
