# YAML Record Review: Fusarium vanettenii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_vanettenii.yaml
- Started UTC: 2026-09-23T03:55:01Z
- Finished UTC: 2026-09-23T03:55:01Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2747968` |
| Label | `Fusarium vanettenii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:232080` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_vanettenii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_udum.yaml data/taxa/eukaryota/fusarium_vanettenii.yaml data/taxa/eukaryota/fusarium_vanettenii_77_13_4.yaml data/taxa/eukaryota/fusarium_venenatum.yaml` | Passed; the strict validator exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with 22 direct organism assertions, 22 exact current native GOLD organisms with 47 linked native GOLD projects and no native analysis rows, eight exact NCBI type-material rows, four exact StrainInfo records carrying four exact deposit rows, six NCBI merged-ID side rows but no retained retired old IDs, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2747968`, `label: Fusarium vanettenii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:232080`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:550456`, which carries the same label, parent, rank, code, nine exact synonyms, six related synonyms, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Fusarium solani species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:25883`, which records 22 retained direct organisms for `NCBITaxon:2747968`; this agrees with `source_attestations[1].assertion_count: 22` and its direct-organism note. A complete native GOLD sweep found the same 22 exact organisms and 47 linked projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2747968`. The YAML preserves the nine exact synonyms and six related synonyms from the NCBI row.

The retained GOLD aggregate supplies 22 direct organism assertions. The current native GOLD catalogs have 22 exact organisms filed directly under `NCBITaxon:2747968`, including strains `230-30-6`, `T2`, `T31 FSSC 11`, `T36`, `T77 FSSC 11`, `T299 FSSC 11`, `T161`, and `T23`; the complete exact sweep found 47 linked projects and no native GOLD analysis currently links to those projects.

The NCBI type-material table has eight exact rows for the target, covering `ATCC MYA-4622`, `ATCC:MYA-4622`, `CBS 123669`, `CBS:123669`, `NRRL 45880`, `NRRL:45880`, `CBS H-23994`, and `CBS:H-23994` under `Fusarium martii var. pisi`. StrainInfo has four exact target records and four exact deposits. These side rows do not create generated local strain entries by themselves.

The side `data/raw/ncbi_merged_ids.tsv` inventory maps six old IDs into `NCBITaxon:2747968`, but no retained row in `data/raw/ncbitaxon_taxa.tsv` carries those old IDs with `retired_into`, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, nine exact synonyms, six related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_vanettenii.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_vanettenii.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_vanettenii` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from direct rows in `data/raw/gold_organisms.tsv`; the `NCBITaxon:660122` child strain has its own separate aggregate and is not included in `NCBITaxon:2747968`'s direct count.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:2747968` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.
