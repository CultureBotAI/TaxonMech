# YAML Record Review: Gigaspora rosea

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/gigaspora_rosea.yaml
- Started UTC: 2026-09-23T04:43:53Z
- Finished UTC: 2026-09-23T04:43:53Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:44941` |
| Label | `Gigaspora rosea` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:4873` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/gigaspora_rosea.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/gigaspora_margarita.yaml data/taxa/eukaryota/gigaspora_rosea.yaml data/taxa/eukaryota/gilbertella_persicaria.yaml data/taxa/eukaryota/gilbertella_persicaria_var_indica.yaml` | Passed; the strict batch scanned 4 files with 0 error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, two exact current native GOLD organisms with two linked native GOLD projects and two linked native analyses, no exact NCBI type-material rows, no exact StrainInfo rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:44941`, `label: Gigaspora rosea`, `rank: SPECIES`, `parent_taxon: NCBITaxon:4873`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:5466`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Gigaspora`; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:35813`, which records two retained direct organisms for `NCBITaxon:44941`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs also contain exact organisms `Go0631665` and `Go0632112`, linked projects `Gp0645213` and `Gp0645933`, and one native analysis linked to each project.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:44941`. The sole synonym, `Gigaspora rosea T.H. Nicolson & N.C. Schenck, 1979`, is present in `data/raw/ncbitaxon_taxa.tsv:5466` as a related synonym and is preserved with `synonym_type: RELATED_SYNONYM`.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have exact organisms for `Gigaspora rosea DAOM 194757` and `Gigaspora rosea FL105`, one linked project for each organism, and one native analysis for each project.

No side `data/raw/ncbi_merged_ids.tsv` row, exact NCBI type-material row, exact StrainInfo row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, one generated NCBI related synonym, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/gigaspora_rosea.yaml` plus `just validate-strict data/taxa/eukaryota/gigaspora_rosea.yaml`.

## Additional Notes

No prior exact ignored review report existed for `gigaspora_rosea` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
