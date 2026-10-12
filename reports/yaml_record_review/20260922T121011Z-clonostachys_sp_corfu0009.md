# YAML Record Review: Clonostachys sp. CORFU0009

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/clonostachys_sp_corfu0009.yaml
- Started UTC: 2026-09-22T12:06:38Z
- Finished UTC: 2026-09-22T12:10:11Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2789332` |
| Label | `Clonostachys sp. CORFU0009` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2628127` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/clonostachys_sp_corfu0009.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/clonostachys_sp_corfu0009.yaml` | Passed; the strict validator exited successfully for one file. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one current native GOLD organism row, two native GOLD project rows, no native GOLD analyses, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2789332`, `label: Clonostachys sp. CORFU0009`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2628127`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:555403`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `unclassified Clonostachys`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species-level ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:26582`, which records one retained organism for `NCBITaxon:2789332`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2789332` with one name assertion. NCBI does not supply generated exact, broad, or related synonyms for this taxon, so the YAML correctly has no `synonyms` block.

The native GOLD snapshot has one exact organism row for `Clonostachys sp. CORFU 0009` on organism `Go0529090`, plus a transcriptome project `Gp0457398` and a standard draft project `Gp0466640`. No native GOLD analysis rows are currently linked to those projects.

The bounded scan found no exact NCBI type-material rows, no exact StrainInfo species entry, and no generated rows for `NCBITaxon:2789332` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:2789332` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/clonostachys_sp_corfu0009.yaml` plus `just validate-strict data/taxa/eukaryota/clonostachys_sp_corfu0009.yaml`.

## Additional Notes

No `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, or exact StrainInfo side rows exist for `NCBITaxon:2789332`.
