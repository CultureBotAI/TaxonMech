# YAML Record Review: Debaryomyces hansenii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/debaryomyces_hansenii.yaml
- Started UTC: 2026-09-22T22:04:08Z
- Finished UTC: 2026-09-22T22:04:08Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:4959` |
| Label | `Debaryomyces hansenii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:4958` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/debaryomyces_hansenii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/debaryomyces_fabryi.yaml data/taxa/eukaryota/debaryomyces_hansenii.yaml data/taxa/eukaryota/debaryomyces_hansenii_cbs767.yaml data/taxa/eukaryota/debaryomyces_hansenii_var_hansenii_mtcc_234.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with six retained direct organisms, four exact native GOLD organisms linked to 14 projects and one analysis, 47 exact NCBI type-material rows, 453 exact StrainInfo direct records carrying 694 matching deposit designations, two joined StrainInfo overlay rows that were not retained into the final raw strain tables, no exact BacDive rows, no final raw strain rows, four NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:4959`, `label: Debaryomyces hansenii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:4958`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:2166`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Debaryomyces` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37213`, which records six retained direct organisms for `NCBITaxon:4959`; this agrees with `source_attestations[1].assertion_count: 6` and its note that descendant taxa are not gathered.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:4959`. The YAML carries all seven exact synonyms and both related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain four exact organisms, `Go0368638`, `Go0384144`, `Go0536089`, and `Go0705630`; 14 exact projects under those organisms, including `Gp0235233`, `Gp0484567` through `Gp0484578`, and `Gp0831676`; and an analysis row named `Debaryomyces hansenii J6` that links back through `AP PROJECT GOLD IDS`.

The NCBI type-material inventory contributes 47 exact rows under the synonym taxon name `Saccharomyces hansenii`, covering culture-from-type-material variants of `ATCC 36239`, `CBS 767`, `KCTC 7645`, `MUCL 30242`, and `NRRL Y-7426`, plus type-material variants of `BCRC 21394`, `CBS 1795`, `DBVPG 6017`, `DBVPG 6050`, `IAM 12835`, `IFO 0083`, `IFO 0623`, `JCM 1521`, `JCM 1990`, `JCM 2101`, `NCTC 1842`, `NCYC 2572`, `NRRL Y-10976`, `NRRL Y-173`, `UCD 74-86`, and `VKM Y-2560`.

The exact StrainInfo side inventory is large for `NCBITaxon:4959`: 453 direct records and 694 matching deposit designations. Two joined intermediate overlay rows in `data/straininfo/related_records.tsv.gz` map `CBS 788.72` to `kgmicrobe.strain:bacdive_15044`, but no exact rows are present in the maintained final strain tables and no `STRAININFO` source attestation is generated for this taxon. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `12`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/debaryomyces_hansenii.yaml` plus `just validate-strict data/taxa/eukaryota/debaryomyces_hansenii.yaml`.

## Additional Notes

The bounded scan found side-inventory `data/raw/ncbi_merged_ids.tsv` mappings from `NCBITaxon:1143188`, `NCBITaxon:1221546`, `NCBITaxon:522691`, and `NCBITaxon:524886` into `NCBITaxon:4959`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` would generate `replaces` entries.
