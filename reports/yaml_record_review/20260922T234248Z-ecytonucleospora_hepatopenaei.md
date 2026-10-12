# YAML Record Review: Ecytonucleospora hepatopenaei

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/ecytonucleospora_hepatopenaei.yaml
- Started UTC: 2026-09-22T23:42:48Z
- Finished UTC: 2026-09-22T23:42:48Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:646526` |
| Label | `Ecytonucleospora hepatopenaei` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:3078583` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/ecytonucleospora_hepatopenaei.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/echria_macrotheca.yaml data/taxa/eukaryota/ectocarpus_siliculosus.yaml data/taxa/eukaryota/ectophoma_multirostrata.yaml data/taxa/eukaryota/ecytonucleospora_hepatopenaei.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism, project, and analysis row, no exact StrainInfo, NCBI type-material, NCBI merged-ID, or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:646526`, `label: Ecytonucleospora hepatopenaei`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3078583`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:149326`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Ecytonucleospora` genus; the bounded scan checked all 10 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:40369`, which records one retained direct organism for `NCBITaxon:646526`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:646526`. The YAML carries both related synonyms filed for this NCBI row; NCBI supplies no exact or broad synonyms.

The native GOLD catalogs contain one exact organism row, `Go0372908` for `Enterocytozoon hepatopenaei TH1`, one matching project, `Gp0219699`, and one analysis for that project.

There are no exact rows for this taxon in the StrainInfo side inventory, NCBI type-material table, NCBI merged-ID table, BacDive, or the maintained final strain tables. `strain_count: 0` is therefore consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/ecytonucleospora_hepatopenaei.yaml` plus `just validate-strict data/taxa/eukaryota/ecytonucleospora_hepatopenaei.yaml`.

## Additional Notes

The native GOLD organism uses the `Enterocytozoon hepatopenaei` spelling recorded by NCBI as part of its related-synonym evidence for the current `Ecytonucleospora hepatopenaei` name.
