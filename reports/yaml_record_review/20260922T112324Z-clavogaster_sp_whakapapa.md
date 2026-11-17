# YAML Record Review: Clavogaster sp. 'whakapapa'

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/clavogaster_sp_whakapapa.yaml
- Started UTC: 2026-09-22T11:17:28Z
- Finished UTC: 2026-09-22T11:23:24Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:3127106` |
| Label | `Clavogaster sp. 'whakapapa'` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:3014270` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/clavogaster_sp_whakapapa.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/clavogaster_sp_whakapapa.yaml` | Passed; the strict validator exited successfully for one file. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one exact native GOLD organism with four projects, no NCBI type-material rows, no final raw strain rows, no StrainInfo exact rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:3127106`, `label: Clavogaster sp. 'whakapapa'`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3014270`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:604537`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `unclassified Clavogaster`; the bounded scan checked all 15 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is also supported. `data/raw/gold_organisms.tsv:31542` records one organism for `NCBITaxon:3127106`, and the native GOLD chain includes organism `Go0586595` plus projects `Gp0593234`, `Gp0593235`, `Gp0593236`, and `Gp0593237`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:3127106` with one name assertion. NCBI supplies no synonyms for this provisional species in `data/raw/ncbitaxon_taxa.tsv`, and the curation-history source list agrees with the two retained source attestations.

No NCBI type-material, BacDive, StrainInfo, or local generated strain rows are attached to `NCBITaxon:3127106`, so `strain_count: 0` is consistent with the maintained inputs inspected.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:3127106` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/clavogaster_sp_whakapapa.yaml` plus `just validate-strict data/taxa/eukaryota/clavogaster_sp_whakapapa.yaml`.

## Additional Notes

The native GOLD organism row uses `Clavogaster whakapapa MYCOTA032` as the organism name for taxon `3127106`; the NCBI ID tie keeps the aggregate `GOLD` attestation exact for `Clavogaster sp. 'whakapapa'`.
