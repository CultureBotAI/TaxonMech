# YAML Record Review: Colletotrichum chlorophyti

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colletotrichum_chlorophyti.yaml
- Started UTC: 2026-09-22T12:52:25Z
- Finished UTC: 2026-09-22T12:55:40Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:708187` |
| Label | `Colletotrichum chlorophyti` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5455` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colletotrichum_chlorophyti.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/colletotrichum_chlorophyti.yaml` | Passed; the strict validator reported 0 errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one native GOLD organism/project/analysis chain, two NCBI type-material rows, exact StrainInfo species/deposit rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:708187`, `label: Colletotrichum chlorophyti`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5455`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:165654`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colletotrichum`; the bounded scan checked all 16 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:41749`, which records one retained organism for `NCBITaxon:708187`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:708187` with one name assertion. NCBI supplies the exact synonym `Colletotrichum chlorophyti S. Chandra & Tandon 1965` present in the YAML, and the curation-history source list agrees with the two retained source attestations.

The native GOLD snapshot has one exact organism/project/analysis chain for this NCBI taxon: `NTL11`, organism `Go0373179`, project `Gp0219980`, and analysis `Colletotrichum chlorophyti NTL11`.

The NCBI type-material side inventory has two exact culture-from-type-material rows for this species, `IMI 103806` and `IMI:103806`. Those rows support an external type-material relationship for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

StrainInfo has one exact species-level side inventory row for `IMI 103806`. Because no generated rows exist for `NCBITaxon:708187` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:708187` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colletotrichum_chlorophyti.yaml` plus `just validate-strict data/taxa/eukaryota/colletotrichum_chlorophyti.yaml`.

## Additional Notes

No `data/raw/ncbi_merged_ids.tsv` side rows exist for `NCBITaxon:708187`.
