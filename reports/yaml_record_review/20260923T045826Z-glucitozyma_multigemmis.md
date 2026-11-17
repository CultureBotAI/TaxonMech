# YAML Record Review: Glucitozyma multigemmis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/glucitozyma_multigemmis.yaml
- Started UTC: 2026-09-23T04:58:26Z
- Finished UTC: 2026-09-23T04:58:26Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:45569` |
| Label | `Glucitozyma multigemmis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:3712549` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/glucitozyma_multigemmis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/glomus_cerebriforme.yaml data/taxa/eukaryota/glonium_stellatum.yaml data/taxa/eukaryota/glucitozyma_multigemmis.yaml data/taxa/eukaryota/glutinoglossum_americanum.yaml` | Passed; the strict batch scanned 4 files with 0 error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with seven organism assertions, seven exact current native GOLD organisms with one linked native GOLD project, no linked native analyses, 15 exact NCBI type-material rows, seven exact StrainInfo rows, 19 exact StrainInfo deposit rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:45569`, `label: Glucitozyma multigemmis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3712549`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:5618`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Glucitozyma`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:36073`, which records seven retained direct organisms for `NCBITaxon:45569`; this agrees with `source_attestations[1].assertion_count: 7` and its organism assertion unit. The current native GOLD catalogs also contain seven exact organisms, including the `Go0705322` organism for strain `NRRL Y-17659` that links to project `Gp0831358`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:45569`. `Candida multigemmis (Buhagiar) S.A. Mey. & Yarrow, 1978` and `Torulopsis multigemmis Buhagiar, 1975` are present in `data/raw/ncbitaxon_taxa.tsv:5618` as exact synonyms, and `Glucitozyma multigemmis (Buhagiar) Q.M. Wang, Boekhout, Yurkov, G. Peter & F.Y. Bai, 2026` is present as a related synonym.

The retained GOLD aggregate supplies seven organism assertions. The current native GOLD catalogs have exact organism rows for `ATCC 28317`, `CBS 6524`, `DSM 70862`, `J 235`, `JCM 9559`, `To-4001`, and `NRRL Y-17659`, with one linked native project for `NRRL Y-17659`.

NCBI type-material rows list `NRRL Y-17659`, `CBS 6524`, `ATCC 28317`, `IFO 10247`, and `JCM 9559` plus formatting variants under `NCBITaxon:45569`. Exact StrainInfo rows are present as side inventory rows, but there are no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; StrainInfo only overlays BacDive-derived local strains, and this taxon has no generated local strain rows.

No side `data/raw/ncbi_merged_ids.tsv` row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `12`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/glucitozyma_multigemmis.yaml` plus `just validate-strict data/taxa/eukaryota/glucitozyma_multigemmis.yaml`.

## Additional Notes

No prior exact ignored review report existed for `glucitozyma_multigemmis` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism and project rows are exact by NCBI taxon ID or organism GOLD ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
