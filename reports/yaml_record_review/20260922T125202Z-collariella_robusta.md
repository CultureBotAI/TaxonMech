# YAML Record Review: Collariella robusta

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/collariella_robusta.yaml
- Started UTC: 2026-09-22T12:48:00Z
- Finished UTC: 2026-09-22T12:52:02Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1934373` |
| Label | `Collariella robusta` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1934365` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/collariella_robusta.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/collariella_robusta.yaml` | Passed; the strict validator exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one native GOLD organism with two projects, two NCBI type-material rows, one NCBI merged-ID side row, no native GOLD analyses, no BacDive or StrainInfo exact rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1934373`, `label: Collariella robusta`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1934365`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:496607`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Collariella`; the bounded scan checked all 16 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:17755`, which records one retained organism for `NCBITaxon:1934373`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1934373` with one name assertion. NCBI supplies both exact synonyms and both related synonyms present in the YAML, and the curation-history source list agrees with the two retained source attestations.

The native GOLD snapshot has one exact organism, `PSN 660` / `Go0651439`, and two projects for this NCBI taxon: `Gp0688343` for the minimal draft and `Gp0699251` for the transcriptome project. No native GOLD analysis rows are currently linked to those projects.

The NCBI type-material side inventory has two exact type-material rows for this species, `CBS 551.83` and `CBS:551.83`. Those rows support an external type-material relationship for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:1934373` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, `data/straininfo/related_records.tsv.gz`, or the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/collariella_robusta.yaml` plus `just validate-strict data/taxa/eukaryota/collariella_robusta.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:159608` into `NCBITaxon:1934373`, but this is only a side-inventory old ID; no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
