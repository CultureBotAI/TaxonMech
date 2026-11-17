# YAML Record Review: Coccolithus braarudii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/coccolithus_braarudii.yaml
- Started UTC: 2026-09-22T12:17:32Z
- Finished UTC: 2026-09-22T12:21:01Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:221442` |
| Label | `Coccolithus braarudii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:97491` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/coccolithus_braarudii.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/coccolithus_braarudii.yaml` | Passed; the strict validator reported 0 errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one current native GOLD organism row, exact StrainInfo species/deposit matches, no native GOLD projects or analyses, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:221442`, `label: Coccolithus braarudii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:97491`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:43633`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Coccolithus`; the bounded scan checked all nine ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:21043`, which records one retained organism for `NCBITaxon:221442`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:221442` with one name assertion. NCBI supplies the two exact synonyms and three related synonyms in the YAML, and the curation-history source list agrees with the two retained source attestations.

The native GOLD snapshot has one exact organism row for `Coccolithus braarudii PLY182g` on organism `Go0368623`; no native GOLD project or analysis rows are currently linked to that organism.

StrainInfo has seven exact species-level entries, including deposits for `RCC 1197`, `RCC 1200`, `RCC 1202`, `RCC 1203`, and `RCC 1198` among the sampled rows. Because no generated rows exist for `NCBITaxon:221442` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:221442` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/coccolithus_braarudii.yaml` plus `just validate-strict data/taxa/eukaryota/coccolithus_braarudii.yaml`.

## Additional Notes

No `data/raw/ncbi_type_material.tsv` or `data/raw/ncbi_merged_ids.tsv` side rows exist for `NCBITaxon:221442`.
