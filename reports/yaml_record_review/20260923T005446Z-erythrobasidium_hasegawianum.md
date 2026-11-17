# YAML Record Review: Erythrobasidium hasegawianum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/erythrobasidium_hasegawianum.yaml
- Started UTC: 2026-09-23T00:54:46Z
- Finished UTC: 2026-09-23T00:54:46Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5414` |
| Label | `Erythrobasidium hasegawianum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5413` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/erythrobasidium_hasegawianum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/erysiphe_pisi.yaml data/taxa/eukaryota/erysiphe_pulchra.yaml data/taxa/eukaryota/erythrobasidium_hasegawianum.yaml data/taxa/eukaryota/erythrobasidium_hasegawianum_atcc_9536.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one direct organism assertion, one exact native GOLD organism/project/analysis row, seven NCBI type-material rows, four exact StrainInfo rows with 17 deposits, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5414`, `label: Erythrobasidium hasegawianum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5413`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2402`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Erythrobasidium` genus; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:38314`, which records one retained direct organism for `NCBITaxon:5414`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The YAML correctly keeps this as a direct-taxonomy assertion and notes that descendant taxa are not gathered.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5414`. The YAML preserves NCBI's exact synonym `Rhodotorula hasegawae` plus the related synonym `Erythrobasidium hasegawianum Hamam., Sugiy. & Komag., 1991`; NCBI supplies no broad synonyms and no old-ID side rows.

The native GOLD catalogs contain one exact organism row, `Go0384295` for `Erythrobasidium hasegawianum JCM 1545`, with one matching project, `Gp0235387`, and one native GOLD analysis row linked through `AP PROJECT GOLD IDS: Gp0235387`.

NCBI type-material evidence contributes seven aliases for `Erythrobasidium hasegawianum`, spanning AS 2.1923, CBS 8253, CGMCC 2.1923, and JCM 1545 variants. StrainInfo contains four exact target rows with 17 deposit designations for `Erythrobasidium hasegawianum`; those side rows do not produce BacDive-derived local strain children for this taxon.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, one NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/erythrobasidium_hasegawianum.yaml` plus `just validate-strict data/taxa/eukaryota/erythrobasidium_hasegawianum.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the one current native GOLD organism row filed directly under `NCBITaxon:5414`; the generated source note correctly excludes descendant strain `NCBITaxon:1397323`.
