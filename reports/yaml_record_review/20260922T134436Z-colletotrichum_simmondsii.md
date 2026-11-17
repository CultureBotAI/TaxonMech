# YAML Record Review: Colletotrichum simmondsii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colletotrichum_simmondsii.yaml
- Started UTC: 2026-09-22T13:39:21Z
- Finished UTC: 2026-09-22T13:44:36Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:703756` |
| Label | `Colletotrichum simmondsii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2707335` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colletotrichum_simmondsii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/colletotrichum_simmondsii.yaml` | Passed; the strict validator exited successfully for this file in a four-file run. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with four retained organisms, three exact native GOLD organisms with three projects and one analysis, five NCBI type-material rows, five exact StrainInfo side rows, no NCBI merged-ID side rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:703756`, `label: Colletotrichum simmondsii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2707335`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:165072`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colletotrichum acutatum species complex`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:41692`, which records four retained organisms for `NCBITaxon:703756`; this agrees with `source_attestations[1].assertion_count: 4`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:703756` with one name assertion. NCBI supplies the single related synonym present in the YAML and no exact synonyms.

The native GOLD snapshot has three exact organism rows for this NCBI taxon, covering `Go0111574` / `Colletotrichum simmondsii IMI 313840`, `Go0111575` / `Colletotrichum simmondsii IMI346326`, and `Go0117446` / `Colletotrichum simmondsii CBS122122`; those rows link to three projects and one analysis row for `Gp0122385`. The generated YAML correctly follows the maintained retained aggregate in `data/raw/gold_organisms.tsv`, which has one additional retained GOLD organism beyond the native exact rows currently visible in the JSONL mirror.

The NCBI type-material side inventory has five exact `Colletotrichum simmondsii` rows: culture-from-holotype designations `CBS 122122`, `CBS:122122`, and `ICMP:17298`, plus type-material designations `BRIP 28519` and `BRIP:28519`. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

The exact StrainInfo side rows cover five deposits, including `ICMP 17298`, and five direct DOI records for the same NCBI taxon. They do not currently join into the maintained final strain tables, so `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated synonym from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:703756` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colletotrichum_simmondsii.yaml` plus `just validate-strict data/taxa/eukaryota/colletotrichum_simmondsii.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:703756`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
