# YAML Record Review: Clitopilus passeckerianus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/clitopilus_passeckerianus.yaml
- Started UTC: 2026-09-22T11:23:25Z
- Finished UTC: 2026-09-22T11:27:52Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:648682` |
| Label | `Clitopilus passeckerianus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:71935` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/clitopilus_passeckerianus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/clitopilus_passeckerianus.yaml` | Passed; the strict validator exited successfully for one file. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, exact StrainInfo entries, no current native GOLD exact rows, no NCBI type-material rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:648682`, `label: Clitopilus passeckerianus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:71935`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:149712`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Clitopilus`; the bounded scan checked all 14 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:40398`, which records one retained organism for `NCBITaxon:648682`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:648682` with one name assertion. NCBI supplies the exact synonym `Pleurotus passeckerianus` and the two related synonyms present in the YAML, and the curation-history source list agrees with the two retained source attestations.

StrainInfo has four exact species-level entries with 14 deposits. Because no generated rows exist for `NCBITaxon:648682` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:648682` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/clitopilus_passeckerianus.yaml` plus `just validate-strict data/taxa/eukaryota/clitopilus_passeckerianus.yaml`.

## Additional Notes

The retained aggregate GOLD table has a row for this taxon even though the local native GOLD `organisms.jsonl.gz`, `projects.jsonl.gz`, and `analyses.jsonl.gz` exact joins did not contain a current organism, project, or analysis for `648682`. That difference is confined to the supporting inventories; the YAML only asserts one aggregate `GOLD` source attestation.
