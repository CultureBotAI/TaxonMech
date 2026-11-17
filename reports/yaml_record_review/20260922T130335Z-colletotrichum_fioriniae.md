# YAML Record Review: Colletotrichum fioriniae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colletotrichum_fioriniae.yaml
- Started UTC: 2026-09-22T12:59:45Z
- Finished UTC: 2026-09-22T13:03:35Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:710243` |
| Label | `Colletotrichum fioriniae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2707335` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colletotrichum_fioriniae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/colletotrichum_fioriniae.yaml` | Passed; the strict validator reported 0 errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with ten retained organisms, ten current native GOLD organisms with 11 linked projects, two native GOLD analyses, four NCBI type-material rows, nine NCBI merged-ID side rows, exact StrainInfo species/deposit rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:710243`, `label: Colletotrichum fioriniae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2707335`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:166423`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colletotrichum acutatum species complex`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:41793`, which records ten retained organisms for `NCBITaxon:710243`; this agrees with `source_attestations[1].assertion_count: 10`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:710243` with one name assertion. NCBI supplies the three exact synonyms and 11 related synonyms present in the YAML, including seven `Colletotrichum sp. EHS*` related synonyms; the curation-history source list agrees with the two retained source attestations.

The native GOLD snapshot has ten exact organisms and 11 linked projects for this NCBI taxon. `Go0019241` / `MH 18` has both a transcriptome project and the `Gp0019317` standard-draft project; each other exact organism has one linked project. Two native analysis rows are linked to this project set, `Gp0019317` and `Gp0780632`.

The NCBI type-material side inventory has four exact rows for this species: colonated and uncolonated `CBS 128517` and `EHS58` designations. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

StrainInfo has exact species-level side inventory rows, including 42 exact deposit matches and 42 direct species matches. Because no generated rows exist for `NCBITaxon:710243` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:710243` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colletotrichum_fioriniae.yaml` plus `just validate-strict data/taxa/eukaryota/colletotrichum_fioriniae.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` maps nine old IDs into `NCBITaxon:710243`, but these are only side-inventory old IDs; no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` generated `replaces` entries.
