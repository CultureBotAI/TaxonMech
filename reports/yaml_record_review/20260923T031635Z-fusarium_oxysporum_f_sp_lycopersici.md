# YAML Record Review: Fusarium oxysporum f. sp. lycopersici

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_oxysporum_f_sp_lycopersici.yaml
- Started UTC: 2026-09-23T03:16:35Z
- Finished UTC: 2026-09-23T03:16:35Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:59765` |
| Label | `Fusarium oxysporum f. sp. lycopersici` |
| Rank | `FORMA_SPECIALIS` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5507` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_oxysporum_f_sp_lycopersici.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_oxysporum_f_sp_lilii.yaml data/taxa/eukaryota/fusarium_oxysporum_f_sp_luffae.yaml data/taxa/eukaryota/fusarium_oxysporum_f_sp_lycopersici.yaml data/taxa/eukaryota/fusarium_oxysporum_f_sp_lycopersici_4287.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with 15 organism assertions, 15 current native GOLD organism rows with 15 linked projects and 15 native analysis rows, one NCBI merged-ID side row, no exact StrainInfo rows, no NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:59765`, `label: Fusarium oxysporum f. sp. lycopersici`, `rank: FORMA_SPECIALIS`, `parent_taxon: NCBITaxon:5507`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:7526`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Fusarium oxysporum`; the bounded scan checked all 18 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy forma-specialis ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:39715`, which records 15 retained direct organisms for `NCBITaxon:59765`; this agrees with `source_attestations[1].assertion_count: 15` and its organism assertion unit. The current native GOLD catalogs also contain 15 exact organisms, 15 linked projects, and 15 analyses linked to those projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:59765`. The YAML preserves the exact synonym `Fusarium lycopersici`, and the NCBI row has no related synonyms.

The retained GOLD aggregate supplies 15 organism assertions filed directly under `NCBITaxon:59765`, matching the YAML note that descendant taxa are not gathered. The current native GOLD catalogs contain the same exact organism count and include `Fol075`, `Fol074`, `Fol073`, `Fol072`, `Fol069`, `Fol038`, `Fol029`, `Fol026`, `Fol018`, `Fol016`, `Fol014`, `Fol007`, `Fol004`, `Fol002`, and `race 3/D11`; all 15 have exact linked projects and project-linked analyses.

The NCBI side merge inventory maps old ID `NCBITaxon:1158299` to `NCBITaxon:59765`, but that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv` with `retired_into`, so the YAML correctly has no generated `replaces` entry. No exact NCBI type-material, exact StrainInfo, exact BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded forma-specialis identity, NCBI and GOLD source attestations, the NCBI exact synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_oxysporum_f_sp_lycopersici.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_oxysporum_f_sp_lycopersici.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_oxysporum_f_sp_lycopersici` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
