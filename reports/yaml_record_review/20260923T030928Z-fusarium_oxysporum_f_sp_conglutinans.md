# YAML Record Review: Fusarium oxysporum f. sp. conglutinans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_oxysporum_f_sp_conglutinans.yaml
- Started UTC: 2026-09-23T03:09:28Z
- Finished UTC: 2026-09-23T03:09:28Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:100902` |
| Label | `Fusarium oxysporum f. sp. conglutinans` |
| Rank | `FORMA_SPECIALIS` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5507` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_oxysporum_f_sp_conglutinans.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_oxysporum_f_sp_ciceris.yaml data/taxa/eukaryota/fusarium_oxysporum_f_sp_conglutinans.yaml data/taxa/eukaryota/fusarium_oxysporum_f_sp_conglutinans_fo5176.yaml data/taxa/eukaryota/fusarium_oxysporum_f_sp_conglutinans_race_2_54008.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, two current native GOLD organism rows with two linked projects and two native analysis rows, one NCBI merged-ID side row, three exact direct StrainInfo entries, four exact StrainInfo deposit references, no NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:100902`, `label: Fusarium oxysporum f. sp. conglutinans`, `rank: FORMA_SPECIALIS`, `parent_taxon: NCBITaxon:5507`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:17342`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Fusarium oxysporum`; the bounded scan checked all 18 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy forma-specialis ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:206`, which records two retained direct organisms for `NCBITaxon:100902`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs still contain exact organisms `Go0144656` and `Go0631228`, their two linked projects, and two analyses linked to those projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:100902`. The YAML preserves the exact synonym `Fusarium oxysporum f. conglutinans`, and the NCBI row has no related synonyms.

The retained GOLD aggregate supplies two organism assertions filed directly under `NCBITaxon:100902`, matching the YAML note that descendant taxa are not gathered. The current native GOLD catalogs still contain exact organism rows for strains `1` and `Cong1-1`; they also contain two linked project rows and two project-linked analysis rows.

The NCBI side merge inventory maps old ID `NCBITaxon:178564` to `NCBITaxon:100902`, but that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv` with `retired_into`, so the YAML correctly has no generated `replaces` entry. StrainInfo contains three exact direct rows and four exact deposit references for the target. No exact NCBI type-material, exact BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded forma-specialis identity, NCBI and GOLD source attestations, the NCBI exact synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_oxysporum_f_sp_conglutinans.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_oxysporum_f_sp_conglutinans.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_oxysporum_f_sp_conglutinans` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
