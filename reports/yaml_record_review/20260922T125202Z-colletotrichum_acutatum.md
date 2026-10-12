# YAML Record Review: Colletotrichum acutatum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colletotrichum_acutatum.yaml
- Started UTC: 2026-09-22T12:48:00Z
- Finished UTC: 2026-09-22T12:52:02Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:27357` |
| Label | `Colletotrichum acutatum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2707335` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colletotrichum_acutatum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/colletotrichum_acutatum.yaml` | Passed; the strict validator reported 0 errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with nine retained organisms, nine current native GOLD organism rows with ten linked projects, three native GOLD analyses, nine NCBI type-material rows, 25 NCBI merged-ID side rows, exact StrainInfo species/deposit rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:27357`, `label: Colletotrichum acutatum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2707335`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2751`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colletotrichum acutatum species complex`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:25521`, which records nine retained organisms for `NCBITaxon:27357`; this agrees with `source_attestations[1].assertion_count: 9`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:27357` with one name assertion. NCBI supplies the three exact synonyms and 27 related synonyms present in the YAML, including the `Colletotrichum sp. PL-*` sequence; the curation-history source list agrees with the two retained source attestations.

The native GOLD snapshot has nine exact organisms and ten linked projects for this NCBI taxon. `Go0111519` / `CBS 112980` has both the `Gp0113518` standard-draft and `Gp0113519` transcriptome projects; the other exact organisms each have one linked project. Three native analysis rows are linked to the project set: `Gp0113518`, `Gp0150878`, and `Gp0235269`.

The NCBI type-material side inventory has nine exact rows for this species: alternative `ATCC 56816`, `CBS 112996`, `ICMP 1783`, `STE-U 5292`, and `CBS H-20723` epitype designations. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

StrainInfo has exact species-level side inventory rows, including 276 exact deposit matches and 241 direct species matches. Because no generated rows exist for `NCBITaxon:27357` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:27357` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colletotrichum_acutatum.yaml` plus `just validate-strict data/taxa/eukaryota/colletotrichum_acutatum.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` maps 25 old IDs into `NCBITaxon:27357`, but these are only side-inventory old IDs; no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` generated `replaces` entries.
