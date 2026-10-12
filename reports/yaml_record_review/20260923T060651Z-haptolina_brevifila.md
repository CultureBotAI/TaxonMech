# YAML Record Review: Haptolina brevifila

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/haptolina_brevifila.yaml
- Started UTC: 2026-09-23T06:06:51Z
- Finished UTC: 2026-09-23T06:06:51Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:156173` |
| Label | `Haptolina brevifila` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1090112` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/haptolina_brevifila.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/haplosporangium_sp_z_27.yaml data/taxa/eukaryota/hapsidospora_chrysogena.yaml data/taxa/eukaryota/haptolina_brevifila.yaml data/taxa/eukaryota/haptolina_ericina.yaml` | Passed; the strict batch exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with no linked native GOLD projects or analyses, no exact NCBI type-material rows, no side NCBI merged-ID rows, one direct exact StrainInfo row with one deposit row, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:156173`, `label: Haptolina brevifila`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1090112`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:32448`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Haptolina`; the bounded scan checked all nine lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:12490`, which records one retained direct organism for `NCBITaxon:156173`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:156173`. `Chrysochromulina brevifilum` is present in `data/raw/ncbitaxon_taxa.tsv:32448` as an exact synonym, and both generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalog has an exact organism for `UTEX LB 985`; it has no linked native GOLD project in the local project catalog.

StrainInfo has one direct exact row with one deposit row for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record. No NCBI type-material row, side NCBI merged-ID row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/haptolina_brevifila.yaml` plus `just validate-strict data/taxa/eukaryota/haptolina_brevifila.yaml`.

## Additional Notes

No prior exact ignored review report existed for `haptolina_brevifila` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism row is exact by NCBI taxon ID but is side evidence only and does not create generated child strains without BacDive-derived local strain inventory entries.
