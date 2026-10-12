# YAML Record Review: Durotheca rogersii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/durotheca_rogersii.yaml
- Started UTC: 2026-09-22T23:40:50Z
- Finished UTC: 2026-09-22T23:40:50Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:419775` |
| Label | `Durotheca rogersii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1912359` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/durotheca_rogersii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/durotheca_rogersii.yaml data/taxa/eukaryota/earliella_scabrosa.yaml data/taxa/eukaryota/ebollia_carnea.yaml data/taxa/eukaryota/echinodontium_tinctorium.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism, two native GOLD projects, three NCBI type-material rows, one exact StrainInfo direct record carrying two matching deposit designations, one NCBI merged-ID side row, no native GOLD analyses, no BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:419775`, `label: Durotheca rogersii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1912359`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:91969`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Durotheca` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:35025`, which records one retained direct organism for `NCBITaxon:419775`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:419775`. The YAML carries the one exact synonym and all four related synonyms filed for this NCBI row; NCBI supplies no broad synonyms.

The single row in `data/raw/ncbi_merged_ids.tsv` retires `NCBITaxon:2305217` into this species ID. That old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`, so omitting `replaces` is expected.

The three NCBI type-material rows preserve `92031201`, `HAST:collector:Y.-M. Ju & H.-M. Hsieh:93062101`, and `YMJ 92031201` as cultures from the `Theissenia rogersii` holotype. The exact StrainInfo side inventory has one direct record carrying `BCRC 34158` and `CCRC 34158` deposit designations, but no rows are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`.

The native GOLD catalogs contain one exact organism row, `Go0498776` for `Durotheca rogersii YMJ 92031201`, with two linked projects: `Gp0383011` for a transcriptome and `Gp0383012` for a standard draft. No native GOLD analysis, exact BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, four NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/durotheca_rogersii.yaml` plus `just validate-strict data/taxa/eukaryota/durotheca_rogersii.yaml`.

## Additional Notes

The one retained GOLD organism can have multiple native GOLD projects without changing the generated organism assertion count.
