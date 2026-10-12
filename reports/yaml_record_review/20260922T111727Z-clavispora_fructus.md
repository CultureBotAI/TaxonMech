# YAML Record Review: Clavispora fructus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/clavispora_fructus.yaml
- Started UTC: 2026-09-22T11:11:06Z
- Finished UTC: 2026-09-22T11:17:27Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:46582` |
| Label | `Clavispora fructus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:36910` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/clavispora_fructus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/clavispora_fructus.yaml` | Passed; the strict validator exited successfully for one file. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, two exact native GOLD organism/project rows with one analysis, 26 NCBI type-material rows, exact StrainInfo entries, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:46582`, `label: Clavispora fructus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:36910`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:5855`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Clavispora`; the bounded scan checked all 13 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported. `data/raw/gold_organisms.tsv:36322` records two organisms for `NCBITaxon:46582`, and the native GOLD snapshot has exact organism/project rows for `NRRL Y-17072` and `NRRL Y-17088`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:46582` with one name assertion. NCBI supplies the four exact synonyms and six related synonyms present in the YAML, and the curation-history source list agrees with the two retained source attestations.

The NCBI type-material side inventory has 26 exact rows under the historical names `Torulopsis fructus` and `Torulopsis musae`, covering normalized forms of `MUCL 29830`, `AJ 4401`, `ATCC 24122`, `CBS 6380`, `NRRL Y-17072`, `CBS 6381`, and `NRRL Y-17088`. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

StrainInfo has seven exact species-level entries with 32 deposits. Because no generated rows exist for `NCBITaxon:46582` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `12`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:46582` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/clavispora_fructus.yaml` plus `just validate-strict data/taxa/eukaryota/clavispora_fructus.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` records old IDs `NCBITaxon:2315448` and `NCBITaxon:45355` as merged into `NCBITaxon:46582`; no retained old-ID row exists for this target, so the generated YAML correctly omits `replaces`.
