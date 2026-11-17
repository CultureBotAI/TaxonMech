# YAML Record Review: Fennellomyces sp. JGI-2019a

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fennellomyces_sp_jgi_2019a.yaml
- Started UTC: 2026-09-23T01:34:49Z
- Finished UTC: 2026-09-23T01:34:49Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2572687` |
| Label | `Fennellomyces sp. JGI-2019a` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2626384` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fennellomyces_sp_jgi_2019a.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fennellomyces_linderi.yaml data/taxa/eukaryota/fennellomyces_sp_jgi_2019a.yaml data/taxa/eukaryota/fennellomyces_verticillatus.yaml data/taxa/eukaryota/feramyces_austinii.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, two current native GOLD organism rows with two linked projects, no current exact native GOLD analyses, no exact StrainInfo rows, no NCBI type-material rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2572687`, `label: Fennellomyces sp. JGI-2019a`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2626384`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:532249`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `unclassified Fennellomyces`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:23476`, which records two retained direct organisms for `NCBITaxon:2572687`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2572687`; the corresponding retained NCBI row has no exact, broad, or related synonyms, so the YAML correctly has no `synonyms` block.

No NCBI merged-ID rows target `NCBITaxon:2572687`, and no retained old IDs in `data/raw/ncbitaxon_taxa.tsv` retire into it, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies two organism assertions, and the current native GOLD catalogs still contain two exact organism rows and two linked project rows for the target NCBI taxon.

No exact BacDive, NCBI type-material, StrainInfo, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage through `unclassified Fennellomyces`, no source synonyms, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive or StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI or GOLD inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fennellomyces_sp_jgi_2019a.yaml` plus `just validate-strict data/taxa/eukaryota/fennellomyces_sp_jgi_2019a.yaml`.

## Additional Notes

The current native GOLD organism rows still carry `Fennellomyces mexicanus` in the organism name for the two rows exact-matched by NCBI taxon ID. The generated YAML is anchored to the NCBI label from `data/raw/ncbitaxon_taxa.tsv`, and the retained GOLD aggregate only contributes an organism assertion count.
