# YAML Record Review: Diplodia seriata

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/diplodia_seriata.yaml
- Started UTC: 2026-09-22T23:07:02Z
- Finished UTC: 2026-09-22T23:07:02Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:420778` |
| Label | `Diplodia seriata` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:66735` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/diplodia_seriata.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/diplodia_sapinea_cmw_190.yaml data/taxa/eukaryota/diplodia_scrobiculata.yaml data/taxa/eukaryota/diplodia_seriata.yaml data/taxa/eukaryota/diplodia_sp.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with three retained direct organisms, three exact native GOLD organisms linked to three projects and three analyses, two exact NCBI type-material rows, 25 exact StrainInfo direct records carrying 25 matching deposit designations, no exact BacDive rows, no final raw strain rows, one NCBI merged-ID side row, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:420778`, `label: Diplodia seriata`, `rank: SPECIES`, `parent_taxon: NCBITaxon:66735`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:92282`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Diplodia` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:35060`, which records three retained direct organisms for `NCBITaxon:420778`; this agrees with `source_attestations[1].assertion_count: 3` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:420778`. The YAML carries the one exact synonym and one related synonym filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain three exact organisms, `Go0114002` for `Diplodia seriata isolate:DS831`, `Go0372893` for `Diplodia seriata F98.1`, and `Go0677872` for `Diplodia seriata B07_159`; three projects, `Gp0117696`, `Gp0219683`, and `Gp0779713`, under those organisms; and three analyses with the same organism names that link back through `AP PROJECT GOLD IDS`.

The NCBI type-material inventory contributes two exact rows under `Diplodia seriata`, covering both spelling variants of the `CBS 112555` culture from epitype.

The exact StrainInfo side inventory has 25 direct records and 25 matching deposit designations for `NCBITaxon:420778`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/diplodia_seriata.yaml` plus `just validate-strict data/taxa/eukaryota/diplodia_seriata.yaml`.

## Additional Notes

The bounded scan found a side-inventory `data/raw/ncbi_merged_ids.tsv` mapping from `NCBITaxon:66732` into `NCBITaxon:420778`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` would generate a `replaces` entry.
