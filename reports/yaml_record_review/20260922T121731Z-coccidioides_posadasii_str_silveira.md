# YAML Record Review: Coccidioides posadasii str. Silveira

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/coccidioides_posadasii_str_silveira.yaml
- Started UTC: 2026-09-22T12:13:58Z
- Finished UTC: 2026-09-22T12:17:31Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:443226` |
| Label | `Coccidioides posadasii str. Silveira` |
| Rank | `STRAIN` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:199306` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/coccidioides_posadasii_str_silveira.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/coccidioides_posadasii_str_silveira.yaml` | Passed; the strict validator reported 0 errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained organisms, two exact native GOLD organism/project/analysis chains, no NCBI type-material rows, no exact StrainInfo species entry, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:443226`, `label: Coccidioides posadasii str. Silveira`, `rank: STRAIN`, `parent_taxon: NCBITaxon:199306`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:98515`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Coccidioides posadasii`; the bounded scan checked all 16 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:35645`, which records two retained organisms for `NCBITaxon:443226`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:443226` with one name assertion. NCBI does not supply generated exact, broad, or related synonyms for this strain-rank taxon, so the YAML correctly has no `synonyms` block.

The native GOLD snapshot has exact organism, project, and analysis rows for `Coccidioides posadasii Silveria` and `Coccidioides posadasii Silveira`, matching the aggregate count of two retained organisms for this NCBI strain ID.

The bounded scan found no exact NCBI type-material rows, no exact StrainInfo species entry, and no generated rows for `NCBITaxon:443226` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:443226` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/coccidioides_posadasii_str_silveira.yaml` plus `just validate-strict data/taxa/eukaryota/coccidioides_posadasii_str_silveira.yaml`.

## Additional Notes

No `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, or exact StrainInfo side rows exist for `NCBITaxon:443226`.
