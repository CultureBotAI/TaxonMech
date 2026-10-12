# YAML Record Review: Hanseniaspora uvarum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hanseniaspora_uvarum.yaml
- Started UTC: 2026-09-23T05:59:03Z
- Finished UTC: 2026-09-23T05:59:03Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:29833` |
| Label | `Hanseniaspora uvarum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:29832` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hanseniaspora_uvarum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hanseniaspora_uvarum.yaml data/taxa/eukaryota/hanseniaspora_valbyensis.yaml data/taxa/eukaryota/hanseniaspora_vineae.yaml data/taxa/eukaryota/hansenula_anomala.yaml` | Passed; the strict batch reported zero ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with eight organism assertions, six exact current native GOLD organisms with six linked native GOLD projects and five linked native analyses, 11 exact NCBI type-material rows, no side NCBI merged-ID rows, 154 direct exact StrainInfo rows with 250 deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:29833`, `label: Hanseniaspora uvarum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:29832`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:3274`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hanseniaspora`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:29836`, which records eight retained direct organisms for `NCBITaxon:29833`; this agrees with `source_attestations[1].assertion_count: 8` and its organism assertion unit. The current native GOLD catalogs contain six exact organisms, six linked projects, and five native analyses linked by `AP PROJECT GOLD IDS`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:29833`. `Hanseniaspora apiculata`, `Kloeckera apiculata`, and `Kloeckeraspora uvarum` are present in `data/raw/ncbitaxon_taxa.tsv:3274` as exact synonyms, and both generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies eight organism assertions. The current native GOLD catalogs have exact organisms for `34-9`, `AWRI3580`, `H4`, `H2`, `H20`, and `NRRL Y-1614`; all six organisms have linked projects, and all exact linked projects except `Gp0831281` have native analysis rows.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:152000` through `data/raw/ncbi_type_material.tsv:152010` as 11 spellings for `ATCC 32369`, `CBS 314`, `DBVPG 6718`, `IFO 10833`, and `NRRL Y-1614`. StrainInfo also has 154 direct exact rows with 250 deposit rows for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

No side NCBI merged-ID row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hanseniaspora_uvarum.yaml` plus `just validate-strict data/taxa/eukaryota/hanseniaspora_uvarum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hanseniaspora_uvarum` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
