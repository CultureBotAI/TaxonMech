# YAML Record Review: Gamsiella multidivaricata

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/gamsiella_multidivaricata.yaml
- Started UTC: 2026-09-23T04:07:01Z
- Finished UTC: 2026-09-23T04:07:01Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:101098` |
| Label | `Gamsiella multidivaricata` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2779868` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/gamsiella_multidivaricata.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/gamarada_debralockiae.yaml data/taxa/eukaryota/gambierdiscus_australes.yaml data/taxa/eukaryota/gamsiella_multidivaricata.yaml data/taxa/eukaryota/ganoderma_adspersum.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, two exact current native GOLD organisms with three linked native GOLD projects and no native analysis rows, eight exact NCBI type-material rows, one exact StrainInfo record carrying three exact deposit rows, no exact BacDive or NCBI merged-ID rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:101098`, `label: Gamsiella multidivaricata`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2779868`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:17418`, which carries the same label, parent, rank, code, one exact synonym, two related synonyms, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Gamsiella`; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:244`, which records two retained direct organisms for `NCBITaxon:101098`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs also contain two exact organisms, `Go0141633` for strain `RSA 2152` and `Go0145900` for strain `NRRL 6456`, with three linked projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:101098`. The YAML preserves exact synonym `Mortierella multidivaricata` and the two related synonyms from the NCBI row.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have exact organisms for `Gamsiella multidivaricata RSA 2152` and `Gamsiella multidivaricata NRRL 6456`; `RSA 2152` has one genome project and one transcriptome project, `NRRL 6456` has one resequencing project, and no native GOLD analysis currently links to those projects.

The NCBI type-material table has eight exact rows for the target, covering `CBS 227.78`, `CBS:227.78`, `IMI 236322`, `IMI:236322`, `RSA 2152`, `RSA:2152`, `SZMC 11224`, and `SZMC:11224`. StrainInfo has one exact target record and three exact deposits. These side rows do not create generated local strain entries by themselves.

No side `data/raw/ncbi_merged_ids.tsv` row maps an old ID into `NCBITaxon:101098`, and no retained row in `data/raw/ncbitaxon_taxa.tsv` carries a retired ID for this target, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, one exact synonym, two related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/gamsiella_multidivaricata.yaml` plus `just validate-strict data/taxa/eukaryota/gamsiella_multidivaricata.yaml`.

## Additional Notes

No prior exact ignored review report existed for `gamsiella_multidivaricata` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:101098` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.
