# YAML Record Review: Drechslerella stenobrocha

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/drechslerella_stenobrocha.yaml
- Started UTC: 2026-09-22T23:30:43Z
- Finished UTC: 2026-09-22T23:30:43Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:314127` |
| Label | `Drechslerella stenobrocha` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:314126` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/drechslerella_stenobrocha.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/dothiorella_sarmentorum.yaml data/taxa/eukaryota/dothistroma_septosporum.yaml data/taxa/eukaryota/drechmeria_coniospora.yaml data/taxa/eukaryota/drechslerella_stenobrocha.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, the retained GOLD aggregate row, one exact native GOLD organism and project, one exact StrainInfo direct record carrying one matching deposit designation, no native GOLD analyses, no NCBI type-material or merged-ID side rows, no lineage mismatches, no BacDive rows, and no final raw strain rows. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:314127`, `label: Drechslerella stenobrocha`, `rank: SPECIES`, `parent_taxon: NCBITaxon:314126`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:64245`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Drechslerella` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:31721`, which records one retained direct organism for `NCBITaxon:314127`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:314127`. The YAML carries the one exact synonym and both related synonyms filed for this NCBI row; NCBI supplies no broad synonyms.

The native GOLD catalogs contain one exact organism row, `Go0005661` for `Drechslerella stenobrocha YNWS02-9-1`, and one matching project, `Gp0005661`. The local native GOLD analysis catalog has no exact analysis row for that project.

The exact StrainInfo side inventory has one direct record and one matching deposit designation for `NCBITaxon:314127`, but no rows are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact NCBI type-material, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/drechslerella_stenobrocha.yaml` plus `just validate-strict data/taxa/eukaryota/drechslerella_stenobrocha.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the one current native GOLD organism row. The absent native GOLD analysis row is consistent with the generated record because GOLD project and analysis rows do not generate child strain records here.
