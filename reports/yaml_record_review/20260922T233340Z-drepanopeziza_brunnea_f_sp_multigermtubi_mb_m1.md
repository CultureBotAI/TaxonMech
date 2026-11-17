# YAML Record Review: Drepanopeziza brunnea f. sp. 'multigermtubi' MB_m1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/drepanopeziza_brunnea_f_sp_multigermtubi_mb_m1.yaml
- Started UTC: 2026-09-22T23:33:40Z
- Finished UTC: 2026-09-22T23:33:40Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1072389` |
| Label | `Drepanopeziza brunnea f. sp. 'multigermtubi' MB_m1` |
| Rank | `STRAIN` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:698441` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/drepanopeziza_brunnea_f_sp_multigermtubi_mb_m1.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/drepanopeziza_brunnea_f_sp_monogermtubi.yaml data/taxa/eukaryota/drepanopeziza_brunnea_f_sp_multigermtubi_mb_m1.yaml data/taxa/eukaryota/dryadomyces_quercivorus.yaml data/taxa/eukaryota/dryadomyces_quercus_mongolicae.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism, one native GOLD project, one native GOLD analysis, no exact StrainInfo, NCBI type-material, NCBI merged-ID, or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1072389`, `label: Drepanopeziza brunnea f. sp. 'multigermtubi' MB_m1`, `rank: STRAIN`, `parent_taxon: NCBITaxon:698441`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:229820`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Drepanopeziza brunnea f. sp. 'multigermtubi'`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:1242`, which records one retained direct organism for `NCBITaxon:1072389`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1072389`. The YAML carries the one exact synonym filed for this NCBI row, `Marssonina brunnea f. sp. 'multigermtubi' S1`; NCBI supplies no related or broad synonyms.

The native GOLD catalogs contain one exact organism row, `Go0038386` for `Drepanopeziza brunnea 'multigermtubi' MB_m1`, one matching project, `Gp0038386`, and one analysis named `Marssonina brunnea f. sp. 'multigermtubi' MB_m1`.

There are no exact rows for this taxon in the StrainInfo side inventory, NCBI type-material table, NCBI merged-ID table, BacDive, or the maintained final strain tables. `strain_count: 0` is therefore consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/drepanopeziza_brunnea_f_sp_multigermtubi_mb_m1.yaml` plus `just validate-strict data/taxa/eukaryota/drepanopeziza_brunnea_f_sp_multigermtubi_mb_m1.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the one current native GOLD organism row. The native GOLD project and analysis retain the `Marssonina` basionym spelling that is also present in the NCBI exact synonym list.
