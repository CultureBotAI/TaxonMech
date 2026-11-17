# YAML Record Review: Cokeromyces recurvatus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cokeromyces_recurvatus.yaml
- Started UTC: 2026-09-22T12:39:30Z
- Finished UTC: 2026-09-22T12:42:57Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:90255` |
| Label | `Cokeromyces recurvatus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:90254` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cokeromyces_recurvatus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cokeromyces_recurvatus.yaml` | Passed; the strict validator reported 0 errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one native GOLD organism with two projects, 13 NCBI type-material rows, exact StrainInfo species/deposit rows, no native GOLD analyses, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:90255`, `label: Cokeromyces recurvatus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:90254`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:14500`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Cokeromyces`; the bounded scan checked all 13 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:44105`, which records one retained organism for `NCBITaxon:90255`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:90255` with one name assertion. NCBI supplies the related synonym `Cokeromyces recurvatus Poitras, 1950` present in the YAML, and the curation-history source list agrees with the two retained source attestations.

The native GOLD snapshot has one exact organism, `NRRL 2243` / `Go0302458`, and two projects for this NCBI taxon: `Gp0156929` for the standard draft and `Gp0215029` for the transcriptome project. No native GOLD analysis rows are currently linked to those projects.

The NCBI type-material side inventory has 13 exact rows for this species: alternative `ATCC 42656`, `CBS 158.50`, `NRRL 2243`, and `STMA 13000` designations. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

StrainInfo has exact species-level side inventory rows, including 19 exact deposit matches and nine direct species matches. Because no generated rows exist for `NCBITaxon:90255` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:90255` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cokeromyces_recurvatus.yaml` plus `just validate-strict data/taxa/eukaryota/cokeromyces_recurvatus.yaml`.

## Additional Notes

No `data/raw/ncbi_merged_ids.tsv` side rows exist for `NCBITaxon:90255`.
