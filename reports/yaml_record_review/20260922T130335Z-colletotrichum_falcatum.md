# YAML Record Review: Colletotrichum falcatum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colletotrichum_falcatum.yaml
- Started UTC: 2026-09-22T12:59:45Z
- Finished UTC: 2026-09-22T13:03:35Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:129314` |
| Label | `Colletotrichum falcatum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2707348` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colletotrichum_falcatum.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/colletotrichum_falcatum.yaml` | Passed; the strict validator reported 0 errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with three retained organisms, two current native GOLD organisms with three linked projects, one native GOLD analysis, four NCBI type-material rows, one NCBI merged-ID side row, exact StrainInfo species/deposit rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:129314`, `label: Colletotrichum falcatum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2707348`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:24743`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colletotrichum graminicola species complex`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:6876`, which records three retained organisms for `NCBITaxon:129314`; this agrees with `source_attestations[1].assertion_count: 3`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:129314` with one name assertion. NCBI supplies both exact synonyms and all four related synonyms present in the YAML, and the curation-history source list agrees with the two retained source attestations.

The native GOLD snapshot has two exact organisms for this NCBI taxon: `MAFF306170` / `Go0102915`, which has two linked projects, and `Cf671` / `Go0118684`, which has one linked project and one linked analysis.

The NCBI type-material side inventory has four exact culture-from-neotype rows for this species: colonated and uncolonated `CBS 127945` and `CGMG 3.14187` designations. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

StrainInfo has exact species-level side inventory rows, including 56 exact deposit matches and 39 direct species matches. Because no generated rows exist for `NCBITaxon:129314` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:129314` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colletotrichum_falcatum.yaml` plus `just validate-strict data/taxa/eukaryota/colletotrichum_falcatum.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:496421` into `NCBITaxon:129314`, but this is only a side-inventory old ID; no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.

The retained GOLD aggregate count is three, while the current local native GOLD JSONL snapshot exposes two exact organisms with three linked projects; the generated source attestation follows the retained aggregate row.
