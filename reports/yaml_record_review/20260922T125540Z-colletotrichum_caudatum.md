# YAML Record Review: Colletotrichum caudatum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colletotrichum_caudatum.yaml
- Started UTC: 2026-09-22T12:52:25Z
- Finished UTC: 2026-09-22T12:55:40Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5460` |
| Label | `Colletotrichum caudatum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2707348` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colletotrichum_caudatum.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/colletotrichum_caudatum.yaml` | Passed; the strict validator exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with three retained organisms, one current native GOLD organism with two projects, six NCBI type-material rows, exact StrainInfo species/deposit rows, no native GOLD analyses, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5460`, `label: Colletotrichum caudatum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2707348`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2418`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colletotrichum graminicola species complex`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:38425`, which records three retained organisms for `NCBITaxon:5460`; this agrees with `source_attestations[1].assertion_count: 3`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5460` with one name assertion. NCBI supplies the exact synonym `Ellisiella caudata` and both related synonyms, `Colletotrichum caudatum (Peck ex Sacc.) Peck, 1909` and `Ellisiella caudata Peck ex Sacc., 1880`, present in the YAML. The curation-history source list agrees with the two retained source attestations.

The native GOLD snapshot has one exact organism, `Go0016969`, and two projects for this NCBI taxon: `Gp0016969` and `Gp0018318`. No native GOLD analysis rows are currently linked to those projects.

The NCBI type-material side inventory has six exact rows for this taxon ID under the synonymous taxon name `Ellisiella caudata`: alternative `CBS 131602`, `NY07-CC04`, and `BPI 892767` epitype designations. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

StrainInfo has exact species-level side inventory rows, including five exact deposit matches and five direct species matches. Because no generated rows exist for `NCBITaxon:5460` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:5460` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colletotrichum_caudatum.yaml` plus `just validate-strict data/taxa/eukaryota/colletotrichum_caudatum.yaml`.

## Additional Notes

No `data/raw/ncbi_merged_ids.tsv` side rows exist for `NCBITaxon:5460`.

The retained GOLD aggregate count is three, while the current local native GOLD JSONL snapshot exposes one exact organism with two linked projects; the generated source attestation follows the retained aggregate row.
