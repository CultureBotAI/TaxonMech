# YAML Record Review: Crinitomyces ghanaensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/crinitomyces_ghanaensis.yaml
- Started UTC: 2026-09-22T15:45:14Z
- Finished UTC: 2026-09-22T15:45:14Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:135453` |
| Label | `Crinitomyces ghanaensis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2982636` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/crinitomyces_ghanaensis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/crepidotus_variabilis.yaml data/taxa/eukaryota/crinitomyces_ghanaensis.yaml data/taxa/eukaryota/cristinia_sonorae.yaml data/taxa/eukaryota/crithidia_acanthocephali.yaml` | Passed; the strict validator scanned four files with zero errors, including this record. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism row, one exact native GOLD project row, no exact native GOLD analysis rows, five NCBI type-material rows, one exact direct StrainInfo record covering two deposits, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:135453`, `label: Crinitomyces ghanaensis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2982636`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:27022`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Crinitomyces` genus; the bounded scan checked all 13 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:8613`, which records one retained organism for `NCBITaxon:135453`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:135453`. NCBI supplies the exact synonym `Candida ghanaensis` and related synonyms `Candida ghanaensis Kurtzman, 2001` and `Crinitomyces ghanaensis (Kurtzman) V. Sakpuntoon, G. Peter, M. Groenew., D. Dlauchy, S. Limtong & N. Srisuk, 2022`, matching the YAML synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot also has exact organism `Go0705678` for `Crinitomyces ghanaensis NRRL YB-1486` and exact project `Gp0831730`; no native analysis rows are filed under that project.

NCBI has five exact type-material side rows for this taxon covering `CBS 8798` and `NRRL YB-1486` designations under the synonymous `Candida ghanaensis` name. StrainInfo has one exact direct record for the taxon, but no BacDive-backed strain row joins it into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; `strain_count: 0` is therefore consistent with the maintained generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/crinitomyces_ghanaensis.yaml` plus `just validate-strict data/taxa/eukaryota/crinitomyces_ghanaensis.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:135453`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
