# YAML Record Review: Colletotrichum tanaceti

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colletotrichum_tanaceti.yaml
- Started UTC: 2026-09-22T13:44:37Z
- Finished UTC: 2026-09-22T13:53:15Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1306861` |
| Label | `Colletotrichum tanaceti` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2707350` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colletotrichum_tanaceti.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/colletotrichum_tanaceti.yaml` | Passed; the strict validator scanned one file with zero errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism/project/analysis chain, six NCBI type-material rows, no NCBI merged-ID side rows, no exact StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1306861`, `label: Colletotrichum tanaceti`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2707350`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:309033`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colletotrichum destructivum species complex`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:7512`, which records one retained organism for `NCBITaxon:1306861`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1306861` with two name assertions. NCBI supplies both related synonyms present in the YAML and no exact synonyms.

The native GOLD snapshot has one exact organism row for this NCBI taxon, `Go0632162` / `Colletotrichum tanaceti BRIP57314`, with project `Gp0645986` / `Colletotrichum tanaceti BRIP57314` and one linked analysis row; this agrees with the retained aggregate count.

The NCBI type-material side inventory has six exact `Colletotrichum tanaceti` culture-from-holotype rows: `BRIP 57314`, `BRIP:57314`, `CBS 132693`, `CBS:132693`, `UM01`, and `UM:01`. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:1306861` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colletotrichum_tanaceti.yaml` plus `just validate-strict data/taxa/eukaryota/colletotrichum_tanaceti.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:1306861`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
