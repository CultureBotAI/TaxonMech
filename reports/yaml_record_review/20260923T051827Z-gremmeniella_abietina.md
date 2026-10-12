# YAML Record Review: Gremmeniella abietina

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/gremmeniella_abietina.yaml
- Started UTC: 2026-09-23T05:18:27Z
- Finished UTC: 2026-09-23T05:18:27Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:127520` |
| Label | `Gremmeniella abietina` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:52285` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/gremmeniella_abietina.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/graphis_scripta.yaml data/taxa/eukaryota/gregarina_niphandrodes.yaml data/taxa/eukaryota/gremmeniella_abietina.yaml data/taxa/eukaryota/grifola_frondosa.yaml` | Passed; the strict batch exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, two exact current native GOLD organisms with four linked native GOLD projects and one linked native analysis, no exact NCBI type-material rows, two side NCBI merged-ID rows with no retained old IDs, 23 direct exact StrainInfo rows with 23 deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:127520`, `label: Gremmeniella abietina`, `rank: SPECIES`, `parent_taxon: NCBITaxon:52285`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:24350`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Gremmeniella`; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:6454`, which records two retained direct organisms for `NCBITaxon:127520`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs also contain exact organisms `Go0146360` for strain `DAOM 170367` and `Go0146361` for strain `DAOM 170408`, four linked projects, and one native analysis linked by `AP PROJECT GOLD IDS`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:127520`. `Ascocalyx abietina`, `Ascocalyx abietis`, `Brunchorstia pinea`, `Crumenula abietina`, and `Scleroderris lagerbergii` are present in `data/raw/ncbitaxon_taxa.tsv:24350` as exact synonyms, and all three generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have two exact organisms for `Gremmeniella abietina`, four linked standard-draft or transcriptome projects, and one native analysis for the `DAOM 170408` standard draft project.

The NCBI merged side inventory maps `NCBITaxon:52286` and `NCBITaxon:767006` into `NCBITaxon:127520`, but neither old ID is retained in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected in the generated YAML. StrainInfo also has 23 direct exact rows with 23 deposit rows for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

No exact NCBI type-material row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/gremmeniella_abietina.yaml` plus `just validate-strict data/taxa/eukaryota/gremmeniella_abietina.yaml`.

## Additional Notes

No prior exact ignored review report existed for `gremmeniella_abietina` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
