# YAML Record Review: Coprinopsis cinerea

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/coprinopsis_cinerea.yaml
- Started UTC: 2026-09-22T14:42:05Z
- Finished UTC: 2026-09-22T14:42:05Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5346` |
| Label | `Coprinopsis cinerea` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:184431` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/coprinopsis_cinerea.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/coprinopsis_cinerea.yaml` | Passed; the strict validator exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with 162 retained organisms, 157 exact native GOLD organisms with 265 projects and one linked analysis, eight NCBI type-material rows, two NCBI merged-ID side rows, 153 exact StrainInfo side deposits, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5346`, `label: Coprinopsis cinerea`, `rank: SPECIES`, `parent_taxon: NCBITaxon:184431`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2365`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Coprinopsis` genus; the bounded scan checked all 14 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:38130`, which records 162 retained organisms for `NCBITaxon:5346`; this agrees with `source_attestations[1].assertion_count: 162`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5346`. NCBI supplies all five exact synonyms and all six related synonyms present in the YAML.

A complete exact native GOLD scan for this taxon found 157 organism IDs, 265 projects linked through those organism IDs, and one analysis row linked through those exact project IDs. That agrees with the bounded scan sample, whose first organisms and projects start at `Go0017443` / `Gp0017443`; the generated `GOLD` assertion count itself comes from the retained aggregate row.

The NCBI type-material table has eight rows for the `Hormographiella aspergillata` synonym, covering the equivalent `IMI 349604`, `CBS 519.91`, `FMR 3839`, and `RV 49160` designations with both space and colon separators.

The exact StrainInfo side inventory has 153 deposits and 126 direct DOI records for the same NCBI taxon. They do not currently join into the maintained final strain tables, so `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated NCBI synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/coprinopsis_cinerea.yaml` plus `just validate-strict data/taxa/eukaryota/coprinopsis_cinerea.yaml`.

## Additional Notes

The bounded scan found two side rows in `data/raw/ncbi_merged_ids.tsv`, mapping old IDs `NCBITaxon:1548396` and `NCBITaxon:5348` into `NCBITaxon:5346`, but there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
