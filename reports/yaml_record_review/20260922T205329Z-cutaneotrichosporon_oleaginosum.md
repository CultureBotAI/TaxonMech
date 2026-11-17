# YAML Record Review: Cutaneotrichosporon oleaginosum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cutaneotrichosporon_oleaginosum.yaml
- Started UTC: 2026-09-22T20:53:29Z
- Finished UTC: 2026-09-22T20:53:29Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:879819` |
| Label | `Cutaneotrichosporon oleaginosum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1838142` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cutaneotrichosporon_oleaginosum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cutaneotrichosporon_dermatis.yaml data/taxa/eukaryota/cutaneotrichosporon_mucoides.yaml data/taxa/eukaryota/cutaneotrichosporon_oleaginosum.yaml data/taxa/eukaryota/cutaneotrichosporon_sp_pdh3307a.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with four retained organisms, three exact native GOLD organism rows, 22 exact native GOLD project rows, three exact native GOLD analysis rows, two exact NCBI type-material rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, one NCBI merged-ID side row, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:879819`, `label: Cutaneotrichosporon oleaginosum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1838142`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:187147`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cutaneotrichosporon` genus; the bounded scan checked all 12 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:43732`, which records four retained organisms for `NCBITaxon:879819`; this agrees with `source_attestations[1].assertion_count: 4`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:879819`. NCBI supplies exact synonym `Trichosporon oleaginosum J.J. Zhou, S.O. Suh & Gujjari, 2011` and three related synonyms, matching the YAML `synonyms` block.

The retained GOLD aggregate row supports the `GOLD` source attestation. The complete local native GOLD JSONL snapshot has exact organisms `Go0044565`, `Go0565671`, and `Go0624899`; a complete follow-up found 22 exact native projects and three exact native analyses, with two duplicate analysis rows tied to `Gp0044565` and one tied to `Gp0536031`. The one-count difference between the retained aggregate and native organism snapshots is local to those side inputs; the generated YAML follows the retained aggregate row.

NCBI lists two exact type-material side rows under `Trichosporon oleaginosum` for `ATCC 20509`. No exact StrainInfo, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, generated NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cutaneotrichosporon_oleaginosum.yaml` plus `just validate-strict data/taxa/eukaryota/cutaneotrichosporon_oleaginosum.yaml`.

## Additional Notes

The bounded scan found one side-inventory old ID in `data/raw/ncbi_merged_ids.tsv:97718`: `NCBITaxon:879820` now maps to `NCBITaxon:879819`. There are no retained retired rows for that old ID, so the generated YAML correctly has no `replaces` entries.
