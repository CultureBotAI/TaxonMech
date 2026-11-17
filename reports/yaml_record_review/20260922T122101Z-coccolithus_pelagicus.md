# YAML Record Review: Coccolithus pelagicus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/coccolithus_pelagicus.yaml
- Started UTC: 2026-09-22T12:17:32Z
- Finished UTC: 2026-09-22T12:21:01Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:97492` |
| Label | `Coccolithus pelagicus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:97491` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/coccolithus_pelagicus.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/coccolithus_pelagicus.yaml` | Passed; the strict validator reported 0 errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained organisms, exact StrainInfo species/deposit matches, no current native GOLD exact rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:97492`, `label: Coccolithus pelagicus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:97491`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:16459`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Coccolithus`; the bounded scan checked all nine ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:45160`, which records two retained organisms for `NCBITaxon:97492`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:97492` with one name assertion. NCBI supplies the exact synonym `Coccosphaera pelagica` and both related synonyms present in the YAML, and the curation-history source list agrees with the two retained source attestations.

StrainInfo has two exact species-level entries with `CCAP 913/2` and `CCAP 913/3` deposits. Because no generated rows exist for `NCBITaxon:97492` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:97492` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/coccolithus_pelagicus.yaml` plus `just validate-strict data/taxa/eukaryota/coccolithus_pelagicus.yaml`.

## Additional Notes

The retained aggregate GOLD table has a row for this taxon even though the local native GOLD `organisms.jsonl.gz`, `projects.jsonl.gz`, and `analyses.jsonl.gz` exact joins did not contain a current organism, project, or analysis for `97492`. That difference is confined to the supporting inventories; the YAML correctly follows the retained aggregate `GOLD` source attestation.

No `data/raw/ncbi_type_material.tsv` or `data/raw/ncbi_merged_ids.tsv` side rows exist for `NCBITaxon:97492`.
